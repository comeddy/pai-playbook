---
ko_hash: 88810e6a4d48cdc1304577555aa665bc9fd2690b
---
# Physical AI Playbook

_最后更新: 2026-09 · owner: Youngjin · volatility: 中_

**L0 TL;DR**: 判断客户机器人业务所需技术，并在 AWS 上从实验、评估走向运营。先确认业务适配、总成本及执行条件。

!!! info "非官方参考资料"
    个人维护资料，不是 AWS 官方文档或立场。技术、许可证、价格及区域须检查所链接的一手来源和日期。样本代码及服务 GA 不保证客户现场结果。

## 按角色开始

| 我是… | 路径 | 产出 |
|---|---|---|
| 客户决策者 | [开始/ROI](start.md) → [高管简报](exec.md) | 业务、替代、预算、试点批准条件 |
| 客户工程师 | [执行](execution.md) → 对应支柱 → [运营](operations.md) | 结果、费用、部署恢复证据 |
| AWS 员工 | [对话指南](exec-guide.md) → [决策](decisions.md) | 需求、适配、伙伴交接 |

## 技术参考 — 五个支柱

| 支柱 | 内容 |
|---|---|
| [P1 数据](pillar-1.md) | 采集、权利、格式、质量、训练管道 |
| [P2 训练](pillar-2.md) | 选型、许可证、资源估算、评估 |
| [P3 仿真](pillar-3.md) | 环境、工具、并行运行、费用 |
| [P4 Sim-to-Real](pillar-4.md) | 实机迁移、边缘部署、验证、安全 |
| [P5 编排](pillar-5.md) | 业务规划、技能、权限、机群连接 |

## 标签及验证范围

GA/Preview/Research 是**发布状态**。原文对照、复现、现场验证、用途、支持方需分别检查。`[1]` 官方文档论文、`[2]` 记录复现、`[3]` 厂商发布、`[4]` 未验证是来源类型，不代表 AWS 批准。见[证据](evidence.md)及[维护](maintenance.md)。

以下问题为探索示例，不是实测咨询频率排名。可从问题开始，提案前确认[试点卡](start.md#pilot)条件。

## 常见问题 Top 20

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
| 11 | "全部跑下来 GPU 要多少钱？预算怎么估？" | [start](start.md) | [AWS Embodied AI 博客](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "如何把既有 ROS 2[^ros] 栈·rosbag[^rosbag] 数据接入 AWS？" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac 博客](https://aws.amazon.com/blogs/robotics/) |
| 13 | "如何跨多节点扩展训练？AWS Batch vs SageMaker HyperPod？" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "实机部署前如何验证·基准测试策略是否真的有效？" | [pillar-4](pillar-4.md) | [NVIDIA 策略评估](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "机器人/工厂数据敏感 —— 云端训练合规吗？本地/混合呢？" | [decisions](decisions.md) | [AWS AI 主权](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "训练好的策略如何做版本管理·复现·检查点恢复？" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Isaac Sim·开源模型能用于商用产品吗？何时需要 NVIDIA AI Enterprise？" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "如何为实时（低延迟）优化策略推理？TensorRT·量化[^quant]·action chunking[^chunk]？" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "如何构建设备/工厂数字孪生[^dtwin]并与机器人仿真连接？TwinMaker·Omniverse？" | [pillar-3](pillar-3.md) | [AWS Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "没有 ML 专家 —— 从哪里开始？如何设计最小 PoC？" | [start](start.md) | [AWS Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/) |

---

## 页面列表

- [开始与 ROI](start.md)
- [执行路径](execution.md)
- [运营恢复](operations.md)
- [使用指南](guide.md)
- [新消息 — 近期官方文章与支柱链接](news.md)
- [工作坊与资料 — 公开工作坊、指南、样本](workshops.md)
- [高管简报](exec.md)
- [AWS 员工对话指南](exec-guide.md)
- [P1 数据](pillar-1.md)
- [P2 训练](pillar-2.md)
- [P3 仿真](pillar-3.md)
- [P4 Sim-to-Real](pillar-4.md)
- [P5 编排](pillar-5.md)
- [决策](decisions.md)
- [Radar](radar.md)
- [证据记录](evidence.md)
- [维护](maintenance.md)
- [设置 · MCP 连接](mcp.md)

_owner: Youngjin · updated: 2026-09 · volatility: 中_

<!-- 용어 각주 -->

[^s2r]: **sim-to-real** — 把在仿真中训练的策略迁移到真实机器人上，或指其方法论。由于仿真与现实的物理·视觉差异（域间差异），直接迁移会导致性能崩溃。🎥 [NVIDIA sim-to-real 机器人展示](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM 智能体** — 大语言模型自行制定计划、挑选并调用工具（API·机器人技能）、执行多步任务的软件。与简单问答不同，关键在于它有"行动"。
[^ros]: **ROS 2（Robot Operating System 2）** — 机器人软件事实上的标准开源中间件。传感器·控制节点通过话题（topic）通信的分布式架构，是工业·研究机器人栈的公共基础。
[^rosbag]: **ROS bag（rosbag2）** — 机器人操作系统 ROS 2 将话题（传感器·命令流）整体录制的标准日志格式。它是机器人公司原始数据的事实默认形态，但无法直接用于训练，需要转换。
[^quant]: **量化（quantization）** — 将模型权重·运算转换为 FP16→INT8/FP4 等更低精度、从而减少内存与计算量的轻量化技术。它是在边缘设备上满足延迟预算的关键手段，需要管理与精度损失之间的权衡。
[^chunk]: **Action chunking** — 一次推理生成多个未来动作。执行频率不同于新观测响应频率，需逐模型验证执行区间、切换及延迟。
[^dtwin]: **数字孪生（digital twin）** — 对真实工厂·仓库·机器人进行物理上忠实复刻的虚拟副本。无需触碰真实环境即可进行策略训练·验证·场景实验。
