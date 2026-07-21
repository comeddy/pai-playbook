---
ko_hash: 9be33fd9be739aa4ef7a81822f962963a7e8ed6f
---
# Radar — キュー / ウォッチリスト


_最終更新: 2026-07 · owner: comeddy · volatility: 高_
[← index へ](index.md)

> **L0 TL;DR**: 包含基準（[2.5 THE FILTER](maintenance.md#包含基準-the-filter)）はまだ通過していないものの、**注目すべきもの**。各項目は一行 — 成熟度ラベル + **なぜ待機中か**。ゲート（4 項目中 2 項目）を通過すると、担当ピラーの owner が標準テンプレートで昇格します。
>
> ⚠️ **ここにある項目を顧客提案で「成熟した能力」のように扱わないでください。** 華やかなデモがデプロイ可能性を覆い隠すことがよくあります。

---

## 🔬 モデル / アルゴリズム（検証待ち）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| Physical Intelligence **π0.7** | 🔵 Research | 二次情報源のみ `[4]`、PI の一次確認なし | PI 公式リリース + 性能検証 |
| **GR00T N1.6 / N1.7 商用ライセンス** | 🟡→ | 商用許可の主張が二次情報源のみ `[4]`（N1.5 はモデルカード上で明確に非商用 `[1]`） | ライブモデルカードでライセンス確定 |
| **World-action models**（DreamZero → GR00T N2） | 🟡 Preview | GR00T N2「年末予定」、DreamZero は研究 | GA + 実デプロイ事例 |
| Google DeepMind **Genie 3**（ロボット学習用ワールドモデル） | 🟡 Preview | ワールドモデル自体はプレビュー、ロボット学習への適用は研究 | ロボットポリシー学習の検証事例 |
| **VLM ベースの SysID**（Vid2Sid, Swim2Real） | 🔵 Research | 2026 プレプリント、単一ラボ | peer-review + 再現 |
| **VIRAL / VideoMimic / Real2Render2Real**（visual sim-to-real at scale） | 🔵 Research | CVPR/CoRL 研究、本番ではない | 本番デプロイの証拠 |
| **Robbyant LingBot-VLA / UnifoLM-VLA-0** | 🔵 Research | 二次情報源、検証なし | 一次確認 + AWS マッピング |

## 🖥️ シミュレーション / ツール（成熟度待ち）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **Genesis** 物理エンジン | ⚪ Hype | 「430,000 倍」は反駁済み `[1]`、接触マニピュレーションで遅い | 独立ベンチマーク + 本番採用 |
| **MuJoCo Warp** | 🟡 Alpha | PyPI classifier「3-Alpha」`[1]`、本番ではない | Beta/GA への移行 |
| **NVIDIA Newton** 物理エンジン | 🟡 Preview | Isaac Sim 6.0 で experimental バックエンド | GA + Isaac Lab 3.0 正式 |
| **Isaac Sim 6.0** | 🟡 Preview | 「Early Developer Release」、API 変動（最新 GA は 5.1） | 6.x GA 宣言 |
| **Cosmos 3 を sim-to-real 学習源として** | 🟢 GA（モデル）/🔵（実戦） | モデルは GA だが「ワールドモデルのデータで実デプロイ可能なポリシーを学習」はアーリーアダプターのみ。⚠️ **AWS 未ホスティング** | AWS マッピング強化 + 学習検証 |

## 🤖 ハードウェア / デプロイ（ロードマップ・デモ）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | Musk の主張のみ、生産未開始 | 検証されたデプロイ |
| **Hyundai·BD オールエレクトリック Atlas** | ⚪ ロードマップ | オールエレクトリック Atlas 製品版を公開（2026-07、BD 公式 `[3]`）。展開 2.5 万+台・生産能力 3 万/年はいずれも **2028 開始**、現在の実稼働 ~0。2026 は小規模パイロットのみ（現代 RMAC + Google DeepMind）。⚠️「第 5 世代」は誤称 | 実稼働出荷の開始 |
| **Apptronik Apollo 2 + Robot Park** | 🟡 パイロット | Mercedes-Benz・GXO で運用パイロット `[3]` + Google DeepMind Gemini Robotics データ提携（9 万平方フィート）。自律・商用拡大は未検証。AWS マッピングは一般的（データ→S3/SageMaker）、提携自体は Google `[4]` | 商用デプロイ規模 + 自律成果の検証 |
| **1X Neo** 自律性 | 🟡 Preview | 製品は発売済みだが自律 ~60~70%、残りは VR 遠隔操作 | 真の自律性の検証 |
| **Figure 03「8 時間自律シフト」** | ⚪ Hype | CEO のツイート、独立検証なし（Figure 02@BMW は検証済みパイロット） | 第三者による自律性監査 |
| **Cosmos 3 採用**（Doosan/LG/Samsung） | 🟢 GA（発表） | 採用は「発表」であって本番検証ではない | 本番事例の公開 |

## 🔗 エージェント / 接続（初期）

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **MCP for robotics**（ros-mcp-server など） | 🔵 Research | 50+ サーバーがあるがオープンソース/デモ、本番なし（安全性・遅延・決定性が未検証） | 本番ハードニング事例 |
| **ROS 2 + LLM エージェント**（NASA JPL ROSA, RAI） | 🔵 Research | ROSA(JPL) が最強の実例だが mock-ops。現場デプロイは限定的 | 現場での本番デプロイ |
| **エージェント物理安全標準**（RoboGuard など） | 🔵 Research | ISO は物理のみ、LLM の意味的リスク標準が不在 | 標準化の進展 |
| **AgentCore Payments / Agent Registry（ソウル）** | 🟡 Preview/未提供 | ソウルリージョン未提供（東京 Agent Registry ✅） | ソウルリージョン拡張 |

## 🆕 最新スキャン流入（2026-07 · 一次検証完了 2026-07-21）

<!-- 自動スキャン（arXiv/ウェブ）の流入分。2026-07-21 に一次ソース検証完了（検証エージェント 4 式、公式発表・arXiv 原文と照合）—— 昇格 0 件、訂正 6 件。THE FILTER を通過するまで顧客提案での使用禁止。定期更新は scripts/radar_scan.md を参照。 -->

| 項目 | ラベル | なぜ待機か | 昇格条件 |
|---|---|---|---|
| **RLWRLD RLDX-1**（デクステリティ優先のファウンデーションモデル） | 🟡 Preview | 重み公開は事実だが ⚠️「オープンソース」ではない —— RLWRLD Model License v1.0（非商用・商用配布禁止）`[3]`、7~9B のバリアント群（主力 8.1B）。RoboCasa/LIBERO/SIMPLER の SOTA は自社発表で独立再現なし。⚠️ AWS との関連の根拠なし（NVIDIA スタックベース）—— 従来表記を訂正。実顧客への展開 0 | 独立ベンチマーク再現 + 検証済みの展開事例 |
| **NEURA Robotics × AWS 戦略的協業** | ⚪ Hype・ロードマップ | AWS 公式プレスで確認、2026-04-21 `[1]` —— AWS が primary cloud、Neuraverse ホスティング + NEURA Gym・SageMaker 連携を明記。ただしフルフィルメントセンターは原文で「展開機会を探る（explore）」段階 —— 実展開は 0 | AWS インフラの実使用事例公開 + フルフィルメントセンター展開の検証 |
| **TACO**（VLA 後処理の自己修正器としての Tactile World Model） | 🔵 Research | 実在確認（arXiv 2607.02840、2026-07-03）`[1]` —— 4 機関の共同研究（「単一ラボ」表記を訂正）、Franka 実機 6 タスクで絶対 +44%p。peer-review 未採択 | peer-review + 独立再現 |
| **MotionWAM**（リアルタイム ヒューマノイド loco-manipulation 向け Foundation World Action Model） | 🔵 Research | 実在確認（arXiv 2606.09215、2026-06-08）`[1]` —— 3 機関の共同研究（「単一ラボ」表記を訂正）、Unitree G1 実機 9 タスクで 76.1%（GR00T-N1.7 比で絶対 +32%p）。peer-review 未採択 | peer-review + 独立再現 |
| **Kairos**（Regret-aware Native World-Action Model スタック） | 🔵 Research | 実在確認（arXiv 2606.16533、2026-06-15）`[1]`、コード公開。⚠️「フルスタック」は誇張 —— 実機クローズドループ検証なし（著者自身が今後の課題と認める）、シミュレーションとベンチマークに限定 | 実機クローズドループ検証 + 独立再現 |
| **Actuator Reality Shaping**（zero-shot sim-to-real） | 🔵 Research | 実在確認（arXiv 2607.02205、2026-07-02）`[1]` —— 実機ハードウェア 4 種（ヒューマノイド歩行を含む）で検証、要約と原文が一致（訂正なし）。peer-review 未採択 | peer-review + 独立再現 |
| **AgiBot 累計 1.5 万号機 + Longcheer ライン配備** | 🟡 パイロット | 累計**量産ラインオフ 1.5 万台**であり、15,000 号機は**顧客 Longcheer の工場に納品**（「自社工場」表記を訂正）+ 品質検査 1 ラインに G2 を 8 台 `[3]`。6 日間 99.99% デモ（作業 64,828 回・生産 17,625 個）は事実だがベンダー管理環境で独立検証なし；データセットのライセンスは [pillar-1](pillar-1.md) | 独立した生産性検証 + ライン拡大 |
| **1X NEO 25-DoF テンドン駆動ハンド** | 🟡 予約販売 | ハンド仕様（25-DoF・テンドン駆動・触覚スキン）は公式確認 `[3]`、「5 日で 1 万台完売」は 1X の自社主張で独立検証なし。**検証済みの消費者納品は 0**（$20k または $499/月、出荷は 2026 年後半予定）—— 初期の家庭配備はテレオペのパイロットで、自律率は 1X 推定 60~70% | 実納品の検証 + 自律マニピュレーション事例 |

## ⚰️ 廃止済み — 提案禁止（記録保存用）

| 項目 | 状態 | 代替 |
|---|---|---|
| **AWS RoboMaker** | 🔴 終了 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **SageMaker Edge Manager** | 🔴 終了 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **IoT Greengrass V1** | 🔴 終了 (2026-06-01) `[1]` | Greengrass V2 |
| **Gazebo Classic 11** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
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
_owner: comeddy · updated: 2026-07 · volatility: 高（Radar は本質的に急速に変化します — 月次レビューを推奨）_
