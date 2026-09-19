---
ko_hash: 6c812de4981e09fc57a08d454791c78c874795a4
---
# 工作坊与资料

_owner: Youngjin · updated: 2026-09 · volatility: 中_

> **L0 TL;DR**: 集中公开自学工作坊、实现指南和样本。**最后确认：2026-09-19**。点击标题访问原文，通过相关支柱了解架构。

时间和费用取决于模块、账户准备及 GPU 可用性。开始前确认原文 Prerequisites/Cleanup、权限和模型条件。本列表记录原文核对，不代表重跑全部实验。

## 按目标选择

| 目标 | 资料 | 相关支柱 |
|---|---|---|
| 入门仿真训练 | [NVIDIA Isaac Lab on AWS](#isaac-lab) | [P3](pillar-3.md) |
| 韩语 RL 到 VLA[^vla] | [Physical AI E2E 工作坊](#physical-ai-e2e) | [P2](pillar-2.md) |
| 智能体组件入门 | [Getting Started with Amazon Bedrock AgentCore](#agentcore-start) | [P5](pillar-5.md) |
| AgentCore 深入应用 | [Diving Deep with Amazon Bedrock AgentCore](#agentcore-deep) | [P5](pillar-5.md) |
| 阅读 π0 训练评估配置 | [在 SageMaker HyperPod EKS 上微调 π0](#pi0-guide) | [P2](pillar-2.md) |
| 连接 3D 资产、传感器、预测 | [OpenUSD 工业数字孪生样本](#spatial) | [P3](pillar-3.md) |
| 无实机查看仿真结果 | [VLA Simulator on AWS](#vla-simulator) | [P4](pillar-4.md) |
| 采集实机演示数据 | [Greengrass 上的 LeRobot 数据采集](#lerobot-collection) | [P1](pillar-1.md) |

## NVIDIA Isaac Lab on AWS { #isaac-lab }

**[NVIDIA Isaac Lab on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/075ce3fe-6888-4ea9-986e-5bdd1b767ef7/en-US) · AWS 官方工作坊 · English**

**内容**: 在 EC2 运行 Isaac Lab，用 AWS Batch 扩展，在 Isaac Sim 查看模型并清理。

**开始前确认**: 准备 AWS 权限、容器基础及 GPU 配额；实验基于仿真。

**相关支柱**: [P3](pillar-3.md).

## Physical AI E2E 工作坊 { #physical-ai-e2e }

**[Physical AI E2E 工作坊](https://hi-space.gitbook.io/physical-ai-on-aws/guide/e2e-workshop) · 社区制作指南 · 韩语**

**内容**: 按模块学习 Isaac Lab RL、GR00T VLA、Batch/SageMaker 和仿真评估。

**开始前确认**: 确认 CDK、Docker、GPU 环境及模型访问权，先选所需路径。

**相关支柱**: [P2](pillar-2.md).

## Getting Started with Amazon Bedrock AgentCore { #agentcore-start }

**[Getting Started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US) · AWS 官方工作坊 · English**

**内容**: 依次学习智能体原型、Memory、Gateway、观测评估、Policy。

**开始前确认**: 确认 AWS 账户及模型服务权限，机器人连接需单独集成。

**相关支柱**: [P5](pillar-5.md).

## Diving Deep with Amazon Bedrock AgentCore { #agentcore-deep }

**[Diving Deep with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-deep-dive/en-US) · AWS 官方工作坊 · English**

**内容**: 通过 Feature Deep Dive 或 Build with Skills 学习功能组合、安全及观测。

**开始前确认**: 官方要求先完成 Getting Started；开发环境按 Prerequisites 准备。

**相关支柱**: [P5](pillar-5.md).

## 在 SageMaker HyperPod EKS 上微调 π0 { #pi0-guide }

**[在 SageMaker HyperPod EKS 上微调 π0](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) · AWS 实现文章 · English**

**内容**: 连接 HyperPod EKS 数据、训练、评估、清理的新指南，2026-09-10 发布。

**开始前确认**: 高级配置。正文公开，但复核时所链接代码路径返回 404；获得代码前作为阅读资料。

**相关支柱**: [P2](pillar-2.md).

## OpenUSD 工业数字孪生样本 { #spatial }

**[OpenUSD 工业数字孪生样本](https://github.com/aws-samples/sample-physical-ai-spatial-intelligence) · aws-samples · English**

**内容**: L1 静态场景、L2 传感器层、L3 预测、L4 再校准；提供本地及 AWS 路径。

**开始前确认**: 按原文准备 Python、Node.js、Docker。使用此处公开 GitHub 地址克隆，而非 README 示例中的内部地址。

**相关支柱**: [P3](pillar-3.md).

## VLA Simulator on AWS { #vla-simulator }

**[VLA Simulator on AWS](https://github.com/aws-samples/sample-vla-simulator-on-aws) · aws-samples · English**

**内容**: 运行受支持的 VLA/仿真组合，将视频及摘要收集至 S3。

**开始前确认**: 确认 CDK、GPU 配额及逐模型许可证。小规模演示成功率不代表客户部署性能。

**相关支柱**: [P4](pillar-4.md).

## Greengrass 上的 LeRobot 数据采集 { #lerobot-collection }

**[Greengrass 上的 LeRobot 数据采集](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass) · aws-samples · 英语/韩语**

**内容**: 将 SO-ARM101 主从机械臂及相机数据记录为 LeRobot 格式并上传 S3。

**开始前确认**: 需要实机、相机和 Greengrass 设备；README 标明教育演示用途，不是直接生产部署代码。

**相关支柱**: [P1](pillar-1.md).

## 建议学习顺序

仿真学习可按 **Isaac Lab → E2E 所需路径 → VLA Simulator**。智能体按 **AgentCore Getting Started → Deep Dive**。数字孪生先 **OpenUSD 本地运行 → 所需 AWS 层级**。

## 资料更新

新资料记录提供者、语言、目的、准备条件、相关支柱、确认日。链接可用与实验可复现需分开核对。新发布见[新消息](news.md)，待验证技术见 [Radar](radar.md)。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 将视觉观测和语言指令转换为机器人动作的模型。
