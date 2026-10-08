---
ko_hash: 88810e6a4d48cdc1304577555aa665bc9fd2690b
---
# Physical AI Playbook

_最終更新: 2026-09 · owner: Youngjin · volatility: 中_

**L0 TL;DR**: 顧客のロボット業務に合う技術を判断し、AWSで実験・評価・運用へ進む案内です。業務適合性・総費用・実行条件を先に確認します。

!!! info "非公式資料"
    個人が運営する資料でありAWS公式文書・見解ではありません。技術・ライセンス・料金・リージョンはリンク先一次資料と確認日を見ます。サンプルコードやサービスGAは現場成果を保証しません。

## 役割別に開始

| 役割 | 経路 | 成果物 |
|---|---|---|
| 顧客意思決定者 | [開始・ROI](start.md) → [経営層資料](exec.md) | 業務・代替・予算・承認条件 |
| 顧客技術者 | [実行](execution.md) → 対象ピラー → [運用](operations.md) | 結果・費用・配備復旧の証拠 |
| AWS担当者 | [対話ガイド](exec-guide.md) → [判断](decisions.md) | ヒアリング・適合判断・引継ぎ |

## 技術参照 — 5つのピラー

| ピラー | 内容 |
|---|---|
| [P1 データ](pillar-1.md) | 収集・権利・形式・品質・学習パイプライン |
| [P2 学習](pillar-2.md) | 選定・ライセンス・資源見積・評価 |
| [P3 シミュレーション](pillar-3.md) | 環境・ツール・並列実行・費用 |
| [P4 Sim-to-Real](pillar-4.md) | 実機移行・エッジ配備・検証・安全 |
| [P5 オーケストレーション](pillar-5.md) | 業務計画・スキル・権限・接続 |

## ラベルと検証範囲

GA/Preview/Researchは**発売状態**です。原文照合・再現・現場検証、用途、支援主体は別に確認します。`[1]`公式資料論文、`[2]`記録付き再現、`[3]`メーカー発表、`[4]`未確認は出典種別で、AWS承認ではありません。[根拠](evidence.md)と[維持管理](maintenance.md)を参照します。

以下は探索用の質問例で、実測した問い合わせ頻度順位ではありません。質問から入り、提案前に[カード](start.md#pilot)を確認します。

## よくある質問 Top 20

| # | 質問 | 行き先 | 出典 |
|---|---|---|---|
| 1 | 「Isaac Sim / Isaac Lab を AWS でどう動かしますか?」 | [pillar-3](pillar-3.md) | シード ⚠️ |
| 2 | 「VLA モデル学習（ファインチューニング）のインフラはどう組めばよいですか?」 | [pillar-2](pillar-2.md) | シード ⚠️ |
| 3 | 「GPU が確保できません — On-Demand、Capacity Blocks、代替案のうち何を使うべきですか?」 | [decisions](decisions.md) | シード ⚠️ |
| 4 | 「sim-to-real[^s2r] gap は実際どう克服しますか? 検証済みの方法はありますか?」 | [pillar-4](pillar-4.md) | シード ⚠️ |
| 5 | 「ロボットのリアルタイム制御（30–100Hz）ですが、推論をクラウドに置けますか?」 | [decisions](decisions.md) | シード ⚠️ |
| 6 | 「基盤モデル（GR00T/π0 など）をファインチューニングしますか、自前で学習しますか?」 | [decisions](decisions.md) | シード ⚠️ |
| 7 | 「ロボット学習データをどう集め、どこに蓄積すべきですか?（テレオペレーション/合成データ）」 | [pillar-1](pillar-1.md) | シード ⚠️ |
| 8 | 「NVIDIA フルスタックにどれだけ依存しますか? オープンソース代替案は?」 | [decisions](decisions.md) | シード ⚠️ |
| 9 | 「エッジデプロイ（Jetson など）と AWS をどう連携しますか?」 | [pillar-4](pillar-4.md) | シード ⚠️ |
| 10 | 「LLM エージェント[^agent]でロボット/設備を指揮するアーキテクチャは実際に成り立ちますか?」 | [pillar-5](pillar-5.md) | シード ⚠️ |
| 11 | 「これを全部回すと GPU コストはどれくらい? 予算はどう見積もりますか?」 | [start](start.md) | [AWS Embodied AI ブログ](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | 「既存の ROS 2[^ros] スタック・rosbag[^rosbag] データを AWS とどう連携しますか?」 | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac ブログ](https://aws.amazon.com/blogs/robotics/) |
| 13 | 「複数ノードに学習をスケールするには? AWS Batch vs SageMaker HyperPod?」 | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | 「実機デプロイ前にポリシーが実際に動くかをどう検証・ベンチマークしますか?」 | [pillar-4](pillar-4.md) | [NVIDIA ポリシー評価](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | 「ロボット/工場データが機微ですが、クラウド学習は規制上問題ないですか? オンプレ・ハイブリッドは?」 | [decisions](decisions.md) | [AWS AI 主権](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | 「学習したポリシーをどうバージョン管理・再現し、チェックポイントを復旧しますか?」 | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | 「Isaac Sim・オープンモデルを商用製品に使えますか? NVIDIA AI Enterprise はいつ必要?」 | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | 「ポリシー推論をリアルタイム（低遅延）に最適化するには? TensorRT・量子化[^quant]・action chunking[^chunk]?」 | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | 「設備/工場のデジタルツイン[^dtwin]を作りロボットシミュレーションと連携するには? TwinMaker・Omniverse?」 | [pillar-3](pillar-3.md) | [AWS Physical AI ブログ](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | 「ML の専門家がいません — どこから始めますか? 最小 PoC の設計は?」 | [start](start.md) | [AWS Physical AI ブログ](https://aws.amazon.com/blogs/physical-ai/) |

---

## ページ一覧

- [開始・ROI](start.md)
- [実行手順](execution.md)
- [運用復旧](operations.md)
- [利用ガイド](guide.md)
- [新着情報 — 最近の公式記事とピラーへの接続](news.md)
- [ワークショップ・資料 — 公開実習・ガイド・サンプル](workshops.md)
- [経営層資料](exec.md)
- [AWS担当者対話ガイド](exec-guide.md)
- [P1 データ](pillar-1.md)
- [P2 学習](pillar-2.md)
- [P3 シミュレーション](pillar-3.md)
- [P4 Sim-to-Real](pillar-4.md)
- [P5 オーケストレーション](pillar-5.md)
- [意思決定](decisions.md)
- [Radar](radar.md)
- [根拠記録](evidence.md)
- [維持管理](maintenance.md)
- [設定 · MCP 接続](mcp.md)

_owner: Youngjin · updated: 2026-09 · volatility: 中_

<!-- 용어 각주 -->

[^s2r]: **sim-to-real** — シミュレーションで学習したポリシーを実際のロボットへ移すこと、またはその方法論です。シミュレーションと現実の物理・視覚の差（ドメインギャップ）のため、そのまま移すと性能が崩れます。🎥 [NVIDIA sim-to-real ロボティクスショーケース](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM エージェント** — 大規模言語モデルが自ら計画を立て、ツール（API・ロボットスキル）を選んで呼び出し、多段階のタスクを遂行するソフトウェアです。単純な質疑応答と異なり「行動」がある点が核心です。
[^ros]: **ROS 2 (Robot Operating System 2)** — ロボットソフトウェアの事実上の標準オープンソースミドルウェアです。センサー・制御ノードがトピック（topic）で通信する分散構造で、産業・研究ロボットスタックの共通基盤です。
[^rosbag]: **ROS bag（rosbag2）** — ロボットオペレーティングシステム ROS 2 がトピック（センサー・コマンドのストリーム）を丸ごと録画する標準ログフォーマットです。ロボット企業の元データの事実上のデフォルト形態ですが、そのままでは学習に使えず変換が必要です。
[^quant]: **量子化（quantization）** — モデルの重み・演算を FP16→INT8/FP4 のように低い精度へ変換し、メモリと演算量を削減する軽量化手法です。エッジデバイスで遅延予算を満たすための中核手段であり、精度損失とのトレードオフを管理します。
[^chunk]: **Action chunking** — 1回の推論で複数の未来動作を生成します。実行頻度と新観測への反応頻度は別で、実行区間・切替・遅延をモデル別に検証します。
[^dtwin]: **デジタルツイン（digital twin）** — 実際の工場・倉庫・ロボットを物理的に忠実に模した仮想レプリカです。実環境に触れずにポリシー学習・検証・シナリオ実験を可能にします。
