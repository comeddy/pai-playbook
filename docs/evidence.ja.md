---
ko_hash: c52bf32e3cb8f788b6384f47337ac5a43f993bf1
---
# 根拠記録 — 主張ごとの確認日・範囲・レビュー状態

_最終更新: 2026-09 · owner: Youngjin · volatility: 中_

**L0 TL;DR**: ページ更新日は全主張の再確認日ではありません。今回の主要修正7件を記録しています。他の既存主張は未移行であり、全件監査を意味しません。

`source-checked`は指定した一次資料との照合、`withdrawn`は以前の一般化・保証の撤回、`reproduction-pending`は実行再現待ちです。全件**人による確認待ち**であり、AWSの公式承認・保証ではありません。原文照合、実験再現、現場配備承認は別段階です。

原本は[claims.json](assets/claims.json)です。本ページのブロックはそこから生成します。CIは必須項目、4言語、影響ページ、日付、表示同期を確認し、期限超過を警告します。出典の真実性や現場適合性は判定しません。

<!-- evidence:start -->

### openvla-license { #openvla-license }

OpenVLAはMITのコードとLlama Community Licenseが適用されるLlama-2派生の事前学習重みを区別します。商用判断では選択した重み・基盤モデル・データの条件を確認し、コードLICENSEだけで判定しません。

- 確認日: 2026-09-15 · 状態: `source-checked` · 確認周期（日）: 30
- 照合担当: Codex (source comparison) · 人による確認: 未実施
- 影響ページ: [pillar-2](pillar-2.md) · [decisions](decisions.md) · [exec](exec.md)
- 出典: [OpenVLA README](https://github.com/openvla/openvla#pretrained-vlas)

### agentcore-residency { #agentcore-residency }

AgentCoreの提供・保存・推論処理リージョンは別です。MemoryはAPAC内の複数リージョンを利用でき、ソウル発Evaluationsはグローバルクロスリージョン推論の対象です。韓国内処理要件を機能・モデル・経路ごとに確認します。

- 確認日: 2026-09-15 · 状態: `source-checked` · 確認周期（日）: 30
- 照合担当: Codex (source comparison) · 人による確認: 未実施
- 影響ページ: [pillar-5](pillar-5.md) · [decisions](decisions.md) · [exec](exec.md) · [operations](operations.md)
- 出典: [AWS cross-region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html) · [AWS Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-cross-region-inference.html)

### fleetwise-new-customers { #fleetwise-new-customers }

IoT FleetWiseは新規顧客の受付を停止し、既存顧客は継続利用できます。サービス終了と断定せず、新規ロボットフリートの既定案には含めません。

- 確認日: 2026-09-15 · 状態: `source-checked` · 確認周期（日）: 30
- 照合担当: Codex (source comparison) · 人による確認: 未実施
- 影響ページ: [pillar-5](pillar-5.md) · [radar](radar.md)
- 出典: [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)

### action-chunking { #action-chunking }

動作出力数と新観測に反応する頻度は異なります。推論Hzとchunk長の積をフィードバック制御周波数にしません。PIは切替・遅延を別問題として扱います。HelixのS1/S2は両方オンボードです。

- 確認日: 2026-09-15 · 状態: `source-checked` · 確認周期（日）: 90
- 照合担当: Codex (source comparison) · 人による確認: 未実施
- 影響ページ: [pillar-2](pillar-2.md) · [pillar-4](pillar-4.md) · [pillar-5](pillar-5.md) · [decisions](decisions.md) · [operations](operations.md)
- 出典: [PI real-time chunking](https://www.physicalintelligence.company/research/real_time_chunking) · [Figure Helix](https://www.figure.ai/news/helix)

### simulation-cost { #simulation-cost }

「ソウルg6e.xlarge＋4～20分＝1回$11～12」という一般化を撤回します。$0.98/時と4～20分の積は算術上約$0.07～0.33で、その機種の実測ではありません。作者の約2時間/$12は別構成の見積です。

- 確認日: 2026-09-15 · 状態: `withdrawn` · 確認周期（日）: 30
- 照合担当: Codex (source comparison) · 人による確認: 未実施
- 影響ページ: [pillar-3](pillar-3.md) · [execution](execution.md) · [exec](exec.md)
- 出典: [Pinned simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [ETH parallel RL paper](https://arxiv.org/abs/2109.11978)

### finetuning-outcomes { #finetuning-outcomes }

「100～500実演で80%以上成功」「100実演で1日成果」という共通保証を撤回します。成功率・期間にはデータ、業務、モデル、学習・評価条件を定めた実験が必要です。

- 確認日: 2026-09-15 · 状態: `withdrawn` · 確認周期（日）: 90
- 照合担当: Codex (source comparison) · 人による確認: 未実施
- 影響ページ: [pillar-2](pillar-2.md) · [exec-guide](exec-guide.md) · [decisions](decisions.md) · [execution](execution.md)
- 出典: [OpenVLA fine-tuning](https://github.com/openvla/openvla#fine-tuning-openvla-via-lora)

### execution-samples { #execution-samples }

3サンプルのコミット・README・コマンドを照合しました。本改訂でAWS・実機実行はしていません。作者のPattern A完走報告とB/C・RL・強制中断復旧の検証を同等に扱いません。

- 確認日: 2026-09-15 · 状態: `reproduction-pending` · 確認周期（日）: 30
- 照合担当: Codex (source comparison) · 人による確認: 未実施
- 影響ページ: [execution](execution.md) · [pillar-1](pillar-1.md) · [pillar-2](pillar-2.md) · [pillar-3](pillar-3.md)
- 出典: [Data sample](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) · [Simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [Training sample](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac)

<!-- evidence:end -->

## 更新とレビュー分担 { #review }

ownerのYoungjinが確認作業を割り当てます。ライセンス、AWSサービス・リージョン、ロボット制御・安全、再現実験の人による確認担当は**未割当**であり、名前を仮定しません。照合担当を記録し、実際に人が確認した場合だけ`human_review: complete`と実名を記入します。

主張変更時は`pages`の原文・要約・翻訳を同時更新し、確認日・根拠も更新します。`python3 scripts/check_evidence.py --render`、翻訳ハッシュ更新、全検査の順に実施します。HTTP 200、ビルド成功、翻訳ハッシュは事実確認の代替ではありません。

_owner: Youngjin · updated: 2026-09 · volatility: 中_
