---
ko_hash: 60b24afbc9edeb9509c8357229ca1bb17b1bce5d
---
# 设置 — MCP 连接

_最后更新: 2026-09 · owner: Youngjin · volatility: 低_

**L0 TL;DR**: 让你使用的 AI 工具（Claude Code、Codex、Kiro、Amazon Quick）通过工具调用读取 Playbook 页面、Radar 与证据记录。只需下载并注册一个 MCP[^mcp] 服务器文件。内容公开，因此不需要登录或 API 密钥。

## 连接的是什么 { #overview }

| 项目 | 值 |
|---|---|
| 服务器文件 | `https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs`（单文件，无需 npm 安装） |
| 运行要求 | Node.js 18+ · macOS/Linux 终端（Windows 使用 WSL）· 互联网（读取 GitHub raw 内容） |
| 连接方式 | 本地 · stdio[^stdio]（默认）· 远程 HTTP 未配置 |
| 内容 | 本站的 Markdown 原文（四种语言）与 `assets/claims.json` — 与网站内容一致，只读 |

提供 4 个工具：

| 工具 | 用途 |
|---|---|
| `playbook_list_pages` | 页面 id、标题、URL 列表 |
| `playbook_read_page` | 读取单个页面原文（`page`、`lang`） |
| `playbook_search` | 全页面字符串搜索 → 片段 |
| `playbook_evidence` | 证据记录摘要或单条主张详情 |

## 各客户端步骤 { #clients }

=== "Claude Code"

    由 Claude Code 运行本地 MCP 服务器。如已有注册，只需修改连接信息。

    **① 下载服务器文件**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② 在 Claude Code 中注册** — 在用户范围注册 `pai-playbook`。不会更改模型或工具审批设置。

    ```bash
    claude mcp add pai-playbook --transport stdio --scope user \
      -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ 确认连接** — 在 `/mcp` 中确认 `pai-playbook` 为 connected，然后发起实际查询。

    ```text
    /mcp
    ```

    ```text
    从 Playbook 读取 P2 模型训练页面
    ```

    ??? info "远程 · HTTP — 地址未配置"
        本站尚未注册公开的 HTTP MCP 地址。以下为步骤说明，需要把占位符（`YOUR_…`）替换为实际值才能使用。以公开 OAuth 客户端为准，需已注册回调 `http://localhost:9876/callback`。

        ```bash
        claude mcp add --transport http --scope user \
          --client-id 'YOUR_CLIENT_ID' --callback-port 9876 \
          pai-playbook 'YOUR_HTTP_MCP_URL'
        ```

    [Claude Code 官方 MCP 文档 ↗](https://code.claude.com/docs/en/mcp)

=== "Codex"

    在 Codex CLI 中注册本地 MCP 服务器的方法。命令以官方文档为准，本仓库未在真机上验证（`[4]`）。

    **① 下载服务器文件**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② 在 Codex 中注册**

    ```bash
    codex mcp add pai-playbook -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ 确认连接** — 重新打开 Codex 并发起查询。

    ```text
    在 Playbook 中搜索 'HyperPod'
    ```

    ??? info "远程 · HTTP — 地址未配置"
        需要把占位符替换为实际值。将命令显示的回调 URL 交给管理员注册，然后用 `codex mcp login pai-playbook` 登录。

        ```bash
        codex mcp add pai-playbook --url 'YOUR_HTTP_MCP_URL' \
          --oauth-client-id 'YOUR_CLIENT_ID'
        ```

    [Codex MCP 文档 ↗](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

=== "Kiro Crew"

    运行 Crew 的电脑上必须有服务器文件。步骤以官方文档为准，未在真机上验证（`[4]`）。

    **① 下载服务器文件**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② 在 Crew 中添加本地服务器** — 在 Agent Capabilities → Integrations (MCP) 中添加基于命令的服务器，或将下面的条目合并到 Crew 读取的 MCP 配置中。把路径占位符替换为实际绝对路径。

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

    **③ 发现·确认连接** — 用 Discover & Sync 应用配置，用 Probe All 确认连接，然后发起查询。

    ```text
    显示 Playbook Radar 的最新流入条目
    ```

    ??? info "远程 · HTTP — 地址未配置"
        在 Crew 仪表盘添加基于 URL 的服务器时，目前还没有可用地址。地址注册后，把 `YOUR_HTTP_MCP_URL` 填入服务器 URL。本服务器提供公开内容，不需要认证头。

    [Kiro Crew MCP 文档 ↗](https://kiro.dev/docs/crew/capabilities/mcp-tools.md)

=== "Amazon Quick"

    Amazon Quick 仅支持远程 HTTP MCP。本站尚无公开 HTTP 地址，目前无法连接。地址注册后按以下顺序进行（`[4]`）。

    1. 在 Connectors → Create for your team → Model Context Protocol (MCP) 中新建连接，输入服务器 URL `YOUR_HTTP_MCP_URL`。
    2. 认证方式取决于服务器端配置。公开内容服务器请选择无认证。
    3. 用连接器的 Sync 加载工具列表，然后发起查询。Quick 的任务超时为 60 秒。

    ```text
    总结 Playbook 决策树页面中 Cloud vs Edge 的判断标准
    ```

    [Amazon Quick MCP 文档 ↗](https://docs.aws.amazon.com/quick/latest/userguide/mcp-integration.html)

=== "Kiro CLI"

    在运行 Kiro CLI 的电脑上注册本地 MCP 服务器。配置以官方文档为准，未在真机上验证（`[4]`）。

    **① 下载服务器文件**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② 添加到 Kiro CLI 设置** — 将下面的条目合并到 `~/.kiro/settings/mcp.json` 的 `mcpServers` 中。保留现有服务器与审批设置，把路径占位符替换为实际绝对路径。

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

    **③ 确认连接**

    ```text
    /mcp
    ```

    ```text
    总结 Playbook 的 P4 Sim-to-Real 页面
    ```

    ??? info "远程 · HTTP — 地址未配置"
        需要把占位符替换为实际值。需已注册回调 `http://localhost:9876/callback`；重新认证使用 `/mcp auth`。

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

    [Kiro CLI MCP 文档 ↗](https://kiro.dev/docs/mcp/configuration.md)

## 连接后可以这样提问 { #prompts }

```text
从 Playbook 读取 P2 模型训练页面
```

```text
在 Playbook 中搜索 'Greengrass' 并告诉我相关页面
```

```text
把 Playbook Radar 的最新流入条目整理成表格
```

```text
把 Playbook 决策树中 Build vs Buy 的判断标准整理成表格
```

## 验证范围与限制 { #scope }

- Claude Code 的步骤已于 2026-09-26 通过在用户范围注册本仓库的服务器文件并确认 `/mcp` connected 与页面列表查询完成验证。Codex、Kiro Crew、Amazon Quick、Kiro CLI 的命令以各自官方文档为准，未验证（`[4]`）。
- 服务器读取 `main` 分支的 Markdown。网站更新前的已提交内容可能先出现；缓存为 10 分钟。
- 在证据记录（`assets/claims.json`）发布到网站之前，`playbook_evidence` 会返回"尚未发布"的提示。
- 服务器文件没有写入工具，也不处理凭证。离线使用可克隆仓库后设置环境变量 `PAI_PLAYBOOK_DOCS_DIR=<克隆目录>/docs`。
- 问题与改进建议请提交到 [GitHub 议题](https://github.com/comeddy/pai-playbook/issues)。

**➡️ 下一步行动**: 在你最常用的一个客户端注册，并在下次客户会议前用 `playbook_search` 搜索一个关键词试试。

<!-- 용어 각주 -->
[^mcp]: **MCP (Model Context Protocol)** — 让 AI 工具以标准方式调用外部数据与功能的开放协议。服务器提供"工具"，Claude Code 等客户端调用这些工具。
[^stdio]: **stdio 传输** — 客户端在本机直接运行服务器程序并通过标准输入输出通信的 MCP 连接方式。不需要网络地址或登录。

_owner: Youngjin · updated: 2026-09 · volatility: 低_
