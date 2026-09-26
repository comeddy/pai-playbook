# MCP 연결 — 서버 파일 + 설정 가이드 페이지 설계

_2026-09-26 · 승인됨 (형태: 서버 + 가이드 — 사용자 선택)_

## 목적

TTOBAK(ttobak.atomai.click/settings)의 "MCP 연결 가이드"와 같은 절차를 Playbook에도 둔다.
독자가 자기 AI 도구(Claude Code · Codex · Kiro CLI · Kiro Crew · Amazon Quick)에서
Playbook 페이지·Radar·근거 기록을 도구 호출로 읽을 수 있게 하고, 그 등록 절차를
4개 언어 페이지로 안내한다. 콘텐츠는 공개 리포이므로 로그인·인증은 없다.

## 구성 요소

| 파일 | 역할 |
|---|---|
| `docs/mcp/pai-playbook-mcp.mjs` | 단일 파일 stdio MCP 서버. mkdocs가 그대로 복사해 `https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs`로 배포 |
| `docs/mcp.md` (+ `.en/.zh/.ja`) | 가이드 페이지 "설정 · MCP 연결" — 클라이언트 탭 5개, stdio 단계, HTTP 미설정 안내 |
| `mkdocs.yml` | nav 마지막에 페이지 추가, `nav_translations` 3개 언어, `pymdownx.tabbed` 확장 추가 |
| `docs/index*.md` | '페이지 목록' 4개 언어에 링크 추가 (check_nav_index_sync 게이트) |
| `tests/test_mcp_server.py` | node 서브프로세스로 서버 프로토콜·도구 검증 |
| `.github/workflows/deploy-docs.yml` | `python -m pytest -q` 단계 1줄 추가 (현재 pytest 단계 없음) |
| `CHANGELOG.md` | 4개 언어 `[Unreleased] / Added` |

## 서버 사양 (`pai-playbook-mcp.mjs`)

- 실행: `node "$HOME/.pai-playbook/server.mjs"`. Node 18+ (내장 `fetch`). npm 설치 없음.
- 전송: stdio, 줄 단위(newline-delimited) JSON-RPC 2.0. 처리 메서드:
  `initialize`(클라이언트가 보낸 `protocolVersion`이 지원 목록 `2025-06-18 · 2025-03-26 · 2024-11-05`에 있으면 그대로 반환, 아니면 `2025-03-26`),
  `notifications/initialized`(무응답), `ping`, `tools/list`, `tools/call`.
  그 외 메서드는 `-32601`. 파싱 실패는 `-32700`. 응답 없는 알림(notification)에는 답하지 않는다.
- 콘텐츠 소스 (우선순위):
  1. 환경변수 `PAI_PLAYBOOK_DOCS_DIR`가 있으면 그 디렉터리(리포의 `docs/`)에서 파일 읽기 — 오프라인·테스트용.
  2. 없으면 `https://raw.githubusercontent.com/comeddy/pai-playbook/main/` 하위 `docs/<file>`·`mkdocs.yml`을 fetch. 실패 시 도구 결과 `isError: true`와 사유 문자열.
- 페이지 목록: `mkdocs.yml`의 `nav:` 블록을 `check_nav_index_sync.nav_targets`와 같은 정규식으로 파싱(`- 라벨: 파일.md`). 라벨을 제목으로 쓰고, 파일 stem이 page id(`start`, `pillar-2`, …).
- 언어: `ko`(원본, 파일 `<stem>.md`) · `en` · `zh` · `ja`(`<stem>.<lang>.md`). 번역 파일 상단 `---\nko_hash: …\n---` frontmatter는 제거해 반환.
- 캐시: 프로세스 내 Map, TTL 10분.
- 도구 4개 (inputSchema는 JSON Schema):
  - `playbook_list_pages` `{lang?}` → 페이지 id·제목·URL(`https://comeddy.github.io/pai-playbook/[<lang>/]<stem>/`) 목록 텍스트.
  - `playbook_read_page` `{page, lang?}` → 마크다운 원문. 없는 page → `isError`.
  - `playbook_search` `{query, lang?, limit?=20}` → 모든 페이지를 대소문자 무시 부분 일치로 검색, `page · 줄번호 · 줄 텍스트(200자 절단)` 스니펫. 랭킹 없음.
  - `playbook_evidence` `{claim_id?}` → `docs/assets/claims.json`. id 지정 시 해당 주장만, 없으면 전체 요약(id·상태·확인일·영향 페이지).
- 도구 결과는 `content: [{type:"text", text}]` 하나. 총 길이 상한 없음(페이지 1개 ≈ 수십 KB).
- 서버 `serverInfo`: `{name:"pai-playbook", version:"1.0.0"}`. 로그는 stderr로만.

## 가이드 페이지 사양 (`docs/mcp.md`)

- 제목 `# 설정 — MCP 연결`, 상단 `_최종 갱신: 2026-09 · owner: Youngjin · volatility: 낮음_`, 하단 `_owner: Youngjin · updated: 2026-09 · volatility: 낮음_`.
- L0 TL;DR: 무엇을 연결하는지(공개 콘텐츠, 로그인 없음), 어떤 도구가 생기는지 한 줄씩.
- 공통 안내 표: 서버 파일 URL · 실행 요건(Node 18+, macOS/Linux, Windows는 WSL) · 도구 4개와 용도.
- 클라이언트 탭 (`=== "Claude Code"` 등 pymdownx.tabbed, 순서는 TTOBAK과 동일: Claude Code · Codex · Kiro Crew · Amazon Quick · Kiro CLI). 각 탭 구조:
  1. 도입 한 문장.
  2. **① 서버 파일 다운로드**: `mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'`
  3. **② 등록**: 클라이언트별 명령/설정 —
     Claude Code `claude mcp add pai-playbook --transport stdio --scope user -- node "$HOME/.pai-playbook/server.mjs"`;
     Codex `codex mcp add pai-playbook -- node "$HOME/.pai-playbook/server.mjs"`;
     Kiro CLI `~/.kiro/settings/mcp.json`의 `mcpServers.pai-playbook = {command:"node", args:["ABSOLUTE_PATH"]}` + 절대경로 확인 `printf '%s\n' "$HOME/.pai-playbook/server.mjs"`;
     Kiro Crew: Agent Capabilities → Integrations (MCP)에 같은 JSON 병합, Discover & Sync → Probe All;
     Amazon Quick: HTTP 전용 — 미설정 안내만(아래).
  4. **③ 연결 확인**: `/mcp`(Claude Code·Kiro CLI) 또는 클라이언트의 상태 화면, 조회 예시 `Playbook에서 P2 모델 학습 페이지를 읽어줘`.
  5. **원격 · HTTP** 접힘 블록(`??? info "원격 · HTTP — 주소 미설정"`): "이 사이트에 공개 HTTP MCP 주소가 아직 등록되지 않았습니다. 아래는 절차 안내이며 자리표시를 실제 값으로 바꿔야 합니다." + 클라이언트별 자리표시 명령(Claude Code `claude mcp add --transport http --scope user --client-id 'YOUR_CLIENT_ID' --callback-port 9876 pai-playbook 'YOUR_HTTP_MCP_URL'`, Codex `codex mcp add pai-playbook --url 'YOUR_HTTP_MCP_URL' --oauth-client-id 'YOUR_CLIENT_ID'`, Kiro `{url, oauth:{clientId, redirectUri:"http://localhost:9876/callback"}}`, Quick 커넥터 URL·OAuth 필드).
- "연결 후 이렇게 요청하세요" 예시 4개: 페이지 읽기·검색·Radar·근거 기록.
- 검증 범위 문단: Claude Code는 이 리포 배포 후 실제 등록·조회로 확인했고, Codex·Kiro·Quick 명령은 공식 문서 기준 미검증(`[4]`)임을 명시. 각 클라이언트 공식 MCP 문서 링크(TTOBAK과 동일 URL 5개).
- 용어 각주 신설: `[^mcp]`(**MCP (Model Context Protocol)** — AI 도구가 외부 데이터·기능을 표준 방식으로 호출하게 하는 개방 프로토콜. 서버가 "도구"를 제공하고 Claude Code 같은 클라이언트가 호출한다), `[^stdio]`(**stdio 전송** — 클라이언트가 서버 프로그램을 자기 컴퓨터에서 직접 실행해 표준 입출력으로 통신하는 방식. 네트워크 주소·로그인이 필요 없다). 마커는 본문 첫 등장에만, 헤딩 금지. 4개 언어 동일 id.
- mermaid 없음. 표·탭·admonition만 사용(`admonition`·`pymdownx.details` 이미 활성).

## 검증 기준

1. `tests/test_mcp_server.py` (pytest, `node` 없으면 skip):
   `PAI_PLAYBOOK_DOCS_DIR=<repo>/docs`로 서버 기동 → `initialize` 응답 `protocolVersion`·`serverInfo.name=="pai-playbook"` →
   `tools/list` 이름 4개 정확히 일치 → `playbook_read_page {page:"start"}` 결과에 `# 시작` 포함 →
   `playbook_read_page {page:"start", lang:"en"}` 결과에 `ko_hash` 미포함 → `playbook_search {query:"Radar"}` 1건 이상 →
   `playbook_read_page {page:"nope"}` `isError: true` → 알 수 없는 메서드 `-32601`.
2. 커밋 게이트: `python3 scripts/check_evidence.py` · `check_translation_sync.py`(비동기 0) · `check_nav_index_sync.py` · `mkdocs build --strict` exit 0, 산출물 `site/mcp/pai-playbook-mcp.mjs` 존재.
3. 이 머신에서 `claude mcp add pai-playbook --transport stdio --scope user -- node <repo>/docs/mcp/pai-playbook-mcp.mjs` 후 `claude mcp list`에 ✓ 연결 표시 (원격 fetch 경로로 실제 raw.githubusercontent 접근 확인). 확인 후 등록은 제거.
4. 배포 후 서버 파일 URL이 200으로 서빙되는지(ship 스킬 절차).

## 범위 제외 (YAGNI)

- HTTP/OAuth 서버 구현(가이드는 TTOBAK처럼 "미설정" 상태로 자리표시만).
- 쓰기 도구, 검색 랭킹·형태소 분석, 결과 페이지네이션.
- Codex·Kiro·Quick 실기기 검증 — 미검증으로 표기.
- Windows 네이티브 경로(WSL 안내로 대체).
