---
ko_hash: 6c812de4981e09fc57a08d454791c78c874795a4
---
# ワークショップ・資料

_owner: Youngjin · updated: 2026-09 · volatility: 中_

> **L0 TL;DR**: 公開の自習ワークショップ・実装ガイド・サンプルを集めました。**最終確認：2026-09-19**。題名から原文へ、関連ピラーから構成の背景へ進めます。

時間と費用はモジュール・アカウント準備・GPU可用性で変わります。Prerequisites・Cleanup、権限、モデル条件を先に確認します。原文閲覧の記録であり全実習の再実行ではありません。

## 目的別に選ぶ

| 目的 | 資料 | 関連ピラー |
|---|---|---|
| シミュレーション学習入門 | [NVIDIA Isaac Lab on AWS](#isaac-lab) | [P3](pillar-3.md) |
| 韓国語でRLからVLA[^vla]まで | [Physical AI E2Eワークショップ](#physical-ai-e2e) | [P2](pillar-2.md) |
| エージェント構成要素の入門 | [Getting Started with Amazon Bedrock AgentCore](#agentcore-start) | [P5](pillar-5.md) |
| AgentCoreの応用 | [Diving Deep with Amazon Bedrock AgentCore](#agentcore-deep) | [P5](pillar-5.md) |
| π0の学習・評価構成を読む | [SageMaker HyperPod EKSでπ0をファインチューニング](#pi0-guide) | [P2](pillar-2.md) |
| 3D資産・センサー・予測の接続 | [OpenUSD産業デジタルツインサンプル](#spatial) | [P3](pillar-3.md) |
| 実機なしでシミュレーション結果を見る | [VLA Simulator on AWS](#vla-simulator) | [P4](pillar-4.md) |
| 実ロボットの実演データ収集 | [GreengrassでLeRobotデータ収集](#lerobot-collection) | [P1](pillar-1.md) |

## NVIDIA Isaac Lab on AWS { #isaac-lab }

**[NVIDIA Isaac Lab on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/075ce3fe-6888-4ea9-986e-5bdd1b767ef7/en-US) · AWS公式ワークショップ · English**

**内容**: EC2上のIsaac Lab、AWS Batchでの拡張、Isaac Simでの確認、後片付けを学びます。

**開始前の確認**: AWS権限、コンテナ基礎、GPUクォータを準備します。シミュレーションの実習です。

**関連ピラー**: [P3](pillar-3.md).

## Physical AI E2Eワークショップ { #physical-ai-e2e }

**[Physical AI E2Eワークショップ](https://hi-space.gitbook.io/physical-ai-on-aws/guide/e2e-workshop) · コミュニティ制作ガイド · 韓国語**

**内容**: Isaac Lab RL、GR00T VLA、Batch・SageMaker、シミュレーション評価をモジュール別に学びます。

**開始前の確認**: CDK・Docker・GPU環境とモデルアクセスを確認し、必要なトラックから選びます。

**関連ピラー**: [P2](pillar-2.md).

## Getting Started with Amazon Bedrock AgentCore { #agentcore-start }

**[Getting Started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US) · AWS公式ワークショップ · English**

**内容**: エージェント原型、Memory、Gateway、観測・評価、Policyを順に確認します。

**開始前の確認**: AWSアカウントとモデル・サービス権限を確認します。ロボット接続は別途統合が必要です。

**関連ピラー**: [P5](pillar-5.md).

## Diving Deep with Amazon Bedrock AgentCore { #agentcore-deep }

**[Diving Deep with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-deep-dive/en-US) · AWS公式ワークショップ · English**

**内容**: Feature Deep DiveまたはBuild with Skillsで機能の組合せ・セキュリティ・観測を学びます。

**開始前の確認**: 公式案内はGetting Startedの事前完了を求めます。開発環境はPrerequisitesに従います。

**関連ピラー**: [P5](pillar-5.md).

## SageMaker HyperPod EKSでπ0をファインチューニング { #pi0-guide }

**[SageMaker HyperPod EKSでπ0をファインチューニング](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) · AWS実装記事 · English**

**内容**: HyperPod EKSでデータ・学習・評価・後片付けをつなぐ2026-09-10公開ガイドです。

**開始前の確認**: 高度な構成です。本文は公開されていますが確認時にコード経路は404でした。アクセス解決までは読解資料として使います。

**関連ピラー**: [P2](pillar-2.md).

## OpenUSD産業デジタルツインサンプル { #spatial }

**[OpenUSD産業デジタルツインサンプル](https://github.com/aws-samples/sample-physical-ai-spatial-intelligence) · aws-samples · English**

**内容**: L1静的場面、L2センサー層、L3予測、L4再校正をローカル・AWSで試せます。

**開始前の確認**: Python・Node.js・Docker等の前提に従います。README例の内部URLではなく、ここで案内する公開GitHubから取得します。

**関連ピラー**: [P3](pillar-3.md).

## VLA Simulator on AWS { #vla-simulator }

**[VLA Simulator on AWS](https://github.com/aws-samples/sample-vla-simulator-on-aws) · aws-samples · English**

**内容**: 対応VLA・シミュレーターの組合せを実行し、映像・結果をS3に集めるサンプルです。

**開始前の確認**: CDK・GPUクォータ・モデル別利用権を確認します。少数デモの成功率は顧客配備性能を意味しません。

**関連ピラー**: [P4](pillar-4.md).

## GreengrassでLeRobotデータ収集 { #lerobot-collection }

**[GreengrassでLeRobotデータ収集](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass) · aws-samples · 英語/韓国語**

**内容**: SO-ARM101リーダー・フォロワーとカメラのデータをLeRobot形式で記録しS3へ送ります。

**開始前の確認**: 実機・カメラ・Greengrass機器が必要です。READMEでは教育・デモ用とされ、そのまま本番利用する資料ではありません。

**関連ピラー**: [P1](pillar-1.md).

## 学習順序

シミュレーションは**Isaac Lab → 必要なE2Eトラック → VLA Simulator**、エージェントは**AgentCore Getting Started → Deep Dive**がおすすめです。デジタルツインは**OpenUSDローカル実行 → 必要なAWS段階**を選びます。

## 資料の更新

提供者・言語・目的・前提・関連ピラー・確認日を記録します。リンク到達性と実習再現性は別に確認します。発表は[新着情報](news.md)、検証待ちは[Radar](radar.md)に接続します。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 映像観測と言語指示からロボット動作を出力するモデルです。
