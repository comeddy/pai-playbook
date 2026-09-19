---
ko_hash: 62cd1ee818e1aa36c2df871bece506e62dd803f7
---
# 新消息

_owner: Youngjin · updated: 2026-09 · volatility: 高_

> **L0 TL;DR**: 精选 AWS Physical AI 新文章并连接现有支柱。以下为**原文发布日期**，列表确认日为 **2026-09-19**。实习路径见[工作坊与资料](workshops.md)。

按官方原文摘要，不代表独立复现性能数字。未验证技术候选继续由 [Radar](radar.md)管理。

## 近期资料一览

| 发布日期 | 资料 | 关联 |
|---|---|---|
| 2026-09-10 | [在 SageMaker HyperPod EKS 上微调 π0](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence 的 DreamZero 实验](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics：太阳能板安装 AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics：人形机器人工具使用学习](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD 与 SDMA 工业数字孪生实现](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-15 | [Config：机器人训练数据增强](#config) | [P1](pillar-1.md) |

## 在 SageMaker HyperPod EKS 上微调 π0 { #pi0-hyperpod }

**发布日期: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

介绍使用 DROID、LIBERO 的 π0 VLA[^vla] 训练评估，连接 HyperPod EKS、FSx for Lustre 与训练任务配置。

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

关注官方 [Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/)及 [RSS](https://aws.amazon.com/blogs/physical-ai/feed/)。共同更新日期、原文、范围、支柱链接；技术晋升遵循现有[维护规则](maintenance.md)。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 将视觉观测和语言指令转换为机器人动作的模型。
[^openloop]: **Open-loop 评估** — 对记录的观测动作计算预测误差，不同于策略与环境交互的任务成功评估。
