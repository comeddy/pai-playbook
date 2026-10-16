---
ko_hash: 97764a94d9bc250fc42d34b6187d4215bf85efa7
---
# 新着情報

_owner: Youngjin · updated: 2026-10 · volatility: 高_

> **L0 TL;DR**: AWS Physical AIの新記事を選び既存ピラーにつなぎます。以下は**原文公開日**、一覧確認日は**2026-10-14**です。[ワークショップ・資料](workshops.md)で学習経路を選べます。

公式原文に基づく要約であり性能数値の独立再現ではありません。未検証候補は既存の[Radar](radar.md)で管理します。

## 最近の資料一覧

| 公開日 | 資料 | 関連 |
|---|---|---|
| 2026-10-07 | [AWS Physical AI Toolchain 公開](#toolchain) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md) |
| 2026-10-06 | [3D Gaussian Splatting の産業活用事例](#gaussian-splatting) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-02 | [Isaac Lab on AWS — シミュレーションからポリシー登録まで](#isaac-lab-aws) | [P3](pillar-3.md) · [Isaac Lab](workshops.md#isaac-lab) |
| 2026-09-28 | [NVIDIA Cosmos 3 on AWS](#cosmos-3) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) |
| 2026-09-10 | [SageMaker HyperPod EKSでπ0をファインチューニング](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [TelexistenceのDreamZero実験](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Roboticsの太陽光パネル設置AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRoboticsのヒューマノイド道具操作学習](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD・SDMAによる産業デジタルツイン](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-17 | [Edge ImpulseとAWS — エッジ推論とクラウドインテリジェンスの統合](#edge-impulse-aws) | [P4](pillar-4.md) · [P5](pillar-5.md) |
| 2026-07-15 | [Configのロボット学習データ拡張](#config) | [P1](pillar-1.md) |

## AWS Physical AI Toolchain 公開 { #toolchain }

**公開日: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

データ収集から合成データ、学習、シミュレーション検証、エッジ展開までの Physical AI 開発サイクルを AWS で回すためのリファレンスアーキテクチャ・IaC・デプロイ自動化の集合です。NVIDIA GR00T（VLA[^vla] 学習）・Isaac Sim・Isaac Lab・Cosmos・OSMO を S3・EKS・AWS Batch・SageMaker・EC2・IoT Greengrass（Jetson 展開）につなぎ、コンポーネントごとの Terraform モジュールを一つずつ導入できます。データは Zarr→LeRobot、エッジは ONNX・ROS 2 などの公開フォーマットを使います。コード：[aws-samples リポジトリ](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws)。

**確認する範囲**: 公式リファレンスアーキテクチャです。記事自身が「完成したロボット動作ではなくインフラパターン」と明言しています。GR00T の例は UR3 pick-and-place のデモ 27 件で動作確認用であり、「数週間ではなく数時間」は AWS 側の説明です。GPU クォータ（SageMaker・EC2）、NGC API キー、Hugging Face トークンが必要で、実習後はクリーンアップ（tear down）しないと費用が止まりません。

**次のアクション**: ボトルネックの段階一つから導入 — P1 データ · P2 学習 · P3 シミュレーション · P5 オーケストレーション（Strands エージェント層）· Radar 待機項目 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting の産業活用事例 { #gaussian-splatting }

**公開日: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

写真・映像から実写の 3D シーンを作る 3DGS[^3dgs] をオープンソースの Splat Toolbox（[AWS Solutions Library ガイダンス](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws)）で処理する 5 段階パイプライン（入力→前処理→再構成→学習→後処理）と、メディア・ロボティクス・建設・製造・不動産での活用を紹介します。Step Functions・Lambda・AWS Batch/ECS と EC2 スポットを使います。

**確認する範囲**: 産業活用の概要です。ロボティクスの項目（合成学習データ、sim-to-real ギャップの縮小、経路計画）は活用の方向性の説明で、ポリシー性能の実測はありません。現在の成果物は静的 3D で、4D（時間軸）アセットはロードマップです。「最大 50% 削減」はスポットとオンデマンドのコンピューティング単価の比較です。

**次のアクション**: P3 デジタルツイン・シーン再構成 · P4 real-to-sim 候補 — [P3](pillar-3.md) · [P4](pillar-4.md).

## Isaac Lab on AWS — シミュレーションからポリシー登録まで { #isaac-lab-aws }

**公開日: 2026-10-02 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/isaac-lab-on-aws-from-simulation-to-registered-policy/) `[3]`**

Isaac Sim 5.1.0・Isaac Lab v2.3.2・NVIDIA ドライバー・Amazon DCV を焼き込んだゴールデン AMI、個人用の Instance モードと複数ユーザー向けの Fleet モード（Cognito MFA・自動スケーリング）、SageMaker 学習ジョブとマネージド MLflow モデルレジストリを一度にデプロイする AWS CDK ソリューションです。デスクトップで作ったプロジェクトをイメージの再ビルドなしに学習ジョブへ送り、学習済みポリシーは MLflow に自動登録されます。サンプルは SO-ARM101 RL・遠隔操作データ収集、Unitree H1 歩行の 3 種です。

**確認する範囲**: 公開リポジトリではありません — 記事によれば **AWS アカウントチーム経由で提供**されます。レジストリはポリシーを記録・ラベル付けするだけでサービングはせず、デプロイ連携はチームが自分で構成する必要があります。公開実習が必要なら別途の Isaac Lab ワークショップを使います。

**次のアクション**: P3 シミュレーション · 公開ワークショップ [Isaac Lab](workshops.md#isaac-lab) — [P3](pillar-3.md).

## NVIDIA Cosmos 3 on AWS { #cosmos-3 }

**公開日: 2026-09-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/nvidia-cosmos-3-on-aws-omnimodal-world-models-for-physical-ai/) `[3]`**

Cosmos 3（2026-05 公開）は従来の Predict・Transfer・Reason の 3 モデルを一つの Mixture-of-Transformers に統合したモデルで、1 回の推論でシーン理解、未来映像の生成（WFM[^wfm]）、ロボット動作軌跡（WAM[^wam]）を同時に出力します。サイズは Super 64B・Nano 16B・Edge 4B です。AWS 側はデータキュレーション（Batch）、HyperPod での事後学習、EKS+NIM または SageMaker JumpStart での推論、Greengrass による Jetson エッジ展開までのリファレンスアーキテクチャとインスタンス推奨を示します。

**確認する範囲**: 「初の完全オープンなオムニモデル」は NVIDIA 側の表現です。フルチェックポイントは BF16 でテストされており、記事自身もインスタンス別の性能主張の前にランタイム構成を検証するよう述べています。ロボット動作の出力は実機成功率の根拠ではありません。

**次のアクション**: P1 合成データ · P2 モデル学習 · P3 シミュレーション — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md).

## SageMaker HyperPod EKSでπ0をファインチューニング { #pi0-hyperpod }

**公開日: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

DROID・LIBEROでのπ0 VLA学習・評価を紹介し、HyperPod EKS、FSx for Lustre、学習ジョブ構成をつなぎます。

**確認する範囲**: 公式実装ガイドです。報告値はn=5のopen-loop[^openloop]で、実機成功率ではありません。本文のコードリンクは404です。コードはマージされておらず[未マージのPR #1174](https://github.com/awslabs/awsome-distributed-ai/pull/1174)にあります（2026-10-14確認）。まず本文を参照します。

**次のアクション**: P2学習・π0読解経路 — [P2](pillar-2.md) · [π0](workshops.md#pi0-guide).

## TelexistenceのDreamZero実験 { #telexistence-dreamzero }

**公開日: 2026-09-09 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/bringing-a-frontier-world-model-to-the-convenience-store-inside-telexistences-dreamzero-experiment-on-aws/) `[3]`**

店舗ロボットのデータ変換・整備、DreamZero適応、シミュレーション・実機評価を扱うEC2・S3上の顧客共同実験です。

**確認する範囲**: 顧客実験・PoCです。既存の店舗ロボット運用実績とDreamZero実験結果を区別します。

**次のアクション**: P1データ・P2学習・P4評価 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md).

## Luminous Roboticsの太陽光パネル設置AI { #luminous }

**公開日: 2026-08-12 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/teaching-robots-to-see-how-luminous-robotics-is-accelerating-energy-infrastructure-construction-with-vision-action-ai/) `[3]`**

パネル配置時の人の確認を減らす視覚ポリシー実験です。Isaac SimデータとEC2・S3の学習フローを紹介します。

**確認する範囲**: 顧客技術事例です。シミュレーション・オフライン評価と現場導入範囲を分けます。

**次のアクション**: P3シミュレーション・P4 Sim-to-Real — [P3](pillar-3.md) · [P4](pillar-4.md).

## WIRoboticsのヒューマノイド道具操作学習 { #wirobotics }

**公開日: 2026-08-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-wirobotics-is-teaching-humanoid-robots-to-use-human-tools-with-aws-and-nvidia/) `[3]`**

韓国ロボット企業のドリル操作学習です。AWS・NVIDIAとの協業でデータ品質・学習設定・実機評価を結びます。

**確認する範囲**: 顧客協業事例です。特定の道具・業務の結果を汎用ヒューマノイド性能に広げません。

**次のアクション**: P2学習・P4実機評価 — [P2](pillar-2.md) · [P4](pillar-4.md).

## OpenUSD・SDMAによる産業デジタルツイン { #openusd }

**公開日: 2026-07-31 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/build-l1-4-industrial-digital-twins-with-openusd-and-sdma-on-aws/) `[3]`**

静的3Dからセンサー情報・予測・再校正へ段階的に拡張する実装です。OpenUSDとS3・Kinesis・Lambda・Batchを接続します。

**確認する範囲**: 参照実装です。合成センサー入力と実設備連携を分け、必要な段階から確認します。

**次のアクション**: P3デジタルツイン・OpenUSD資料 — [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial).

## Edge ImpulseとAWS — エッジ推論とクラウドインテリジェンスの統合 { #edge-impulse-aws }

**公開日: 2026-07-17 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/edge-impulse-and-aws-combining-edge-inference-with-cloud-intelligence-for-physical-ai/) `[4]` · ⏳ 原文照合待ち (自動スキャン 2026-10-16)**

Edge Impulse（Qualcomm傘下）とAWSの共同記事で、倉庫設備の位置追跡を例にハイブリッドなエッジ・クラウドアーキテクチャを紹介します。カメラのエッジデバイスでEdge Impulse YOLO Proの物体検出とQwen2-VL 8Bビジョン言語モデルによる一次判定を行い、確定した検知のみクラウドへ送って、Amazon Bedrock AgentCore（Nova Lite）が「フォークリフトはどこか」といった自然言語の問い合わせに答えます。AWS IoT Coreがデバイス接続とMQTTメッセージングを、Greengrassがエッジモデルの展開・管理を、S3が再学習用画像の保存を担います。

**確認する範囲**: AWS×Edge Impulseの共同パートナー紹介記事です。コードサンプルの場所が原文で明確でないため、公開リポジトリかアカウントチーム経由かは追加確認が必要です。「レイテンシ・帯域幅の削減」はエッジ優先設計の利点の説明であり、数値化されたベンチマークではありません — ベンダーの説明と実測を区別して読みます。

**次のアクション**: P4 エッジ推論展開 · P5 エージェントオーケストレーション（Bedrock AgentCore） — [P4](pillar-4.md) · [P5](pillar-5.md).

## Configのロボット学習データ拡張 { #config }

**公開日: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

収集済み実演の視覚的多様性をS3、Bedrockの説明生成、Cosmos変換、HyperPod/EC2で増やします。

**確認する範囲**: 顧客共同技術記事です。拡張映像品質と実ポリシー改善を個別評価する際の参考です。

**次のアクション**: P1データ収集・処理 — [P1](pillar-1.md).

## 継続して確認

公式[Physical AIブログ](https://aws.amazon.com/blogs/physical-ai/)と[RSS](https://aws.amazon.com/blogs/physical-ai/feed/)を確認します。公開日・原文・範囲・ピラーリンクを同時更新します。日次自動スキャンがこのページにない記事を `[4]` · ⏳ 原文照合待ち の表示で先に追加し、オーナーが原文を照合した後 `[3]` に変更します。また、技術昇格は既存の[維持管理ルール](maintenance.md)に従います。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 映像観測と言語指示からロボット動作を出力するモデルです。
[^openloop]: **Open-loop評価** — 記録済み観測・動作で予測誤差を測ります。環境と相互作用するポリシーの成功評価とは異なります。
[^3dgs]: **3D Gaussian Splatting（3DGS）** — 複数の写真・映像に多数の 3D ガウシアン（楕円体の点）を当てはめ、実写シーンをリアルタイムにレンダリングする 3D 再構成手法です。実際の現場をシミュレーションの背景に移す real-to-sim に使われます。
[^wfm]: **ワールド基盤モデル（WFM, World Foundation Model）** — 物理世界の次のシーンを予測・生成するよう学習された大型モデルです。テキスト・映像プロンプトから物理的にもっともらしい映像・シナリオを作り、ロボット学習データを拡張します。🎥 [NVIDIA Cosmos 紹介](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **ワールド・アクションモデル（WAM, World Action Model）** — 未来シーンの予測とロボット動作の生成を一つのモデルで同時に行うモデルです。映像だけを作るワールドモデルと異なり、関節角度やグリッパー指令など実行可能な動作を出力します。
