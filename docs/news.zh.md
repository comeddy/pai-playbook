---
ko_hash: 6d385b283f526caca083d3149b2aa9ee357e351f
---
# 新消息

_owner: Youngjin · updated: 2026-11 · volatility: 高_

> **L0 TL;DR**: 精选 AWS Physical AI 新文章并连接现有支柱。以下为**原文发布日期**，列表确认日为 **2026-10-14**。实习路径见[工作坊与资料](workshops.md)。

按官方原文摘要，不代表独立复现性能数字。未验证技术候选继续由 [Radar](radar.md)管理。

> **re:Invent 2026（11/30–12/4，拉斯维加斯）**：已从完整场次目录中[挑选](#reinvent-2026) 45 个 Physical AI、仿真、模型训练、数据、边缘、AgentCore 相关场次。

## 近期资料一览

| 发布日期 | 资料 | 关联 |
|---|---|---|
| 2026-10-28 | [AWS × RLWRLD —— 为明日的劳动力打造 Physical AI](#aws-rlwrld-workforce) | [Radar](radar.md) · [P2](pillar-2.md) |
| 2026-10-28 | [Visual Asset Management System 2.6 发布](#vams-2-6) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-07 | [AWS Physical AI Toolchain 发布](#toolchain) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md) |
| 2026-10-06 | [3D Gaussian Splatting 行业应用案例](#gaussian-splatting) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-02 | [Isaac Lab on AWS — 从仿真到策略注册](#isaac-lab-aws) | [P3](pillar-3.md) · [Isaac Lab](workshops.md#isaac-lab) |
| 2026-09-28 | [NVIDIA Cosmos 3 on AWS](#cosmos-3) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) |
| 2026-09-10 | [在 SageMaker HyperPod EKS 上微调 π0](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence 的 DreamZero 实验](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics：太阳能板安装 AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics：人形机器人工具使用学习](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD 与 SDMA 工业数字孪生实现](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-17 | [Edge Impulse 与 AWS — 结合边缘推理与云端智能](#edge-impulse-aws) | [P4](pillar-4.md) · [P5](pillar-5.md) |
| 2026-07-15 | [Config：机器人训练数据增强](#config) | [P1](pillar-1.md) |

## AWS × RLWRLD —— 为明日的劳动力打造 Physical AI { #aws-rlwrld-workforce }

**发布日期: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/aws-rlwrld-building-the-workforce-of-tomorrow-with-physical-ai/) `[4]` · ⏳ 待原文核对 (自动扫描 2026-11-02)**

AWS 与 RLWRLD 合作系列的第二篇文章，是 2026-06-22 第一篇（"Putting Dexterous Robots to Work"）的后续。文章介绍 RLWRLD 已成为 AWS Validated Partner，并在 AWS Marketplace 上架两款产品，还涉及针对劳动力短缺场景（搬箱子、商品拣选、货架补货）的 PoC 计划，以及通过 AWS Physical AI 路演形成的客户管道。文章还引用了 RLDX-1 以约 20% 的训练算力达到与领先基础模型相当性能的说法。

**阅读范围**: AWS·RLWRLD 官方合作系列文章（客户合作介绍性质）。"AWS Validated Partner"与 Marketplace 上架是合作伙伴项目身份，不是实际部署成果。搬箱子·商品拣选·货架补货 PoC 在原文中描述为"计划"（planned）阶段，并非已投入实际运行。"约 20% 算力达到相当性能"的说法引用了 RLWRLD 自家技术博客，属于厂商自行表述，与 Radar 中 RLDX-1 条目已有的自行公布基准性质相同——不是独立实测。本次会话因全局 egress 封锁无法直接访问 aws.amazon.com 原文，改用多条独立搜索结果（标题·日期·核心表述一致）交叉核对——具体数字仍需 owner 对照原文确认。

**后续行动**: 连接现有 RLDX-1 Radar 条目 · P2 模型训练 — [Radar](radar.md) · [P2](pillar-2.md).

## Visual Asset Management System 2.6 发布 { #vams-2-6 }

**发布日期: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/visual-asset-management-system-2-6-release/) `[4]` · ⏳ 待原文核对 (自动扫描 2026-11-02)**

VAMS 是 AWS Physical AI·PACE 团队打造的开源 3D/空间资产管理加速器，2.6 被称为自 2.0（2024-06）以来"最大的一次更新"。本次重新设计了编排层，新增多文件·多资产执行、全局执行视图、上传触发自动工作流，并加入 AWS European Sovereign Cloud 部署模板、Amazon Cognito OIDC 联合登录、更细粒度的 IAM 角色定制、默认拦截型 WAF，以及资产生命周期·逐版本变更历史等溯源追踪功能。演示内容包括语义搜索、浏览器内 SuperSplat（高斯泼溅[^3dgs]）编辑器、IFC BIM 查看器、地理空间地图搜索，以及 NVIDIA Cosmos text-to-world 工作流。代码在 [GitHub awslabs/visual-asset-management-system](https://github.com/awslabs/visual-asset-management-system) 开源。

**阅读范围**: 官方开源方案更新文章。"自 2.0 以来最大的更新"是 AWS 自己的说法，文章未给出实际客户生产环境采用成果或性能数字。这是公开仓库，不是客户团队专属路径——任何人都能从 GitHub 获取。本次会话因全局 egress 封锁无法直接访问 aws.amazon.com 原文，改用搜索结果片段与 GitHub 发布标签（2.6.0 于 2026-09-11 至 2.6.6 于 2026-10-30）交叉核对——发布日期（2026-10-28）同样以搜索结果片段为准，需 owner 对照原文确认。

**后续行动**: P3 数字孪生与场景重建 · P4 real-to-sim 候选 — [P3](pillar-3.md) · [P4](pillar-4.md).

## AWS Physical AI Toolchain 发布 { #toolchain }

**发布日期: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

在 AWS 上运行从数据采集、合成数据、训练、仿真验证到边缘部署的 Physical AI 开发周期的参考架构、IaC 与部署自动化集合。它将 NVIDIA GR00T（VLA[^vla] 训练）、Isaac Sim、Isaac Lab、Cosmos、OSMO 连接到 S3、EKS、AWS Batch、SageMaker、EC2、IoT Greengrass（Jetson 部署），每个组件对应一个 Terraform 模块，可逐个引入。数据使用 Zarr→LeRobot，边缘使用 ONNX、ROS 2 等开放格式。代码：[aws-samples 仓库](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws)。

**阅读范围**: 官方参考架构。文章自述提供的是"基础设施模式，而非完成的机器人行为"。GR00T 示例使用 27 条 UR3 pick-and-place 演示，用于确认能否运行；"数小时而非数周"是 AWS 方面的说法。需要 GPU 配额（SageMaker 与 EC2）、NGC API 密钥和 Hugging Face 令牌，实验后须执行清理（tear down）以停止计费。

**后续行动**: 先引入一个瓶颈环节 — P1 数据 · P2 训练 · P3 仿真 · P5 编排（Strands 智能体层）· Radar 队列条目 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting 行业应用案例 { #gaussian-splatting }

**发布日期: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

介绍用开源 Splat Toolbox（[AWS Solutions Library 指导方案](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws)）处理 3DGS（由照片和视频生成写实 3D 场景）的五阶段流水线（输入→预处理→重建→训练→后处理），以及在媒体、机器人、建筑、制造、房地产中的应用。使用 Step Functions、Lambda、AWS Batch/ECS 与 EC2 Spot。

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

**阅读范围**: 官方实现指南。报告的评估为 n=5 open-loop[^openloop]，不是实机任务成功率。正文中的代码链接返回 404——代码未合并，仍在[未合并 PR #1174](https://github.com/awslabs/awsome-distributed-ai/pull/1174)中（2026-10-14 确认），先阅读正文。

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

## Edge Impulse 与 AWS — 结合边缘推理与云端智能 { #edge-impulse-aws }

**发布日期: 2026-07-17 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/edge-impulse-and-aws-combining-edge-inference-with-cloud-intelligence-for-physical-ai/) `[4]` · ⏳ 待原文核对 (自动扫描 2026-10-16)**

Edge Impulse（Qualcomm 旗下公司）与 AWS 联合撰写的文章，以仓库设备位置追踪为例介绍混合边缘-云架构。摄像头边缘设备先用 Edge Impulse YOLO Pro 目标检测和 Qwen2-VL 8B 视觉-语言模型做初判，只有确认的检测结果才上传云端，由 Amazon Bedrock AgentCore（Nova Lite）回答"叉车在哪里"之类的自然语言查询。AWS IoT Core 负责设备连接与 MQTT 消息，Greengrass 负责边缘模型部署与管理，S3 存储用于再训练的图像。

**阅读范围**: AWS×Edge Impulse 联合伙伴介绍文章。原文未明确说明代码示例的位置，是公开仓库还是客户团队路径尚需进一步确认。"降低延迟与带宽"描述的是边缘优先设计的优点，不是量化基准测试——需将厂商说法与实测区分开。

**后续行动**: P4 边缘推理部署 · P5 智能体编排（Bedrock AgentCore） — [P4](pillar-4.md) · [P5](pillar-5.md).

## Config：机器人训练数据增强 { #config }

**发布日期: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

利用 S3、Bedrock 描述生成、Cosmos 变换及 HyperPod/EC2，增加已有机器人演示的视觉多样性。

**阅读范围**: 客户联合技术文章。可用于分别评估增强视频质量与实际策略改善。

**后续行动**: P1 数据采集处理 — [P1](pillar-1.md).

## re:Invent 2026 — Physical AI 相关场次 { #reinvent-2026 }

**活动：2026-11-30 至 12-04 · [re:Invent 2026 活动目录](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog) `[3]` · 目录确认日：2026-11-02**

获取目录中全部 2,415 个场次（含重复场），按标题与摘要中的 Physical AI、机器人、世界模型、仿真、数字孪生、模型训练（HyperPod、Trainium）、训练数据、边缘、AgentCore 关键词初筛，再保留与支柱直接相关的 45 个。仅标题含 AgentCore 的场次就超过 60 个，因此以生产运维模式和制造/现场案例为主保留。点击场次代码会打开目录搜索结果。时间为当地时间（PT），同一场次的其他场次标为"重复"。形式：Workshop 120 分钟动手 · Builders' session 60 分钟小组动手 · Chalk talk 60 分钟白板讨论 · Code talk 60 分钟现场编码 · Lightning talk 20 分钟。

**主题演讲与座谈**

| 时间 (PT) | 场次 | 形式 | 关注点 |
|---|---|---|---|
| 12/1(周二) 08:30 | [KEY002](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY002) CEO Keynote | Keynote | AI 基础设施、推理、智能体平台的新发布 —— 用于确认是否有 Physical AI 相关发布 |
| 12/2(周三) 08:30 | [KEY003](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY003) Data & AI Keynote | Keynote | 智能体如何触达数据、衡量价值、设定边界 —— P1 数据与 P5 智能体视角 |
| 12/2(周三) 14:00 | [SUP201](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=SUP201) Training and simulation turn robot capabilities into useful products | Breakout session | NEURA Robotics、1X、Highlanders 座谈 —— 把训练、仿真、数据管线变成产品 |
| 12/3(周四) 08:30 | [KEY005](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY005) Technical Innovations Keynote | Keynote | Graviton、Trainium、网络、存储的内部结构 —— 训练基础设施选型的背景 |
| 12/3(周四) 10:00 | [AIM2215](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2215) World Models & Physical AI: The next frontier in intelligent systems | Breakout session | 世界模型座谈 —— 研究者与客户的生产部署经验与技术难题 |
| 12/3(周四) 13:30 | [AIM2213](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2213) How leading AI builders push the frontier with AWS Trainium | Breakout session | 四家客户使用 Trainium 的座谈，涵盖世界模型与 Physical AI |

**Physical AI 管线 — P1·P2·P3·P5**

| 时间 (PT) | 场次 | 形式 | 关注点 |
|---|---|---|---|
| 11/30(周一) 10:00 | [IND3338-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3338-R) Accelerate Physical AI development with NVIDIA on AWS | Chalk talk | 用 AWS Physical AI Toolchain 走完合成数据→训练→sim-to-real→硬件在环验证全周期 |
| 11/30(周一) 12:00 | [AIM449](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM449) One agent, any robot: building physical AI with Strands Robots | Chalk talk | Strands Robots SDK —— 一个参数切换 MuJoCo 仿真与实机；GR00T、Cosmos 3、LeRobot 策略；IoT 桥接机队 |
| 11/30(周一) 15:00 | [IND389](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND389) Physical AI for MedTech: From Intelligent Devices to Business Impact | Chalk talk | 医疗器械 Physical AI 栈 —— SageMaker 训练、Greengrass 边缘推理、合规 OTA |
| 12/1(周二) 13:30<br>重复 12/1(周二) 15:00 | [IND322-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND322-R) Physical AI in Telecom: A Framework for Workload Placement | Chalk talk | Physical AI 工作负载部署框架 —— Region、Local Zones、Outposts 或基站侧 |
| 12/1(周二) 16:30 | [AIM413](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM413) Build a Physical AI Model Factory on SageMaker HyperPod | Chalk talk | 在 HyperPod EKS 异构 GPU 池上运行合成场景→后训练→评估的数据飞轮 |
| 12/2(周三) 08:30<br>重复 12/3(周四) 14:30 | [CMP407-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP407-R) Orchestrating Physical AI workloads on AWS: Compute and pipeline patterns | Chalk talk | Batch（并行仿真）、EKS+Karpenter（训练）、HyperPod 对比；Capacity Blocks 与 Spot 成本策略 |
| 12/2(周三) 12:30 | [AIM458-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM458-S) The Physical AI Blueprint: A Full-Stack Solution with AWS and NVIDIA (sponsored by NVIDIA) | Workshop | 动手：Isaac Sim 合成数据、GR00T/Cosmos 训练、Omniverse 孪生、Greengrass 部署、AgentCore 多机器人编排 |

**仿真与数字孪生 — P3**

| 时间 (PT) | 场次 | 形式 | 关注点 |
|---|---|---|---|
| 11/30(周一) 13:30 | [CMP408](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP408) The cloud holodeck: Stream NVIDIA Omniverse, scale headless sim on AWS | Chalk talk | 通过 DCV 流式传输 Omniverse/Isaac Sim 工作站 + Batch 无头批量渲染，由 VAMS 管理 |
| 12/1(周二) 15:00 | [IND102-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND102-S) Accelerating with NVIDIA Omniverse: VW’s Battery Manufacturing Digital Twin (sponsored by NVIDIA) | Breakout session | 大众电池工厂 OpenUSD 数字孪生 —— 虚拟调试与合成检测数据 |
| 12/1(周二) 16:00<br>重复 12/2(周三) 09:00 | [IND401-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND401-R) Build, simulate, and validate physical AI-driven robotic systems | Builders' session | 动手：用虚拟 PLC、现场总线、Omniverse 物理仿真构建多机器人单元数字孪生 |
| 12/2(周三) 16:30 | [CON409](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CON409) ML, automotive, and robotics simulations at scale on AWS Batch | Breakout session | 用 Batch 编排汽车/机器人仿真→数据湖→GPU 训练闭环 |
| 12/3(周四) 16:30 | [IND3355](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3355) Building Worlds for Machines: VAMS and 3DGS for Autonomy | Lightning talk | 现场传感器采集→3DGS 重建→可用于仿真的环境（20 分钟闪电演讲） |

**世界模型与机器人学习研究 — P2**

| 时间 (PT) | 场次 | 形式 | 关注点 |
|---|---|---|---|
| 11/30(周一) 13:00<br>重复 12/2(周三) 12:00 | [AIM305-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM305-R) Hands-on training world models and deploying agents for Physical AI | Builders' session | 动手：在 Trainium/Neuron 上微调 Transformer 世界模型（PEFT）并部署智能体 |
| 11/30(周一) 16:00 | [AIM323](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM323) Serving world models on AWS Trainium with native PyTorch | Code talk | 用 torch.compile 与自定义内核在 Trainium 上提供世界模型推理 |
| 11/30(周一) 16:30 | [INV531](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV531) Visual reasoning will be bigger than language reasoning | Chalk talk | 华盛顿大学 Ranjay Krishna —— 用点、轨迹、深度等视觉表示推理的机器人基础模型 |
| 12/1(周二) 11:30<br>重复 12/3(周四) 13:30 | [AIM304-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM304-R) Deploy and optimize world models with agentic AI workflows | Builders' session | 动手：在 Trainium 上部署实时视频世界模型，用 Neuron 智能体技能优化内核 |
| 12/2(周三) 10:30 | [INV527](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV527) World models for indoor robots: what breaks and why | Chalk talk | Diligent Robotics 医院机器人的激光雷达世界模型 —— Transformer 几何推理在哪里失效 |
| 12/2(周三) 13:30 | [INV537](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV537) No torque sensors, no problem: learning safe physical interaction for humanoids | Chalk talk | Fauna Robotics —— 无力矩传感器人形机器人的柔顺控制学习 |

**模型训练与数据基础设施 — P1·P2**

| 时间 (PT) | 场次 | 形式 | 关注点 |
|---|---|---|---|
| 11/30(周一) 08:30 | [AIM406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM406) End-to-end foundation model pipelines on SageMaker HyperPod with EKS | Workshop | 动手：在 HyperPod EKS 上完成数据准备→分布式微调→同集群推理 |
| 11/30(周一) 15:00 | [AIM318](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM318) Resilient VLM Training at Scale on Amazon SageMaker HyperPod | Workshop | 动手：在 VLM 训练中注入节点故障，并通过自动修复与检查点继续训练 |
| 11/30(周一) 15:00 | [AIM433](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM433) Maximize GPU utilization across training and inference on HyperPod | Chalk talk | 把 HyperPod 用作数据处理、训练、推理共享 GPU 池 —— 跨团队调度 |
| 12/1(周二) 12:00<br>重复 12/3(周四) 08:00 | [AIM334-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM334-R) Hands-on distributed training with AWS Trainium and PyTorch | Workshop | 动手：用 TorchTitan 在 Trainium 上分布式训练 —— 并行策略与性能调优 |
| 12/1(周二) 14:30 | [AIM362](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM362) Which customization compute? A decision approach for model fine-tuning | Chalk talk | 微调计算选型 —— 无服务器定制、训练作业或 HyperPod |
| 12/2(周三) 15:00 | [AIM3308](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM3308) What's new: SageMaker HyperPod, with learnings from Multiverse | Breakout session | SageMaker HyperPod 新功能（EKS 与 Slurm）—— 包括世界模型在内的大规模训练与服务 |
| 12/2(周三) 15:30<br>重复 12/3(周四) 08:00 | [AIM434-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM434-R) From raw data to custom model: Dataset prep with Amazon SageMaker AI | Workshop | 动手：通过数据画像、自动标注、人工审核与合成数据准备训练数据 |

**现场运营与边缘 — P4**

| 时间 (PT) | 场次 | 形式 | 关注点 |
|---|---|---|---|
| 11/30(周一) 10:00 | [DVT210-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=DVT210-S) When Telemetry Steers the Robot: Observability for Physical AI (sponsored by groundcover) | Breakout session | Path Robotics 焊接机器人与四足机器人的可观测性案例（赞助场次） |
| 11/30(周一) 15:00<br>重复 12/1(周二) 12:30 | [IND402-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND402-R) Agentic AI for manufacturing: Build a cross-domain digital thread | Workshop | 动手：用 Neptune、AgentCore、IoT SiteWise 打通 OT 与 IT 数据的制造数字主线 |
| 12/1(周二) 12:30<br>重复 12/3(周四) 08:30 | [HMC403-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC403-R) Self-managed agentic AI at the hybrid edge | Workshop | 动手：在 Local Zones 与 Outposts 上运行自管智能体 AI（数据驻留、低延迟） |
| 12/2(周三) 16:30 | [IND378](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND378) How Mercedes-Benz accelerates engineering and production with AI | Breakout session | 梅赛德斯-奔驰 —— AgentCore 工程智能体与云原生 MES、数字孪生 |
| 12/3(周四) 08:30 | [HMC406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC406) How Amazon Robotics runs AWS Outposts across hundreds of fulfillment centers | Code talk | Amazon Robotics 如何在数百个仓储中心运行 Outposts —— 隔离与故障切换 |
| 12/3(周四) 09:00 | [IND384](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND384) Inside T-Mobile's Kinetic Edge: Real-Time Physical AI at Scale | Breakout session | T-Mobile Kinetic Edge —— 用 Outposts、SageMaker、AgentCore 在网络边缘做实时 Physical AI |
| 12/4(周五) 08:30 | [IND345](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND345) Human+AI Collaboration: How Amazon Deploys Autonomous Operations on AWS | Breakout session | Amazon 仓储现场 —— 人形、四足、AMR、无人机混合机队编排架构 |

**AgentCore — P5**

| 时间 (PT) | 场次 | 形式 | 关注点 |
|---|---|---|---|
| 11/30(周一) 08:30<br>重复 12/2(周三) 08:00 | [AIM439-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM439-R) Getting Started with AgentCore: ship an agent to production in 2 hours | Workshop | 2 小时动手：用 AgentCore CLI 逐步加入运行时、记忆、网关、身份、策略、可观测性、评估 |
| 11/30(周一) 10:00<br>重复 12/2(周三) 15:00 | [AIM436-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM436-R) Scale production agents reliably with AgentCore | Chalk talk | 从 10 个到 1 万个会话的扩展模式 —— microVM 隔离、工具调用失败与超时处理 |
| 11/30(周一) 14:00<br>重复 12/3(周四) 08:00 | [TNC331-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=TNC331-R) Ship AI Agents Faster with AgentCore Harness | Lab | 实验：AgentCore Harness —— 用配置声明智能体循环，添加工具与技能，发布版本化端点 |
| 11/30(周一) 14:30 | [AIM370](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM370) Trusting agents in production: end-to-end security with AgentCore | Breakout session | AgentCore 端到端安全 —— microVM 隔离、身份传递、Gateway 策略、Cedar 最小权限 |
| 12/2(周三) 11:30 | [AIM450-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM450-R) Context engineering for production agents on AgentCore | Chalk talk | 上下文工程 —— 系统提示、技能、工具定义与记忆的分配 |
| 12/2(周三) 15:00 | [AIM212](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM212) Best practices for production agents on AgentCore, with Nasdaq | Breakout session | AgentCore 生产最佳实践 + Nasdaq 的多账户隔离与智能体身份运维 |
| 12/3(周四) 14:30 | [AIM452](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM452) Build long-running agents that persist for days on AgentCore | Chalk talk | 持续数天的智能体 —— Runtime 持久执行、Memory、人工审批暂停/恢复 |

**阅读时确认范围**：这些是场次摘要（预告），不是演讲内容本身。日程与会场可能变更，请在活动 App 中再次确认。"35 周→3.5 周"（IND378）、"数周→数小时"（IND401）等数字为演讲方说法。AIM305、AIM304 预告在 Trainium 上训练与服务世界模型的动手内容 —— [P2](pillar-2.md) 中"没有用 Trainium 训练 VLA 的公开案例"的判断，将在场次资料公开并确认可复现后重新评估。

**下一步**：按负责的支柱挑选场次 —— [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P4](pillar-4.md) · [P5](pillar-5.md)。活动结束后，录像与讲义公开时把对应行替换为原文链接，新服务与新功能走 [Radar](radar.md) 流程。

## 持续关注

关注官方 [Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/)及 [RSS](https://aws.amazon.com/blogs/physical-ai/feed/)。共同更新日期、原文、范围、支柱链接。每日自动扫描会先以 `[4]` · ⏳ 待原文核对 标记添加本页缺少的文章，负责人核对原文后改为 `[3]`；技术晋升遵循现有[维护规则](maintenance.md)。

<!-- 용어 각주 -->

[^vla]: **VLA（Vision-Language-Action）** — 将视觉观测和语言指令转换为机器人动作的模型。
[^openloop]: **Open-loop 评估** — 对记录的观测动作计算预测误差，不同于策略与环境交互的任务成功评估。
[^3dgs]: **3D Gaussian Splatting（3DGS）** — 用大量 3D 高斯（椭球形点）拟合多张照片或视频，实时渲染写实场景的 3D 重建技术。用于 real-to-sim，即把真实现场搬进仿真作为背景。
[^wfm]: **世界基础模型（WFM, World Foundation Model）** — 为预测·生成物理世界的下一场景而训练的大型模型。通过文本·视频提示生成物理上合理的视频·场景，用于增强机器人学习数据。🎥 [NVIDIA Cosmos 介绍](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **世界-动作模型（WAM, World Action Model）** — 在一个模型中同时进行未来场景预测与机器人动作生成。与只生成视频的世界模型不同，它输出关节角度、夹爪指令等可执行动作。
