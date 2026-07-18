---
ko_hash: be63066cfda3cea2fe37cf8958b3837afac82b48
---
# Decisions — 横断的な意思決定ツリー


_最終更新: 2026-07 · owner: 未定 ⚠️ · volatility: 中_
[← index へ](index.md)

> **L0 TL;DR**: 顧客が頻繁に直面する 4 つの分岐点を、散文ではなく**決定表/ツリー**で示します。各決定はピラーを横断します。急ぐ場合は該当する表だけを見て方向を定めてください。

目次: [1) Cloud vs Edge](#1-cloud-training-vs-edge-inference-境界) · [2) NVIDIA vs オープンソース](#2-nvidia-フルスタック-vs-オープンソース) · [3) GPU 確保戦略](#3-gpu-確保戦略) · [4) Build vs Buy](#4-build-vs-buy基盤モデル)

---

## 1) Cloud training vs Edge inference 境界

**核心的な問い: 「この推論はクラウドに置けるのか、それともエッジに置く必要があるのか？」**

最も重要な判別要素は**制御周波数**です。

```
推論周波数の要求は？
├─ 30~100Hz+ 反応型制御（バランス·力·把持·歩行·回避）
│     → 🔴 必ずエッジオンボード (Jetson Thor/Orin)。クラウド往復は不可。
│        System 1（軽量 diffusion/flow-matching ポリシー, sub-20ms）
│
├─ few-Hz ~ sub-1Hz 高レベルの計画·再計画·ツール選択·シーン理解
│     → 🟢 クラウド/非同期が可能 (Bedrock AgentCore, 大型 VLM)。
│        System 2（重量級 VLM プランナー, 5~10Hz またはそれ以下）
│
└─ 両方が必要（ほぼすべての実ロボット）
      → 🟡 分離デプロイ: System 2=クラウド, System 1=エッジ。
         action chunking で 2 つの rate を接続。← 標準アーキテクチャ
```

| 区分 | System 2（計画） | System 1（制御） |
|---|---|---|
| 周波数 | 5~10Hz 以下 | 50~200Hz |
| 遅延許容 | あり（非同期） | なし（sub-20ms） |
| 位置 | **クラウド** (AgentCore) またはオンボード | **エッジオンボード** (Jetson) |
| モデル | 大型 VLM/LLM | 軽量 diffusion/flow-matching |
| AWS | Bedrock AgentCore, EC2 | IoT Greengrass V2, SageMaker Neo, ONNX/TensorRT |

> **判定原則**: 「リアルタイムの安全·反応が絡むループならエッジ、考える時間があるならクラウド。」action chunking が橋渡しです。
> 根拠: [pillar-4 エッジ](pillar-4.md)、[pillar-2 System1/System2](pillar-2.md)、[pillar-5](pillar-5.md)。

---

## 2) NVIDIA フルスタック vs オープンソース

**核心的な問い: 「Isaac に全賭けするか、それともオープンソースで行くか？」**

```
ワークロードの性質は？
├─ フォトリアルなレンダリング + 合成データ生成(SDG) + フルスタック統合
│     → Isaac Sim/Lab (🟢 GA 5.1)。GPU は RTX 必須 (G6e/G7e)。
│
├─ 高速な RL 反復 · 微分可能物理 · クロスベンダー GPU · 軽量
│     → MuJoCo/MJX (🟢)。コンピュート GPU(P5 A100/H100) も活用可 → コスト優位。
│        Unitree 実使用 [1]（本番検証 → pillar-3）。
│
├─ ROS 2 ネイティブ統合 · CPU · 従来型ロボティクス
│     → Gazebo (🟢 Jetty/Harmonic)。⚠️ Classic 11 は EOL。GPU 並列 RL には不適。
│
└─ 「話題性」の Genesis？
      → ⚪ PoC/実験のみ。「430,000 倍」は反論済み [1]（→ pillar-3）。本番依存は禁止。
```

| 基準 | Isaac Sim/Lab | MuJoCo/MJX | Gazebo |
|---|---|---|---|
| 成熟度 | 🟢 GA 5.1 | 🟢 GA（Warp は Alpha） | 🟢 GA（Classic EOL） |
| GPU | **RTX 必須**（A100/H100 ✗） | コンピュート GPU 可能（P5 ✓） | CPU 中心 |
| レンダリング/SDG | 最高 | 限定的 | 限定的 |
| 微分可能 | △ | ✓ (JAX) | ✗ |
| ROS 統合 | 可能 | 補助 | **ネイティブ** |
| ライセンス | Apache（ソース）+AI Enterprise（再配布/SaaS） | Apache | Apache |
| AWS | G6e/G7e + AMI + Batch | EC2（P5 含む）+ Batch | EC2 + Batch |

> **判定原則**: ワークロードで選べばよいです。**「AWS は 3 つとも問題なく動かせる」** —— NVIDIA 依存を懸念する顧客に対する中立ポジション。MuJoCo ならコンピュート GPU を再活用できるコスト優位があります。
> 根拠: [pillar-3](pillar-3.md)。

---

## 3) GPU 確保戦略

**核心的な問い: 「GPU をどう確保するか？On-Demand が取れない。」**

```
学習の規模·期間は？
├─ 少数 GPU · 単発 · LoRA ファインチューニング（多くの出発点）
│     → On-Demand G7e/G6e。即時·柔軟。十分。
│
├─ 大規模 · 将来時点が確定 · 超大型クラスター(P6e-GB200 など)
│     → Capacity Blocks for ML。事前予約し、UltraServer を確保。
│
├─ 柔軟な日程 · コスト最適 · 数日~数週単位の学習ウィンドウ
│     → Flexible Training Plans (SageMaker HyperPod)。
│
└─ RTX レンダリングが必要 (Isaac Sim) vs コンピュートのみ (MuJoCo/VLA 学習)
      → レンダリング=G6e/G7e (RTX)、コンピュート=P5/P6 (A100/H100/B200) または MuJoCo なら P5 を再活用。
```

| 戦略 | いつ | AWS |
|---|---|---|
| On-Demand | 少数·単発·探索 | EC2 G7e/G6e/P6 |
| Capacity Blocks for ML | 大規模·時点確定·UltraServer | P6e-GB200、予約 |
| Flexible Training Plans | 柔軟な日程·コスト最適 | SageMaker HyperPod |
| Trainium | LLM 学習コスト削減 | Trn2/Trn3 ⚠️ **VLA は公開事例なし [4]**（→ pillar-2） |

> **判定原則**: 開始は On-Demand G7e。取れないか大規模なら Capacity Blocks/Flexible Training Plans。**Trainium は LLM には安全だが、VLA/ロボティクスは検証事例なし** —— 提案時にはリスクを明示します。
> 根拠: [pillar-2 学習スタック](pillar-2.md)、[pillar-3](pillar-3.md)。

---

## 4) Build vs Buy（基盤モデル）

**核心的な問い: 「基盤モデルをファインチューニングするか、それとも自前で学習するか？」**

```
データ·目標·リソースは？
├─ 実デモ 100~数千個 · 特定タスク · 迅速な結果
│     → オープン VLA のファインチューニング (LoRA)。単一 G7e、1 日 PoC。← 99% の現実
│        商用ならライセンス確認: π=Apache-2.0 ✅, OpenVLA=MIT ✅, GR00T=要確認 ⚠️
│
├─ 複数 embodiment · 大規模な実データ · バックボーンまで調整
│     → フルファインチューニング (P6/HyperPod)。70~100GB+ GPU。
│
├─ ゼロからの事前学習（フロンティア VLA を自社開発）
│     → 🔴 ごく少数のみ。マルチノード Blackwell クラスター·大規模な実データ。
│        大半の顧客には非推奨 —— ファインチューニングで十分。
│
└─ 推論·計画レイヤーのみ必要（低レベル制御は不要）
      → Gemini Robotics-ER(API) または AgentCore でオーケストレーション。
```

| オプション | データ | GPU | いつ |
|---|---|---|---|
| LoRA ファインチューニング | 100~数千デモ | 単一 24~40GB | **デフォルトの出発点** |
| フルファインチューニング | 大規模な実データ | 70~100GB+ / マルチノード | 複数 embodiment |
| 事前学習(Build) | 超大規模 | Blackwell クラスター | ごく少数のフロンティア |
| 推論レイヤーの Buy | — | — | 制御はオープンモデル、計画は API |

> **判定原則**: **ほぼ常にファインチューニング(Buy+adapt) が答えです。** ゼロからの事前学習はごく少数。商用ではライセンスが最初のゲート（GR00T の非商用に注意）。「シミュレーションだけで操作ポリシー」は落とし穴 —— 実データが必須（[pillar-4](pillar-4.md)）。
> 根拠: [pillar-2](pillar-2.md)、[pillar-1 データ·ライセンス](pillar-1.md)、[pillar-4](pillar-4.md)。

---

## 付録 — リージョン/データレジデンシーの迅速判定

_（下表は揮発性が高い —— 2026-07、AWS 公式リージョン表 `[1]` で直接確認した基準。引用前に最新のリージョン表を再確認）_

| サービス | ソウル(ap-northeast-2) | 備考 |
|---|---|---|
| Bedrock AgentCore（コア+Policy+Evaluations） | ✅ | Agent Registry·Payments は ✗（東京は Registry ✅）—— 2026-07 リージョン表基準 |
| EC2 G7e / G6e / P6 | ✅（リージョン別に確認） | Capacity Blocks を活用 |
| SageMaker HyperPod | ✅ | Flexible Training Plans はリージョン拡張中 |
| IoT Greengrass V2 | ✅ | V1 は 2026-06 EOL |

> データレジデンシーを懸念する顧客: まず **AgentCore ソウル GA** を確認させて安心させます（古い「ソウル未対応」情報を訂正）。→ [pillar-5](pillar-5.md)。

---
_owner: 未定 ⚠️ · updated: 2026-07 · volatility: 中（ツリーの原理は低、インスタンス/リージョンの詳細は高）_
