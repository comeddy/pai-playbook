---
ko_hash: b883f09cce87a233271097a1c5160900d47f325f
---
# Physical AI Playbook 介绍

_最终更新: 2026-07 · owner: Youngjin · 状态: 初期构建中_

> **L0 TL;DR**: 当客户抛出 Physical AI 问题时，无需翻查 Slack，**仅凭这一份 playbook 就能在 5 分钟内**给出架构方向、AWS 映射与后续行动的参考资产。它既不是论文摘要集，也不是新闻归档。

<!-- 임시 숨김(2026-08-07): 비공식 자료 박스 — 복원하려면 주석 해제
!!! info "非官方资料（Unofficial）"
    本站是个人维护的参考资产，**并非 AWS（Amazon Web Services）的官方文档或官方立场。** 本站中的服务规格、价格、区域支持，请务必在 [AWS 官方文档](https://docs.aws.amazon.com/)中再次确认。
-->


---

## 如何阅读本文档（30 秒）

1. **赶时间**：直接跳到下方 [常见问题 Top 20](#常见问题-top-20) 中对应的条目。
2. **主题明确后**：进入 5 个支柱之一。每个条目按 **L0（1~2 句）→ L1（1 页）→ L2（deep-dive 链接）** 分层——只读顶部即可确定方向。
3. **面临岔路口**：[决策树](decisions.md) —— Cloud vs Edge、NVIDIA vs 开源、GPU 获取、Build vs Buy。
4. **"这个为什么没有？"**：先查看 [Radar](radar.md)。因未达纳入标准而待定的条目在那里。新候选的上报走 [维护指南](maintenance.md) 的晋升管道。

### 如何阅读标签

| 成熟度 | 含义 |
|---|---|
| 🟢 GA | 正式发布，可用于生产环境 |
| 🟡 Preview | 公开预览 / 有明确的 GA 路线图 |
| 🔵 Research-only | 论文·研究阶段，禁止用于客户提案 |
| ⚪ Hype | 仅有演示。"令人印象深刻的演示" ≠ "可部署" |

| 来源等级 | 含义 |
|---|---|
| [1] | 官方文档 / 论文 |
| [2] | AWS 内部验证（我们亲自跑过） |
| [3] | 厂商官方博客 |
| [4] | 未经验证（Slack/传闻）—— 引用时务必再次确认 |

---

## 5 个支柱

| # | 支柱 | L0 一句话 | 前往 |
|---|---|---|---|
| 1 | **数据采集 & 处理** | 机器人学习的瓶颈不是模型而是数据 —— 如何用 AWS 管道处理遥操作[^teleop]、开放数据集与合成数据 | [pillar-1](pillar-1.md) |
| 2 | **模型训练 (VLA)** | 如何从 GPU 规模、以及是微调[^ft]还是预训练[^pretrain]入手，来设计 VLA[^vla]/机器人基础模型的训练 | [pillar-2](pillar-2.md) |
| 3 | **仿真** | Isaac Sim/Lab vs 开源的选择，以及在 AWS 上运行大规模并行仿真的模式 | [pillar-3](pillar-3.md) |
| 4 | **Sim-to-Real** | 将仿真中训练的策略迁移到真实机体的经过验证的方法论，以及边缘推理的部署路径 | [pillar-4](pillar-4.md) |
| 5 | **智能体编排** | LLM 规划器（System 2[^sys]）指挥机器人控制器（System 1）与机群[^fleet]的层 —— 以 Bedrock AgentCore 为中心 | [pillar-5](pillar-5.md) |

> 各支柱之间权重均等。每个支柱内部按 **客户实际需求 × production-readiness** 排序，顶部有"本支柱中客户最常问的问题 Top 3"。

---

## 常见问题 Top 20

<!-- 1~10: 初期种子（master prompt 示例 + IA 结构）。11~20: 公开社区/博客深入调研（2026-07）。⚠️ 两者都不是 SA 实际咨询日志；获取 Slack 咨询记录后按频率重新排序。 -->

| # | 问题 | 前往何处 | 来源 |
|---|---|---|---|
| 1 | "Isaac Sim / Isaac Lab 在 AWS 上怎么跑？" | [pillar-3](pillar-3.md) | 种子 ⚠️ |
| 2 | "VLA 模型训练（微调）的基础设施该怎么搭？" | [pillar-2](pillar-2.md) | 种子 ⚠️ |
| 3 | "GPU 拿不到 —— On-Demand、Capacity Blocks、替代方案中该用哪个？" | [decisions](decisions.md) | 种子 ⚠️ |
| 4 | "sim-to-real[^s2r] gap 实际上怎么克服？有经过验证的方法吗？" | [pillar-4](pillar-4.md) | 种子 ⚠️ |
| 5 | "机器人实时控制（30–100Hz），推理能放到云上吗？" | [decisions](decisions.md) | 种子 ⚠️ |
| 6 | "基础模型（GR00T/π0 等）是微调好，还是自行训练好？" | [decisions](decisions.md) | 种子 ⚠️ |
| 7 | "机器人学习数据怎么采集、该存到哪里？（遥操作/合成数据）" | [pillar-1](pillar-1.md) | 种子 ⚠️ |
| 8 | "对 NVIDIA 全栈的依赖有多深？开源替代方案呢？" | [decisions](decisions.md) | 种子 ⚠️ |
| 9 | "边缘部署（Jetson 等）与 AWS 怎么连接？" | [pillar-4](pillar-4.md) | 种子 ⚠️ |
| 10 | "用 LLM 智能体[^agent]指挥机器人/设备的架构实际可行吗？" | [pillar-5](pillar-5.md) | 种子 ⚠️ |
| 11 | "全部跑下来 GPU 要多少钱？预算怎么估？" | [decisions](decisions.md) | [AWS Embodied AI 博客](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "如何把既有 ROS 2[^ros] 栈·rosbag[^rosbag] 数据接入 AWS？" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac 博客](https://aws.amazon.com/blogs/robotics/) |
| 13 | "如何跨多节点扩展训练？AWS Batch vs SageMaker HyperPod？" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "实机部署前如何验证·基准测试策略是否真的有效？" | [pillar-4](pillar-4.md) | [NVIDIA 策略评估](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "机器人/工厂数据敏感 —— 云端训练合规吗？本地/混合呢？" | [decisions](decisions.md) | [AWS AI 主权](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "训练好的策略如何做版本管理·复现·检查点恢复？" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Isaac Sim·开源模型能用于商用产品吗？何时需要 NVIDIA AI Enterprise？" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "如何为实时（低延迟）优化策略推理？TensorRT·量化[^quant]·action chunking[^chunk]？" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "如何构建设备/工厂数字孪生[^dtwin]并与机器人仿真连接？TwinMaker·Omniverse？" | [pillar-3](pillar-3.md) | [AWS Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "没有 ML 专家 —— 从哪里开始？如何设计最小 PoC？" | [decisions](decisions.md) | [AWS Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/) |

---

## 页面列表

- [guide — 本手册的构建与维护方式（完整验证管道）](guide.md)
- [高管简报 — 面向高管的 5 分钟判断框架（现在/即将/尚未 矩阵）](exec.md)
- [高管对话指南 — SA 的高管会议准备（电梯演讲·Top 10 问答·禁用表述）](exec-guide.md)
- [pillar-1 — 数据采集 & 处理](pillar-1.md)
- [pillar-2 — 模型训练 (VLA)](pillar-2.md)
- [pillar-3 — 仿真](pillar-3.md)
- [pillar-4 — Sim-to-Real](pillar-4.md)
- [pillar-5 — 智能体编排](pillar-5.md)
- [decisions — 横向决策树](decisions.md)
- [radar — 队列/观察列表](radar.md)
- [maintenance — 所有权 · 更新规则 · 晋升管道](maintenance.md)

---

## 本 playbook 不涵盖的内容

- **未达纳入标准的条目**: ⓐ production 验证 ⓑ 可映射到 AWS ⓒ 实际咨询记录 ⓓ GA（路线图）—— 其中**不足 2 项**则不入正文。仅在 [Radar](radar.md) 中以一句话存在。
- **新闻快讯**: "刚出来"不是纳入的理由。
- **止于概念说明的条目**: 每个条目都以"➡️ 后续行动"结尾。没有行动就是未完成。

---

_owner: Youngjin · updated: 2026-07 · volatility: 低（结构性页面 —— 仅 FAQ Top 20 排名按季度复核）_

<!-- 용어 각주 -->

[^teleop]: **遥操作（teleoperation）** — 由人通过 VR 控制器·主导臂等远程操控机器人并记录示范动作的数据采集方式。质量最高，但人的时间会直接变成成本。🎥 [Stanford Mobile ALOHA 遥操作演示](https://www.youtube.com/watch?v=mnLVbwxSdNM)
[^vla]: **VLA (Vision-Language-Action)** — 以相机图像（Vision）与自然语言指令（Language）为输入、直接输出机器人动作（Action）的基础模型。对它说"把杯子拿起来"，它就会生成关节运动。🎥 [NVIDIA Isaac GR00T N1 介绍](https://www.youtube.com/watch?v=m1CH-mgpdYg)
[^ft]: **微调（fine-tuning）** — 用自己任务·机器人的少量数据，对经过大规模数据预训练的模型进行追加训练。相比从零训练，数据·GPU 可节省数十~数百倍。
[^pretrain]: **预训练（pre-training）** — 用大规模通用数据从零开始训练模型、建立基础能力的阶段。之后再用少量数据微调来适配特定任务。前沿 VLA 预训练是极少数组织的领域。
[^sys]: **System 2 / System 1** — 把认知科学中"慢思考 / 快反应"的区分应用到机器人架构的结构。System 2 由慢速大模型负责规划（5~10Hz），System 1 由小型策略负责实时控制（50~200Hz）。它是决定推理放云上还是边缘的标准。
[^fleet]: **机群（fleet）协调** — 把大量机器人作为一个系统进行调度·路径分配。像仓库机器人那样在数百~数千台规模上已经过生产验证的领域。
[^s2r]: **sim-to-real** — 把在仿真中训练的策略迁移到真实机器人上，或指其方法论。由于仿真与现实的物理·视觉差异（域间差异），直接迁移会导致性能崩溃。🎥 [NVIDIA sim-to-real 机器人展示](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM 智能体** — 大语言模型自行制定计划、挑选并调用工具（API·机器人技能）、执行多步任务的软件。与简单问答不同，关键在于它有"行动"。
[^ros]: **ROS 2（Robot Operating System 2）** — 机器人软件事实上的标准开源中间件。传感器·控制节点通过话题（topic）通信的分布式架构，是工业·研究机器人栈的公共基础。
[^rosbag]: **ROS bag（rosbag2）** — 机器人操作系统 ROS 2 将话题（传感器·命令流）整体录制的标准日志格式。它是机器人公司原始数据的事实默认形态，但无法直接用于训练，需要转换。
[^quant]: **量化（quantization）** — 将模型权重·运算转换为 FP16→INT8/FP4 等更低精度、从而减少内存与计算量的轻量化技术。它是在边缘设备上满足延迟预算的关键手段，需要管理与精度损失之间的权衡。
[^chunk]: **action chunking** — 不是每步只预测 1 个动作，而是一次预测未来多步动作（块）的技术。减少推理次数，更容易满足实时控制频率。
[^dtwin]: **数字孪生（digital twin）** — 对真实工厂·仓库·机器人进行物理上忠实复刻的虚拟副本。无需触碰真实环境即可进行策略训练·验证·场景实验。
