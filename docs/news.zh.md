---
ko_hash: 5694ea64d5c0808c4703e3fc02a864757e025127
---
# 新消息

_owner: Youngjin · updated: 2026-10 · volatility: 高_

> **L0 TL;DR**: 精选 AWS Physical AI 新文章并连接现有支柱。以下为**原文发布日期**，列表确认日为 **2026-10-14**。实习路径见[工作坊与资料](workshops.md)。

按官方原文摘要，不代表独立复现性能数字。未验证技术候选继续由 [Radar](radar.md)管理。

## 近期资料一览

| 发布日期 | 资料 | 关联 |
|---|---|---|
| 2026-10-07 | [AWS Physical AI Toolchain 发布](#toolchain) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md) |
| 2026-10-06 | [3D Gaussian Splatting 行业应用案例](#gaussian-splatting) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-02 | [Isaac Lab on AWS — 从仿真到策略注册](#isaac-lab-aws) | [P3](pillar-3.md) · [Isaac Lab](workshops.md#isaac-lab) |
| 2026-09-28 | [NVIDIA Cosmos 3 on AWS](#cosmos-3) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) |
| 2026-09-10 | [在 SageMaker HyperPod EKS 上微调 π0](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence 的 DreamZero 实验](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics：太阳能板安装 AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics：人形机器人工具使用学习](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD 与 SDMA 工业数字孪生实现](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-15 | [Config：机器人训练数据增强](#config) | [P1](pillar-1.md) |

## AWS Physical AI Toolchain 发布 { #toolchain }

**发布日期: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

在 AWS 上运行从数据采集、合成数据、训练、仿真验证到边缘部署的 Physical AI 开发周期的参考架构、IaC 与部署自动化集合。它将 NVIDIA GR00T（VLA[^vla] 训练）、Isaac Sim、Isaac Lab、Cosmos、OSMO 连接到 S3、EKS、AWS Batch、SageMaker、EC2、IoT Greengrass（Jetson 部署），每个组件对应一个 Terraform 模块，可逐个引入。数据使用 Zarr→LeRobot，边缘使用 ONNX、ROS 2 等开放格式。代码：[aws-samples 仓库](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws)。

**阅读范围**: 官方参考架构。文章自述提供的是"基础设施模式，而非完成的机器人行为"。GR00T 示例使用 27 条 UR3 pick-and-place 演示，用于确认能否运行；"数小时而非数周"是 AWS 方面的说法。需要 GPU 配额（SageMaker 与 EC2）、NGC API 密钥和 Hugging Face 令牌，实验后须执行清理（tear down）以停止计费。

**后续行动**: 先引入一个瓶颈环节 — P1 数据 · P2 训练 · P3 仿真 · P5 编排（Strands 智能体层）· Radar 队列条目 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting 行业应用案例 { #gaussian-splatting }

**发布日期: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

介绍用开源 Splat Toolbox（[AWS Solutions Library 指导方案](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws)）处理 3DGS[^3dgs]（由照片和视频生成写实 3D 场景）的五阶段流水线（输入→预处理→重建→训练→后处理），以及在媒体、机器人、建筑、制造、房地产中的应用。使用 Step Functions、Lambda、AWS Batch/ECS 与 EC2 Spot。

**阅读范围**: 行业应用概述。机器人部分（合成训练数据、缩小 sim-to-real 差距、路径规划）是应用方向说明，没有策略性能实测。目前产出为静态 3D，4D（时间轴）资产在路线图上。"最高节省 50%"是 Spot 与按需计算价格的比较。

**后续行动**: P3 数字孪生与场景重建 · P4 real-to-sim 候选 — [P3](pillar-3.md) · [P4](pillar-4.md).

## Isaac Lab on AWS — 从仿真到策略注册 { #isaac-lab-aws }

**发布日期: 2026-10-02 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/isaac-lab-on-aws-from-simulation-to-registered-policy/) `[3]`**

一个 AWS CDK 解决方案，一次性部署预装 Isaac Sim 5.1.0、Isaac Lab v2.3.2、NVIDIA 驱动和 Amazon DCV 的黄金 AMI，单用户 Instance 模式与多用户 Fleet 模式（Cognito MFA、自动扩展），以及 SageMaker 训练任务与托管 MLflow 模型注册表。在桌面上构建的项目无需重建镜像即可提交为训练任务，训练出的策略会自动注册到 MLflow。示例包括 SO-ARM101 RL、SO-ARM101 遥操作数据采集和 Unitree H1 行走三种。

**阅读范围**: 不是公开仓库 — 按文章所述**通过 AWS 客户团队提供**。注册表只记录和标注策略，不负责服务部署，部署对接需团队自行构建。如需公开实习，请使用单独的 Isaac Lab 工作坊。

**后续行动**: P3 仿真 · 公开工作坊 [Isaac Lab](workshops.md#isaac-lab) — [P3](pillar-3.md).

## NVIDIA Cosmos 3 on AWS { #cosmos-3 }

**发布日期: 2026-09-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/nvidia-cosmos-3-on-aws-omnimodal-world-models-for-physical-ai/) `[3]`**

Cosmos 3（2026-05 发布）把此前的 Predict、Transfer、Reason 三个模型合并为一个 Mixture-of-Transformers 模型，一次推理即可同时输出场景理解、未来视频（WFM[^wfm]）和机器人动作轨迹（WAM[^wam]）。规模为 Super 64B、Nano 16B、Edge 4B。AWS 方面给出了从数据整理（Batch）、HyperPod 后训练、EKS+NIM 或 SageMaker JumpStart 推理到经 Greengrass 部署至 Jetson 边缘的参考架构及实例建议。

**阅读范围**: "首个完全开放的全模态模型"是 NVIDIA 的说法。完整检查点按 BF16 测试，文章自身也要求在给出各实例性能结论前先验证运行时配置。动作输出不能作为实机任务成功的依据。

**后续行动**: P1 合成数据 · P2 模型训练 · P3 仿真 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md).

## 在 SageMaker HyperPod EKS 上微调 π0 { #pi0-hyperpod }

**发布日期: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

介绍使用 DROID、LIBERO 的 π0 VLA 训练评估，连接 HyperPod EKS、FSx for Lustre 与训练任务配置。

**阅读范围**: 官方实现指南。报告的评估为 n=5 open-loop[^openloop]，不是实机任务成功率。2026-09-19 未能公开访问所链接代码路径，先阅读正文。

**后续行动**: P2 训练 · π0 阅读路径 — [P2](pillar-2.md) · [π0](workshops.md#pi0-guide).

## Telexistence 的 DreamZero 实验 { #telexistence-dreamzero }

**发布日期: 2026-09-09 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/bringing-a-frontier-world-model-to-the-convenience-store-inside-telexistences-dreamzero-experiment-on-aws/) `[3]`**

介绍零售机器人数据转换清洗、DreamZero 适配及仿真/实机评估，是使用 EC2、S3 的客户合作实验。

**阅读范围**: 客户实验/PoC。区分既有零售机器人运营实绩与 DreamZero 实验结果。

**后续行动**: P1 数据 · P2 训练 · P4 评估 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md).

## Luminous Robotics：太阳能板安装 AI { #luminous }

**发布日期: 2026-08-12 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/teaching-robots-to-see-how-luminous-robotics-is-accelerating-energy-infrastructure-construction-with-vision-action-ai/) `[3]`**

探索减少太阳能板放置时人工确认的视觉策略，采用 Isaac Sim 数据及 EC2、S3 学习流程。

**阅读范围**: 客户技术案例。区分仿真/离线评估与现场部署范围。

**后续行动**: P3 仿真 · P4 Sim-to-Real — [P3](pillar-3.md) · [P4](pillar-4.md).

## WIRobotics：人形机器人工具使用学习 { #wirobotics }

**发布日期: 2026-08-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-wirobotics-is-teaching-humanoid-robots-to-use-human-tools-with-aws-and-nvidia/) `[3]`**

韩国机器人企业的电钻操作学习项目，介绍如何在 AWS、NVIDIA 合作中连接数据质量、训练配置和实机评估。

**阅读范围**: 客户合作案例。特定工具任务的观察结果不代表通用人形机器人能力。

**后续行动**: P2 训练 · P4 实机评估 — [P2](pillar-2.md) · [P4](pillar-4.md).

## OpenUSD 与 SDMA 工业数字孪生实现 { #openusd }

**发布日期: 2026-07-31 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/build-l1-4-industrial-digital-twins-with-openusd-and-sdma-on-aws/) `[3]`**

从静态 3D 场景扩展至传感器信息、预测、再校准的分阶段实现，连接 OpenUSD 与 S3、Kinesis、Lambda、Batch。

**阅读范围**: 参考实现。区分合成传感器输入与实际设备集成，从需要的层级开始。

**后续行动**: P3 数字孪生 · OpenUSD 资料 — [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial).

## Config：机器人训练数据增强 { #config }

**发布日期: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

利用 S3、Bedrock 描述生成、Cosmos 变换及 HyperPod/EC2，增加已有机器人演示的视觉多样性。

**阅读范围**: 客户联合技术文章。可用于分别评估增强视频质量与实际策略改善。

**后续行动**: P1 数据采集处理 — [P1](pillar-1.md).

## 持续关注

关注官方 [Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/)及 [RSS](https://aws.amazon.com/blogs/physical-ai/feed/)。共同更新日期、原文、范围、支柱链接。每日自动扫描会先以 `[4]` · ⏳ 待原文核对 标记添加本页缺少的文章，负责人核对原文后改为 `[3]`；技术晋升遵循现有[维护规则](maintenance.md)。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 将视觉观测和语言指令转换为机器人动作的模型。
[^openloop]: **Open-loop 评估** — 对记录的观测动作计算预测误差，不同于策略与环境交互的任务成功评估。
[^3dgs]: **3D Gaussian Splatting（3DGS）** — 用大量 3D 高斯（椭球形点）拟合多张照片或视频，实时渲染写实场景的 3D 重建技术。用于 real-to-sim，即把真实现场搬进仿真作为背景。
[^wfm]: **世界基础模型（WFM, World Foundation Model）** — 为预测·生成物理世界的下一场景而训练的大型模型。通过文本·视频提示生成物理上合理的视频·场景，用于增强机器人学习数据。🎥 [NVIDIA Cosmos 介绍](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **世界-动作模型（WAM, World Action Model）** — 在一个模型中同时进行未来场景预测与机器人动作生成。与只生成视频的世界模型不同，它输出关节角度、夹爪指令等可执行动作。
