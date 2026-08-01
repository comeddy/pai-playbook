---
ko_hash: 46de1fdef05e9b4bcd7187d1e740403a135a577d
---
# Physical AI Playbook のご案内


_最終更新: 2026-07 · owner: Youngjin · ステータス: 初期構築中_

> **L0 TL;DR**: 顧客が Physical AI の質問を投げかけたとき、Slack を掘り返さずに **この playbook 一つでアーキテクチャの方向性・AWS マッピング・次のアクションを5分以内に** 提示するための参照資産です。論文要約集でも、ニュースアーカイブでもありません。

---

## このドキュメントの読み方（30秒）

1. **急いでいるとき**: 下記の [よくある質問 Top 20](#よくある質問-top-20) から該当項目へ直接移動。
2. **テーマが定まったら**: 5つのピラーのいずれかに入る。各項目は **L0（1～2文）→ L1（1ページ）→ L2（deep-dive リンク）** に階層化されています — 上部だけ読んでも方向性がつかめます。
3. **岐路に立ったら**: [意思決定ツリー](decisions.md) — Cloud vs Edge、NVIDIA vs オープンソース、GPU 確保、Build vs Buy。
4. **「これはなぜ無いの?」**: まず [Radar](radar.md) を確認。包含基準未達で待機中の項目がそこにあります。新しい候補の報告は [メンテナンスガイド](maintenance.md) の昇格パイプラインへ。

### ラベルの読み方

| 成熟度 | 意味 |
|---|---|
| 🟢 GA | 正式リリース、本番環境で使用可能 |
| 🟡 Preview | 公開プレビュー / 明確な GA ロードマップあり |
| 🔵 Research-only | 論文・研究段階、顧客提案での使用禁止 |
| ⚪ Hype | デモのみ存在。「印象的なデモ」≠「デプロイ可能」 |

| 出典グレード | 意味 |
|---|---|
| [1] | 公式ドキュメント / 論文 |
| [2] | AWS 内部検証（自ら実行して確認） |
| [3] | ベンダー公式ブログ |
| [4] | 未検証（Slack/噂）— 引用時は必ず再確認 |

---

## 5つのピラー

| # | ピラー | L0 一言 | ショートカット |
|---|---|---|---|
| 1 | **データ収集 & 処理** | ロボット学習のボトルネックはモデルではなくデータである — テレオペレーション[^teleop]・オープンデータセット・合成データを AWS パイプラインで処理する方法 | [pillar-1](pillar-1.md) |
| 2 | **モデル学習 (VLA)** | VLA[^vla]/ロボット基盤モデルをどの規模の GPU で、ファインチューニング[^ft]か事前学習[^pretrain]かの分岐から設計する方法 | [pillar-2](pillar-2.md) |
| 3 | **シミュレーション** | Isaac Sim/Lab vs オープンソースの選択と、AWS 上での大規模並列シミュレーション実行パターン | [pillar-3](pillar-3.md) |
| 4 | **Sim-to-Real** | シミュレーションで学習したポリシーを実機に移す検証済みの方法論と、エッジ推論のデプロイ経路 | [pillar-4](pillar-4.md) |
| 5 | **エージェントオーケストレーション** | LLM プランナー（System 2[^sys]）がロボットコントローラー（System 1）とフリート[^fleet]を指揮する階層 — Bedrock AgentCore 中心 | [pillar-5](pillar-5.md) |

> ピラー間の比重は均等。各ピラー内部は **顧客の実際の需要 × production-readiness** 順に並んでおり、上部に「このピラーで顧客が最も頻繁に問う質問 Top 3」があります。

---

## よくある質問 Top 20

<!-- 1～10: 初期シード（マスタープロンプト例 + IA 構造）。11～20: 公開コミュニティ/ブログの深掘り調査（2026-07）。⚠️ どちらも SA の実際の問い合わせログではないため、Slack 問い合わせ履歴を入手したら頻度順に再ソートすること。 -->

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
| 11 | 「これを全部回すと GPU コストはどれくらい? 予算はどう見積もりますか?」 | [decisions](decisions.md) | [AWS Embodied AI ブログ](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | 「既存の ROS 2[^ros] スタック・rosbag[^rosbag] データを AWS とどう連携しますか?」 | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac ブログ](https://aws.amazon.com/blogs/robotics/) |
| 13 | 「複数ノードに学習をスケールするには? AWS Batch vs SageMaker HyperPod?」 | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | 「実機デプロイ前にポリシーが実際に動くかをどう検証・ベンチマークしますか?」 | [pillar-4](pillar-4.md) | [NVIDIA ポリシー評価](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | 「ロボット/工場データが機微ですが、クラウド学習は規制上問題ないですか? オンプレ・ハイブリッドは?」 | [decisions](decisions.md) | [AWS AI 主権](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | 「学習したポリシーをどうバージョン管理・再現し、チェックポイントを復旧しますか?」 | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | 「Isaac Sim・オープンモデルを商用製品に使えますか? NVIDIA AI Enterprise はいつ必要?」 | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | 「ポリシー推論をリアルタイム（低遅延）に最適化するには? TensorRT・量子化[^quant]・action chunking[^chunk]?」 | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | 「設備/工場のデジタルツイン[^dtwin]を作りロボットシミュレーションと連携するには? TwinMaker・Omniverse?」 | [pillar-3](pillar-3.md) | [AWS Physical AI ブログ](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | 「ML の専門家がいません — どこから始めますか? 最小 PoC の設計は?」 | [decisions](decisions.md) | [AWS Physical AI ブログ](https://aws.amazon.com/blogs/physical-ai/) |

---

## ページ一覧

- [guide — このプレイブックの作られ方と維持のしくみ（検証パイプライン全体）](guide.md)
- [経営層ブリーフィング — 経営層向け 5 分の判断フレーム（今/まもなく/まだ マトリクス）](exec.md)
- [経営層対話ガイド — SA の経営層ミーティング準備（ピッチ・Top 10 Q&A・禁止表現）](exec-guide.md)
- [pillar-1 — データ収集 & 処理](pillar-1.md)
- [pillar-2 — モデル学習 (VLA)](pillar-2.md)
- [pillar-3 — シミュレーション](pillar-3.md)
- [pillar-4 — Sim-to-Real](pillar-4.md)
- [pillar-5 — エージェントオーケストレーション](pillar-5.md)
- [decisions — 横断的意思決定ツリー](decisions.md)
- [radar — キュー/ウォッチリスト](radar.md)
- [maintenance — オーナーシップ · 更新ルール · 昇格パイプライン](maintenance.md)

---

## この playbook が扱わないもの

- **包含基準未達の項目**: ⓐ production 検証 ⓑ AWS マッピング可能 ⓒ 実際の問い合わせ履歴 ⓓ GA（ロードマップ）— このうち **2個未満** なら本文にありません。[Radar](radar.md) に一行だけ存在します。
- **ニュース速報**: 「新しく出た」は収録理由ではありません。
- **概念説明で終わる項目**: すべての項目は「➡️ 次のアクション」で終わります。アクションが無ければ未完成です。

---

_owner: Youngjin · updated: 2026-07 · volatility: 低（構造ページ — FAQ Top 20 の順位のみ四半期ごとに再検討）_

<!-- 용어 각주 -->

[^teleop]: **テレオペレーション** — 人が VR コントローラーやリーダーアームなどでロボットを遠隔操縦しながら実演動作を記録するデータ収集方式です。品質は最も高いものの、人の時間がそのままコストになります。🎥 [Stanford Mobile ALOHA テレオペレーション実演](https://www.youtube.com/watch?v=mnLVbwxSdNM)
[^vla]: **VLA (Vision-Language-Action)** — カメラ映像（Vision）と自然言語の指示（Language）を入力に、ロボットの動作（Action）を直接出力する基盤モデルです。「コップを掴んで」と言えば関節の動きを生成する、という具合です。🎥 [NVIDIA Isaac GR00T N1 紹介](https://www.youtube.com/watch?v=m1CH-mgpdYg)
[^ft]: **ファインチューニング（fine-tuning）** — 大規模データで事前学習されたモデルを、自分のタスク・ロボットの少量データで追加学習させることです。ゼロから学習するよりデータ・GPU が数十~数百倍節約できます。
[^pretrain]: **事前学習（pre-training）** — 大規模な汎用データでモデルをゼロから学習させ、基礎能力を作る段階です。その後、少量データのファインチューニングで特定タスクに合わせます。フロンティア VLA の事前学習はごく少数の組織の領域です。
[^sys]: **System 2 / System 1** — 認知科学の「遅い思考 / 速い反応」の区分をロボットアーキテクチャに適用した構造です。System 2 は遅い大型モデルが計画を（5~10Hz）、System 1 は小さなポリシーがリアルタイム制御を（50~200Hz）担います。推論をクラウドに置くかエッジに置くかを分ける基準になります。
[^fleet]: **フリート（fleet）協調** — 多数のロボット群を一つのシステムとしてスケジューリング・経路配分することです。倉庫ロボットのように数百~数千台規模ですでに本番検証済みの領域です。
[^s2r]: **sim-to-real** — シミュレーションで学習したポリシーを実際のロボットへ移すこと、またはその方法論です。シミュレーションと現実の物理・視覚の差（ドメインギャップ）のため、そのまま移すと性能が崩れます。🎥 [NVIDIA sim-to-real ロボティクスショーケース](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM エージェント** — 大規模言語モデルが自ら計画を立て、ツール（API・ロボットスキル）を選んで呼び出し、多段階のタスクを遂行するソフトウェアです。単純な質疑応答と異なり「行動」がある点が核心です。
[^ros]: **ROS 2 (Robot Operating System 2)** — ロボットソフトウェアの事実上の標準オープンソースミドルウェアです。センサー・制御ノードがトピック（topic）で通信する分散構造で、産業・研究ロボットスタックの共通基盤です。
[^rosbag]: **ROS bag（rosbag2）** — ロボットオペレーティングシステム ROS 2 がトピック（センサー・コマンドのストリーム）を丸ごと録画する標準ログフォーマットです。ロボット企業の元データの事実上のデフォルト形態ですが、そのままでは学習に使えず変換が必要です。
[^quant]: **量子化（quantization）** — モデルの重み・演算を FP16→INT8/FP4 のように低い精度へ変換し、メモリと演算量を削減する軽量化手法です。エッジデバイスで遅延予算を満たすための中核手段であり、精度損失とのトレードオフを管理します。
[^chunk]: **action chunking** — 毎ステップ動作 1 個ではなく、将来の動作を複数ステップ（チャンク）まとめて一度に予測する手法です。推論回数を減らし、リアルタイム制御の周波数を満たしやすくします。
[^dtwin]: **デジタルツイン（digital twin）** — 実際の工場・倉庫・ロボットを物理的に忠実に模した仮想レプリカです。実環境に触れずにポリシー学習・検証・シナリオ実験を可能にします。
