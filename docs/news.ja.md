---
ko_hash: 62cd1ee818e1aa36c2df871bece506e62dd803f7
---
# 新着情報

_owner: Youngjin · updated: 2026-09 · volatility: 高_

> **L0 TL;DR**: AWS Physical AIの新記事を選び既存ピラーにつなぎます。以下は**原文公開日**、一覧確認日は**2026-09-19**です。[ワークショップ・資料](workshops.md)で学習経路を選べます。

公式原文に基づく要約であり性能数値の独立再現ではありません。未検証候補は既存の[Radar](radar.md)で管理します。

## 最近の資料一覧

| 公開日 | 資料 | 関連 |
|---|---|---|
| 2026-09-10 | [SageMaker HyperPod EKSでπ0をファインチューニング](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [TelexistenceのDreamZero実験](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Roboticsの太陽光パネル設置AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRoboticsのヒューマノイド道具操作学習](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD・SDMAによる産業デジタルツイン](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-15 | [Configのロボット学習データ拡張](#config) | [P1](pillar-1.md) |

## SageMaker HyperPod EKSでπ0をファインチューニング { #pi0-hyperpod }

**公開日: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

DROID・LIBEROでのπ0 VLA[^vla]学習・評価を紹介し、HyperPod EKS、FSx for Lustre、学習ジョブ構成をつなぎます。

**確認する範囲**: 公式実装ガイドです。報告値はn=5のopen-loop[^openloop]で、実機成功率ではありません。2026-09-19時点でリンク先コードに公開アクセスできず、まず本文を参照します。

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

## Configのロボット学習データ拡張 { #config }

**公開日: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

収集済み実演の視覚的多様性をS3、Bedrockの説明生成、Cosmos変換、HyperPod/EC2で増やします。

**確認する範囲**: 顧客共同技術記事です。拡張映像品質と実ポリシー改善を個別評価する際の参考です。

**次のアクション**: P1データ収集・処理 — [P1](pillar-1.md).

## 継続して確認

公式[Physical AIブログ](https://aws.amazon.com/blogs/physical-ai/)と[RSS](https://aws.amazon.com/blogs/physical-ai/feed/)を確認します。公開日・原文・範囲・ピラーリンクを同時更新し、技術昇格は既存の[維持管理ルール](maintenance.md)に従います。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 映像観測と言語指示からロボット動作を出力するモデルです。
[^openloop]: **Open-loop評価** — 記録済み観測・動作で予測誤差を測ります。環境と相互作用するポリシーの成功評価とは異なります。
