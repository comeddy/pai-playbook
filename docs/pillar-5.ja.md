---
ko_hash: 301fcc497bdcab115a9021056c5f9f79cba38358
---
# Pillar 5 — エージェントオーケストレーション (Agentic Orchestration)


_最終更新: 2026-09 · owner: Youngjin · volatility: 高（AgentCore の機能・リージョンが頻繁に拡張）_
_個別項目は別途表記がない限りページメタデータ（owner/updated/volatility）を継承します。項目ごとに owner を指定する場合は項目フッターを追加します。_
[← index へ](index.md)

> **L0 TL;DR**: 業務計画・スキル呼出し・フリート接続を分け、必要なエージェント機能にAgentCoreを選びます。制御・安全・データ処理場所は[別途検証](operations.md)します。

---

> **確認範囲**：ページ更新日は全項目の再確認日ではありません。主要訂正の日付・再現/人の確認状態は[根拠](evidence.md)を参照し、既存項目の確認日は従来どおり適用します。

## このピラーで顧客が最もよく尋ねる質問 Top 3

> 質問は探索例であり、実測した問い合わせ頻度順位ではありません。

1. **「LLM エージェントでロボット/設備を指揮するのは実際に可能ですか？AWS には何がありますか？」** → [Bedrock AgentCore](#1-amazon-bedrock-agentcore--ga)
2. **「リアルタイムロボットにエージェントをどう？エッジでオフラインでも？」** → [エッジエージェントオーケストレーション](#3-エッジエージェントオーケストレーション--preview参考アーキテクチャ)
3. **「エージェントが物理システムを制御するとき、安全はどう保証しますか？」** → [安全 & ガードレール](#5-安全--ガードレール--gaエージェント層--未解決物理-意味-gap)

> **L0/L1**: 業務計画・観測ポリシー・低レベル制御・独立安全は別責任です。サービス発売と現場検証を区別します。

---

## 1. Amazon Bedrock AgentCore  🟢 GA

**L0 TL;DR**: AgentCoreはエージェント実行・ツールアクセス・認証・観測のサービスです。**サービスGAと現場検証、ソウル提供と韓国内処理を区別します。**

| 構成 | 検討する役割 | 限界 |
|---|---|---|
| Runtime | 業務計画エージェント実行 | ロボットの制御期限を保証する制御器ではありません |
| Gateway・Identity | 許可スキルAPIの接続・認証 | 完了・取消・重複排除は別途実装 |
| Policy | Gateway経由ツール呼出しの権限確認 | 物理状態確認・独立安全の代替ではありません |
| Memory・Evaluations | 文脈・評価 | 保存・推論処理場所を個別確認 |
| Observability | 業務・ツール追跡 | 機器・制御・安全ログとの関連付けが必要 |

**リージョン・データ訂正** `[1]`：ソウル利用可能だけでレジデンシを解決しません。[AWSクロスリージョン推論](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html)はMemory等の入出力が基本リージョン外で処理される場合を明記しています。ソウル発Evaluationsはグローバル推論対象です。機能・モデル・外部ツールごとに処理国を記録します（[根拠](evidence.md#agentcore-residency)）。

**判断基準**：単発推論はモデル直接呼出しから検討します。継続セッション・権限・追跡が必要な場合に構成要素を選びます。機能別[提供表](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)と[料金](https://aws.amazon.com/bedrock/agentcore/pricing/)を確認し、モデル/API・通信・ログも見積もります。「ハーネス無料」で総費用を説明しません。

**顧客事例**：既存AWS×SoftServe紹介はデモであり顧客生産ラインの運用実証ではありません。

**➡️ 次のアクション**：スキル入力・権限・完了取消の契約と処理経路を定め、[運用復旧試験](operations.md)へ接続します。

**🔗 関連アセット**:

- プレイブック: [pillar-4 エッジ](pillar-4.md)
- [AgentCore 入門ワークショップ](https://catalog.workshops.aws/agentcore-getting-started/en-US) · [AgentCore Deep Dive ワークショップ](https://catalog.workshops.aws/agentcore-deep-dive/en-US)
- [AgentCore リテールエージェントワークショップ「Build! Deploy! Observe!」](https://catalog.us-east-1.prod.workshops.aws/workshops/3cab1e1f-1dfa-42e0-959c-6e2e0a072ea3/ko-KR) — 韓国語。リテール事例ながら AgentCore の 7 サービス（Gateway・Runtime・Observability・Code Interpreter・Memory・Policy・Browser）すべてを 3 フェーズのハンズオンでカバー — Policy ガードレール・エスカレーション実習は第 5 項（安全 & ガードレール）との接点。ガイド: [ワークショップサイト](https://dxdbmmdwak6t8.cloudfront.net/)（イベント向け CloudFront 配信 — リンクの持続性は要確認 ⚠️）
- （社内 AgentCore ワークショップ — 要確認 ⚠️）
- [AWS Physical AI Toolchain](https://github.com/aws-samples/sample-aws-physical-ai-toolchain) — aws-samples。4 ピラー・フライホイールのリファレンスアーキテクチャ。⚠️ 現在 Available なのは NVIDIA OSMO 6.3 on EKS オーケストレーションのみ、Cosmos·Isaac Lab·GR00T·Strands+AgentCore エージェンティックレイヤーは Planned
- [Self-improving Physical AI](https://github.com/aws-samples/sample-self-improving-physical-AI) — aws-samples。Bedrock エージェントが Isaac Sim と実機 SO-ARM101/XGO2/Zumi を IoT 経由で制御、エージェントメモリで sim-to-real 反復学習
- [Agentic AI Robot — 産業安全モニタリング](https://github.com/aws-samples/sample-agentic-ai-robot) — aws-samples。AgentCore+IoT+ロボットの自律パトロール·エッジ推論デモ、AWS AI x Industry Week 2025 で展示、韓国語 README あり。⚠️ 実験·教育用と明記 — 本番環境向けではありません
- [Smart Machines — 産業設備ハイブリッド Physical AI](https://github.com/aws-samples/sample-smart-machines-physical-hybrid-ai) — aws-samples。エージェントがフリートテレメトリの異常検知→原因診断→チケット作成・パラメータ調整まで行うフルスタックデモ（マルチエージェントチャット・自然言語シナリオビルダー・KVS 映像→Bedrock 分析・Jetson YOLOWorld+VLM エッジモニタリング）。⚠️ README 明記のデモ — 現在ショベル（シミュレーションテレメトリ）のみ完動、ロボットアームは WIP

---

## 2. 業務計画とロボット制御の分離 { #2-system-2--system-1-オーケストレーションパターン--ga安定原理 }

**L0 TL;DR**: 業務計画エージェントとロボット実行・制御・安全を分けますが、モデル内部System 1/2と同一視しません。

**配置基準**：許容クラウド遅延・通信断時間・処理国を先に決めます。観測ポリシー・ローカル制御・独立安全は期限とリスク評価で配置します。Helixの両モデルがオンボードである点は[P2](pillar-2.md)・[根拠](evidence.md#action-chunking)を参照します。

**AWSマッピング**：AgentCoreは条件を満たす業務計画の選択肢です。スキル呼出しにはID・期限・前提・完了確認が必要で、action chunkingだけで通信遅延や安全を解決できません。

**➡️ 次のアクション**：[運用](operations.md)の4階層図・障害表で担当、取消、復旧を設計します。

**🔗 関連アセット**: [pillar-2 VLA 構造](pillar-2.md) · [pillar-4 エッジ](pillar-4.md) · [decisions](decisions.md)

---

## 3. エッジエージェントオーケストレーション  🟡 Preview（参考アーキテクチャ）

**L0 TL;DR**: オフライン・低遅延の現場でエージェントをエッジデバイスにデプロイするパターンです。AWS **Solutions Guidance("AI Agents to Device Fleets via IoT Greengrass")** が実在する参考アーキテクチャ — ただし **GA 製品ではなくガイダンス/サンプルコード**です。

**顧客ニーズ/課題**: 「工場がオフライン/低帯域だ。クラウドなしでもエージェントが現場で判断できるようにしたい。」

**ソリューション概要** `[1]/[3]`: AWS Guidance = **[IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) デバイスに Strands Agents + ローカル SLM([Ollama](https://ollama.com/))** をデプロイ。GGUF モデルを S3 にプッシュし、IoT Core MQTT でクエリ、Orchestrator Agent が専門エージェント（文書・OPC-UA など）へファンアウト。接続されると Bedrock クラウドモデルへ切り替え。対象産業に **ロボティクス** を明示。2026 パターン: 学習済みモデル → Greengrass で Jetson Thor にデプロイ、VDA 5050 プロトコル変換で AMR フリートを協調。

**AWS マッピング**: IoT Greengrass V2 + Strands + ローカル SLM(Ollama) + IoT Core(MQTT) + S3（モデル）。オンライン時は Bedrock/AgentCore へ昇格。

**意思決定基準**: オフライン・データ主権・低遅延 → エッジエージェント。常時接続・複雑な推論 → クラウドの AgentCore。

**顧客事例**: AWS×SoftServe（上記の第 1 項、デモ）。

**➡️ 次のアクション**: オフライン顧客に **AWS Greengrass エージェント Guidance + サンプルコードを出発点として** 提示します（GA 製品ではないことを正直に）。オン/オフラインのハイブリッド（エッジ SLM ↔ クラウド AgentCore）を設計します。

**🔗 関連アセット**: [pillar-4 エッジデプロイ](pillar-4.md) · [pillar-1](pillar-1.md) · [MCP+MQTT on AWS IoT Core パターン](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/) — 公式ブログ。ロボット・エッジ機器を MCP ツールのように扱う Physical AI エージェントを IoT Core(MQTT) 上に編む実戦パターン — エッジ運用(P4)と多数機器の協調(P5)をつなぐ現行の標準経路

---

## 4. フリート運用 — 製品・制御・クラウドの境界 { #4-フリートオーケストレーション--ga一部-mixed }

**L0 TL;DR**: 現場の作業・交通調整、機器運用、開発ジョブのスケジューリングは別問題です。要件に合わせ既存製品・SI・自社ロジックを比較します。

**参照範囲**：[Amazon DeepFleet](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model)はAmazon内部事例で、購入できるAgentCore機能ではありません `[3]`。[NVIDIA OSMO](https://developer.nvidia.com/osmo)は開発・データ・学習用であり、現場交通制御と区別します。

**AWSマッピング**：IoT Core/Greengrass接続・状態収集と必要な保存・分析を設計します。業務計画にエージェントが必要な場合のみAgentCoreを検討します。衝突回避・作業割当・オフライン復旧はロボット/フリート側の責任範囲を明示します。

**FleetWise訂正** `[1]`：[AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)は**新規受付停止**です。既存顧客は利用を継続できますが、新規構成の既定案には含めません（[根拠](evidence.md#fleetwise-new-customers)）。

**顧客事例**：[Certis巡回ロボット](https://aws.amazon.com/blogs/physical-ai/how-certis-achieved-autonomous-robot-security-patrols-with-aws/)はAWS公開事例ですが他顧客への効果保証ではありません。

**➡️ 次のアクション**：製品境界、完了、通信断、介入、復旧を[カード](start.md#pilot)に記載し、[障害試験](operations.md#failure)を行います。

**🔗 関連アセット**: [pillar-2 学習](pillar-2.md) · [pillar-3 OSMO](pillar-3.md)

---

## 5. 安全 & ガードレール  🟢 GA（エージェント層）/ 🔵 未解決（物理-意味 gap）

**L0 TL;DR**: エージェントが物理システムを制御するとき、安全は**階層防御**で担保します。**AgentCore Policy(Cedar) が エージェント→ツール 呼び出しをゲーティング**し、ロボット層は **ISO 決定論的安全層**が担います。⚠️ 現行標準(ISO) は物理安全のみをカバーし、**LLM の意味的リスク（幻覚・脱獄）をカバーする標準はまだありません** — 正直な未解決問題です。

**顧客ニーズ/課題**: 「エージェントが誤判断してロボットが危険な行動をしたら？どう防ぐのか？」

**ソリューション概要** `[1]/[4]`:

- **エージェント層（AWS ネイティブ）**: **AgentCore Policy** — すべての エージェント→ツール 呼び出しを Cedar でリアルタイムに allow/deny(ms)。物理アクションのツール呼び出しを制約する実用層。**[Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)** — LLM の入出力（コンテンツ・トピック・PII）をフィルタ（アクチュエーション自体ではない）。
- **ロボット層（機能安全）**: **[ISO 10218-1/2](https://www.iso.org/standard/73933.html)**（ロボット・統合システム）、**ISO/TS 15066**（協働ロボット）、**ISO 13482**（個人支援ロボット）。⚠️ これらは**物理安全のみ** — LLM の意味的悪用/幻覚は未カバー。
- **研究**: RoboGuard（安全ルールの grounding）、BadRobot（組み込み LLM 脱獄攻撃）、LLM 意味的 DoS — 🔵 研究段階。標準が機能安全(ISO) と LLM リスクをつなげない**未解決の gap**。

**AWS マッピング**: AgentCore Policy(Cedar) + Bedrock Guardrails（エージェント層）+ ロボットオンボードの決定論的安全（ISO 準拠、AWS 外）。

**意思決定基準**: 物理アクションエージェント → **必ず階層防御**（AgentCore Policy でツールゲーティング + ロボットオンボードの ISO 安全層）。どちらか一方だけでは不十分。「エージェントが自ら安全を保証する」は禁止。

**顧客事例**: （本番の安全事例は非公開/初期）

**➡️ 次のアクション**: 安全の質問に対し **「エージェント層は AgentCore Policy/Cedar でツール呼び出しをゲーティング、ロボット層は ISO 決定論的安全 — 二重防御」** を提示します。「LLM の意味的リスク標準はまだない」と正直に認め、階層防御で補完する角度で。

**🔗 関連アセット**: [pillar-4 エッジ](pillar-4.md) · （社内エージェント安全ガイド — 新規作成が必要 ⚠️）

---

## 6. 物理世界のエージェント標準 — Anthropic MHS & AWS Strands Robots  🟡 Research Preview

**L0 TL;DR**: 2026-08-27、Anthropic が **[Model Hardware Standard(MHS)](https://www.anthropic.com/news/model-hardware-standard-research-preview)** の research preview を公開 — AI エージェントが物理デバイス（顕微鏡・liquid handler・ロボットアーム）を **標準化されたドライバー（read/write primitive）** で操作し、複数デバイスを並列オーケストレーションできるようにする共有規格です。MCP がデータ・ツールに対して果たしたことのハードウェア版。**AWS は Strands Robots で MHS をサポート**（preview 参加者向けの private pre-release）、**Doosan Robotics（韓国）がローンチパートナー**。⚠️ research preview — 顧客への本番提案は禁止、方向性の指標としてのみ。

**顧客ニーズ/課題**: 「デバイスごとにカスタム統合（数週間~数か月）を繰り返している。エージェント-ハードウェア連携に標準はないのか？」

**ソリューション概要** `[1]/[3]`:

- **動作方式**: デバイスを read（例: get temperature）/write（set temperature）の primitive 集合として公開する **標準ドライバー** + 自然言語タグから生成される reference file（そのデバイスの測定・調整可能な項目と **強制される安全限界（safety limits）** を記載）。エージェントは 3 つのメカニズム（MCP・CLI・code files/API）でデバイスを制御し、手順を組み、結果を観測してリアルタイムでパラメータを調整します。model-agnostic — 統合期間が数週間~数か月から数時間~数分に縮むというのが核心の主張です。
- **AWS の立ち位置**: Anthropic の発表文が "AWS will support MHS through **Strands Robots**, the library for connecting AI agents to physical devices" と明記。公開されている [strands-labs/robots](https://github.com/strands-labs/robots)（Apache-2.0 — Strands Agents + GR00T VLA + LeRobot 統合のロボット制御ライブラリ）につながりますが、⚠️ **公開パッケージ自体は MHS に言及していません** — MHS 対応ビルドは別の private pre-release です。
- **韓国との関連性** `[3]`: Doosan Robotics がローンチパートナーとして、ロボットアームでの自動品質検査（QA）・複数ロボットの協調に MHS をテスト中（Universal Robots・Tecan・QIAGEN などとともに）。
- **正直な限界**: LLM は物理世界をテキスト・画像で学ぶため、**空間・物理の推論には専門家の監督が依然として必要** — Anthropic 自身、Genentech の研究者が「サンプルの foaming はソフトウェアのバグではなく物理的な失敗」であることを Claude に教える必要があった例を挙げています。オープンソース化が予定されています。

**AWS マッピング**: AgentCore（1 番）がエージェントランタイム・Policy ゲートを、MHS/Strands Robots がデバイス接続標準を担う絵 — 5 番の多層防御の「ツールゲート」の下に **「デバイスドライバー + safety limits」** の層がもう一つ生まれる形です。

**意思決定基準**: 今日の設計に入れる段階ではありません（research preview）。ただしデバイス統合のバックログが大きい顧客（ラボ自動化・多品種セル）には **ウォッチリスト第一候補** として案内。

**顧客事例**: Doosan Robotics（ローンチパートナー、テスト段階）`[3]`。

**➡️ 次のアクション**: MCP をすでに使っている顧客に **「MCP はデータ・ツール、MHS はハードウェア」** のフレームで紹介し、公開されたら Strands Robots 経由の検証 PoC を計画します。それまでの現行の代替は [MCP+MQTT on IoT Core パターン](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/)（3 番の関連アセット）です。

**🔗 関連アセット**: [strands-labs/robots](https://github.com/strands-labs/robots) · [pillar-4 エッジ](pillar-4.md)

---

## このピラーの正直な現実（SA 必読）

- **ソウル提供と処理場所を分けます。** 機能・モデル・経路ごとに[クロスリージョン推論](evidence.md#agentcore-residency)を確認します。
- **Policy は GA(2026-03)** — 「プレビュー」と呼ばないこと。
- **DeepFleet ≠ LLM エージェントオーケストレーター。** 倉庫ロボット協調の基盤モデル（マルチロボット RL）。誤分類は禁止。
- **真の本番はフリート協調(DeepFleet/CoEvolution) と開発ワークロード(OSMO)。** MCP-ロボット連携とヒューマノイドのフルスタックエージェントは大半が研究/デモ。
- **LLM の意味的安全標準はない。** ISO は物理のみ。階層防御(Cedar Policy + ISO ロボット層) が正直な答え。
- **Lotte 30% など韓国数値は単一出典** — ハード引用の前に要再確認。

---
_owner: Youngjin · updated: 2026-09 · volatility: 高（AgentCore の機能・リージョンは折りたたみブロックで管理）· sources: [1] 公式, [3] ベンダー/press, [4] 研究/コミュニティ_

<!-- 용어 각주 -->
