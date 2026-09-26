---
ko_hash: 60b24afbc9edeb9509c8357229ca1bb17b1bce5d
---
# Settings — MCP Connection

_Last updated: 2026-09 · owner: Youngjin · volatility: low_

**L0 TL;DR**: This setup lets your AI tool (Claude Code, Codex, Kiro, Amazon Quick) read Playbook pages, the Radar, and evidence records through tool calls. Download one MCP[^mcp] server file and register it; that is all. The content is public, so there is no login or API key.

## What gets connected { #overview }

| Item | Value |
|---|---|
| Server file | `https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs` (single file, no npm install) |
| Requirements | Node.js 18+ · macOS/Linux terminal (WSL on Windows) · internet access (reads content from GitHub raw) |
| Transport | Local · stdio[^stdio] (default) · remote HTTP not configured |
| Content | This site's markdown sources (four languages) and `assets/claims.json` — identical to the site, read-only |

Four tools are provided:

| Tool | Purpose |
|---|---|
| `playbook_list_pages` | List of page ids, titles, and URLs |
| `playbook_read_page` | Source of one page (`page`, `lang`) |
| `playbook_search` | Search a string across all pages → snippets |
| `playbook_evidence` | Evidence-record summary or one claim in detail |

## Per-client procedure { #clients }

=== "Claude Code"

    Claude Code runs the local MCP server. If a registration already exists, only update its connection details.

    **① Download the server file**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Register in Claude Code** — registers `pai-playbook` at user scope. Model and tool-approval settings are not changed.

    ```bash
    claude mcp add pai-playbook --transport stdio --scope user \
      -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ Verify the connection** — check in `/mcp` that `pai-playbook` is connected, then ask for a real lookup.

    ```text
    /mcp
    ```

    ```text
    Read the P2 model training page from the Playbook
    ```

    ??? info "Remote · HTTP — address not configured"
        No public HTTP MCP address is registered for this site yet. The steps below are for reference; replace the placeholders (`YOUR_…`) with real values before use. They assume a public OAuth client with the callback `http://localhost:9876/callback` registered.

        ```bash
        claude mcp add --transport http --scope user \
          --client-id 'YOUR_CLIENT_ID' --callback-port 9876 \
          pai-playbook 'YOUR_HTTP_MCP_URL'
        ```

    [Claude Code official MCP docs ↗](https://code.claude.com/docs/en/mcp)

=== "Codex"

    How to register a local MCP server in the Codex CLI. Commands follow the official docs and have not been verified on a real device in this repo (`[4]`).

    **① Download the server file**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Register in Codex**

    ```bash
    codex mcp add pai-playbook -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ Verify the connection** — reopen Codex and ask for a lookup.

    ```text
    Search the Playbook for 'HyperPod'
    ```

    ??? info "Remote · HTTP — address not configured"
        Replace the placeholders with real values. Send the callback URL the command prints to the administrator for registration, then log in with `codex mcp login pai-playbook`.

        ```bash
        codex mcp add pai-playbook --url 'YOUR_HTTP_MCP_URL' \
          --oauth-client-id 'YOUR_CLIENT_ID'
        ```

    [Codex MCP docs ↗](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

=== "Kiro Crew"

    The server file must be on the machine where Crew runs. The steps follow the official docs and have not been verified on a real device (`[4]`).

    **① Download the server file**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Add a local server in Crew** — in Agent Capabilities → Integrations (MCP), add a command-based server, or merge the entry below into the MCP config Crew reads. Replace the path placeholder with the real absolute path.

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

    **③ Discover and verify** — apply the config with Discover & Sync, confirm the connection with Probe All, then ask for a lookup.

    ```text
    Show me the latest intake items on the Playbook Radar
    ```

    ??? info "Remote · HTTP — address not configured"
        There is no address yet for adding a URL-based server in the Crew dashboard. Once one is registered, enter `YOUR_HTTP_MCP_URL` as the server URL. This server serves public content, so no authentication header is needed.

    [Kiro Crew MCP docs ↗](https://kiro.dev/docs/crew/capabilities/mcp-tools.md)

=== "Amazon Quick"

    Amazon Quick supports remote HTTP MCP only. This site has no public HTTP address yet, so it cannot be connected at the moment. Once an address is registered, proceed as follows (`[4]`).

    1. In Connectors → Create for your team → Model Context Protocol (MCP), create a new connection and enter the server URL `YOUR_HTTP_MCP_URL`.
    2. Authentication follows the server-side configuration. For a public-content server, choose no authentication.
    3. Use the connector's Sync to load the tool list, then ask for a lookup. Quick's task timeout is 60 seconds.

    ```text
    Summarize the Cloud vs Edge decision criteria from the Playbook decision trees page
    ```

    [Amazon Quick MCP docs ↗](https://docs.aws.amazon.com/quick/latest/userguide/mcp-integration.html)

=== "Kiro CLI"

    Registers a local MCP server on the machine where the Kiro CLI runs. The configuration follows the official docs and has not been verified on a real device (`[4]`).

    **① Download the server file**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Add to the Kiro CLI settings** — merge the entry below into `mcpServers` in `~/.kiro/settings/mcp.json`. Keep existing servers and approval settings, and replace the path placeholder with the real absolute path.

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

    **③ Verify the connection**

    ```text
    /mcp
    ```

    ```text
    Summarize the P4 Sim-to-Real page from the Playbook
    ```

    ??? info "Remote · HTTP — address not configured"
        Replace the placeholders with real values. The callback `http://localhost:9876/callback` must be registered; use `/mcp auth` to re-authenticate.

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

    [Kiro CLI MCP docs ↗](https://kiro.dev/docs/mcp/configuration.md)

## After connecting, ask like this { #prompts }

```text
Read the P2 model training page from the Playbook
```

```text
Search the Playbook for 'Greengrass' and tell me the related pages
```

```text
Put the latest intake items on the Playbook Radar into a table
```

```text
Put the Build vs Buy decision criteria from the Playbook decision trees into a table
```

## Verification scope and limits { #scope }

- The Claude Code procedure was confirmed on 2026-09-26 by registering this repo's server file at user scope and checking `/mcp` connected plus a page-list lookup. The Codex, Kiro Crew, Amazon Quick, and Kiro CLI commands follow their official docs and are unverified (`[4]`).
- The server reads markdown from the `main` branch. Committed content may appear before the site reflects it; the cache lasts 10 minutes.
- Until the evidence records (`assets/claims.json`) are published on the site, `playbook_evidence` returns a "not published yet" notice.
- The server file has no write tools and handles no credentials. For offline use, clone the repo and set the `PAI_PLAYBOOK_DOCS_DIR=<clone>/docs` environment variable.
- Report problems and suggestions as [GitHub issues](https://github.com/comeddy/pai-playbook/issues).

**➡️ Next action**: Register the one client you use most and try `playbook_search` with one keyword before your next customer meeting.

<!-- 용어 각주 -->
[^mcp]: **MCP (Model Context Protocol)** — An open protocol that lets AI tools call external data and functions in a standard way. A server exposes "tools" and a client such as Claude Code invokes them.
[^stdio]: **stdio transport** — An MCP connection mode in which the client runs the server program on the same machine and talks to it over standard input/output. No network address or login is needed.

_owner: Youngjin · updated: 2026-09 · volatility: low_
