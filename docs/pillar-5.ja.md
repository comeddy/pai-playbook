---
ko_hash: bc6fff65fa54d83b3f5ddd5bca9e32e21a4c4221
---
# Pillar 5 — エージェントオーケストレーション (Agentic Orchestration)


_最終更新: 2026-07 · owner: Youngjin · volatility: 高（AgentCore の機能・リージョンが頻繁に拡張）_
_個別項目は別途表記がない限りページメタデータ（owner/updated/volatility）を継承します。項目ごとに owner を指定する場合は項目フッターを追加します。_
[← index へ](index.md)

> **L0 TL;DR**: LLM エージェントがロボット・設備を指揮する階層です。ここが **AWS が最も強いピラー**です — **[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) が GA(2025-10) かつソウルリージョン完全対応**、ツール呼び出しをリアルタイムで横取りする **Policy(Cedar) も GA(2026-03)**。構造としては **System 2（低速な LLM プランナー、クラウド）+ System 1（高速な制御、エッジ）** の分離が定石です。⚠️ Amazon DeepFleet は「LLM エージェント」ではなく倉庫ロボット協調の基盤モデルなので混同しないでください。

---

## このピラーで顧客が最もよく尋ねる質問 Top 3

1. **「LLM エージェントでロボット/設備を指揮するのは実際に可能ですか？AWS には何がありますか？」** → [Bedrock AgentCore](#1-amazon-bedrock-agentcore--ga)
2. **「リアルタイムロボットにエージェントをどう？エッジでオフラインでも？」** → [エッジエージェントオーケストレーション](#3-エッジエージェントオーケストレーション--preview参考アーキテクチャ)
3. **「エージェントが物理システムを制御するとき、安全はどう保証しますか？」** → [安全 & ガードレール](#5-安全--ガードレール--gaエージェント層--未解決物理-意味-gap)

> **安定原理（ほとんど変わらない）**: エージェントはロボットを「直接リアルタイム制御」しません。**高レベルの計画・ツール選択(System 2) はエージェントが、低レベルのリアルタイム制御(System 1) はエッジポリシーが**担います（→ [pillar-2](pillar-2.md)、[pillar-4](pillar-4.md)）。本番で実際に稼働しているのは (1) **倉庫フリート協調**(DeepFleet, CoEvolution) と (2) **開発/データワークロードのオーケストレーション**(OSMO) であり、ヒューマノイドのフルスタックエージェントや MCP-ロボット連携は大半が研究/デモです。

---

## 1. Amazon Bedrock AgentCore  🟢 GA

**L0 TL;DR**: 本番エージェント向けのマネージドスタック — Runtime、Memory、Gateway（ツール連携）、Identity、Observability、そして **Policy（Cedar ベースのリアルタイムツール呼び出しゲート）**。**ソウルリージョン完全対応**。ハーネスは無料、リソース使用量のみ課金。

**顧客ニーズ/課題**: 「エージェントを PoC から本番へ引き上げたい。セッション管理、ツール連携、権限・セキュリティ、可観測性を毎回自分で作りたくない。」

**ソリューション概要** `[1]`:

- **GA の経緯**: プレビュー 2025-07 → **GA 2025-10-13**。コンポーネント: **Runtime、Memory、Gateway、Identity、Observability、Built-in Tools（Browser·Code Interpreter）**。re:Invent 2025-12 で Policy·Evaluations プレビュー、episodic Memory GA、音声向けの双方向ストリーミング Runtime GA を追加。**Policy は 2026-03-03 GA**。
- **Policy（中核）**: Gateway と統合し、**すべての エージェント→ツール 呼び出しをリアルタイムで横取り**して、ポリシー(allow/deny) を ms 単位で評価します。自然言語で記述 → **[Cedar](https://www.cedarpolicy.com/)**（AWS のオープンソースポリシー言語）にコンパイル。**ソウルを含む 13 リージョンで GA**。→ 物理システムのツール呼び出しを制約する直接的なプリミティブ（第 5 項の安全）。
- **[Strands Agents SDK](https://strandsagents.com/)**（付随）: モデル・クラウド中立のオーケストレーション SDK、**1.0 到達（GA 級）**。Amazon Q Developer·Glue が内部利用。AgentCore とペアリング。（バージョン・指標は折りたたみブロック）
- **[Nova Act](https://nova.amazon.com/act)**（関連）: ブラウザ/UI 自動化エージェント、re:Invent 2025 **GA**。ベンダーが高いタスク信頼性を主張（数値は折りたたみブロック — 測定条件は非公開）。

**AWS マッピング**: サービス自体がマッピングです。ロボットスキルを Gateway にツールとして登録 → エージェントが自然言語の計画で呼び出し、Policy でゲーティング、Memory でセッション維持、Observability で追跡。

**意思決定基準**:

- 本番エージェント（セッション・ツール・権限・可観測性が必要）→ **AgentCore Runtime + Gateway + Policy**。
- 単純な単発推論 → Bedrock 直接呼び出しで十分、AgentCore は過剰。
- マルチエージェント·A2A → Strands 1.0。
- オフライン・低遅延のエッジが必要 → 第 3 項（エッジ）。

**顧客事例**: **AWS×SoftServe 自律生産ライン**(AgentCore + IoT Greengrass + Nova Pro + Jetson Thor) — Hannover Messe 2026 **デモ/ショーケース**([1]/[3])。

**➡️ 次のアクション**: 韓国顧客にまず **「AgentCore はソウルリージョン GA — データレジデンシー問題なし」** を確認させ（古い「ソウル非対応」情報を訂正）、ロボットスキルを Gateway ツールとして登録する PoC を提案します。価格は「ハーネス無料、リソースのみ課金」で安心させます。

**🔗 関連アセット**:

- プレイブック: [pillar-4 エッジ](pillar-4.md)
- [AgentCore 入門ワークショップ](https://catalog.workshops.aws/agentcore-getting-started/en-US) · [AgentCore Deep Dive ワークショップ](https://catalog.workshops.aws/agentcore-deep-dive/en-US)
- （社内 AgentCore ワークショップ — 要確認 ⚠️）
- [AWS Physical AI Toolchain](https://github.com/aws-samples/sample-aws-physical-ai-toolchain) — aws-samples。4 ピラー・フライホイールのリファレンスアーキテクチャ。⚠️ 現在 Available なのは NVIDIA OSMO 6.3 on EKS オーケストレーションのみ、Cosmos·Isaac Lab·GR00T·Strands+AgentCore エージェンティックレイヤーは Planned
- [Self-improving Physical AI](https://github.com/aws-samples/sample-self-improving-physical-AI) — aws-samples。Bedrock エージェントが Isaac Sim と実機 SO-ARM101/XGO2/Zumi を IoT 経由で制御、エージェントメモリで sim-to-real 反復学習
- [Agentic AI Robot — 産業安全モニタリング](https://github.com/aws-samples/sample-agentic-ai-robot) — aws-samples。AgentCore+IoT+ロボットの自律パトロール·エッジ推論デモ、AWS AI x Industry Week 2025 で展示、韓国語 README あり。⚠️ 実験·教育用と明記 — 本番環境向けではありません

<details markdown="1"><summary>🔄 揮発性データ（コンポーネント・リージョン・価格 — 2026-07 確認）</summary>

| コンポーネント | ステータス | ソウル |
|---|---|---|
| Runtime / Memory / Gateway / Identity / Observability / Built-in Tools | 🟢 GA | ✅ |
| Policy (Cedar ツールゲート) | 🟢 GA (2026-03) | ✅ |
| Evaluations | 🟡 Preview→ | ✅ |
| Payments | 🟡 Preview | ❌ |
| Agent Registry | — | ❌（東京 ✅） |

**価格**: ハーネス無料、リソースのみ。Runtime/Browser/Code Interpreter = $0.0895/vCPU-hr + $0.00945/GB-hr（秒単位）。Gateway $0.005/1,000 呼び出し。Memory 短期 $0.25/1,000 イベント、長期保存 $0.75/1,000 レコード·月。
**リージョン**: ソウル(ap-northeast-2) 全コア+Policy+Evaluations ✅。東京(ap-northeast-1) + Agent Registry ✅。（AWS 公式リージョン表 `[1]`、2026-07 に直接確認）
**Strands**: Python 1.0(2026-05-21)、TS 1.0(2026-04-30)、~16.7M ダウンロード/月(2026-06, `[3]`)。
**Nova Act**: 「90%+ タスク信頼性」 — Amazon 発表数値、測定条件は非公開(2025-12, `[3]`)。条件なしの断定的な引用は禁止。
</details>

---

## 2. System 2 + System 1 オーケストレーションパターン  🟢 GA（安定原理）

**L0 TL;DR**: エージェントオーケストレーションのアーキテクチャの骨格です。**重量級の VLM/LLM が 5~10Hz で計画・再計画(System 2)**、**軽量ポリシーが 50~200Hz で実行(System 1)**。この分離が「何をクラウドに、何をエッジに」を決定します。

**顧客ニーズ/課題**: 「大規模な推論モデルとリアルタイム制御をどうやって一つのシステムに収めるのか？」

**ソリューション概要** `[1]/[4]`: SayCan/PaLM-E(2022~23 研究) の系譜から進化しました。現在の支配的パターン = 高レベルプランナー（タスク分解・ツール呼び出し、低速）+ 低レベルアクションポリシー（高速）。例示数値（ベンダー公開、桁感覚用）: Figure Helix S2 7~9Hz + S1 200Hz(Figure, 2025)、GR00T N1 S1 diffusion ~10ms(NVIDIA, 2025)。⚠️ **パターン自体は標準ですが、全身ヒューマノイドのフルスタックは大半がパイロット/デモ**です。

**AWS マッピング**: **System 2 = クラウドの Bedrock AgentCore**（計画・ツールオーケストレーション・ガードレール）、**System 1 = エッジの Jetson**（リアルタイム制御、→ [pillar-4](pillar-4.md)）。遅延が許容されれば System 2 をクラウドに、そうでなければエッジオンボードに。

```mermaid
graph TD
    subgraph CLOUD["クラウド（遅延許容 · 秒単位）"]
        S2["System 2 · 低速な LLM プランナー<br>5~10Hz 計画/再計画 · ツール呼び出し<br>Bedrock AgentCore"]
        POL["Policy(Cedar) · ツール呼び出しゲート"]
        S2 --> POL
    end
    subgraph EDGE["エッジオンボード（リアルタイム · ミリ秒）"]
        S1["System 1 · 高速なアクションポリシー<br>50~200Hz リアルタイム制御<br>Jetson"]
    end
    POL -. 高レベル計画 · action chunking .-> S1
    S1 --> ROB["ロボット · 設備"]
```

**意思決定基準**: [decisions Cloud vs Edge](decisions.md) を参照。リアルタイム制御ループ → 無条件でエッジ。計画・再計画 → クラウド/非同期が可能。

**顧客事例**: Figure、GR00T（オープン）。検証済みの本番環境は限定的。

**➡️ 次のアクション**: 「エージェントがロボットをリアルタイム制御するのか？」という誤解に対し、**「エージェントは計画、リアルタイム制御はエッジポリシー」** として図を整理します。AgentCore（計画）+ Jetson（制御）の組み合わせを提示します。

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

**🔗 関連アセット**: [pillar-4 エッジデプロイ](pillar-4.md) · [pillar-1](pillar-1.md)

---

## 4. フリートオーケストレーション  🟢 GA（一部）/ mixed

**L0 TL;DR**: 複数のロボットを協調させる階層です。**実際の本番は倉庫フリート協調**(Amazon DeepFleet, CoEvolution) と **開発ワークロードのオーケストレーション**(NVIDIA OSMO) です。⚠️ DeepFleet は LLM エージェントではなく、マルチロボット協調の基盤モデルです。

**顧客ニーズ/課題**: 「数百~数千台のロボットをどうやって中央から協調・監視するのか？」

**ソリューション概要** `[1]/[3]`:

- **[Amazon DeepFleet](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model)** 🟢 — Amazon 倉庫ロボットフリート協調の生成型基盤モデル（「交通管制」）、移動時間効率を ~10% 改善、100 万台目のロボットとともに発表(2025-07)。**本番（Amazon 内部）**。⚠️ **LLM エージェントオーケストレーターではない** — マルチロボット RL の意味での「マルチエージェント」。誤分類は禁止。
- **[NVIDIA Isaac OSMO](https://developer.nvidia.com/osmo)** 🟢 — ロボティクスの**開発/データ/学習ワークロード**のオーケストレーション（合成データ・学習・RL・SIL）。GTC 2026 でコーディングエージェント(Claude Code/Codex/Cursor) を統合。⚠️ **現場ロボットフリートのリアルタイム制御ではない** — 開発パイプラインのオーケストレーション。
- **Formant** 🟡 — フリート管理 SaaS。数百の組織で運用中だが小規模（具体的な指標は `[3]` PitchBook/Crunchbase 基準 — 644 組織·<$5M ARR, 2026-05, 変動が頻繁）、未買収。
- **CoEvolution** — Lotte Global Logistics 417 スーパーストアのマルチフリート協調、30% 効率を主張（⚠️ 単一 [3] 出典、要再確認）。

**AWS マッピング**: IoT Core/Greengrass（フリート接続）+ AgentCore（オーケストレーションロジック）+ IoT FleetWise/SiteWise（テレメトリ）。DeepFleet 式の協調モデルは SageMaker で学習。

```mermaid
graph TD
    ORCH["オーケストレーションロジック<br>AgentCore"]
    CONN["接続層<br>IoT Core / Greengrass"]
    TEL["テレメトリ<br>IoT FleetWise / SiteWise"]
    TRAIN["協調モデル学習<br>SageMaker"]
    FLEET["ロボットフリート（倉庫 · AMR）"]
    ORCH --> CONN
    CONN --> FLEET
    FLEET -. 状態 · 位置 .-> TEL
    TEL --> ORCH
    TRAIN -. DeepFleet 式の協調モデル .-> ORCH
```

**意思決定基準**: 倉庫/AMR フリート協調 → 検証済み領域（DeepFleet 式アプローチを参照）。ヒューマノイドエージェントフリート → まだ初期。開発ワークロード → OSMO(NVIDIA) または AWS Batch/Step Functions。

**顧客事例**（⚠️ 韓国は初期/デモ/発表）: **Lotte Global Logistics×CoEvolution**(30%、単一出典)、**LG CNS** 倉庫デモ（ヒューマノイド+ロボット犬+モバイル）、**Naver** AI Agent Platform 2026 下半期予定（NVIDIA ブループリント）。

**➡️ 次のアクション**: フリート顧客に **「協調ロジックは AgentCore、接続は IoT、学習は SageMaker」** の 3 階層として整理します。DeepFleet を LLM エージェントと誤解しないよう正確に説明します。

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

## このピラーの正直な現実（SA 必読）

- **AgentCore はソウルリージョン完全対応**（Policy·Evaluations を含む）。「ソウル非対応」は GA 初期の話 — 現在は誤り。データレジデンシーを安心させてください。
- **Policy は GA(2026-03)** — 「プレビュー」と呼ばないこと。
- **DeepFleet ≠ LLM エージェントオーケストレーター。** 倉庫ロボット協調の基盤モデル（マルチロボット RL）。誤分類は禁止。
- **真の本番はフリート協調(DeepFleet/CoEvolution) と開発ワークロード(OSMO)。** MCP-ロボット連携とヒューマノイドのフルスタックエージェントは大半が研究/デモ。
- **LLM の意味的安全標準はない。** ISO は物理のみ。階層防御(Cedar Policy + ISO ロボット層) が正直な答え。
- **Lotte 30% など韓国数値は単一出典** — ハード引用の前に要再確認。

---
_owner: Youngjin · updated: 2026-07 · volatility: 高（AgentCore の機能・リージョンは折りたたみブロックで管理）· sources: [1] 公式, [3] ベンダー/press, [4] 研究/コミュニティ_
