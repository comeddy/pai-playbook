---
ko_hash: 21be7119020c5e687a3ef6fa2dff17a68b67dc3c
---
# Radar — キュー / ウォッチリスト


_最終更新: 2026-07 · owner: Youngjin · volatility: 高_
[← index へ](index.md)

> **L0 TL;DR**: 包含基準（[2.5 THE FILTER](maintenance.md#包含基準-the-filter)）はまだ通過していないものの、**注目すべきもの**。各項目は一行 — 成熟度ラベル + **なぜ待機中か**。ゲート（4 項目中 2 項目）を通過すると、担当ピラーの owner が標準テンプレートで昇格します。
>
> ⚠️ **ここにある項目を顧客提案で「成熟した能力」のように扱わないでください。** 華やかなデモがデプロイ可能性を覆い隠すことがよくあります。

---

## 🔬 モデル / アルゴリズム（検証待ち）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| Physical Intelligence **[π0.7](https://www.physicalintelligence.company/)** | 🔵 Research | 二次情報源のみ `[4]`、PI の一次確認なし | PI 公式リリース + 性能検証 |
| **[GR00T N1.6 / N1.7](https://github.com/NVIDIA/Isaac-GR00T) 商用ライセンス** | 🟡→ | 商用許可の主張が二次情報源のみ `[4]`（N1.5 はモデルカード上で明確に非商用 `[1]`） | ライブモデルカードでライセンス確定 |
| **[World-action models](https://developer.nvidia.com/isaac/gr00t)**（DreamZero → GR00T N2） | 🟡 Preview | GR00T N2「年末予定」、DreamZero は研究 | GA + 実デプロイ事例 |
| Google DeepMind **[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)**（ロボット学習用ワールドモデル） | 🟡 Preview | ワールドモデル自体はプレビュー、ロボット学習への適用は研究 | ロボットポリシー学習の検証事例 |
| **VLM ベースの SysID**（[Vid2Sid](https://arxiv.org/abs/2602.19359), [Swim2Real](https://arxiv.org/abs/2603.20827)） | 🔵 Research | 2026 プレプリント、単一ラボ | peer-review + 再現 |
| **VIRAL / [VideoMimic](https://www.videomimic.net/) / [Real2Render2Real](https://real2render2real.com/)**（visual sim-to-real at scale） | 🔵 Research | CVPR/CoRL 研究、本番ではない | 本番デプロイの証拠 |
| **Robbyant [LingBot-VLA](https://huggingface.co/robbyant) / [UnifoLM-VLA-0](https://huggingface.co/unitreerobotics)** | 🔵 Research | 二次情報源、検証なし | 一次確認 + AWS マッピング |

## 🖥️ シミュレーション / ツール（成熟度待ち）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** 物理エンジン | ⚪ Hype | 「430,000 倍」は反駁済み `[1]`、接触マニピュレーションで遅い | 独立ベンチマーク + 本番採用 |
| **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** | 🟡 Alpha | PyPI classifier「3-Alpha」`[1]`、本番ではない | Beta/GA への移行 |
| **[NVIDIA Newton](https://github.com/newton-physics/newton)** 物理エンジン | 🟡 Preview | Isaac Sim 6.0 で experimental バックエンド | GA + Isaac Lab 3.0 正式 |
| **[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)** | 🟡 Preview | 「Early Developer Release」、API 変動（最新 GA は 5.1） | 6.x GA 宣言 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) を sim-to-real 学習源として** | 🟢 GA（モデル）/🔵（実戦） | モデルは GA だが「ワールドモデルのデータで実デプロイ可能なポリシーを学習」はアーリーアダプターのみ。⚠️ **AWS 未ホスティング** | AWS マッピング強化 + 学習検証 |

## 🤖 ハードウェア / デプロイ（ロードマップ・デモ）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | Musk の主張のみ、生産未開始 | 検証されたデプロイ |
| **Hyundai·BD オールエレクトリック [Atlas](https://bostondynamics.com/atlas/)** | ⚪ ロードマップ | オールエレクトリック Atlas 製品版を公開（2026-07、BD 公式 `[3]`）。展開 2.5 万+台・生産能力 3 万/年はいずれも **2028 開始**、現在の実稼働 ~0。2026 は小規模パイロットのみ（現代 RMAC + Google DeepMind）。⚠️「第 5 世代」は誤称 | 実稼働出荷の開始 |
| **[Apptronik Apollo 2 + Robot Park](https://apptronik.com/)** | 🟡 パイロット | Mercedes-Benz・GXO で運用パイロット `[3]` + Google DeepMind Gemini Robotics データ提携（9 万平方フィート）。自律・商用拡大は未検証。AWS マッピングは一般的（データ→S3/SageMaker）、提携自体は Google `[4]` | 商用デプロイ規模 + 自律成果の検証 |
| **[1X Neo](https://www.1x.tech/neo)** 自律性 | 🟡 Preview | 製品は発売済みだが自律 ~60~70%、残りは VR 遠隔操作 | 真の自律性の検証 |
| **[Figure 03](https://www.figure.ai/)「8 時間自律シフト」** | ⚪ Hype | CEO のツイート、独立検証なし（Figure 02@BMW は検証済みパイロット） | 第三者による自律性監査 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 採用**（Doosan/LG/Samsung） | 🟢 GA（発表） | 採用は「発表」であって本番検証ではない | 本番事例の公開 |

## 🔗 エージェント / 接続（初期）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **MCP for robotics**（[ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) など） | 🔵 Research | 50+ サーバーがあるがオープンソース/デモ、本番なし（安全性・遅延・決定性が未検証） | 本番ハードニング事例 |
| **ROS 2 + LLM エージェント**（NASA JPL [ROSA](https://github.com/nasa-jpl/rosa), [RAI](https://github.com/RobotecAI/rai)） | 🔵 Research | ROSA(JPL) が最強の実例だが mock-ops。現場デプロイは限定的 | 現場での本番デプロイ |
| **エージェント物理安全標準**（[RoboGuard](https://arxiv.org/abs/2503.07885) など） | 🔵 Research | ISO は物理のみ、LLM の意味的リスク標準が不在 | 標準化の進展 |
| **[AgentCore Payments / Agent Registry](https://aws.amazon.com/bedrock/agentcore/)（ソウル）** | 🟡 Preview/未提供 | ソウルリージョン未提供（東京 Agent Registry ✅） | ソウルリージョン拡張 |

## 🆕 最新スキャン流入（2026-07-31 · 一次検証完了 2026-07-21）

<!-- 自動スキャン（arXiv/ウェブ）の流入分。2026-07-21 に一次ソース検証完了（検証エージェント 4 式、公式発表・arXiv 原文と照合）—— 昇格 0 件、訂正 6 件。THE FILTER を通過するまで顧客提案での使用禁止。定期更新は scripts/radar_scan.md を参照。 -->

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **[RLWRLD RLDX-1](https://huggingface.co/RLWRLD)**（デクステリティ優先のファウンデーションモデル） | 🟡 Preview | 重み公開は事実だが ⚠️「オープンソース」ではない —— RLWRLD Model License v1.0（非商用・商用配布禁止）`[3]`、7~9B のバリアント群（主力 8.1B）。RoboCasa/LIBERO/SIMPLER の SOTA は自社発表で独立再現なし（[aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws) が EC2 上で n=5 スモーク実測を提供 — 完全なベンチマーク再現ではありません）。AWS との関連はシミュレーションベンチマーキングに限定（非商用ライセンスが明示的に許可する用途、商用ポジショニング不可）—— 「関連の根拠なし」表記を更新（2026-07）。実顧客への展開 0 | 独立ベンチマーク再現 + 検証済みの展開事例 |
| **[NEURA Robotics × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale) 戦略的協業** | ⚪ Hype・ロードマップ | AWS 公式プレスで確認、2026-04-21 `[1]` —— AWS が primary cloud、Neuraverse ホスティング + NEURA Gym・SageMaker 連携を明記。ただしフルフィルメントセンターは原文で「展開機会を探る（explore）」段階 —— 実展開は 0。NEURA Gym RWTH Aachen などの訓練網拡大発表（2026-07-22）には AWS への言及なし —— 別トラックとして観察 | AWS インフラの実使用事例公開 + フルフィルメントセンター展開の検証 |
| **[Actuator Reality Shaping](https://arxiv.org/abs/2607.02205)**（zero-shot sim-to-real） | 🔵 Research | 実在確認（arXiv 2607.02205、2026-07-02）`[1]` —— 実機ハードウェア 4 種（ヒューマノイド歩行を含む）で検証、要約と原文が一致（訂正なし）。peer-review 未採択 | peer-review + 独立再現 |
| **[AgiBot World 2026](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)**（オープンソースの実世界ロボットマニピュレーションデータセット、5 段階で順次公開） | 🔵 Research | AgiBot 公式公開（HuggingFace `agibot-world/AgiBotWorld2026`、2026-07）`[4]` —— AgiBot G2 実機で収集した 100% 実世界データ、5 つの研究軸（模倣学習など）を段階的に公開予定、第 1 弾は商業・サービス環境で数百時間分。ライセンス・商用利用条件は未確認、独立ベンチマーク・学習検証事例なし | ライセンス確定 + 独立した学習検証（SOTA 再現）事例 |
| **[AXIS](https://arxiv.org/abs/2607.21588)**（コミュニティ駆動の成長型ロボット操作データエンジン） | 🔵 Research | 実在確認（arXiv 2607.21588、2026-07-23）`[4]` —— 8 大学 + Axis Robotics の共同、ブラウザベース MuJoCo-WASM テレオペでクラウドソーシングし IsaacSim で拡張。Franka アームでのシミュレーションのみ（207 タスク・5 万+ 軌跡）、π0.5 の continual pretraining で LIBERO-Plus が +4.9pp 向上と報告（自己申告ベンチマーク、独立再現なし）。著者自身が sim-to-real を今後の課題として明記 —— 実機では未検証 | peer-review + 実機での sim-to-real 検証 |
| **[AMD Ryzen AI Embedded X100 + Kria AI SoM](https://www.amd.com/en/products/embedded.html)**（ロボット向けエッジコンピュート、NVIDIA Jetson Thor に対抗） | ⚪ Hype・ロードマップ | AMD 公式発表 `[4]`（2026-07-24）—— Zen 5 CPU・RDNA 3.5 iGPU・XDNA 2 NPU による統合メモリ（最大 128GB）、Jetson Thor 比 FP32 3 倍・Intel 比マルチスレッド 2.1 倍を主張（自社ベンチマーク、独立検証なし）。SOM 量産は 2026 年 Q4 予定（Arbor・Congatec など）、現時点でロボットへのエッジ展開事例は 0 | 独立ベンチマーク + 実ロボットへのエッジ展開事例 |
| **[NVIDIA Cosmos 3 Edge](https://www.nvidia.com/en-us/ai/cosmos/)**（Cosmos 3 系列のオンデバイス 4B ワールドモデル+ポリシー） | 🟡 Preview | NVIDIA 公式発表 `[4]`（2026-07-21、HuggingFace/developer ブログ）—— Jetson Thor 上のオンデバイス推論で 15Hz のリアルタイムロボットポリシー制御（自己申告ベンチマーク、独立検証なし）、Cosmos 3 Edge Policy（DROID）で pick-and-place のファインチューニングに対応。既存の「Cosmos 3 を sim-to-real 学習源として」項目（🖥️ セクション）とは別に、エッジ展開の軸のみを扱う —— AMD Ryzen AI Embedded X100（本表）と並行して競合構図を観察。現時点で実際の量産ロボット展開事例は 0 | 独立ベンチマーク + 実際の量産ロボット展開事例 |
| **[Walden Robotics](https://www.waldenrobotics.com/news/walden-robotics-launches-from-stealth)**（Toyota Research Institute からのスピンアウト、Large Behavior Models ヒューマノイド） | 🟡 パイロット | 公式発表（2026-07-15）`[4]` —— 2026-01 に TRI からスピンアウト（創業者 Russ Tedrake、元 TRI SVP）、Toyota・Deviation Capital 共同リード + NVIDIA・Boeing・Samsung Ventures などが参加したシード 3 億ドル（バリュエーション 11 億ドル）。ヒューマノイド上半身+ホイール式移動ベース、Diffusion Policy・Large Behavior Models ベースの方策で、北米 Toyota 工場にて 2026-02 からパイロット→「本番転換」を自社主張、第三者検証なし | 第三者監査・独立検証 + 展開規模拡大の事例 |
| **[Generalist AI GEN-1](https://generalistai.com/blog/gen-1)**（幅広いエンドエフェクタに対応する embodied foundation model） | 🟡 Preview | Generalist AI 公式ブログ発表（2026-07）`[4]` —— 5 指ハンドから専用ツールまで約 9,000 種のエンドエフェクタ、実測データ 50 万+時間で事前学習、自己申告で成功率 99%・速度 3 倍を主張（独立再現なし）。Generalist AI は [pillar-1](pillar-1.md) で Cosmos WFM のデータ生成活用企業として既に言及されているが、GEN-1 モデル自体は別の新規事案 | 独立ベンチマーク再現 + 実展開事例 |
| **[Generative Bionics GENE.01](https://gbionics.ai)**（フルボディ・マルチモーダルスマートスキンのヒューマノイド） | 🟡 Preview | イタリアのスタートアップによる公式発表（2026-07-20）`[4]` —— 触覚・近接・力・温度を検知するフルボディスマートスキンと「physics-native AI」（Nature Machine Intelligence の peer-review 済み研究に基づくと自社主張）、主要な Physical AI ソフトウェアエコシステムにオープンソースのデジタルツインを公開した初のヒューマノイドと主張。Fincantieri 造船所での適用協業の発表のみで、実稼働・独立検証なし | 実稼働事例の公開 + 独立検証（センサー性能・安全性） |

## ⚰️ 廃止済み — 提案禁止（記録保存用）

| 項目 | 状態 | 代替 |
|---|---|---|
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 終了 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 終了 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 終了 (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 公開事例なし `[4]` | 現在は CUDA/NVIDIA（提案時にリスクを明示） |

> ⚠️ **噂への警戒（事実ではない）**: 「AWS IoT TwinMaker 廃止」は**誤情報** — TwinMaker は GA・新規顧客に開放（低速度）。SiteWise のメンテナンスと混同した第三者ブログの主張です。繰り返さないでください。→ [pillar-3](pillar-3.md)。

---

## 昇格手順（要約）

1. **キャプチャ**: 指定チャンネル/絵文字で候補を収集
2. **フィルタ**: [2.5 ゲート](maintenance.md#包含基準-the-filter)を適用（4 項目中 2 項目以上）
3. **通過時**: 担当ピラーの owner が[標準テンプレート](maintenance.md#標準テンプレート)で編入し、Radar から削除
4. **未達時**: ここに一行で保持し、昇格条件を明示

パイプライン全体 → [maintenance](maintenance.md#playbook-昇格パイプライン)。

---
_owner: Youngjin · updated: 2026-07 · volatility: 高（Radar は本質的に急速に変化します — 月次レビューを推奨）_
