---
ko_hash: 60b24afbc9edeb9509c8357229ca1bb17b1bce5d
---
# 設定 — MCP 接続

_最終更新: 2026-09 · owner: Youngjin · volatility: 低_

**L0 TL;DR**: 使っている AI ツール（Claude Code、Codex、Kiro、Amazon Quick）から Playbook のページ・Radar・根拠記録をツール呼び出しで読めるようにする設定。MCP[^mcp] サーバーファイル 1 つをダウンロードして登録すれば完了する。公開コンテンツなのでログインや API キーは不要。

## 何が接続されるか { #overview }

| 項目 | 値 |
|---|---|
| サーバーファイル | `https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs`（単一ファイル、npm インストール不要） |
| 実行要件 | Node.js 18+ · macOS/Linux ターミナル（Windows は WSL）· インターネット（GitHub raw からコンテンツ取得） |
| 接続方式 | ローカル · stdio[^stdio]（既定）· リモート HTTP は未設定 |
| コンテンツ | 本サイトの Markdown 原文（4 言語）と `assets/claims.json` — サイトと同一内容、書き込みなし |

提供ツール 4 つ:

| ツール | 用途 |
|---|---|
| `playbook_list_pages` | ページ id・タイトル・URL の一覧 |
| `playbook_read_page` | ページ 1 件の原文（`page`、`lang`） |
| `playbook_search` | 全ページの文字列検索 → スニペット |
| `playbook_evidence` | 根拠記録の要約または主張 1 件の詳細 |

## クライアント別手順 { #clients }

=== "Claude Code"

    Claude Code がローカル MCP サーバーを実行する。既存の登録がある場合は接続情報のみ修正する。

    **① サーバーファイルのダウンロード**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Claude Code に登録** — ユーザースコープに `pai-playbook` を登録する。モデルやツール承認の設定は変更しない。

    ```bash
    claude mcp add pai-playbook --transport stdio --scope user \
      -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ 接続確認** — `/mcp` で `pai-playbook` が connected になっていることを確認してから実際の照会を依頼する。

    ```text
    /mcp
    ```

    ```text
    Playbook から P2 モデル学習ページを読んで
    ```

    ??? info "リモート · HTTP — アドレス未設定"
        本サイトには公開 HTTP MCP アドレスがまだ登録されていない。以下は手順の案内であり、プレースホルダー（`YOUR_…`）を実際の値に置き換える必要がある。公開 OAuth クライアントを前提とし、コールバック `http://localhost:9876/callback` が登録されていること。

        ```bash
        claude mcp add --transport http --scope user \
          --client-id 'YOUR_CLIENT_ID' --callback-port 9876 \
          pai-playbook 'YOUR_HTTP_MCP_URL'
        ```

    [Claude Code 公式 MCP ドキュメント ↗](https://code.claude.com/docs/en/mcp)

=== "Codex"

    Codex CLI にローカル MCP サーバーを登録する方法。コマンドは公式ドキュメントに基づき、本リポジトリでは実機検証していない（`[4]`）。

    **① サーバーファイルのダウンロード**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Codex に登録**

    ```bash
    codex mcp add pai-playbook -- node "$HOME/.pai-playbook/server.mjs"
    ```

    **③ 接続確認** — Codex を再度開いて照会を依頼する。

    ```text
    Playbook で 'HyperPod' を検索して
    ```

    ??? info "リモート · HTTP — アドレス未設定"
        プレースホルダーを実際の値に置き換えること。コマンドが表示するコールバック URL を管理者に伝えて登録した後、`codex mcp login pai-playbook` でログインする。

        ```bash
        codex mcp add pai-playbook --url 'YOUR_HTTP_MCP_URL' \
          --oauth-client-id 'YOUR_CLIENT_ID'
        ```

    [Codex MCP ドキュメント ↗](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

=== "Kiro Crew"

    Crew を実行するマシンにサーバーファイルが必要。手順は公式ドキュメントに基づき、実機検証はしていない（`[4]`）。

    **① サーバーファイルのダウンロード**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Crew にローカルサーバーを追加** — Agent Capabilities → Integrations (MCP) でコマンド型サーバーを追加するか、Crew が読む MCP 設定に以下の項目をマージする。パスのプレースホルダーは実際の絶対パスに置き換える。

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

    **③ 検出・接続確認** — Discover & Sync で設定を反映し、Probe All で接続を確認してから照会を依頼する。

    ```text
    Playbook Radar の最新流入項目を見せて
    ```

    ??? info "リモート · HTTP — アドレス未設定"
        Crew ダッシュボードで URL 型サーバーを追加する際に使うアドレスがまだない。アドレスが登録されたら `YOUR_HTTP_MCP_URL` をサーバー URL に入力する。本サーバーは公開コンテンツのため認証ヘッダーは不要。

    [Kiro Crew MCP ドキュメント ↗](https://kiro.dev/docs/crew/capabilities/mcp-tools.md)

=== "Amazon Quick"

    Amazon Quick はリモート HTTP MCP のみ対応。本サイトには公開 HTTP アドレスがまだないため、現時点では接続できない。アドレスが登録されたら以下の順に進める（`[4]`）。

    1. Connectors → Create for your team → Model Context Protocol (MCP) で新しい接続を作成し、サーバー URL `YOUR_HTTP_MCP_URL` を入力する。
    2. 認証はサーバー側の設定に従う。公開コンテンツのサーバーなら認証なしを選ぶ。
    3. コネクタの Sync でツール一覧を反映し、照会を依頼する。Quick のタスク制限時間は 60 秒。

    ```text
    Playbook の意思決定ツリーページから Cloud vs Edge の判断基準を要約して
    ```

    [Amazon Quick MCP ドキュメント ↗](https://docs.aws.amazon.com/quick/latest/userguide/mcp-integration.html)

=== "Kiro CLI"

    Kiro CLI を実行するマシンにローカル MCP サーバーを登録する。設定は公式ドキュメントに基づき、実機検証はしていない（`[4]`）。

    **① サーバーファイルのダウンロード**

    ```bash
    mkdir -p "$HOME/.pai-playbook" && curl --fail --location --show-error \
      --output "$HOME/.pai-playbook/server.mjs" 'https://comeddy.github.io/pai-playbook/mcp/pai-playbook-mcp.mjs'
    ```

    **② Kiro CLI 設定に追加** — `~/.kiro/settings/mcp.json` の `mcpServers` に以下の項目をマージする。既存のサーバーと承認設定は維持し、パスのプレースホルダーは実際の絶対パスに置き換える。

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

    **③ 接続確認**

    ```text
    /mcp
    ```

    ```text
    Playbook の P4 Sim-to-Real ページを要約して
    ```

    ??? info "リモート · HTTP — アドレス未設定"
        プレースホルダーを実際の値に置き換えること。コールバック `http://localhost:9876/callback` の登録が必要で、再認証は `/mcp auth` を使う。

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

    [Kiro CLI MCP ドキュメント ↗](https://kiro.dev/docs/mcp/configuration.md)

## 接続後はこう依頼する { #prompts }

```text
Playbook から P2 モデル学習ページを読んで
```

```text
Playbook で 'Greengrass' を検索して関連ページを教えて
```

```text
Playbook Radar の最新流入項目を表に整理して
```

```text
Playbook の意思決定ツリーから Build vs Buy の判断基準を表に整理して
```

## 検証範囲と制限 { #scope }

- Claude Code の手順は 2026-09-26 に本リポジトリのサーバーファイルをユーザースコープに登録し、`/mcp` connected とページ一覧の照会で確認した。Codex・Kiro Crew・Amazon Quick・Kiro CLI のコマンドは各公式ドキュメントに基づき、未検証（`[4]`）。
- サーバーは `main` ブランチの Markdown を読む。サイト反映前のコミット内容が見えることがあり、キャッシュは 10 分。
- 根拠記録（`assets/claims.json`）がサイトに公開されるまでは、`playbook_evidence` は「まだ公開されていません」という案内を返す。
- サーバーファイルには書き込みツールがなく、資格情報も扱わない。オフライン利用はリポジトリをクローンし、環境変数 `PAI_PLAYBOOK_DOCS_DIR=<クローン>/docs` を設定すれば可能。
- 問題・改善提案は [GitHub Issues](https://github.com/comeddy/pai-playbook/issues) に残す。

**➡️ 次のアクション**: よく使うクライアント 1 つに登録し、次回の顧客ミーティング前に `playbook_search` でキーワード 1 つを検索してみる。

<!-- 용어 각주 -->
[^mcp]: **MCP (Model Context Protocol)** — AI ツールが外部データ・機能を標準的な方法で呼び出せるようにするオープンプロトコル。サーバーが「ツール」を提供し、Claude Code などのクライアントがそれを呼び出す。
[^stdio]: **stdio トランスポート** — クライアントがサーバープログラムを自分のマシンで直接実行し、標準入出力で通信する MCP 接続方式。ネットワークアドレスやログインは不要。

_owner: Youngjin · updated: 2026-09 · volatility: 低_
