---
ko_hash: 52dcd5923b7070599439d837777f9d94048d8ad9
---
# 新着情報

_owner: Youngjin · updated: 2026-11 · volatility: 高_

> **L0 TL;DR**: AWS Physical AIの新記事を選び既存ピラーにつなぎます。以下は**原文公開日**、一覧確認日は**2026-11-04**です。[ワークショップ・資料](workshops.md)で学習経路を選べます。

公式原文に基づく要約であり性能数値の独立再現ではありません。未検証候補は既存の[Radar](radar.md)で管理します。

> **re:Invent 2026（11/30–12/4、ラスベガス）**：全セッションカタログから Physical AI・シミュレーション・モデル学習・データ・エッジ・AgentCore のセッション 45 件を[選んでおきました](#reinvent-2026)。

## 最近の資料一覧

| 公開日 | 資料 | 関連 |
|---|---|---|
| 2026-11-03 | [NVIDIA CloudXR 6 on AWS — デジタルツインを XR ヘッドセットへストリーミング](#cloudxr-6) | [P1](pillar-1.md) · [P3](pillar-3.md) |
| 2026-10-28 | [Archetype AI Newton — 産業センサーデータを運用インテリジェンスへ](#archetype-newton) | [P4](pillar-4.md) · [P5](pillar-5.md) |
| 2026-10-28 | [AWS × RLWRLD — 明日の労働力のための Physical AI](#aws-rlwrld-workforce) | [Radar](radar.md) · [P2](pillar-2.md) |
| 2026-10-28 | [Visual Asset Management System 2.6 公開](#vams-2-6) | [P3](pillar-3.md) · [P4](pillar-4.md) |
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

## NVIDIA CloudXR 6 on AWS — デジタルツインを XR ヘッドセットへストリーミング { #cloudxr-6 }

**公開日: 2026-11-03 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/streaming-physical-ai-digital-twins-and-immersive-experiences-to-xr-headsets-with-nvidia-cloudxr-6-on-aws/) `[4]` · ⏳ owner の原文照合待ち (ローカルセッション 2026-11-04 で RSS 本文を確認)**

GPU でレンダリングした OpenXR コンテンツを軽量 XR ヘッドセットへストリーミングする NVIDIA CloudXR 6 を、Amazon EC2 GPU インスタンスで動かす AWS サンプル（[aws-samples/sample-cloudxr6-on-aws](https://github.com/aws-samples/sample-cloudxr6-on-aws)）を紹介しています。Physical AI での用途は、デジタルツイン[^dtwin]のレビュー、シミュレーションシーンの検証、シミュレーション内テレオペレーションによるポリシー学習用デモデータ収集で、NVIDIA Isaac GR00T エンドツーエンドワークフローにおける Isaac Sim の XR テレオペレーション例にも触れています。構成は CloudFront（入口・CloudXR.js Web クライアント）→ ECS Fargate のシグナリングプロキシ（Cognito 認証、DynamoDB インスタンスレジストリ）→ Local Zone またはリージョンの EC2 GPU プールで、メディアはヘッドセットと GPU インスタンスの間を UDP で直接流れます。クライアントは Apple Vision Pro（ネイティブ）と Meta Quest・Pico（ブラウザ WebRTC）の 2 経路に対応します。

**読む際に確認する範囲**: AWS サンプルの公開記事（アーキテクチャ・デプロイガイド）です。レイテンシ値は AWS 自身のテスト 1 件によるもので、ロサンゼルス Local Zone の g7e インスタンスから同じ LA 地域の Meta Quest 3 へ約 90 FPS、pose-to-render レイテンシ[^p2r]約 35 ms（ネットワーク往復約 8–9 ms）でした。NVIDIA の目標値（20–30 ms）よりは高く、上限（100 ms）よりは低い値です。韓国で再現するには、ソウルリージョンまたは近隣 Local Zone の GPU インスタンス提供状況と実測レイテンシを別途確認する必要があります。記事に顧客の本番事例はありません。

**次のアクション**: P1 テレオペレーションによるデータ収集 · P3 デジタルツインレビュー — [P1](pillar-1.md) · [P3](pillar-3.md).

## Archetype AI Newton — 産業センサーデータを運用インテリジェンスへ { #archetype-newton }

**公開日: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/industrial-sensor-data-to-operational-intelligence-with-archetype-ai-on-aws/) `[4]` · ⏳ owner の原文照合待ち (ローカルセッション 2026-11-04 で RSS 本文を確認)**

Archetype AI の物理ワールドモデル Newton を AWS にデプロイし、振動・圧力・温度・電流・レーダー・映像などのマルチモーダルセンサー信号から異常検知・稼働状態モニタリング・作業検証を行うパートナー紹介記事です。Newton は 80 億（8B）パラメータのモデルで、エッジ向けに 8,500 万（85M）パラメータのモデルへ蒸留できると説明しています。プラットフォームは [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-pjqoobj6vnbhm) から顧客アカウントの専用 VPC にデプロイされ、Amazon EKS（CPU・GPU ノードグループ）と S3・Aurora PostgreSQL・ElastiCache 上で動作します。エッジエージェントはオンプレミス・産業用エッジハードウェアにデプロイし、AWS IoT Greengrass・Outposts を任意で使います。クラウドの取り込み経路は IoT Core・Kinesis Data Streams・MSK です。

**読む際に確認する範囲**: パートナー（Archetype AI）のソリューション紹介記事です。性能値はすべてベンダー自身の発表で、独立した実測ではありません。ポンプ状態検知の「最大 90% の精度（少数のラベル付き例）」、ギアボックス故障検知の「99% の精度・従来方式より 80% 速いデプロイ」、建設現場映像 12,000 時間の分析事例は、いずれも顧客名なしで示されています。「タスク別の学習なしですぐ動作（zero-shot）」もベンダーの主張です。ロボットポリシーではなく産業設備のセンサー解釈モデルなので、本プレイブックのロボット学習軸よりもエッジ運用・モニタリング軸に近い内容です。

**次のアクション**: P4 エッジデプロイ（Greengrass・Outposts） · P5 運用モニタリング — [P4](pillar-4.md) · [P5](pillar-5.md).

## AWS × RLWRLD — 明日の労働力のための Physical AI { #aws-rlwrld-workforce }

**公開日: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/aws-rlwrld-building-the-workforce-of-tomorrow-with-physical-ai/) `[4]` · ⏳ 原文照合待ち (自動スキャン 2026-11-02)**

AWS と RLWRLD の Physical AI 協業シリーズの第 2 弾で、2026-06-22 の第 1 弾（"Putting Dexterous Robots to Work"）の続編です。RLWRLD が新たに AWS Validated Partner として登録され、AWS Marketplace に 2 種類の製品を掲載したことを紹介し、人手不足対応のユースケース（箱の持ち上げ、商品ピッキング、棚の補充）向けの PoC 計画と、AWS Physical AI ロードショーを通じた顧客パイプラインの形成を扱います。また、RLDX-1 が主要な基盤モデルの約 20% の学習コンピュートで同等の性能に達したという主張も引用しています。

**確認する範囲**: AWS×RLWRLD の公式パートナーシップシリーズ記事（顧客協業の紹介という性質）です。「AWS Validated Partner」と Marketplace への掲載はパートナープログラム上の地位であり、実際のデプロイ成果ではありません。箱の持ち上げ・商品ピッキング・棚の補充の PoC は原文で「計画中」(planned) と記載されており、すでに稼働している事例ではありません。「約 20% のコンピュートで同等の性能」という主張は RLWRLD 自身の技術ブログを引用したベンダー側の表現であり、Radar の RLDX-1 項目に既にある自社公表ベンチマークと同じ性質です — 独立した実測ではありません。今回のセッションは全面的な egress 制限により aws.amazon.com の原文に直接アクセスできず、複数の独立した検索結果（タイトル・日付・主要な記述が一致）で代わりに照合しました — 具体的な数値は owner による原文照合が必要です。

**次のアクション**: 既存の RLDX-1 Radar 項目との連携 · P2 モデル学習 — [Radar](radar.md) · [P2](pillar-2.md).

## Visual Asset Management System 2.6 公開 { #vams-2-6 }

**公開日: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/visual-asset-management-system-2-6-release/) `[4]` · ⏳ 原文照合待ち (自動スキャン 2026-11-02)**

VAMS は AWS Physical AI・PACE チームによるオープンソースの 3D/空間アセット管理アクセラレータで、2.6 は 2.0（2024-06）以降「最大のアップデート」とされています。オーケストレーション層を再設計し、マルチファイル・マルチアセット実行、グローバル実行ビュー、アップロードトリガーによる自動ワークフローを追加したほか、AWS European Sovereign Cloud デプロイテンプレート、Amazon Cognito OIDC 連携、より細かい IAM ロールのカスタマイズ、デフォルトで遮断する WAF、資産のライフサイクル・バージョンごとの変更履歴を追跡する来歴管理機能を加えました。デモにはセマンティック検索、ブラウザ内の SuperSplat（ガウシアンスプラット[^3dgs]）エディタ、IFC BIM ビューア、地理空間マップ検索、NVIDIA Cosmos の text-to-world ワークフローが含まれます。コードは [GitHub awslabs/visual-asset-management-system](https://github.com/awslabs/visual-asset-management-system) でオープンソース公開されています。

**確認する範囲**: 公式のオープンソースソリューション更新記事です。「2.0 以降最大のアップデート」は AWS 側の表現であり、記事内に実顧客のプロダクション採用成果や性能数値は示されていません。公開リポジトリであり、アカウントチーム限定の経路ではありません — 誰でも GitHub から入手できます。今回のセッションは全面的な egress 制限により aws.amazon.com の原文に直接アクセスできず、検索結果のスニペットと GitHub のリリースタグ（2.6.0 が 2026-09-11、2.6.6 が 2026-10-30）で代わりに照合しました — 公開日（2026-10-28）も検索結果のスニペットに基づくもので、owner による原文照合が必要です。

**次のアクション**: P3 デジタルツイン・シーン再構成 · P4 real-to-sim 候補 — [P3](pillar-3.md) · [P4](pillar-4.md).

## AWS Physical AI Toolchain 公開 { #toolchain }

**公開日: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

データ収集から合成データ、学習、シミュレーション検証、エッジ展開までの Physical AI 開発サイクルを AWS で回すためのリファレンスアーキテクチャ・IaC・デプロイ自動化の集合です。NVIDIA GR00T（VLA[^vla] 学習）・Isaac Sim・Isaac Lab・Cosmos・OSMO を S3・EKS・AWS Batch・SageMaker・EC2・IoT Greengrass（Jetson 展開）につなぎ、コンポーネントごとの Terraform モジュールを一つずつ導入できます。データは Zarr→LeRobot、エッジは ONNX・ROS 2 などの公開フォーマットを使います。コード：[aws-samples リポジトリ](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws)。

**確認する範囲**: 公式リファレンスアーキテクチャです。記事自身が「完成したロボット動作ではなくインフラパターン」と明言しています。GR00T の例は UR3 pick-and-place のデモ 27 件で動作確認用であり、「数週間ではなく数時間」は AWS 側の説明です。GPU クォータ（SageMaker・EC2）、NGC API キー、Hugging Face トークンが必要で、実習後はクリーンアップ（tear down）しないと費用が止まりません。

**次のアクション**: ボトルネックの段階一つから導入 — P1 データ · P2 学習 · P3 シミュレーション · P5 オーケストレーション（Strands エージェント層）· Radar 待機項目 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting の産業活用事例 { #gaussian-splatting }

**公開日: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

写真・映像から実写の 3D シーンを作る 3DGS をオープンソースの Splat Toolbox（[AWS Solutions Library ガイダンス](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws)）で処理する 5 段階パイプライン（入力→前処理→再構成→学習→後処理）と、メディア・ロボティクス・建設・製造・不動産での活用を紹介します。Step Functions・Lambda・AWS Batch/ECS と EC2 スポットを使います。

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

## re:Invent 2026 — Physical AI 関連セッション { #reinvent-2026 }

**開催：2026-11-30 〜 12-04 · [re:Invent 2026 イベントカタログ](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog) `[3]` · カタログ確認日：2026-11-02**

カタログの全 2,415 セッション（再演回を含む）を取得し、タイトル・概要の Physical AI・ロボティクス・ワールドモデル・シミュレーション・デジタルツイン・モデル学習（HyperPod・Trainium）・学習データ・エッジ・AgentCore のキーワードで一次抽出したうえで、ピラーに直接つながる 45 件を選びました。タイトルに AgentCore を含むセッションだけで 60 件を超えるため、本番運用パターンと製造・現場事例を中心に残しています。セッションコードを押すとカタログの検索結果が開きます。時刻は現地（PT）、同じセッションの別の回は「再演」と記載しています。形式：Workshop 120 分ハンズオン · Builders' session 60 分少人数ハンズオン · Chalk talk 60 分ホワイトボード討論 · Code talk 60 分ライブコーディング · Lightning talk 20 分。

**キーノート・パネル**

| 日時 (PT) | セッション | 形式 | 見どころ |
|---|---|---|---|
| 12/1(火) 08:30 | [KEY002](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY002) CEO Keynote | Keynote | AI インフラ・推論・エージェント基盤の新発表 —— Physical AI 関連の発表有無を確認 |
| 12/2(水) 08:30 | [KEY003](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY003) Data & AI Keynote | Keynote | エージェントのデータ到達・価値測定・制約設定 —— P1 データと P5 エージェントの観点 |
| 12/2(水) 14:00 | [SUP201](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=SUP201) Training and simulation turn robot capabilities into useful products | Breakout session | NEURA Robotics・1X・Highlanders のパネル —— 学習・シミュレーション・データパイプラインを製品へ |
| 12/3(木) 08:30 | [KEY005](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY005) Technical Innovations Keynote | Keynote | Graviton・Trainium・ネットワーク・ストレージの内部 —— 学習インフラ選定の背景 |
| 12/3(木) 10:00 | [AIM2215](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2215) World Models & Physical AI: The next frontier in intelligent systems | Breakout session | ワールドモデルのパネル —— 研究者・顧客の本番展開経験と技術課題 |
| 12/3(木) 13:30 | [AIM2213](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2213) How leading AI builders push the frontier with AWS Trainium | Breakout session | ワールドモデル・Physical AI を含む 4 社の Trainium 活用パネル |

**Physical AI パイプライン — P1·P2·P3·P5**

| 日時 (PT) | セッション | 形式 | 見どころ |
|---|---|---|---|
| 11/30(月) 10:00 | [IND3338-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3338-R) Accelerate Physical AI development with NVIDIA on AWS | Chalk talk | AWS Physical AI Toolchain で合成データ→学習→sim-to-real→HIL 検証の全周期 |
| 11/30(月) 12:00 | [AIM449](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM449) One agent, any robot: building physical AI with Strands Robots | Chalk talk | Strands Robots SDK —— パラメータ 1 つで MuJoCo シミュレーションと実機を切替、GR00T・Cosmos 3・LeRobot ポリシー、IoT ブリッジのフリート |
| 11/30(月) 15:00 | [IND389](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND389) Physical AI for MedTech: From Intelligent Devices to Business Impact | Chalk talk | 医療機器の Physical AI スタック —— SageMaker 学習、Greengrass エッジ推論、規制対応 OTA |
| 12/1(火) 13:30<br>再演 12/1(火) 15:00 | [IND322-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND322-R) Physical AI in Telecom: A Framework for Workload Placement | Chalk talk | Physical AI ワークロードの配置基準 —— リージョン・Local Zones・Outposts・セルサイト |
| 12/1(火) 16:30 | [AIM413](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM413) Build a Physical AI Model Factory on SageMaker HyperPod | Chalk talk | 合成シナリオ→事後学習→評価のデータフライホイールを HyperPod EKS の異種 GPU プールで運用 |
| 12/2(水) 08:30<br>再演 12/3(木) 14:30 | [CMP407-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP407-R) Orchestrating Physical AI workloads on AWS: Compute and pipeline patterns | Chalk talk | Batch（並列シミュレーション）・EKS+Karpenter（学習）・HyperPod の比較、Capacity Blocks・Spot のコスト戦略 |
| 12/2(水) 12:30 | [AIM458-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM458-S) The Physical AI Blueprint: A Full-Stack Solution with AWS and NVIDIA (sponsored by NVIDIA) | Workshop | ハンズオン：Isaac Sim 合成データ、GR00T・Cosmos 学習、Omniverse ツイン、Greengrass 配備、AgentCore マルチロボット連携 |

**シミュレーション・デジタルツイン — P3**

| 日時 (PT) | セッション | 形式 | 見どころ |
|---|---|---|---|
| 11/30(月) 13:30 | [CMP408](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP408) The cloud holodeck: Stream NVIDIA Omniverse, scale headless sim on AWS | Chalk talk | DCV で Omniverse・Isaac Sim ワークステーションを配信 + Batch でヘッドレス大量レンダリング、VAMS で管理 |
| 12/1(火) 15:00 | [IND102-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND102-S) Accelerating with NVIDIA Omniverse: VW’s Battery Manufacturing Digital Twin (sponsored by NVIDIA) | Breakout session | フォルクスワーゲン電池工場の OpenUSD デジタルツイン —— 仮想立ち上げ・合成検査データ |
| 12/1(火) 16:00<br>再演 12/2(水) 09:00 | [IND401-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND401-R) Build, simulate, and validate physical AI-driven robotic systems | Builders' session | ハンズオン：仮想 PLC・フィールドバス・Omniverse 物理シミュレーションでマルチロボットセルのデジタルツイン |
| 12/2(水) 16:30 | [CON409](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CON409) ML, automotive, and robotics simulations at scale on AWS Batch | Breakout session | 自動車・ロボティクスのシミュレーション→データレイク→GPU 学習ループを Batch で編成 |
| 12/3(木) 16:30 | [IND3355](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3355) Building Worlds for Machines: VAMS and 3DGS for Autonomy | Lightning talk | 現場センサーデータ→3DGS 再構成→シミュレーション用環境（20 分ライトニング） |

**ワールドモデル・ロボット学習研究 — P2**

| 日時 (PT) | セッション | 形式 | 見どころ |
|---|---|---|---|
| 11/30(月) 13:00<br>再演 12/2(水) 12:00 | [AIM305-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM305-R) Hands-on training world models and deploying agents for Physical AI | Builders' session | ハンズオン：Trainium・Neuron で Transformer ワールドモデルを微調整（PEFT）しエージェントを配備 |
| 11/30(月) 16:00 | [AIM323](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM323) Serving world models on AWS Trainium with native PyTorch | Code talk | torch.compile・カスタムカーネルでワールドモデル推論を Trainium で提供 |
| 11/30(月) 16:30 | [INV531](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV531) Visual reasoning will be bigger than language reasoning | Chalk talk | UW の Ranjay Krishna —— 点・軌跡・深度など視覚表現で推論するロボット基盤モデル |
| 12/1(火) 11:30<br>再演 12/3(木) 13:30 | [AIM304-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM304-R) Deploy and optimize world models with agentic AI workflows | Builders' session | ハンズオン：リアルタイム映像ワールドモデルを Trainium に配備し Neuron エージェントスキルでカーネル最適化 |
| 12/2(水) 10:30 | [INV527](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV527) World models for indoor robots: what breaks and why | Chalk talk | Diligent Robotics 病院ロボットのライダー世界モデル —— Transformer の幾何推論が破綻する点 |
| 12/2(水) 13:30 | [INV537](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV537) No torque sensors, no problem: learning safe physical interaction for humanoids | Chalk talk | Fauna Robotics —— トルクセンサーなしのヒューマノイドで柔軟（コンプライアント）制御を学習 |

**モデル学習・データ基盤 — P1·P2**

| 日時 (PT) | セッション | 形式 | 見どころ |
|---|---|---|---|
| 11/30(月) 08:30 | [AIM406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM406) End-to-end foundation model pipelines on SageMaker HyperPod with EKS | Workshop | ハンズオン：HyperPod EKS でデータ準備→分散ファインチューニング→同一クラスターで推論 |
| 11/30(月) 15:00 | [AIM318](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM318) Resilient VLM Training at Scale on Amazon SageMaker HyperPod | Workshop | ハンズオン：VLM 学習中にノード障害を起こし、自動修復・チェックポイントで継続 |
| 11/30(月) 15:00 | [AIM433](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM433) Maximize GPU utilization across training and inference on HyperPod | Chalk talk | HyperPod をデータ処理・学習・推論の共用 GPU プールに —— チーム間スケジューリング |
| 12/1(火) 12:00<br>再演 12/3(木) 08:00 | [AIM334-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM334-R) Hands-on distributed training with AWS Trainium and PyTorch | Workshop | ハンズオン：TorchTitan で Trainium 分散学習 —— 並列化戦略・性能チューニング |
| 12/1(火) 14:30 | [AIM362](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM362) Which customization compute? A decision approach for model fine-tuning | Chalk talk | ファインチューニングの計算資源選定 —— サーバーレスカスタマイズ・学習ジョブ・HyperPod |
| 12/2(水) 15:00 | [AIM3308](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM3308) What's new: SageMaker HyperPod, with learnings from Multiverse | Breakout session | SageMaker HyperPod の新機能（EKS・Slurm）—— ワールドモデルを含む大規模学習・サービング |
| 12/2(水) 15:30<br>再演 12/3(木) 08:00 | [AIM434-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM434-R) From raw data to custom model: Dataset prep with Amazon SageMaker AI | Workshop | ハンズオン：プロファイリング・自動ラベル付け・人手レビュー・合成データで学習データを準備 |

**現場運用・エッジ — P4**

| 日時 (PT) | セッション | 形式 | 見どころ |
|---|---|---|---|
| 11/30(月) 10:00 | [DVT210-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=DVT210-S) When Telemetry Steers the Robot: Observability for Physical AI (sponsored by groundcover) | Breakout session | Path Robotics の溶接ロボット・四足ロボットのオブザーバビリティ事例（スポンサーセッション） |
| 11/30(月) 15:00<br>再演 12/1(火) 12:30 | [IND402-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND402-R) Agentic AI for manufacturing: Build a cross-domain digital thread | Workshop | ハンズオン：Neptune・AgentCore・IoT SiteWise で OT・IT データをつなぐ製造デジタルスレッド |
| 12/1(火) 12:30<br>再演 12/3(木) 08:30 | [HMC403-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC403-R) Self-managed agentic AI at the hybrid edge | Workshop | ハンズオン：Local Zones・Outposts で自己管理型エージェント AI を実行（データ所在・低遅延） |
| 12/2(水) 16:30 | [IND378](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND378) How Mercedes-Benz accelerates engineering and production with AI | Breakout session | メルセデス・ベンツ —— AgentCore のエンジニアリングエージェントとクラウドネイティブ MES・デジタルツイン |
| 12/3(木) 08:30 | [HMC406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC406) How Amazon Robotics runs AWS Outposts across hundreds of fulfillment centers | Code talk | Amazon Robotics が数百の物流センターで Outposts を運用する方法 —— 分離・フェイルオーバー |
| 12/3(木) 09:00 | [IND384](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND384) Inside T-Mobile's Kinetic Edge: Real-Time Physical AI at Scale | Breakout session | T-Mobile Kinetic Edge —— Outposts・SageMaker・AgentCore でネットワークエッジのリアルタイム Physical AI |
| 12/4(金) 08:30 | [IND345](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND345) Human+AI Collaboration: How Amazon Deploys Autonomous Operations on AWS | Breakout session | Amazon 物流現場 —— ヒューマノイド・四足・AMR・ドローン混在フリートの編成アーキテクチャ |

**AgentCore — P5**

| 日時 (PT) | セッション | 形式 | 見どころ |
|---|---|---|---|
| 11/30(月) 08:30<br>再演 12/2(水) 08:00 | [AIM439-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM439-R) Getting Started with AgentCore: ship an agent to production in 2 hours | Workshop | 2 時間ハンズオン：AgentCore CLI でランタイム・メモリ・ゲートウェイ・ID・ポリシー・可観測性・評価を順に追加 |
| 11/30(月) 10:00<br>再演 12/2(水) 15:00 | [AIM436-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM436-R) Scale production agents reliably with AgentCore | Chalk talk | セッション 10→1 万への拡張パターン —— microVM 分離、ツール呼び出し失敗・タイムアウト対応 |
| 11/30(月) 14:00<br>再演 12/3(木) 08:00 | [TNC331-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=TNC331-R) Ship AI Agents Faster with AgentCore Harness | Lab | ラボ：AgentCore Harness —— 設定だけでエージェントループを実行、ツール・スキル追加、バージョン付きエンドポイント |
| 11/30(月) 14:30 | [AIM370](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM370) Trusting agents in production: end-to-end security with AgentCore | Breakout session | AgentCore のエンドツーエンドセキュリティ —— microVM 分離・ID 伝播・Gateway ポリシー・Cedar 最小権限 |
| 12/2(水) 11:30 | [AIM450-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM450-R) Context engineering for production agents on AgentCore | Chalk talk | コンテキストエンジニアリング —— システムプロンプト・スキル・ツール定義・メモリの配分 |
| 12/2(水) 15:00 | [AIM212](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM212) Best practices for production agents on AgentCore, with Nasdaq | Breakout session | AgentCore 本番ベストプラクティス + Nasdaq のマルチアカウント分離・エージェント ID 運用 |
| 12/3(木) 14:30 | [AIM452](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM452) Build long-running agents that persist for days on AgentCore | Chalk talk | 数日続くエージェント —— Runtime の耐久実行・Memory・人の承認による一時停止/再開 |

**読むときに確認する範囲**：セッション概要（事前告知）であり、講演内容そのものではありません。日程・会場は変わることがあるため、イベントアプリで再確認してください。「35 週→3.5 週」（IND378）、「数週間→数時間」（IND401）などの数値は登壇者側の主張です。AIM305・AIM304 は Trainium でのワールドモデル学習・サービングのハンズオンを予告しています —— [P2](pillar-2.md) の「Trainium で VLA を学習した公開事例なし」という判断は、セッション資料が公開され再現が確認された後に見直します。

**次のアクション**：担当ピラーごとにセッションを選ぶ —— [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P4](pillar-4.md) · [P5](pillar-5.md)。イベント後、録画・資料が公開されたら該当行を原文リンクに差し替え、新サービス・新機能は [Radar](radar.md) の経路に乗せます。

## 継続して確認

公式[Physical AIブログ](https://aws.amazon.com/blogs/physical-ai/)と[RSS](https://aws.amazon.com/blogs/physical-ai/feed/)を確認します。公開日・原文・範囲・ピラーリンクを同時更新します。日次自動スキャンがこのページにない記事を `[4]` · ⏳ 原文照合待ち の表示で先に追加し、オーナーが原文を照合した後 `[3]` に変更します。また、技術昇格は既存の[維持管理ルール](maintenance.md)に従います。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 映像観測と言語指示からロボット動作を出力するモデルです。
[^openloop]: **Open-loop評価** — 記録済み観測・動作で予測誤差を測ります。環境と相互作用するポリシーの成功評価とは異なります。
[^3dgs]: **3D Gaussian Splatting（3DGS）** — 複数の写真・映像に多数の 3D ガウシアン（楕円体の点）を当てはめ、実写シーンをリアルタイムにレンダリングする 3D 再構成手法です。実際の現場をシミュレーションの背景に移す real-to-sim に使われます。
[^wfm]: **ワールド基盤モデル（WFM, World Foundation Model）** — 物理世界の次のシーンを予測・生成するよう学習された大型モデルです。テキスト・映像プロンプトから物理的にもっともらしい映像・シナリオを作り、ロボット学習データを拡張します。🎥 [NVIDIA Cosmos 紹介](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **ワールド・アクションモデル（WAM, World Action Model）** — 未来シーンの予測とロボット動作の生成を一つのモデルで同時に行うモデルです。映像だけを作るワールドモデルと異なり、関節角度やグリッパー指令など実行可能な動作を出力します。
[^dtwin]: **デジタルツイン（digital twin）** — 実際の工場・倉庫・ロボットを物理的に忠実に模した仮想レプリカです。実環境に触れずにポリシー学習・検証・シナリオ実験を可能にします。
[^p2r]: **pose-to-render レイテンシ** — ユーザーが頭を動かしてから、それに対応するフレームがヘッドセットに表示されるまでの時間です。長くなると見える映像と身体感覚がずれて酔いを引き起こすため、XR ストリーミング品質の中核指標です。
