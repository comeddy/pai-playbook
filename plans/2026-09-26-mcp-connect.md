# MCP 연결 (서버 파일 + 설정 가이드) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a single-file stdio MCP server that exposes Playbook pages/Radar/evidence to AI clients, plus a four-language "설정 · MCP 연결" guide page mirroring TTOBAK's connection guide.

**Architecture:** `docs/mcp/pai-playbook-mcp.mjs` is a dependency-free Node 18+ script speaking newline-delimited JSON-RPC over stdio; it reads markdown from `raw.githubusercontent.com` (or a local docs dir via `PAI_PLAYBOOK_DOCS_DIR`) and offers four read-only tools. MkDocs copies the `.mjs` into the site, so users `curl` it from GitHub Pages. The guide page uses `pymdownx.tabbed` for one tab per client, with stdio steps and an "HTTP 미설정" collapsible.

**Tech Stack:** Node 24 (target 18+, built-in `fetch`), MkDocs Material 9.7 + mkdocs-static-i18n (suffix), pymdown-extensions 10.21, pytest 3.9-compatible Python.

**Spec:** `specs/2026-09-26-mcp-connect-design.md`

## Global Constraints

- Server: Node 18+, **no npm dependencies**, stdio only, logs to stderr only, `serverInfo = {name:"pai-playbook", version:"1.0.0"}`.
- Protocol negotiation: echo client `protocolVersion` if in `["2025-06-18","2025-03-26","2024-11-05"]`, else `"2025-03-26"`.
- Content source order: `PAI_PLAYBOOK_DOCS_DIR` (filesystem) → `https://raw.githubusercontent.com/comeddy/pai-playbook/main/`.
- Tool names exactly: `playbook_list_pages`, `playbook_read_page`, `playbook_search`, `playbook_evidence`.
- Languages: `ko` (file `<stem>.md`), `en`/`zh`/`ja` (`<stem>.<lang>.md`); strip `ko_hash` frontmatter from translations.
- Pages: ko is the source; en/zh/ja must carry `ko_hash` matching `python3 scripts/check_translation_sync.py --hash docs/<file>.md`.
- Every page: top `_최종 갱신: 2026-09 · owner: Youngjin · volatility: 낮음_` and bottom `_owner: Youngjin · updated: 2026-09 · volatility: 낮음_` (translated wording per existing pages).
- Footnote ids identical across languages: `[^mcp]`, `[^stdio]`; markers only at first body occurrence, never in headings.
- Commit gates (all must pass before any commit that touches docs): `python3 scripts/check_evidence.py`, `python3 scripts/check_translation_sync.py` (0 drift), `python3 scripts/check_nav_index_sync.py`, `mkdocs build --strict`.
- Commit with explicit paths only (`git commit -- <paths>`) — the working tree holds ~80 unrelated uncommitted files from another session; never `git add -A`.
- Commit messages end with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.

## Review Focus

1. Client sends a JSON-RPC **notification** (no `id`, e.g. `notifications/initialized`, `notifications/cancelled`) — server must stay silent, not emit a response with `id: undefined`. (Test in Task 1.)
2. A blank or non-JSON line on stdin — server must reply `-32700` for non-JSON and ignore empty lines, never crash. (Test in Task 1.)
3. `playbook_read_page` with `lang` outside ko/en/zh/ja — `isError: true` with a message listing valid values, not an unhandled exception. (Test in Task 1.)
4. `playbook_search` with an empty query — return `isError: true` rather than every line of every page. (Test in Task 1.)
5. Guide page code blocks must be copy-safe: the `curl` download URL must be the **exact** published path `https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs`, and `mkdocs build --strict` must produce `site/mcp/pai-playbook-mcp.mjs`. (Checked in Task 2 build step and Task 5 live check.)

---

### Task 1: MCP server + protocol tests

**Files:**
- Create: `docs/mcp/pai-playbook-mcp.mjs`
- Create: `tests/test_mcp_server.py`

**Interfaces:**
- Produces: script runnable as `node docs/mcp/pai-playbook-mcp.mjs`; env `PAI_PLAYBOOK_DOCS_DIR=<repo>/docs` switches to filesystem mode (reads `<dir>/../mkdocs.yml` for nav, `<dir>/<file>` for pages, `<dir>/assets/claims.json` for evidence).
- Produces: tools `playbook_list_pages {lang?}`, `playbook_read_page {page, lang?}`, `playbook_search {query, lang?, limit?}`, `playbook_evidence {claim_id?}`; all return `{content:[{type:"text",text}], isError?}`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_mcp_server.py
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


def rpc(messages, timeout=20):
    """메시지 목록을 한 번에 보내고 응답 줄들을 JSON으로 파싱해 돌려준다."""
    payload = "".join(json.dumps(m) + "\n" for m in messages)
    proc = subprocess.run(
        [NODE, str(SERVER)],
        input=payload, capture_output=True, text=True, timeout=timeout,
        env={**os.environ, "PAI_PLAYBOOK_DOCS_DIR": str(ROOT / "docs")},
    )
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
    proc = subprocess.run([NODE, str(SERVER)], input=payload, capture_output=True, text=True,
                          timeout=20, env={**os.environ, "PAI_PLAYBOOK_DOCS_DIR": str(ROOT / "docs")})
    lines = [l for l in proc.stdout.splitlines() if l.strip()]
    assert len(lines) == 1  # initialize 응답만


def test_parse_error_returns_32700_and_keeps_running():
    payload = "not json\n" + json.dumps({"jsonrpc": "2.0", "id": 9, "method": "ping"}) + "\n"
    proc = subprocess.run([NODE, str(SERVER)], input=payload, capture_output=True, text=True,
                          timeout=20, env={**os.environ, "PAI_PLAYBOOK_DOCS_DIR": str(ROOT / "docs")})
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/ec2-user/pai-playbook && python3 -m pytest tests/test_mcp_server.py -q`
Expected: all FAIL (node exits non-zero because the file does not exist → `IndexError` / empty output).

- [ ] **Step 3: Write the server**

```js
#!/usr/bin/env node
// docs/mcp/pai-playbook-mcp.mjs — Physical AI Playbook MCP 서버 (stdio, 단일 파일, 의존성 없음)
// 실행: node "$HOME/.pai-playbook/server.mjs"   (Node 18+)
// 콘텐츠: PAI_PLAYBOOK_DOCS_DIR(로컬 docs/)가 있으면 파일, 없으면 GitHub raw(main).
import { readFile } from "node:fs/promises";
import path from "node:path";
import readline from "node:readline";

const NAME = "pai-playbook";
const VERSION = "1.0.0";
const RAW = "https://raw.githubusercontent.com/comeddy/pai-playbook/main/";
const SITE = "https://comeddy.github.io/pai-playbook/";
const LANGS = ["ko", "en", "zh", "ja"];
const SUPPORTED = ["2025-06-18", "2025-03-26", "2024-11-05"];
const DOCS_DIR = process.env.PAI_PLAYBOOK_DOCS_DIR || null;
const TTL_MS = 10 * 60 * 1000;
const cache = new Map();

const log = (...a) => process.stderr.write(a.join(" ") + "\n");

// rel: "mkdocs.yml" | "docs/<file>"
async function source(rel) {
  const hit = cache.get(rel);
  if (hit && hit.until > Date.now()) return hit.text;
  let text;
  if (DOCS_DIR) {
    const p = rel === "mkdocs.yml"
      ? path.join(DOCS_DIR, "..", "mkdocs.yml")
      : path.join(DOCS_DIR, rel.replace(/^docs\//, ""));
    text = await readFile(p, "utf8");
  } else {
    const res = await fetch(RAW + rel);
    if (!res.ok) throw new Error(`${rel}: HTTP ${res.status}`);
    text = await res.text();
  }
  cache.set(rel, { text, until: Date.now() + TTL_MS });
  return text;
}

async function pages() {
  const lines = (await source("mkdocs.yml")).split("\n");
  const start = lines.findIndex((l) => l.trimEnd() === "nav:");
  if (start < 0) throw new Error("mkdocs.yml: nav 블록 없음");
  const out = [];
  for (const line of lines.slice(start + 1)) {
    if (line.trim() && !line.startsWith(" ")) break;
    const m = line.match(/^\s+-\s+"?(.*?)"?:\s*(\S+)\.md\s*$/);
    if (m) out.push({ id: m[2], title: m[1] });
  }
  return out;
}

function checkLang(lang) {
  if (!LANGS.includes(lang)) throw new Error(`lang은 ${LANGS.join("/")} 중 하나여야 합니다 (받은 값: ${lang})`);
}

async function pageText(id, lang) {
  checkLang(lang);
  const list = await pages();
  if (!list.some((p) => p.id === id)) {
    throw new Error(`알 수 없는 페이지: ${id}. 사용 가능: ${list.map((p) => p.id).join(", ")}`);
  }
  const file = lang === "ko" ? `${id}.md` : `${id}.${lang}.md`;
  const raw = await source(`docs/${file}`);
  return raw.replace(/^---\n[\s\S]*?\n---\n/, "");
}

const pageUrl = (id, lang) => `${SITE}${lang === "ko" ? "" : lang + "/"}${id === "index" ? "" : id + "/"}`;

const TOOLS = [
  {
    name: "playbook_list_pages",
    description: "Physical AI Playbook의 페이지 목록(id·제목·URL). 다른 도구의 page 인자에 id를 사용한다.",
    inputSchema: { type: "object", properties: { lang: { type: "string", enum: LANGS, description: "기본 ko" } } },
  },
  {
    name: "playbook_read_page",
    description: "Playbook 페이지 1개의 마크다운 원문을 읽는다 (예: start, execution, pillar-2, radar, evidence).",
    inputSchema: {
      type: "object", required: ["page"],
      properties: { page: { type: "string", description: "페이지 id (playbook_list_pages 참고)" },
                    lang: { type: "string", enum: LANGS, description: "기본 ko" } },
    },
  },
  {
    name: "playbook_search",
    description: "모든 Playbook 페이지에서 문자열을 검색해 'page:줄번호: 텍스트' 스니펫을 돌려준다 (대소문자 무시, 랭킹 없음).",
    inputSchema: {
      type: "object", required: ["query"],
      properties: { query: { type: "string" }, lang: { type: "string", enum: LANGS, description: "기본 ko" },
                    limit: { type: "integer", minimum: 1, maximum: 100, description: "기본 20" } },
    },
  },
  {
    name: "playbook_evidence",
    description: "근거 기록(claims.json): claim_id를 주면 해당 주장 전체, 없으면 전체 요약(id·상태·확인일·영향 페이지).",
    inputSchema: { type: "object", properties: { claim_id: { type: "string" } } },
  },
];

const handlers = {
  async playbook_list_pages({ lang = "ko" }) {
    checkLang(lang);
    const list = await pages();
    return list.map((p) => `${p.id} — ${p.title} — ${pageUrl(p.id, lang)}`).join("\n");
  },
  async playbook_read_page({ page, lang = "ko" }) {
    if (!page) throw new Error("page 인자가 필요합니다");
    return pageText(page, lang);
  },
  async playbook_search({ query, lang = "ko", limit = 20 }) {
    if (!query || !String(query).trim()) throw new Error("query가 비어 있습니다");
    checkLang(lang);
    const q = String(query).toLowerCase();
    const max = Math.min(Math.max(Number(limit) || 20, 1), 100);
    const hits = [];
    for (const p of await pages()) {
      let text;
      try { text = await pageText(p.id, lang); } catch (e) { log(`search skip ${p.id}: ${e.message}`); continue; }
      const lines = text.split("\n");
      for (let i = 0; i < lines.length && hits.length < max; i++) {
        if (lines[i].toLowerCase().includes(q)) hits.push(`${p.id}:${i + 1}: ${lines[i].trim().slice(0, 200)}`);
      }
      if (hits.length >= max) break;
    }
    return hits.length ? hits.join("\n") : `검색 결과 없음: ${query}`;
  },
  async playbook_evidence({ claim_id }) {
    const data = JSON.parse(await source("docs/assets/claims.json"));
    const claims = data.claims || [];
    if (claim_id) {
      const c = claims.find((x) => x.id === claim_id);
      if (!c) throw new Error(`알 수 없는 claim_id: ${claim_id}. 사용 가능: ${claims.map((x) => x.id).join(", ")}`);
      return JSON.stringify(c, null, 2);
    }
    return claims.map((c) => `${c.id} · ${c.status} · checked_on ${c.checked_on} · pages ${(c.pages || []).join(", ")}`).join("\n");
  },
};

const reply = (id, result) => process.stdout.write(JSON.stringify({ jsonrpc: "2.0", id, result }) + "\n");
const fail = (id, code, message) => process.stdout.write(JSON.stringify({ jsonrpc: "2.0", id, error: { code, message } }) + "\n");

async function dispatch(msg) {
  const { id, method, params = {} } = msg;
  const isNotification = id === undefined || id === null;
  if (isNotification) return; // notifications/initialized 등 — 응답 금지
  switch (method) {
    case "initialize": {
      const v = SUPPORTED.includes(params.protocolVersion) ? params.protocolVersion : "2025-03-26";
      return reply(id, { protocolVersion: v, capabilities: { tools: {} }, serverInfo: { name: NAME, version: VERSION } });
    }
    case "ping": return reply(id, {});
    case "tools/list": return reply(id, { tools: TOOLS });
    case "tools/call": {
      const fn = handlers[params.name];
      if (!fn) return fail(id, -32602, `알 수 없는 도구: ${params.name}`);
      try {
        const text = await fn(params.arguments || {});
        return reply(id, { content: [{ type: "text", text }] });
      } catch (e) {
        return reply(id, { content: [{ type: "text", text: e.message }], isError: true });
      }
    }
    default: return fail(id, -32601, `지원하지 않는 메서드: ${method}`);
  }
}

let chain = Promise.resolve(); // 요청 순서대로 응답 (테스트·클라이언트 모두 순서에 의존하지 않지만 단순화)
readline.createInterface({ input: process.stdin, crlfDelay: Infinity }).on("line", (line) => {
  if (!line.trim()) return;
  let msg;
  try { msg = JSON.parse(line); } catch { fail(null, -32700, "JSON 파싱 실패"); return; }
  chain = chain.then(() => dispatch(msg)).catch((e) => { log("dispatch error:", e.message); if (msg.id != null) fail(msg.id, -32603, e.message); });
});
process.stdin.on("end", () => chain.then(() => process.exit(0)));
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /home/ec2-user/pai-playbook && python3 -m pytest tests/test_mcp_server.py -q`
Expected: 12 passed. If `test_search_hits_and_rejects_empty_query` fails because `hits[0]` lacks "radar", check that `index.md` line order puts a Radar mention early — the assertion only requires the matched line to contain the query, which `includes` guarantees; a failure means the search loop is wrong.

- [ ] **Step 5: Smoke-run in remote mode (no env var) against GitHub raw**

Run:
```bash
cd /home/ec2-user/pai-playbook && printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18"}}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"playbook_list_pages","arguments":{}}}' \
 | node docs/mcp/pai-playbook-mcp.mjs | cut -c1-300
```
Expected: two lines; the second lists page ids from the **live** `main` mkdocs.yml (start/execution may be absent until the other session's pages are pushed — that is expected, not a bug).

- [ ] **Step 6: Commit**

```bash
cd /home/ec2-user/pai-playbook && git add docs/mcp/pai-playbook-mcp.mjs tests/test_mcp_server.py && git commit -m "mcp: 단일 파일 stdio MCP 서버(docs/mcp/pai-playbook-mcp.mjs) — list_pages·read_page·search·evidence 도구 4개, GitHub raw/로컬 docs 소스, pytest 12건

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" -- docs/mcp/pai-playbook-mcp.mjs tests/test_mcp_server.py
```

---

### Task 2: Korean guide page + mkdocs wiring + home list (ko)

**Files:**
- Create: `docs/mcp.md`
- Modify: `mkdocs.yml` (nav, `markdown_extensions`, `nav_translations` ×3)
- Modify: `docs/index.md` (`## 페이지 목록`)

**Interfaces:**
- Consumes: published server URL `https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs` (Task 1 file location).
- Produces: nav label `"설정 · MCP 연결": mcp.md`; footnote ids `[^mcp]`, `[^stdio]`; heading anchors `{ #overview }`, `{ #clients }`, `{ #prompts }`, `{ #scope }` used by translations.

- [ ] **Step 1: Enable tabs and add nav entry + translations in `mkdocs.yml`**

Add under `markdown_extensions:` (after `- pymdownx.details`):
```yaml
  - pymdownx.tabbed:
      alternate_style: true   # 설정 · MCP 연결 페이지의 클라이언트 탭 (Claude Code/Codex/Kiro/Quick)
```
Add as the last `nav:` item:
```yaml
  - "설정 · MCP 연결": mcp.md
```
Add to each `nav_translations` block:
```yaml
            "설정 · MCP 연결": "Settings · MCP Connection"     # en
            "설정 · MCP 연결": "设置 · MCP 连接"                # zh
            "설정 · MCP 연결": "設定 · MCP 接続"                # ja
```

- [ ] **Step 2: Write `docs/mcp.md`**

```markdown
# 설정 — MCP 연결

_최종 갱신: 2026-09 · owner: Youngjin · volatility: 낮음_

**L0 TL;DR**: 사용하는 AI 도구(Claude Code, Codex, Kiro, Amazon Quick)에서 Playbook 페이지·Radar·근거 기록을 도구 호출로 읽게 하는 설정이다. MCP[^mcp] 서버 파일 1개를 내려받아 등록하면 끝난다. 공개 콘텐츠이므로 로그인·API 키는 없다.

## 무엇이 연결되는가 { #overview }

| 항목 | 값 |
|---|---|
| 서버 파일 | `https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs` (단일 파일, npm 설치 없음) |
| 실행 요건 | Node.js 18+ · macOS/Linux 터미널 (Windows는 WSL) · 인터넷(GitHub raw 콘텐츠 조회) |
| 연결 방식 | 로컬 · stdio[^stdio] (기본) · 원격 HTTP는 미설정 |
| 콘텐츠 | 이 사이트의 마크다운 원문(4개 언어)과 `assets/claims.json` — 사이트와 동일한 내용, 쓰기 없음 |

제공 도구 4개:

| 도구 | 용도 |
|---|---|
| `playbook_list_pages` | 페이지 id·제목·URL 목록 |
| `playbook_read_page` | 페이지 1개 원문(`page`, `lang`) |
| `playbook_search` | 전 페이지 문자열 검색 → 스니펫 |
| `playbook_evidence` | 근거 기록 요약 또는 주장 1건 상세 |

## 클라이언트별 절차 { #clients }

=== "Claude Code"

    Claude Code가 로컬 MCP 서버를 실행한다. 기존 등록이 있다면 연결 정보만 수정한다.

    **① 서버 파일 다운로드**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Claude Code에 등록** — 사용자 범위에 `pai-playbook`을 등록한다. 모델·도구 승인 설정은 바꾸지 않는다.

    ```bash
    claude mcp add pai-playbook --transport stdio --scope user \
      -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ 연결 확인** — `/mcp`에서 `pai-playbook`이 connected인지 확인한 뒤 실제 조회를 요청한다.

    ```text
    /mcp
    ```

    ```text
    Playbook에서 P2 모델 학습 페이지를 읽어줘
    ```

    ??? info "원격 · HTTP — 주소 미설정"
        이 사이트에 공개 HTTP MCP 주소가 아직 등록되지 않았다. 아래는 절차 안내이며 자리표시(`YOUR_…`)를 실제 값으로 바꿔야 동작한다. 공개 OAuth 클라이언트 기준으로 콜백 `http://localhost:9876/callback`이 등록되어 있어야 한다.

        ```bash
        claude mcp add --transport http --scope user \
          --client-id 'YOUR_CLIENT_ID' --callback-port 9876 \
          pai-playbook 'YOUR_HTTP_MCP_URL'
        ```

    [Claude Code 공식 MCP 문서 ↗](https://code.claude.com/docs/en/mcp)

=== "Codex"

    Codex CLI에 로컬 MCP 서버를 등록하는 방법이다. 명령은 공식 문서 기준이며 이 리포에서 실기기 검증은 하지 않았다(`[4]`).

    **① 서버 파일 다운로드**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Codex에 등록**

    ```bash
    codex mcp add pai-playbook -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ 연결 확인** — Codex를 다시 열고 조회를 요청한다.

    ```text
    Playbook에서 'HyperPod'를 검색해줘
    ```

    ??? info "원격 · HTTP — 주소 미설정"
        자리표시를 실제 값으로 바꿔야 한다. 명령이 표시하는 콜백 URL을 관리자에게 전달해 등록한 뒤 `codex mcp login pai-playbook`으로 로그인한다.

        ```bash
        codex mcp add pai-playbook --url 'YOUR_HTTP_MCP_URL' \
          --oauth-client-id 'YOUR_CLIENT_ID'
        ```

    [Codex MCP 문서 ↗](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

=== "Kiro Crew"

    Crew가 실행되는 컴퓨터에 서버 파일이 있어야 한다. 절차는 공식 문서 기준이며 실기기 검증은 하지 않았다(`[4]`).

    **① 서버 파일 다운로드**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Crew에 로컬 서버 추가** — Agent Capabilities → Integrations (MCP)에서 명령 기반 서버를 추가하거나, Crew가 읽는 MCP 설정에 아래 항목을 병합한다. 경로 자리표시는 실제 절대경로로 바꾼다.

    ```bash
    printf '%s\n' "$HOME/.pai-playbook/server.mjs"
    ```

    ```json
    {
      "mcpServers": {
        "pai-playbook": {
          "command": "node",
          "args": ["ABSOLUTE_PATH_TO_SERVER_MJS"]
        }
      }
    }
    ```

    **③ 검색·연결 확인** — Discover & Sync로 설정을 반영하고 Probe All로 연결을 확인한 뒤 조회를 요청한다.

    ```text
    Playbook Radar의 최신 유입 항목을 보여줘
    ```

    ??? info "원격 · HTTP — 주소 미설정"
        Crew 대시보드에서 URL 기반 서버를 추가할 때 사용할 주소가 아직 없다. 주소가 등록되면 `YOUR_HTTP_MCP_URL`을 서버 URL로 입력한다. 이 서버는 공개 콘텐츠라 인증 헤더가 필요 없다.

    [Kiro Crew MCP 문서 ↗](https://kiro.dev/docs/crew/capabilities/mcp-tools.md)

=== "Amazon Quick"

    Amazon Quick은 원격 HTTP MCP만 지원한다. 이 사이트에 공개 HTTP 주소가 아직 없어 현재는 연결할 수 없다. 주소가 등록되면 아래 순서로 진행한다(`[4]`).

    1. Connectors → Create for your team → Model Context Protocol (MCP)에서 새 연결을 만들고 서버 URL `YOUR_HTTP_MCP_URL`을 입력한다.
    2. 인증은 서버 측 설정에 따른다. 공개 콘텐츠 서버라면 인증 없음을 선택한다.
    3. 커넥터의 Sync로 도구 목록을 반영하고 조회를 요청한다. Quick의 작업 제한 시간은 60초다.

    ```text
    Playbook 근거 기록에서 OpenVLA 라이선스 주장을 확인해줘
    ```

    [Amazon Quick MCP 문서 ↗](https://docs.aws.amazon.com/quick/latest/userguide/mcp-integration.html)

=== "Kiro CLI"

    Kiro CLI가 실행되는 컴퓨터에 로컬 MCP 서버를 등록한다. 설정은 공식 문서 기준이며 실기기 검증은 하지 않았다(`[4]`).

    **① 서버 파일 다운로드**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Kiro CLI 설정에 추가** — `~/.kiro/settings/mcp.json`의 `mcpServers`에 아래 항목을 병합한다. 기존 서버와 승인 설정은 유지하고, 경로 자리표시는 실제 절대경로로 바꾼다.

    ```bash
    printf '%s\n' "$HOME/.pai-playbook/server.mjs"
    ```

    ```json
    {
      "mcpServers": {
        "pai-playbook": {
          "command": "node",
          "args": ["ABSOLUTE_PATH_TO_SERVER_MJS"]
        }
      }
    }
    ```

    **③ 연결 확인**

    ```text
    /mcp
    ```

    ```text
    Playbook에서 실행 경로 페이지를 요약해줘
    ```

    ??? info "원격 · HTTP — 주소 미설정"
        자리표시를 실제 값으로 바꿔야 한다. 콜백 `http://localhost:9876/callback` 등록이 필요하며 재인증은 `/mcp auth`를 사용한다.

        ```json
        {
          "mcpServers": {
            "pai-playbook": {
              "url": "YOUR_HTTP_MCP_URL",
              "oauth": {
                "clientId": "YOUR_CLIENT_ID",
                "redirectUri": "http://localhost:9876/callback",
                "oauthScopes": ["openid", "email", "profile"]
              }
            }
          }
        }
        ```

    [Kiro CLI MCP 문서 ↗](https://kiro.dev/docs/mcp/configuration.md)

## 연결 후 이렇게 요청하세요 { #prompts }

```text
Playbook에서 P2 모델 학습 페이지를 읽어줘
```

```text
Playbook에서 'Greengrass'를 검색해서 관련 페이지를 알려줘
```

```text
Playbook Radar의 최신 유입 항목을 표로 정리해줘
```

```text
Playbook 근거 기록에서 OpenVLA 라이선스 주장의 출처와 확인일을 보여줘
```

## 검증 범위와 한계 { #scope }

- Claude Code 절차는 이 리포 배포 후 실제 등록·조회로 확인했다. Codex·Kiro Crew·Amazon Quick·Kiro CLI의 명령은 각 공식 문서 기준이며 미검증(`[4]`)이다.
- 서버는 `main` 브랜치의 마크다운을 읽는다. 사이트 반영 전 커밋 내용이 보일 수 있고, 캐시는 10분이다.
- 서버 파일은 쓰기 도구가 없고 자격증명을 다루지 않는다. 오프라인 사용은 리포를 클론한 뒤 `PAI_PLAYBOOK_DOCS_DIR=<클론>/docs` 환경변수로 가능하다.
- 문제·개선 제안은 [GitHub 이슈](https://github.com/comeddy/pai-playbook/issues)로 남긴다.

**➡️ 다음 액션**: 자주 쓰는 클라이언트 1개에 등록하고 `playbook_search`로 고객 미팅 전 키워드 1개를 검색해 본다.

<!-- 용어 각주 -->
[^mcp]: **MCP (Model Context Protocol)** — AI 도구가 외부 데이터·기능을 표준 방식으로 호출하게 하는 개방 프로토콜. 서버가 "도구"를 제공하고 Claude Code 같은 클라이언트가 그 도구를 호출한다.
[^stdio]: **stdio 전송** — 클라이언트가 서버 프로그램을 자기 컴퓨터에서 직접 실행해 표준 입출력으로 통신하는 MCP 연결 방식. 네트워크 주소·로그인이 필요 없다.

_owner: Youngjin · updated: 2026-09 · volatility: 낮음_
```

- [ ] **Step 3: Add the page to `docs/index.md` '페이지 목록'**

Append after `- [유지보수](maintenance.md)`:
```markdown
- [설정 · MCP 연결](mcp.md)
```

- [ ] **Step 4: Build strict and check the nav/index gate**

Run:
```bash
cd /home/ec2-user/pai-playbook && python3 scripts/check_nav_index_sync.py && mkdocs build --strict --site-dir /tmp/claude-1000/-home-ec2-user-pai-playbook/211d6819-b234-4e5d-8158-fc7cfaf1fdb4/scratchpad/site-check 2>&1 | tail -20 && ls /tmp/claude-1000/-home-ec2-user-pai-playbook/211d6819-b234-4e5d-8158-fc7cfaf1fdb4/scratchpad/site-check/mcp/ && grep -c 'tabbed-set' /tmp/claude-1000/-home-ec2-user-pai-playbook/211d6819-b234-4e5d-8158-fc7cfaf1fdb4/scratchpad/site-check/mcp/index.html
```
Expected: `OK — nav ↔ 홈 페이지 목록 일치`; build exit 0 (warnings about missing `mcp.en.md` etc. are acceptable **only until Task 3**; with `fallback_to_default: true` the build stays green); `pai-playbook-mcp.mjs` and `index.html` both present in `site-check/mcp/`; tabbed count ≥ 1.

- [ ] **Step 5: Do NOT commit yet** — `check_translation_sync.py` reports 3 missing translations for `mcp.md` and drift for `index.md` until Task 3 finishes. Proceed directly to Task 3.

---

### Task 3: en/zh/ja translations + ko_hash re-sync, then commit the page

**Files:**
- Create: `docs/mcp.en.md`, `docs/mcp.zh.md`, `docs/mcp.ja.md`
- Modify: `docs/index.en.md`, `docs/index.zh.md`, `docs/index.ja.md` (list entry + `ko_hash`)

**Interfaces:**
- Consumes: `docs/mcp.md` structure from Task 2 (same headings/anchors, same code blocks, same footnote ids).

- [ ] **Step 1: Load translation rules**

Run: `cat /home/ec2-user/pai-playbook/i18n/glossary.md` and follow the "번역 금지" list (keep MCP, Claude Code, Codex, Kiro, Amazon Quick, Radar, GitHub, Node.js, stdio, OAuth, `[4]` untouched) and the fixed terms table. Meta lines: en `_Last updated: 2026-09 · owner: Youngjin · volatility: low_` / `_owner: Youngjin · updated: 2026-09 · volatility: low_`; zh `_最后更新: 2026-09 · owner: Youngjin · volatility: 低_`; ja `_最終更新: 2026-09 · owner: Youngjin · volatility: 低_` — copy the exact wording used in `docs/start.en.md`, `docs/start.zh.md`, `docs/start.ja.md` top/bottom lines (verify with `sed -n 3p` and `tail -1`).

- [ ] **Step 2: Compute hashes**

Run:
```bash
cd /home/ec2-user/pai-playbook && python3 scripts/check_translation_sync.py --hash docs/mcp.md && python3 scripts/check_translation_sync.py --hash docs/index.md
```
Record both hashes.

- [ ] **Step 3: Write the three translations of `mcp.md`**

Each starts with:
```markdown
---
ko_hash: <hash of docs/mcp.md>
---
```
Then a full translation of Task 2's page. Rules: all code blocks byte-identical to ko (commands, JSON, URLs, `YOUR_…` placeholders); example prompts translated into the target language (e.g. en `Read the P2 model training page from the Playbook`); tab titles unchanged (`=== "Claude Code"` etc.); heading anchors identical (`{ #overview }`, `{ #clients }`, `{ #prompts }`, `{ #scope }`); footnotes:

- en: `[^mcp]: **MCP (Model Context Protocol)** — An open protocol that lets AI tools call external data and functions in a standard way. A server exposes "tools" and a client such as Claude Code invokes them.` / `[^stdio]: **stdio transport** — An MCP connection mode in which the client runs the server program on the same machine and talks to it over standard input/output. No network address or login is needed.`
- zh: `[^mcp]: **MCP (Model Context Protocol)** — 让 AI 工具以标准方式调用外部数据与功能的开放协议。服务器提供"工具"，Claude Code 等客户端调用这些工具。` / `[^stdio]: **stdio 传输** — 客户端在本机直接运行服务器程序并通过标准输入输出通信的 MCP 连接方式。不需要网络地址或登录。`
- ja: `[^mcp]: **MCP (Model Context Protocol)** — AI ツールが外部データ・機能を標準的な方法で呼び出せるようにするオープンプロトコル。サーバーが「ツール」を提供し、Claude Code などのクライアントがそれを呼び出す。` / `[^stdio]: **stdio トランスポート** — クライアントがサーバープログラムを自分のマシンで直接実行し、標準入出力で通信する MCP 接続方式。ネットワークアドレスやログインは不要。`

Nav-title line for each: en `# Settings — MCP Connection`, zh `# 设置 — MCP 连接`, ja `# 設定 — MCP 接続`.

- [ ] **Step 4: Add the list entry to the three index translations and bump their `ko_hash`**

Append after the maintenance entry in each file: en `- [Settings · MCP Connection](mcp.md)`, zh `- [设置 · MCP 连接](mcp.md)`, ja `- [設定 · MCP 接続](mcp.md)`. Replace each file's `ko_hash:` value with the new hash of `docs/index.md`.

- [ ] **Step 5: Run all gates**

Run:
```bash
cd /home/ec2-user/pai-playbook && python3 scripts/check_evidence.py && python3 scripts/check_translation_sync.py | tail -5 && python3 scripts/check_nav_index_sync.py && mkdocs build --strict --site-dir /tmp/claude-1000/-home-ec2-user-pai-playbook/211d6819-b234-4e5d-8158-fc7cfaf1fdb4/scratchpad/site-check 2>&1 | tail -5 && for l in en zh ja; do grep -c 'tabbed-set' /tmp/claude-1000/-home-ec2-user-pai-playbook/211d6819-b234-4e5d-8158-fc7cfaf1fdb4/scratchpad/site-check/$l/mcp/index.html; done && python3 -m pytest -q
```
Expected: evidence OK; translation sync reports 0 non-OK pairs (other pre-existing drift from the other session's uncommitted edits, if any, must be reported to the user — not fixed here); nav/index OK; strict build exit 0; tabbed count ≥1 in all three; pytest all passed.

- [ ] **Step 6: Commit page + wiring (explicit paths)**

```bash
cd /home/ec2-user/pai-playbook && git add mkdocs.yml docs/mcp.md docs/mcp.en.md docs/mcp.zh.md docs/mcp.ja.md docs/index.md docs/index.en.md docs/index.zh.md docs/index.ja.md && git commit -m "docs: 설정 · MCP 연결 페이지 신설 — 클라이언트 탭 5개(Claude Code·Codex·Kiro Crew·Amazon Quick·Kiro CLI) stdio 절차 + HTTP 미설정 안내, 용어 각주 [^mcp]·[^stdio], nav·홈 페이지 목록·nav_translations, 4개 언어 + ko_hash 동기화

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" -- mkdocs.yml docs/mcp.md docs/mcp.en.md docs/mcp.zh.md docs/mcp.ja.md docs/index.md docs/index.en.md docs/index.zh.md docs/index.ja.md
```
**Caution:** `mkdocs.yml`, `docs/index*.md` already have unrelated uncommitted edits from another session. Before committing, run `git diff mkdocs.yml docs/index.md` and confirm the diff is acceptable to ship together; if it contains half-finished work, use `git add -p` to stage only the MCP hunks and tell the user what was left unstaged.

---

### Task 4: CI pytest step + CHANGELOG (4 languages)

**Files:**
- Modify: `.github/workflows/deploy-docs.yml` (build job, before `mkdocs build --strict`)
- Modify: `CHANGELOG.md` (`[Unreleased] / Added` in English → 한국어 → 中文 → 日本語)

- [ ] **Step 1: Add the pytest step**

Insert after the `check_staleness.py --inject` step:
```yaml
      # MCP 서버(docs/mcp/pai-playbook-mcp.mjs) 프로토콜·도구 검사 + 스크립트 단위 테스트 (러너 기본 Node 20 사용)
      - run: pip install pytest && python -m pytest -q
```
Verify locally that `python3 -m pytest -q` passes from a clean shell (Task 3 Step 5 already did).

- [ ] **Step 2: Add CHANGELOG entries**

Under each language's `## [Unreleased]` → `### Added` (category heading stays English), add as the first bullet:

- English: `- Add a "Settings · MCP Connection" page and a single-file stdio MCP server (docs/mcp/pai-playbook-mcp.mjs) so Claude Code, Codex, Kiro CLI/Crew, and Amazon Quick can read Playbook pages, Radar, and evidence records via four tools; client tabs follow the TTOBAK connection-guide structure, HTTP is marked as not configured, in all four languages`
- 한국어: `- "설정 · MCP 연결" 페이지와 단일 파일 stdio MCP 서버(docs/mcp/pai-playbook-mcp.mjs) 추가 — Claude Code·Codex·Kiro CLI/Crew·Amazon Quick에서 도구 4개로 Playbook 페이지·Radar·근거 기록을 조회, TTOBAK 연결 가이드 구조의 클라이언트 탭, HTTP는 미설정 표기, 4개 언어`
- 中文: `- 新增"设置 · MCP 连接"页面与单文件 stdio MCP 服务器（docs/mcp/pai-playbook-mcp.mjs），Claude Code、Codex、Kiro CLI/Crew、Amazon Quick 可通过 4 个工具读取 Playbook 页面、Radar 与证据记录；客户端标签沿用 TTOBAK 连接指南结构，HTTP 标记为未配置，四种语言`
- 日本語: `- 「設定 · MCP 接続」ページと単一ファイル stdio MCP サーバー（docs/mcp/pai-playbook-mcp.mjs）を追加 — Claude Code・Codex・Kiro CLI/Crew・Amazon Quick から 4 つのツールで Playbook ページ・Radar・根拠記録を参照、TTOBAK 接続ガイド構造のクライアントタブ、HTTP は未設定と表記、4 言語`

Find the insertion points with `grep -n "^## \[Unreleased\]" CHANGELOG.md` (4 hits) and the first `### Added` after each.

- [ ] **Step 3: Commit**

```bash
cd /home/ec2-user/pai-playbook && git add .github/workflows/deploy-docs.yml CHANGELOG.md && git commit -m "ci+changelog: deploy-docs에 pytest 단계 추가(MCP 서버 테스트), CHANGELOG 4개 언어 Added — 설정 · MCP 연결 페이지·서버

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" -- .github/workflows/deploy-docs.yml CHANGELOG.md
```
Same caution as Task 3 Step 6: both files have unrelated uncommitted hunks; stage only MCP hunks with `git add -p` if needed and report leftovers.

---

### Task 5: Live verification with Claude Code on this box, then ship

**Files:** none created (temporary user-scope MCP registration, removed afterwards).

- [ ] **Step 1: Register the local server file with Claude Code exactly as the guide says (path swapped to the repo copy)**

Run:
```bash
claude mcp add pai-playbook --transport stdio --scope user -- node /home/ec2-user/pai-playbook/docs/mcp/pai-playbook-mcp.mjs && claude mcp list 2>&1 | grep -i pai-playbook
```
Expected: line shows `pai-playbook: node … - ✓ Connected`. This exercises the **remote** GitHub-raw path (no env var).

- [ ] **Step 2: Remove the temporary registration**

Run: `claude mcp remove pai-playbook --scope user`
Expected: removed; `claude mcp list` no longer shows it.

- [ ] **Step 3: Push and verify the live site (ship skill)**

Invoke `Skill: ship`. Its procedure: `git push origin main`, wait for the `deploy-docs` run to succeed (`gh run watch`), then verify:
```bash
curl -s -o /dev/null -w "%{http_code}\n" https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs
curl -s -o /dev/null -w "%{http_code}\n" https://comeddy.github.io/pai-playbook/mcp/
curl -s https://comeddy.github.io/pai-playbook/mcp/ | grep -c 'tabbed-set'
```
Expected: `200`, `200`, `≥1`. Then re-run Step 1's `claude mcp add` **using the published URL download command from the guide** (`curl … --output "$HOME/.pai-playbook/server.mjs"` then `claude mcp add … "$HOME/.pai-playbook/server.mjs"`), confirm `✓ Connected`, and remove again. Only after this does the guide's "Claude Code 절차는 … 실제 등록·조회로 확인했다" sentence become true; if it fails, fix and re-ship before declaring done.

- [ ] **Step 4: Report** — show the user: commit hashes, pytest count, gate results, live URLs, and any unrelated uncommitted hunks intentionally left unstaged.
