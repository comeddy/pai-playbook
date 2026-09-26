"""docs/mcp/pai-playbook-mcp.mjs 프로토콜·도구 검증 — node 서브프로세스로 stdio JSON-RPC를 주고받는다.
PAI_PLAYBOOK_DOCS_DIR 로 tmp 픽스처(docs/ + ../mkdocs.yml)를 가리켜 오프라인·리포 내용 무관하게 동작."""
import json
import os
import pathlib
import shutil
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SERVER = ROOT / "docs" / "mcp" / "pai-playbook-mcp.mjs"
NODE = shutil.which("node")

pytestmark = pytest.mark.skipif(NODE is None, reason="node 미설치")

MKDOCS = """site_name: fixture
nav:
  - 홈: index.md
  - 가이드: guide.md
  - "Radar (대기열)": radar.md

theme:
  name: material
"""
CLAIMS = {"schema_version": 1, "claims": [{
    "id": "openvla-license", "checked_on": "2026-09-15", "review_after_days": 30,
    "status": "source-checked", "verified_by": "Source comparison", "human_review": "pending",
    "pages": ["guide.md"], "summary": {"ko": "주장", "en": "Claim", "zh": "主张", "ja": "主張"},
    "sources": [{"label": "Official", "url": "https://example.org/license"}],
}]}


@pytest.fixture(scope="module")
def docs_dir(tmp_path_factory):
    """서버가 읽는 최소 콘텐츠: mkdocs.yml(nav) + docs/*.md(ko·en) + docs/assets/claims.json."""
    root = tmp_path_factory.mktemp("fixture")
    docs = root / "docs"
    (docs / "assets").mkdir(parents=True)
    (root / "mkdocs.yml").write_text(MKDOCS, encoding="utf-8")
    pages = {"index": ("홈", "Home"), "guide": ("가이드", "Guide"), "radar": ("Radar 대기열", "Radar queue")}
    for stem, (ko, en) in pages.items():
        (docs / f"{stem}.md").write_text(f"# {ko}\n\n본문 Radar 언급.\n", encoding="utf-8")
        (docs / f"{stem}.en.md").write_text(f"---\nko_hash: {'0' * 40}\n---\n# {en}\n\nBody.\n", encoding="utf-8")
    (docs / "assets" / "claims.json").write_text(json.dumps(CLAIMS), encoding="utf-8")
    return docs


def run_raw(docs_dir, payload, timeout=20):
    return subprocess.run(
        [NODE, str(SERVER)],
        input=payload, capture_output=True, text=True, timeout=timeout,
        env={**os.environ, "PAI_PLAYBOOK_DOCS_DIR": str(docs_dir)},
    )


def rpc(docs_dir, messages, timeout=20):
    """메시지 목록을 한 번에 보내고 응답 줄들을 JSON으로 파싱해 돌려준다."""
    payload = "".join(json.dumps(m) + "\n" for m in messages)
    proc = run_raw(docs_dir, payload, timeout)
    return [json.loads(l) for l in proc.stdout.splitlines() if l.strip()], proc.stderr


def init_msg(version="2025-06-18"):
    return {"jsonrpc": "2.0", "id": 1, "method": "initialize",
            "params": {"protocolVersion": version, "capabilities": {},
                       "clientInfo": {"name": "pytest", "version": "0"}}}


def call(id_, name, args):
    return {"jsonrpc": "2.0", "id": id_, "method": "tools/call",
            "params": {"name": name, "arguments": args}}


def text_of(resp):
    return resp["result"]["content"][0]["text"]


def test_initialize_echoes_supported_version_and_server_info(docs_dir):
    out, _ = rpc(docs_dir, [init_msg("2025-03-26")])
    assert out[0]["id"] == 1
    assert out[0]["result"]["protocolVersion"] == "2025-03-26"
    assert out[0]["result"]["serverInfo"]["name"] == "pai-playbook"
    assert "tools" in out[0]["result"]["capabilities"]


def test_initialize_falls_back_on_unknown_version(docs_dir):
    out, _ = rpc(docs_dir, [init_msg("1999-01-01")])
    assert out[0]["result"]["protocolVersion"] == "2025-03-26"


def test_notifications_and_blank_lines_get_no_response(docs_dir):
    payload = json.dumps(init_msg()) + "\n\n" + json.dumps(
        {"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n"
    proc = run_raw(docs_dir, payload)
    lines = [l for l in proc.stdout.splitlines() if l.strip()]
    assert len(lines) == 1  # initialize 응답만


def test_parse_error_returns_32700_and_keeps_running(docs_dir):
    payload = "not json\n" + json.dumps({"jsonrpc": "2.0", "id": 9, "method": "ping"}) + "\n"
    proc = run_raw(docs_dir, payload)
    out = [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]
    assert out[0]["error"]["code"] == -32700
    assert out[1] == {"jsonrpc": "2.0", "id": 9, "result": {}}


def test_unknown_method_returns_32601(docs_dir):
    out, _ = rpc(docs_dir, [{"jsonrpc": "2.0", "id": 2, "method": "resources/list"}])
    assert out[0]["error"]["code"] == -32601


def test_tools_list_has_exactly_four_tools(docs_dir):
    out, _ = rpc(docs_dir, [{"jsonrpc": "2.0", "id": 3, "method": "tools/list"}])
    names = sorted(t["name"] for t in out[0]["result"]["tools"])
    assert names == ["playbook_evidence", "playbook_list_pages", "playbook_read_page", "playbook_search"]
    for t in out[0]["result"]["tools"]:
        assert t["inputSchema"]["type"] == "object"


def test_list_pages_parses_nav_with_titles_and_lang_urls(docs_dir):
    out, _ = rpc(docs_dir, [call(4, "playbook_list_pages", {"lang": "en"})])
    lines = text_of(out[0]).splitlines()
    assert lines[0] == "index — 홈 — https://comeddy.github.io/pai-playbook/en/"
    assert lines[1] == "guide — 가이드 — https://comeddy.github.io/pai-playbook/en/guide/"
    assert lines[2].startswith("radar — Radar (대기열) — ")  # 따옴표 라벨 파싱


def test_read_page_ko_and_en_strips_frontmatter(docs_dir):
    out, _ = rpc(docs_dir, [call(5, "playbook_read_page", {"page": "guide"}),
                            call(6, "playbook_read_page", {"page": "guide", "lang": "en"})])
    assert text_of(out[0]).startswith("# 가이드")
    assert "ko_hash" not in text_of(out[1]) and text_of(out[1]).startswith("# Guide")


def test_read_page_unknown_page_and_lang_are_tool_errors(docs_dir):
    out, _ = rpc(docs_dir, [call(7, "playbook_read_page", {"page": "nope"}),
                            call(8, "playbook_read_page", {"page": "guide", "lang": "fr"})])
    assert out[0]["result"]["isError"] is True and "guide" in text_of(out[0])  # 사용 가능 목록 안내
    assert out[1]["result"]["isError"] is True and "ko" in text_of(out[1])


def test_search_hits_respect_limit_and_reject_empty_query(docs_dir):
    out, _ = rpc(docs_dir, [call(10, "playbook_search", {"query": "radar", "limit": 2}),
                            call(11, "playbook_search", {"query": "   "})])
    hits = text_of(out[0]).splitlines()
    assert len(hits) == 2 and all("radar" in h.lower() for h in hits)  # 3페이지 모두 매치하지만 limit=2
    assert hits[0].startswith("index:3: ")  # page:줄번호: 형식
    assert out[1]["result"]["isError"] is True


def test_evidence_summary_and_single_claim(docs_dir):
    out, _ = rpc(docs_dir, [call(12, "playbook_evidence", {}),
                            call(13, "playbook_evidence", {"claim_id": "openvla-license"}),
                            call(14, "playbook_evidence", {"claim_id": "nope"})])
    assert text_of(out[0]) == "openvla-license · source-checked · checked_on 2026-09-15 · pages guide.md"
    single = json.loads(text_of(out[1]))
    assert single["id"] == "openvla-license" and "sources" in single
    assert out[2]["result"]["isError"] is True


def test_unknown_tool_is_invalid_params(docs_dir):
    out, _ = rpc(docs_dir, [call(15, "playbook_nope", {})])
    assert out[0]["error"]["code"] == -32602
