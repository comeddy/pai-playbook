---
ko_hash: 5a3463b7c8a1274dfa99487730b7b3dc561aaea2
---
# 执行路径 — 数据、仿真与微调

_最后更新: 2026-09 · owner: Youngjin · volatility: 中_

**L0 TL;DR**: 填写[试点卡](start.md#pilot)后，选择解决当前瓶颈的一条路径。以下指南基于公开样本的**固定提交**。2026-09-15 对照了原文与命令；本次修改未新运行 AWS 资源或实机。区分样本作者的结果与本手册的复现。

## 共同准备与运行记录 { #prepare }

指定 AWS/IAM/数据、机器人/ML 负责人，实机试验还需现场安全负责人。检查 GPU 配额、区域、许可证及数据处理地点，设置时间和费用上限。预算告警本身不会停止任务，应指定停止负责人及流程。

```text
repo commit / container digest / dependency versions:
region / AZ / instance type / instance count:
dataset version / robot-camera configuration / train-eval split:
start-end time / setup-training-evaluation hours / actual cost:
success numerator-denominator / cycle time / interventions / latency:
failure evidence / cleanup result / operator / reviewer:
```

## A. 采集机器人数据并检查质量 { #data }

**适用**：使用 SO-ARM101 主从机械臂和双相机采集演示的团队。**其他机器人或 ROS bag 转换需要适配器工作**，不要假定样本自动支持。

**准备与版本**：[固定样本](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) `[1]`（MIT-0，教育/演示）。作者报告在 Jetson AGX Thor/JetPack 7 验证。需要 HEALTHY 的 Greengrass V2、Docker/NVIDIA runtime、已校准机器人/相机、同区域的 S3 桶及 IoT thing group。

```bash
git clone https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass.git
cd sample-lerobot-data-collection-on-aws-iot-greengrass
git checkout 6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e
```

**执行**：按固定版 `DEPLOYMENT_GUIDE.md` 0~0.2 节准备设备、权限及认证 → 部署 CloudFormation → 上传 `collect.py` → 以同版本 `recipe.yaml` 注册部署组件 → 网页录制短会话 → Save & Next → End Session → 检查 S3 产物与回放。替换指南命令中的环境 placeholder。

**产物与通过条件**：版本化数据集、回合清单、相机/动作时间对齐、缺帧、单位及成功/失败标签检查报告。满足约定的数据契约并可恢复中断上传。录制成功不保证训练质量。

**费用与停止**：设备/人员时间、S3、可选 KVS 视频传输、日志及网页资源。使用[预算表](start.md#roi)。对齐、校准、权限或安全条件不满足时停止采集。

**清理**：停止录制与视频流，从 Greengrass 部署移除组件。先决定保留数据，再检查本实验创建的 CloudFormation 资源、IoT 证书/策略、KVS、日志及桶。区分共享资源。

## B. 仿真训练与评估 { #simulation }

**适用**：通过 ANYmal-C 步行例子学习云训练和策略导出。合成图像或其他机器人任务需另行实验。

**准备与版本**：[固定样本](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) `[1]`（MIT，教育用）。**Isaac Lab v2.1.0 + Isaac Sim 4.5.0**，默认 `us-east-1`、`g6e.4xlarge`。与支柱的最新版本表不同，不可随意混用。需要 Terraform ≥1.5、AWS CLI、NGC 访问、GPU 配额及 SSH 密钥。

```bash
git clone https://github.com/aws-samples/sample-issac-lab-on-aws.git
cd sample-issac-lab-on-aws
git checkout 50ea76d87d873c1d69bed92c450ab144894f437e
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform validate
terraform plan
```

在变量文件填写区域、允许的 SSH 地址、密钥、存储等，审查 plan 后运行 `terraform apply`。样本将 NGC 密钥写入 state/user data，共享或长期环境应先改造密钥管理。按 README **bootstrap → 核心包安装 → 容器运行**的顺序。在已准备容器的 `/workspace/isaaclab` 中：

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py   --task Isaac-Velocity-Rough-Anymal-C-v0 --headless
```

**产物与通过条件**：配置、训练日志、checkpoint、独立评估视频和 `.pt`/`.onnx`。除奖励曲线外，测量约定地形的失败和跟踪误差。导出成功不等于通过实机部署。

**费用与停止**：作者约两小时/$12 是该研讨会估算，不能与首尔 g6e.xlarge 或 ETH 论文的 4~20 分钟结果组合。分别核算完整准备、训练、评估实例时间及 EBS、S3、公网 IPv4、日志。bootstrap 失败、显存不足或达到上限时停止。

**清理**：另行保留结果，审查 `terraform plan -destroy`，在该实验目录运行 `terraform destroy`。检查保留的 S3 对象、快照、日志、IP 等费用。实机测试是遵守[发布条件](operations.md#release)的独立阶段。

## C. 微调及有限边缘评估 { #finetuning }

**适用**：训练/评估数据分开且机器人观测、动作定义明确的团队。本路径不从零预训练基础模型。

**准备与证据范围**：[固定样本](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac) `[1]`（MIT-0）。作者报告 **IL Pattern A（Batch）**完成运行。B/C（SageMaker/HyperPod）未验证部署，RL 未在 GPU 运行，强制 Spot 中断恢复也未实证。需要 Node/npm/CDK、Python（`boto3`、`sagemaker`）、S3 数据、模型及基础模型访问权/许可证、GPU 配额。

```bash
git clone https://github.com/aws-samples/sample-vla-finetuning.git
cd sample-vla-finetuning
git checkout f21e4a9bf0ec11f40c2298a85951690b61efeaac
npm ci
npm run build
export PAI_AWS_REGION=us-west-2
npm run cdk -- synth PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

`us-west-2` 仅为示例；改为满足数据处理及容量要求的批准区域，CDK 与 CLI 使用相同值。

完成样本的 bootstrap、镜像及账户准备，审查资源后部署 Pattern A。

```bash
npm run cdk -- deploy PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

然后激活 Python 环境并运行：

```bash
cd containers/vla-ft
python vla_ft_cli.py --help
python vla_ft_cli.py --quickstart --backend batch --region "$PAI_AWS_REGION" --dry-run
```

dry-run 可能查询账户及容量，但不提交训练任务。**默认 quickstart 可能选 Pattern B，因此显式限定 `--backend batch`**。确认模型、batch、显存、估价后，如要运行自带数据实验，将同一命令的 `--dry-run` 改为 `--yes`。客户数据用 `--dataset s3://... --model ...` 代替 `--quickstart`，按 `--help` 配置。

**产物与通过条件**：数据、基础 checkpoint、配置、新 checkpoint 的谱系；与基线模型同条件评估；成功分子/分母、重复及未学习环境、周期、人工介入。演示数量不保证成功率或完成日期。

**边缘交接**：训练样本不完成实机部署。验证模型特定导出/服务、观测顺序及归一化、动作单位、设备兼容性、观测到动作延迟。连接 [P4 部署资产](pillar-4.md)和[发布条件](operations.md#release)，开展有监督的有限测试。

**费用、停止与清理**：分别记录估价和实际账单。显存不足、评估停滞、预算或时间到限时停止。保留 checkpoint，检查 Batch 任务及计算环境，删除实验专用 CDK stack。GPU 为零仍可能产生 EFS、S3、NAT、日志费用。共享 stack 应与负责人核对。

**➡️ 后续行动**：记录准备、执行、评估及清理结果，以[试点卡](start.md#pilot)决定下一阶段。将实际复现证据加入[证据记录](evidence.md)。

_owner: Youngjin · updated: 2026-09 · volatility: 中_
