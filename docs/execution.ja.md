---
ko_hash: 5a3463b7c8a1274dfa99487730b7b3dc561aaea2
---
# 実行手順 — データ・シミュレーション・ファインチューニング

_最終更新: 2026-09 · owner: Youngjin · volatility: 中_

**L0 TL;DR**: [パイロットカード](start.md#pilot)を作成し、現在のボトルネックに対応する手順を1つ選びます。公開サンプルの**固定コミット**を読んで整理したガイドです。2026-09-15に原文・コマンドを照合しましたが、本改訂でAWSリソースや実機は新規実行していません。作者の実測と本書の再現を区別します。

## 共通準備と実行記録 { #prepare }

AWS/IAM・データ、ロボット・ML担当、実機試験では現場安全責任者を定めます。GPUクォータ、リージョン、ライセンス、データ処理場所を確認し、実行時間・費用の上限を設定します。予算通知だけではジョブは停止しないため、停止担当者と手順を決めます。

```text
repo commit / container digest / dependency versions:
region / AZ / instance type / instance count:
dataset version / robot-camera configuration / train-eval split:
start-end time / setup-training-evaluation hours / actual cost:
success numerator-denominator / cycle time / interventions / latency:
failure evidence / cleanup result / operator / reviewer:
```

## A. ロボットデータ収集と品質確認 { #data }

**対象**：SO-ARM101のリーダー/フォロワーと2台のカメラで実演を収集するチームです。**他機種やROS bag変換は別途アダプター実装が必要**です。

**準備・バージョン**：[固定サンプル](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) `[1]`（MIT-0、教育・デモ用）。作者はJetson AGX Thor・JetPack 7での検証を記載しています。HEALTHYのGreengrass V2、Docker/NVIDIAランタイム、校正したロボット・カメラ、同じリージョンのS3バケット・IoT thing groupが必要です。

```bash
git clone https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass.git
cd sample-lerobot-data-collection-on-aws-iot-greengrass
git checkout 6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e
```

**実行順序**：固定版`DEPLOYMENT_GUIDE.md`の0～0.2節で機器・権限・認証を準備 → CloudFormation配備 → `collect.py`アップロード → 同版の`recipe.yaml`でコンポーネント登録・配備 → Webコンソールで短い収録 → Save & Next → End Session → S3結果と再生を確認します。AWSコマンドはガイドの環境placeholderを置き換えます。

**成果物・合格条件**：版付きデータセット、エピソード一覧、カメラ/動作時刻の整合、欠落フレーム、単位、成功/失敗ラベルの検査報告です。データ契約を満たし、中断アップロードを復旧できることを確認します。収録成功は学習品質の保証ではありません。

**費用・中止**：機器・操作者時間、S3、任意のKVS映像・転送、ログ・Web資源を[予算表](start.md#roi)で見積もります。時刻整合・校正・権限・安全条件に失敗したら追加収集を停止します。

**後片付け**：収録・映像配信を停止し、Greengrass配備からコンポーネントを外します。保存要否を先に決め、実験で作ったCloudFormation資源、IoT証明書・ポリシー、KVS、ログ、バケットを確認します。共有資源を区別します。

## B. シミュレーション学習・評価 { #simulation }

**対象**：ANYmal-Cの歩行例でクラウド学習とポリシーexportを学ぶチームです。合成画像や他ロボットの性能検証は別実験です。

**準備・バージョン**：[固定サンプル](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) `[1]`（MIT、教育用）。**Isaac Lab v2.1.0 + Isaac Sim 4.5.0**、既定は`us-east-1`、`g6e.4xlarge`です。ピラーの最新版表とは異なるため混在させません。Terraform ≥1.5、AWS CLI、NGCアクセス、GPUクォータ、SSHキーが必要です。

```bash
git clone https://github.com/aws-samples/sample-issac-lab-on-aws.git
cd sample-issac-lab-on-aws
git checkout 50ea76d87d873c1d69bed92c450ab144894f437e
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform validate
terraform plan
```

変数ファイルにリージョン、許可SSHアドレス、キー、ストレージ等を記入し、planを確認後`terraform apply`します。NGCキーがstate/user dataに保存されるため、共有・長期環境では先にシークレット管理を変更します。READMEの**bootstrap → コアパッケージ導入 → コンテナ実行**に従います。準備済みコンテナの`/workspace/isaaclab`内では：

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py   --task Isaac-Velocity-Rough-Anymal-C-v0 --headless
```

**成果物・合格条件**：設定、学習ログ、チェックポイント、別評価の映像、`.pt`/`.onnx`です。報酬以外にも合意した地形で失敗・追従誤差を測ります。export成功は実機配備の合格ではありません。

**費用・中止**：作者の約2時間/$12は当該ワークショップの見積であり、ソウルg6e.xlarge料金やETH論文の4～20分の結果と組み合わせません。準備・学習・評価の全時間、EBS、S3、パブリックIPv4、ログを算出します。起動失敗、メモリ不足、上限到達で停止します。

**後片付け**：結果を別途保存し、実験ディレクトリで`terraform plan -destroy`を確認して`terraform destroy`します。残ったS3オブジェクト、スナップショット、ログ、IP等の費用を確認します。実機試験は[配備ゲート](operations.md#release)に従う別段階です。

## C. ファインチューニングと限定エッジ評価 { #finetuning }

**対象**：学習・評価データを分離し、ロボット観測・動作を定義したチームです。基盤モデルをゼロから事前学習する手順ではありません。

**準備・検証範囲**：[固定サンプル](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac) `[1]`（MIT-0）。作者は**IL Pattern A（Batch）**の完走を報告しています。B/C（SageMaker/HyperPod）は配備未検証、RLはGPU未実行、強制Spot中断・復旧も未実証です。Node/npm/CDK、Python（`boto3`、`sagemaker`）、S3データ、モデル・基盤モデルのアクセスと利用権、GPUクォータが必要です。

```bash
git clone https://github.com/aws-samples/sample-vla-finetuning.git
cd sample-vla-finetuning
git checkout f21e4a9bf0ec11f40c2298a85951690b61efeaac
npm ci
npm run build
export PAI_AWS_REGION=us-west-2
npm run cdk -- synth PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

`us-west-2`は例です。データ処理・容量要件を満たす承認済み地域に変更し、CDKとCLIで同じ値を使います。

サンプルのbootstrap、イメージ準備、アカウント設定を完了し、資源を確認してPattern Aを配備します。

```bash
npm run cdk -- deploy PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

その後Python環境を有効にして実行します：

```bash
cd containers/vla-ft
python vla_ft_cli.py --help
python vla_ft_cli.py --quickstart --backend batch --region "$PAI_AWS_REGION" --dry-run
```

dry-runはアカウント・容量を照会する場合がありますが学習ジョブを投入しません。**既定quickstartがPattern Bを選ぶ場合があるため、`--backend batch`で限定**します。モデル、バッチ、メモリ、見積を確認し、同梱データで実行する場合は同じコマンドの`--dry-run`を`--yes`に変更します。顧客データは`--quickstart`の代わりに`--dataset s3://... --model ...`を指定し、`--help`に従います。

**成果物・合格条件**：データ・基盤チェックポイント・設定・新チェックポイントの系譜、同条件の基準モデル比較、成功数/試行数、反復・未学習条件、作業時間、人の介入を記録します。実演数から成功率や完了日を保証しません。

**エッジ引継ぎ**：学習サンプルだけで実機配備は完了しません。モデル別export/serving、観測順序・正規化、動作単位、機器互換性、観測→動作遅延を検証します。[P4の配備資産](pillar-4.md)と[配備ゲート](operations.md#release)を接続して監督下で限定試験します。

**費用・中止・後片付け**：見積と実請求を分けます。メモリ不足、評価停滞、費用・期限上限で中止します。チェックポイントを保存し、Batchジョブ・計算環境を確認して実験専用CDKスタックを削除します。GPUがゼロでもEFS・S3・NAT・ログ等は課金が残ります。共有スタックは担当者と確認します。

**➡️ 次のアクション**：準備・実行・評価・後片付けを記録し、[パイロットカード](start.md#pilot)で次段階を判断します。実際の再現証拠を[根拠記録](evidence.md)に追加します。

_owner: Youngjin · updated: 2026-09 · volatility: 中_
