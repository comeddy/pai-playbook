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
