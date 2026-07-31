---
ko_hash: 21be7119020c5e687a3ef6fa2dff17a68b67dc3c
---
# Radar — 队列 / 观察列表

_最终更新: 2026-07 · owner: Youngjin · volatility: 高_
[← 返回 index](index.md)

> **L0 TL;DR**: 尚未通过纳入标准（[2.5 THE FILTER](maintenance.md#纳入标准-the-filter)）但**值得关注**的东西。每个条目一句话 —— 成熟度标签 + **为何待定**。一旦通过门禁（4 项中 2 项），由负责的支柱 owner 用标准模板晋升。
>
> ⚠️ **不要把这里的条目当作"成熟能力"用于客户提案。** 华丽的演示常常掩盖可部署性。

---

## 🔬 模型 / 算法（待验证）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| Physical Intelligence **[π0.7](https://www.physicalintelligence.company/)** | 🔵 Research | 仅二手来源 `[4]`，无 PI 一手确认 | PI 官方发布 + 性能验证 |
| **[GR00T N1.6 / N1.7](https://github.com/NVIDIA/Isaac-GR00T) 商业许可证** | 🟡→ | 允许商用的说法仅来自二手来源 `[4]`（N1.5 在模型卡上明确为非商业 `[1]`） | 在实时模型卡确定许可证 |
| **[World-action models](https://developer.nvidia.com/isaac/gr00t)**（DreamZero → GR00T N2） | 🟡 Preview | GR00T N2 "计划年底"，DreamZero 为研究 | GA + 实际部署案例 |
| Google DeepMind **[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)**（用于机器人学习的世界模型） | 🟡 Preview | 世界模型本身为预览，用于机器人学习为研究 | 机器人策略学习验证案例 |
| **基于 VLM 的 SysID**（[Vid2Sid](https://arxiv.org/abs/2602.19359), [Swim2Real](https://arxiv.org/abs/2603.20827)） | 🔵 Research | 2026 预印本，单一实验室 | peer-review + 复现 |
| **VIRAL / [VideoMimic](https://www.videomimic.net/) / [Real2Render2Real](https://real2render2real.com/)**（visual sim-to-real at scale） | 🔵 Research | CVPR/CoRL 研究，非生产 | 生产部署证据 |
| **Robbyant [LingBot-VLA](https://huggingface.co/robbyant) / [UnifoLM-VLA-0](https://huggingface.co/unitreerobotics)** | 🔵 Research | 二手来源，无验证 | 一手确认 + AWS 映射 |

## 🖥️ 仿真 / 工具（待成熟）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** 物理引擎 | ⚪ Hype | "430,000 倍"已被反驳 `[1]`，接触操作中慢 | 独立基准 + 生产采用 |
| **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** | 🟡 Alpha | PyPI classifier "3-Alpha" `[1]`，非生产 | Beta/GA 转换 |
| **[NVIDIA Newton](https://github.com/newton-physics/newton)** 物理引擎 | 🟡 Preview | 在 Isaac Sim 6.0 中为 experimental 后端 | GA + Isaac Lab 3.0 正式 |
| **[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)** | 🟡 Preview | "Early Developer Release"，API 变动（最新 GA 为 5.1） | 6.x GA 宣布 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 作为 sim-to-real 学习源** | 🟢 GA（模型）/🔵（实战） | 模型 GA，但"用世界模型数据训练可实际部署策略"仅早期采用者。⚠️ **AWS 未托管** | 强化 AWS 映射 + 学习验证 |

## 🤖 硬件 / 部署（路线图·演示）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | 仅 Musk 的主张，生产未启动 | 经过验证的部署 |
| **Hyundai·BD 全电动 [Atlas](https://bostondynamics.com/atlas/)** | ⚪ 路线图 | 全电动 Atlas 产品版本公开（2026-07，BD 官方 `[3]`）。部署 2.5 万+台·产能 3 万/年均 **2028 启动**，当前实际运行 ~0。2026 仅小规模试点（现代 RMAC + Google DeepMind）。⚠️"第五代"为误称 | 实际运行出货启动 |
| **[Apptronik Apollo 2 + Robot Park](https://apptronik.com/)** | 🟡 试点 | Mercedes-Benz·GXO 运营试点 `[3]` + Google DeepMind Gemini Robotics 数据合作（9 万平方英尺）。自主·商用扩散未验证。AWS 映射为通用（数据→S3/SageMaker），合作本身属 Google `[4]` | 商用部署规模 + 自主成果验证 |
| **[1X Neo](https://www.1x.tech/neo)** 自主性 | 🟡 Preview | 已发布产品但自主 ~60~70%，其余为 VR 远程操作 | 真正自主的验证 |
| **[Figure 03](https://www.figure.ai/) "8 小时自主班次"** | ⚪ Hype | CEO 推文，无独立验证（Figure 02@BMW 为已验证试点） | 第三方自主性审计 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 采用**（Doosan/LG/Samsung） | 🟢 GA（公布） | 采用为"公布"而非生产验证 | 公开生产案例 |

## 🔗 智能体 / 连接（早期）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| **MCP for robotics**（[ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 等） | 🔵 Research | 有 50+ 服务器但为开源/演示，无生产（安全·延迟·确定性未验证） | 生产硬化案例 |
| **ROS 2 + LLM 智能体**（NASA JPL [ROSA](https://github.com/nasa-jpl/rosa), [RAI](https://github.com/RobotecAI/rai)） | 🔵 Research | ROSA(JPL) 为最强实例但为 mock-ops。现场部署有限 | 现场生产部署 |
| **智能体物理安全标准**（[RoboGuard](https://arxiv.org/abs/2503.07885) 等） | 🔵 Research | ISO 只管物理，缺乏 LLM 语义风险标准 | 标准化进展 |
| **[AgentCore Payments / Agent Registry](https://aws.amazon.com/bedrock/agentcore/)（首尔）** | 🟡 Preview/未提供 | 首尔区域未提供（东京 Agent Registry ✅） | 首尔区域扩展 |

## 🆕 最新扫描流入（2026-07-31 · 一手验证完成 2026-07-21）

<!-- 自动扫描（arXiv/网络）流入项。2026-07-21 完成一手来源验证（4 个验证代理，对照官方发布与 arXiv 原文）—— 晋升 0 项，更正 6 项。在通过 THE FILTER 之前禁止用于客户提案。定期刷新参见 scripts/radar_scan.md。 -->

| 项目 | 标签 | 为何等待 | 晋升条件 |
|---|---|---|---|
| **[RLWRLD RLDX-1](https://huggingface.co/RLWRLD)**（灵巧手优先的基础模型） | 🟡 Preview | 权重公开属实，但 ⚠️ 并非开源 —— RLWRLD Model License v1.0（非商业·禁止商业分发）`[3]`，7~9B 变体系列（主力 8.1B）。RoboCasa/LIBERO/SIMPLER SOTA 为自报，无独立复现（[aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws) 在 EC2 上提供 n=5 冒烟实测 —— 并非完整基准复现）。AWS 关联仅限仿真基准测试（非商业许可证明确允许的用途，不可用于商业定位）—— "未发现关联"表述已更新（2026-07）。真实客户部署为 0 | 独立基准复现 + 验证过的部署案例 |
| **[NEURA Robotics × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale) 战略合作** | ⚪ Hype·路线图 | 经 AWS 官方新闻稿确认，2026-04-21 `[1]` —— AWS 为 primary cloud，明确写入 Neuraverse 托管 + NEURA Gym·SageMaker 集成。但履行中心在原文中为"探索部署机会（explore）"阶段 —— 实际部署为 0。NEURA Gym RWTH Aachen 等训练网络扩展公告（2026-07-22）未提及 AWS —— 作为独立线索观察 | 实际 AWS 基础设施使用案例公开 + 履行中心部署验证 |
| **[Actuator Reality Shaping](https://arxiv.org/abs/2607.02205)**（zero-shot sim-to-real） | 🔵 Research | 确认实存（arXiv 2607.02205，2026-07-02）`[1]` —— 在 4 种实物硬件（含人形行走）上验证，摘要与原文一致（无需更正）。未经 peer-review | peer-review + 独立复现 |
| **[AgiBot World 2026](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)**（开源真实世界机器人操作数据集，分 5 阶段陆续公开） | 🔵 Research | AgiBot 官方发布（HuggingFace `agibot-world/AgiBotWorld2026`，2026-07）`[4]` —— 在 AgiBot G2 平台上采集的 100% 真实世界数据，将分阶段公开 5 个研究方向（模仿学习等），第一批为商业·服务场景数百小时。许可证及商业使用条款未确认，尚无独立基准或训练验证案例 | 确认许可证 + 独立训练验证（SOTA 复现）案例 |
| **[AXIS](https://arxiv.org/abs/2607.21588)**（社区驱动的可增长机器人操作数据引擎） | 🔵 Research | 确认实存（arXiv 2607.21588，2026-07-23）`[4]` —— 8 所大学 + Axis Robotics 共同研发，通过浏览器端 MuJoCo-WASM 遥操作众包后在 IsaacSim 中增强。仅限 Franka 机械臂仿真（207 项任务·5 万+条轨迹），报告称 π0.5 持续预训练使 LIBERO-Plus 提升 +4.9pp（自报基准，无独立复现）。作者自己将 sim-to-real 列为未来工作 —— 未在真实硬件上验证 | peer-review + 真实硬件 sim-to-real 验证 |
| **[AMD Ryzen AI Embedded X100 + Kria AI SoM](https://www.amd.com/en/products/embedded.html)**（机器人边缘计算，对标 NVIDIA Jetson Thor） | ⚪ Hype·路线图 | AMD 官方发布 `[4]`（2026-07-24）—— Zen 5 CPU·RDNA 3.5 iGPU·XDNA 2 NPU 统一内存（最高 128GB），宣称 FP32 性能为 Jetson Thor 的 3 倍、多线程性能为 Intel 的 2.1 倍（自报基准，无独立验证）。SOM 量产计划于 2026 年 Q4（Arbor/Congatec 等），目前机器人边缘部署案例为 0 | 独立基准测试 + 实际机器人边缘部署案例 |
| **[NVIDIA Cosmos 3 Edge](https://www.nvidia.com/en-us/ai/cosmos/)**（Cosmos 3 系列端侧 4B 世界模型+策略） | 🟡 Preview | NVIDIA 官方发布 `[4]`（2026-07-21，HuggingFace/developer 博客）—— 在 Jetson Thor 上端侧推理，实现 15Hz 实时机器人策略控制（自报基准，无独立验证），Cosmos 3 Edge Policy（DROID）支持 pick-and-place 微调。与既有的"Cosmos 3 作为 sim-to-real 学习源"条目（🖥️ 部分）不同，本条仅涉及边缘部署方向 —— 与 AMD Ryzen AI Embedded X100（本表）并行观察为竞争方案。目前实际生产机器人部署案例为 0 | 独立基准测试 + 实际生产机器人部署案例 |
| **[Walden Robotics](https://www.waldenrobotics.com/news/walden-robotics-launches-from-stealth)**（Toyota Research Institute 分拆，Large Behavior Models 人形机器人） | 🟡 试点 | 公司官方发布（2026-07-15）`[4]` —— 2026-01 从 TRI 分拆（创始人 Russ Tedrake，前 TRI SVP），Toyota·Deviation Capital 联合领投 + NVIDIA·Boeing·Samsung Ventures 等参与的 3 亿美元种子轮（估值 11 亿美元）。人形上半身+轮式移动底座，基于 Diffusion Policy·Large Behavior Models 的策略，宣称自 2026-02 起在北美 Toyota 工厂实现试点→"量产转换"，无第三方验证 | 第三方审计·独立验证 + 部署规模扩大案例 |
| **[Generalist AI GEN-1](https://generalistai.com/blog/gen-1)**（支持广泛末端执行器的 embodied foundation model） | 🟡 Preview | Generalist AI 官方博客发布（2026-07）`[4]` —— 基于约 9,000 种末端执行器（五指手至专用工具）、50 万+小时真实交互数据预训练，宣称自报成功率 99%·速度提升 3 倍（无独立复现）。Generalist AI 已在 [pillar-1](pillar-1.md) 中作为 Cosmos WFM 数据生成使用方被提及，但 GEN-1 模型本身属于独立的新条目 | 独立基准复现 + 实际部署案例 |
| **[Generative Bionics GENE.01](https://gbionics.ai)**（全身多模态智能皮肤人形机器人） | 🟡 Preview | 意大利初创公司官方发布（2026-07-20）`[4]` —— 全身智能皮肤可感知触觉·接近·力·温度，配合"physics-native AI"（自称基于经同行评审的 Nature Machine Intelligence 研究），宣称是首个在主要 Physical AI 软件生态系统中发布开源数字孪生的人形机器人。仅发布了与 Fincantieri 造船厂的合作，尚无实际运行或独立验证 | 公开实际运行案例 + 独立验证（传感器性能·安全性） |

## ⚰️ 已废弃 — 禁止提议（存档保留）

| 条目 | 状态 | 替代 |
|---|---|---|
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 终止 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 终止 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 终止 (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 无公开案例 `[4]` | 当前为 CUDA/NVIDIA（提议时明示风险） |

> ⚠️ **传闻警戒（并非事实）**: "AWS IoT TwinMaker 废弃"是**误信息** —— TwinMaker 是 GA·对新客户开放（低速度）。是与 SiteWise 维护混淆的第三方博客主张。禁止重复。→ [pillar-3](pillar-3.md)。

---

## 晋升流程（摘要）

1. **捕获**: 用指定频道/表情收集候选
2. **过滤**: 应用 [2.5 门禁](maintenance.md#纳入标准-the-filter)（4 项中 2 项以上）
3. **通过时**: 由负责的支柱 owner 用[标准模板](maintenance.md#标准模板)编入，并从 Radar 移除
4. **未达时**: 在此保留一句话，明示晋升条件

完整管道 → [maintenance](maintenance.md#playbook-晋升管道)。

---
_owner: Youngjin · updated: 2026-07 · volatility: 高（Radar 本质上快速变化 —— 建议月度评审）_
