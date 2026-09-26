"""docs/mcp/pai-playbook-mcp.mjs 프로토콜·도구 검증 — node 서브프로세스로 stdio JSON-RPC를 주고받는다.
PAI_PLAYBOOK_DOCS_DIR=docs 로 오프라인 동작(네트워크 없음)."""
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


def run_raw(payload, timeout=20):
    proc = subprocess.run(
        [NODE, str(SERVER)],
        input=payload, capture_output=True, text=True, timeout=timeout,
        env={**os.environ, "PAI_PLAYBOOK_DOCS_DIR": str(ROOT / "docs")},
    )
    return proc


def rpc(messages, timeout=20):
    """메시지 목록을 한 번에 보내고 응답 줄들을 JSON으로 파싱해 돌려준다."""
    payload = "".join(json.dumps(m) + "\n" for m in messages)
    proc = run_raw(payload, timeout)
    out = [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]
    return out, proc.stderr


def init_msg(version="2025-06-18"):
    return {"jsonrpc": "2.0", "id": 1, "method": "initialize",
            "params": {"protocolVersion": version, "capabilities": {},
                       "clientInfo": {"name": "pytest", "version": "0"}}}


def call(id_, name, args):
    return {"jsonrpc": "2.0", "id": id_, "method": "tools/call",
            "params": {"name": name, "arguments": args}}


def text_of(resp):
    return resp["result"]["content"][0]["text"]


def test_initialize_echoes_supported_version_and_server_info():
    out, _ = rpc([init_msg("2025-03-26")])
    assert out[0]["id"] == 1
    assert out[0]["result"]["protocolVersion"] == "2025-03-26"
    assert out[0]["result"]["serverInfo"]["name"] == "pai-playbook"
    assert "tools" in out[0]["result"]["capabilities"]


def test_initialize_falls_back_on_unknown_version():
    out, _ = rpc([init_msg("1999-01-01")])
    assert out[0]["result"]["protocolVersion"] == "2025-03-26"


def test_notifications_and_blank_lines_get_no_response():
    payload = json.dumps(init_msg()) + "\n\n" + json.dumps(
        {"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n"
    proc = run_raw(payload)
    lines = [l for l in proc.stdout.splitlines() if l.strip()]
    assert len(lines) == 1  # initialize 응답만


def test_parse_error_returns_32700_and_keeps_running():
    payload = "not json\n" + json.dumps({"jsonrpc": "2.0", "id": 9, "method": "ping"}) + "\n"
    proc = run_raw(payload)
    out = [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]
    assert out[0]["error"]["code"] == -32700
    assert out[1] == {"jsonrpc": "2.0", "id": 9, "result": {}}


def test_unknown_method_returns_32601():
    out, _ = rpc([{"jsonrpc": "2.0", "id": 2, "method": "resources/list"}])
    assert out[0]["error"]["code"] == -32601


def test_tools_list_has_exactly_four_tools():
    out, _ = rpc([{"jsonrpc": "2.0", "id": 3, "method": "tools/list"}])
    names = sorted(t["name"] for t in out[0]["result"]["tools"])
    assert names == ["playbook_evidence", "playbook_list_pages", "playbook_read_page", "playbook_search"]
    for t in out[0]["result"]["tools"]:
        assert t["inputSchema"]["type"] == "object"


def test_list_pages_includes_start_with_title_and_url():
    out, _ = rpc([call(4, "playbook_list_pages", {"lang": "en"})])
    text = text_of(out[0])
    assert "start" in text and "comeddy.github.io/pai-playbook/en/start/" in text


def test_read_page_ko_and_en_strips_frontmatter():
    out, _ = rpc([call(5, "playbook_read_page", {"page": "start"}),
                  call(6, "playbook_read_page", {"page": "start", "lang": "en"})])
    assert "# 시작" in text_of(out[0])
    assert "ko_hash" not in text_of(out[1]) and text_of(out[1]).startswith("# Start")


def test_read_page_unknown_page_and_lang_are_tool_errors():
    out, _ = rpc([call(7, "playbook_read_page", {"page": "nope"}),
                  call(8, "playbook_read_page", {"page": "start", "lang": "fr"})])
    assert out[0]["result"]["isError"] is True
    assert out[1]["result"]["isError"] is True and "ko" in text_of(out[1])


def test_search_hits_and_rejects_empty_query():
    out, _ = rpc([call(10, "playbook_search", {"query": "Radar", "limit": 3}),
                  call(11, "playbook_search", {"query": "   "})])
    hits = text_of(out[0]).splitlines()
    assert 1 <= len(hits) <= 3 and "radar" in hits[0].lower()
    assert out[1]["result"]["isError"] is True


def test_evidence_summary_and_single_claim():
    out, _ = rpc([call(12, "playbook_evidence", {}),
                  call(13, "playbook_evidence", {"claim_id": "openvla-license"}),
                  call(14, "playbook_evidence", {"claim_id": "nope"})])
    assert "openvla-license" in text_of(out[0])
    single = json.loads(text_of(out[1]))
    assert single["id"] == "openvla-license" and "sources" in single
    assert out[2]["result"]["isError"] is True


def test_unknown_tool_is_invalid_params():
    out, _ = rpc([call(15, "playbook_nope", {})])
    assert out[0]["error"]["code"] == -32602
