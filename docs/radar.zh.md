---
ko_hash: 94c646a040dbcc708bfece1bbc163ab857c998d4
---
# Radar — 队列 / 观察列表

_最终更新: 2026-07 · owner: Youngjin · volatility: 高_
[← 返回 index](index.md)

> **L0 TL;DR**: 尚未通过纳入标准（[2.5 THE FILTER](maintenance.md#纳入标准-the-filter)）但**值得关注**的东西。每个条目一句话 —— 成熟度标签 + **为何受关注 + 为何待定**。一旦通过门禁（4 项中 2 项），由负责的支柱 owner 用标准模板晋升。
>
> ⚠️ **不要把这里的条目当作"成熟能力"用于客户提案。** 华丽的演示常常掩盖可部署性。

---

## 🔬 模型 / 算法（待验证）

| 条目 | 标签 | 要点 | 晋升条件 |
|---|---|---|---|
| Physical Intelligence **[π0.7](https://www.physicalintelligence.company/)** | 🔵 Research | ✨ **关注**：以 π0/π0.5 领跑 VLA 的 PI 下一代旗舰传闻 —— 一旦发布可能再次刷新行业基准<br>⏳ **待定**：仅二手来源 `[4]`，无 PI 一手确认 | PI 官方发布 + 性能验证 |
| **[GR00T N1.6 / N1.7](https://github.com/NVIDIA/Isaac-GR00T) 商业许可证** | 🟡→ | ✨ **关注**：若允许商用属实，将成为可用于客户提案的罕见开放 VLA（N1.5 为非商业，无法用于提案）<br>⏳ **待定**：允许商用的说法仅来自二手来源 `[4]`（N1.5 在模型卡上明确为非商业 `[1]`） | 在实时模型卡确定许可证 |
| **[World-action models](https://developer.nvidia.com/isaac/gr00t)**（DreamZero → GR00T N2） | 🟡 Preview | ✨ **关注**：被视为 VLA 之后一代的"同时生成动作的世界模型"方向 —— NVIDIA 路线图的方向指标<br>⏳ **待定**：GR00T N2 "计划年底"，DreamZero 为研究 | GA + 实际部署案例 |
| Google DeepMind **[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)**（用于机器人学习的世界模型[^wfm]） | 🟡 Preview | ✨ **关注**：尝试把前沿级世界模型用作机器人策略学习的数据源 —— 若成立可绕过真实数据瓶颈<br>⏳ **待定**：世界模型本身为预览，用于机器人学习为研究 | 机器人策略学习验证案例 |
| **基于 VLM 的 SysID[^sysid]**（[Vid2Sid](https://arxiv.org/abs/2602.19359), [Swim2Real](https://arxiv.org/abs/2603.20827)） | 🔵 Research | ✨ **关注**：仅凭视频估计物理参数、自动完成仿真器校准 —— 有望消除 sim-to-real 的手工校准<br>⏳ **待定**：2026 预印本，单一实验室 | peer-review + 复现 |
| **VIRAL / [VideoMimic](https://www.videomimic.net/) / [Real2Render2Real](https://real2render2real.com/)**（visual sim-to-real[^s2r] at scale） | 🔵 Research | ✨ **关注**：从普通视频重建仿真环境与演示的 visual sim-to-real —— 改变数据采集成本结构的候选<br>⏳ **待定**：CVPR/CoRL 研究，非生产 | 生产部署证据 |
| **Robbyant [LingBot-VLA](https://huggingface.co/robbyant) / [UnifoLM-VLA-0](https://huggingface.co/unitreerobotics)** | 🔵 Research | ✨ **关注**：中国新兴开放 VLA 系列 —— 用于观察开放权重竞争格局<br>⏳ **待定**：二手来源，无验证 | 一手确认 + AWS 映射 |

## 🖥️ 仿真 / 工具（待成熟）

| 条目 | 标签 | 要点 | 晋升条件 |
|---|---|---|---|
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** 物理引擎[^physeng] | ⚪ Hype | ✨ **关注**：以"超高速通用物理引擎"之说引发热议 —— 若属实将改变 GPU 仿真的成本结构<br>⏳ **待定**："430,000 倍"已被反驳 `[1]`，接触操作中慢 | 独立基准 + 生产采用 |
| **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** | 🟡 Alpha | ✨ **关注**：结合 MuJoCo 精度与 GPU 并行 —— Isaac 一家独大格局的替代候选<br>⏳ **待定**：PyPI classifier "3-Alpha" `[1]`，非生产 | Beta/GA 转换 |
| **[NVIDIA Newton](https://github.com/newton-physics/newton)** 物理引擎 | 🟡 Preview | ✨ **关注**：与 Google DeepMind·Disney Research 共同开发的新一代开源物理引擎 —— Isaac 生态下一代标准的有力候选<br>⏳ **待定**：在 Isaac Sim 6.0 中为 experimental 后端 | GA + Isaac Lab 3.0 正式 |
| **[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)** | 🟡 Preview | ✨ **关注**：包含 Newton 集成的新一代架构改造 —— 现行 5.x 栈迁移方向的指标<br>⏳ **待定**："Early Developer Release"，API 变动（最新 GA 为 5.1） | 6.x GA 宣布 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 作为 sim-to-real 学习源** | 🟢 GA（模型）/🔵（实战） | ✨ **关注**：用世界模型生成数据训练可实际部署策略的方向 —— 若成立将改写 SDG 管道格局<br>⏳ **待定**：模型 GA，但"用世界模型数据训练可实际部署策略"仅早期采用者。⚠️ **AWS 未托管** | 强化 AWS 映射 + 学习验证 |

## 🤖 硬件 / 部署（路线图·演示）

| 条目 | 标签 | 要点 | 晋升条件 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | ✨ **关注**：话题度最高的人形机器人量产计划 —— 客户提问频率最高的条目<br>⏳ **待定**：仅 Musk 的主张，生产未启动 | 经过验证的部署 |
| **Hyundai·BD 全电动 [Atlas](https://bostondynamics.com/atlas/)** | ⚪ 路线图 | ✨ **关注**：现代汽车集团的量产路线图（2028 起 3 万台/年）—— 韩国客户触点上最直接的人形机器人赛道<br>⏳ **待定**：全电动 Atlas 产品版本公开（2026-07，BD 官方 `[3]`）。部署 2.5 万+台·产能 3 万/年均 **2028 启动**，当前实际运行 ~0。2026 仅小规模试点（现代 RMAC + Google DeepMind）。⚠️"第五代"为误称 | 实际运行出货启动 |
| **[Apptronik Apollo 2 + Robot Park](https://apptronik.com/)** | 🟡 试点 | ✨ **关注**：Mercedes·GXO 实际运营试点 + Google DeepMind 数据合作 —— 人形机器人商业化最前线的指标<br>⏳ **待定**：Mercedes-Benz·GXO 运营试点 `[3]` + Google DeepMind Gemini Robotics 数据合作（9 万平方英尺）。自主·商用扩散未验证。AWS 映射为通用（数据→S3/SageMaker），合作本身属 Google `[4]` | 商用部署规模 + 自主成果验证 |
| **[1X Neo](https://www.1x.tech/neo)** 自主性 | 🟡 Preview | ✨ **关注**：真正开售（$20k）的首批家用人形机器人 —— 遥操作混合运营模式的试验场<br>⏳ **待定**：自主 + VR 遥操作（Expert Mode）混合运行 — CEO 亲自承认（[Engadget](https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html) `[3]`）。"自主 60~70%" 的数字无一手来源 `[4]` | 真正自主的验证 |
| **[Figure 03](https://www.figure.ai/) "8 小时自主班次"** | ⚪ Hype | ✨ **关注**：在已验证的 BMW 试点业绩之上的自主性主张 —— 若属实将刷新工业人形机器人自主性标准<br>⏳ **待定**：CEO 推文，无独立验证（Figure 02@BMW 为已验证试点） | 第三方自主性审计 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 采用**（Doosan/LG/Samsung） | 🟢 GA（公布） | ✨ **关注**：韩国三大企业集团的采用公告 —— 韩国客户对话中随时被提及的参考案例<br>⏳ **待定**：采用为"公布"而非生产验证 | 公开生产案例 |

## 🔗 智能体 / 连接（早期）

| 条目 | 标签 | 要点 | 晋升条件 |
|---|---|---|---|
| **MCP[^mcp] for robotics**（[ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 等） | 🔵 Research | ✨ **关注**：将智能体标准协议接入机器人技能的实验激增（50+ 服务器）—— AgentCore 联动的切入角度<br>⏳ **待定**：有 50+ 服务器但为开源/演示，无生产（安全·延迟·确定性未验证） | 生产硬化案例 |
| **ROS 2[^ros] + LLM 智能体[^agent]**（NASA JPL [ROSA](https://github.com/nasa-jpl/rosa), [RAI](https://github.com/RobotecAI/rai)） | 🔵 Research | ✨ **关注**：NASA JPL ROSA 等实际组织的验证案例 —— 自然语言→机器人运维最现实的切入口<br>⏳ **待定**：ROSA(JPL) 为最强实例但为 mock-ops。现场部署有限 | 现场生产部署 |
| **智能体物理安全标准**（[RoboGuard](https://arxiv.org/abs/2503.07885) 等） | 🔵 Research | ✨ **关注**：LLM 语义层风险的标准空白地带 —— 可能上升为监管·采购要求<br>⏳ **待定**：ISO 只管物理，缺乏 LLM 语义风险标准 | 标准化进展 |
| **[AgentCore Payments / Agent Registry](https://aws.amazon.com/bedrock/agentcore/)（首尔）** | 🟡 Preview/未提供 | ✨ **关注**：机器人智能体商务·注册基础设施的 AWS 原生方向 —— 首尔区域开放后可立即用于提案<br>⏳ **待定**：首尔区域未提供 —— Agent Registry 在东京 ✅，Payments 连东京也未提供（APAC 仅悉尼）`[1]` | 首尔区域扩展 |

## 🆕 最新扫描流入（2026-08-13 · 一手验证完成 2026-07-21）

<!-- 自动扫描（arXiv/网络）流入项。2026-07-21 完成一手来源验证（4 个验证代理，对照官方发布与 arXiv 原文）—— 晋升 0 项，更正 6 项。在通过 THE FILTER 之前禁止用于客户提案。定期刷新参见 scripts/radar_scan.md。 -->

| 项目 | 标签 | 要点 | 晋升条件 |
|---|---|---|---|
| **[RLWRLD RLDX-1](https://huggingface.co/RLWRLD)**（灵巧手[^dex]优先的基础模型） | 🟡 Preview | ✨ **关注**：韩国初创公司的灵巧手操作专用基础模型 —— 三大仿真基准自报 SOTA 叠加权重实际公开，可直接上手实测<br>⏳ **待定**：权重公开属实，但 ⚠️ 并非开源 —— RLWRLD Model License v1.0（非商业·禁止商业分发）`[3]`，7~9B 变体系列（主力 8.1B）。RoboCasa/LIBERO/SIMPLER[^simbench] SOTA 为自报，无独立复现（[aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws) 在 EC2 上提供 n=5 冒烟[^smoke]实测 —— 并非完整基准复现）。AWS 关联仅限仿真基准测试（非商业许可证明确允许的用途，不可用于商业定位）—— "未发现关联"表述已更新（2026-07）。真实客户部署为 0 | 独立基准复现 + 验证过的部署案例 |
| **[NEURA Robotics × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale) 战略合作** | ⚪ Hype·路线图 | ✨ **关注**：人形机器人厂商明确将 AWS 列为 primary cloud 的罕见官方合作 —— "Physical AI on AWS" 客户对话的直接参考案例候选<br>⏳ **待定**：经 AWS 官方新闻稿确认，2026-04-21 `[1]` —— AWS 为 primary cloud，明确写入 Neuraverse 托管 + NEURA Gym·SageMaker 集成。但履行中心在原文中为"探索部署机会（explore）"阶段 —— 实际部署为 0。NEURA Gym RWTH Aachen 等训练网络扩展公告（2026-07-22）未提及 AWS —— 作为独立线索观察 | 实际 AWS 基础设施使用案例公开 + 履行中心部署验证 |
| **[NVIDIA Cosmos 3 Edge](https://www.nvidia.com/en-us/ai/cosmos/)**（Cosmos 3 系列端侧 4B 世界模型+策略） | 🟡 Preview | ✨ **关注**：在 Jetson Thor 上以 15Hz 端侧运行世界模型+策略 —— 无需云端往返的边缘推理方向的领先案例<br>⏳ **待定**：NVIDIA 官方发布 `[4]`（2026-07-21，HuggingFace/developer 博客）—— 在 Jetson Thor 上端侧推理，实现 15Hz 实时机器人策略控制（自报基准，无独立验证），Cosmos 3 Edge Policy（DROID[^droid]）支持 pick-and-place 微调。与既有的"Cosmos 3 作为 sim-to-real 学习源"条目（🖥️ 部分）不同，本条仅涉及边缘部署方向 —— 与 AMD Ryzen AI Embedded X100（本表）并行观察为竞争方案。目前实际生产机器人部署案例为 0 | 独立基准测试 + 实际生产机器人部署案例 |
| **[Walden Robotics](https://www.waldenrobotics.com/news/walden-robotics-launches-from-stealth)**（Toyota Research Institute 分拆，Large Behavior Models[^lbm] 人形机器人） | 🟡 试点 | ✨ **关注**：曾执掌 TRI 机器人研究的 Russ Tedrake 的分拆公司 + 3 亿美元种子轮 —— LBM 商业化最前线，拥有 Toyota 工厂实际试点<br>⏳ **待定**：公司官方发布（2026-07-15）`[4]` —— 2026-01 从 TRI 分拆（创始人 Russ Tedrake，前 TRI SVP），Toyota·Deviation Capital 联合领投 + NVIDIA·Boeing·Samsung Ventures 等参与的 3 亿美元种子轮（估值 11 亿美元）。人形上半身+轮式移动底座，基于 Diffusion Policy[^diffpol]·Large Behavior Models 的策略，宣称自 2026-02 起在北美 Toyota 工厂实现试点→"量产转换"，无第三方验证 | 第三方审计·独立验证 + 部署规模扩大案例 |
| **[Generalist AI GEN-1](https://generalistai.com/blog/gen-1)**（支持广泛末端执行器[^eef]的 embodied foundation model） | 🟡 Preview | ✨ **关注**：单一模型覆盖约 9,000 种末端执行器 + 50 万小时实测数据预训练 —— 在 embodiment 通用性上宣称前所未有的规模<br>⏳ **待定**：Generalist AI 官方博客发布（2026-07）`[4]` —— 基于约 9,000 种末端执行器（五指手至专用工具）、50 万+小时真实交互数据预训练，宣称自报成功率 99%·速度提升 3 倍（无独立复现）。Generalist AI 已在 [pillar-1](pillar-1.md) 中作为 Cosmos WFM 数据生成使用方被提及，但 GEN-1 模型本身属于独立的新条目 | 独立基准复现 + 实际部署案例 |
| **[Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)**（VLA[^vla] 基础模型，10 万+小时真实世界 UMI[^umi] 轨迹） | 🔵 Research | ✨ **关注**：凭借 10 万+小时真实世界 UMI 轨迹的数据规模在四个基准上自报 SOTA —— 中国大厂正式加入 VLA 竞争的信号<br>⏳ **待定**：小米官方 arXiv 发布（2607.15330，2026-07-16）`[4]` —— 基于 Qwen3-VL 的 MoT（VLM+DiT）架构，在 RoboCasa365（57.4%，此前 SOTA 为 46.6%）等四个基准上自报 SOTA（与 RLDX-1·GR00T N1.6 等对比，无独立复现）。⚠️ **更正（2026-08-10）**：已确认 2026-08-03 在 GitHub 实际发布代码与权重（5B 基础模型 + RoboCasa/RoboCasa365/VLABench 三个任务专用版本）—— **Apache-2.0**（与 RLDX-1 不同，明确允许商用，具备 AWS 映射可能性）。仓库自报的排行榜数据与 arXiv 论文的表述方式不同，需直接对照；独立复现与实际部署仍为零 | 独立基准复现 + 实际部署案例 |
| **[Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**（Google DeepMind，全身控制 VLA） | 🟡 Preview | ✨ **关注**：前沿实验室 VLA 从上半身操作扩展到全身（行走·双手协调）控制 —— 改变竞品栈格局的代际转换信号<br>⏳ **待定**：官方发布（2026-07-30）`[4]` —— 从此前仅上半身控制扩展为全身控制（行走·弯腰·双手协调），同时推出推理模型 Gemini Robotics ER 2 与端侧模型 On-Device 2。在 Apptronik Apollo 2 实机演示（拧灯泡 92% 成功率），自报基准，无独立验证。仅 ER 2 公开预览（AI Studio/Enterprise Agent Platform），VLA·On-Device 2 仅限早期访问合作伙伴。⚠️ [pillar-2](pillar-2.md) 中"Gemini Robotics"竞品栈章节为本次发布前的快照（确认于 2026-07，仅覆盖 ER 1.6/On-Device/1.5）—— 需 pillar owner 更新 | 早期访问结束·GA 公开 + 独立基准验证 |
| **[SiMDex](https://arxiv.org/abs/2608.04196)**（挖掘第一视角人类视频以获取机器人操作数据） | 🔵 Research | ✨ **关注**：以推荐系统式的 recall→rank→re-rank 流程，从约 3200 万条已有第一视角人类视频中挑出与任务相关的片段，复用于 VLA 后训练 —— 无需新采集示范即可绕开真实数据瓶颈<br>⏳ **待定**：arXiv 2608.04196（2026-08-04，东京大学·ByteDance Seed 等）`[4]` —— 采用与具身形态无关、可复用的动作表示，无需改动 VLA 架构，在实物灵巧操作任务上使用不到 5% 的可用样本，自报成功率从 47.7% 提升至 61.1%。未经 peer-review，无独立复现 | peer-review + 独立复现 |
| **[Xiaomi-Robotics-U0](https://arxiv.org/abs/2607.11643)**（统一具身数据合成世界基础模型，38B） | 🔵 Research | ✨ **关注**：将文本生成图像·场景合成·视频生成·"embodied transfer" 统一到单一自回归框架中，直接为机器人学习生成合成数据 —— 自报在 WorldArena 基准 100+ 模型中综合排名第一，并将增强数据应用于真实 π0.5 策略，使 held-out（背景·光照变化）条件下的任务完成率从 36.9% 提升至 63.2%<br>⏳ **待定**：小米官方 arXiv 发布（2607.11643，2026-07-13）`[4]` —— 基准与实机结果均为自报，无独立复现·无 peer-review，权重·代码是否开源尚不明确。与本表既有条目 Xiaomi-Robotics-1（VLA 策略模型）为不同模型·不同事项（本条为数据合成用 WFM） | peer-review + 独立复现 + 确认权重·代码公开 |
| **[ω-0](https://arxiv.org/abs/2608.06375)**（同时控制移动+操作的世界-动作模型） | 🔵 Research | ✨ **关注**：不将移动、姿态调整、平衡与操作分离，由单一模型同时完成（concurrent loco-manipulation）——生成基于 diffusion[^diffpol] 的 whole-body 动作，在真实硬件（Unitree G1）上演示 11 项家庭任务的自主执行，还包含人类动作数据迁移（human-to-humanoid）<br>⏳ **待定**：arXiv 2608.06375（2026-08-06，南洋理工·北大·BAAI 等）`[4]` —— 在自报基准上宣称优于现有模仿学习·VLA·人形机器人·WAM 基线，无独立复现·peer-review。40 小时规模的 ω-HOME 数据集是否公开尚不明确 | peer-review + 独立复现 + 确认数据集·代码公开 |

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

<!-- 용어 각주 -->

[^wfm]: **世界基础模型（WFM, World Foundation Model）** — 为预测·生成物理世界的下一场景而训练的大型模型。通过文本·视频提示生成物理上合理的视频·场景，用于增强机器人学习数据。🎥 [NVIDIA Cosmos 介绍](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **系统辨识（SysID, System Identification）** — 测量真实机器人的物理参数（摩擦·质量·电机响应），把仿真器校准到与实物一致的工作。
[^s2r]: **sim-to-real** — 把在仿真中训练的策略迁移到真实机器人上，或指其方法论。由于仿真与现实的物理·视觉差异（域间差异），直接迁移会导致性能崩溃。🎥 [NVIDIA sim-to-real 机器人展示](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **物理引擎（physics engine）** — 数值计算刚体动力学·接触·摩擦·碰撞的仿真器核心软件。引擎的精度·速度权衡左右着仿真器的选择（Isaac/MuJoCo/Genesis）。
[^mcp]: **MCP（Model Context Protocol）** — 连接智能体与工具·数据源的开放标准协议。常被比作"智能体的 USB-C"，把机器人技能暴露为 MCP 服务器的实验正在增多。
[^ros]: **ROS 2（Robot Operating System 2）** — 机器人软件事实上的标准开源中间件。传感器·控制节点通过话题（topic）通信的分布式架构，是工业·研究机器人栈的公共基础。
[^agent]: **LLM 智能体** — 大语言模型自行制定计划、挑选并调用工具（API·机器人技能）、执行多步任务的软件。与简单问答不同，关键在于它有"行动"。
[^vla]: **VLA (Vision-Language-Action)** — 以相机图像（Vision）与自然语言指令（Language）为输入、直接输出机器人动作（Action）的基础模型。对它说"把杯子拿起来"，它就会生成关节运动。🎥 [NVIDIA Isaac GR00T N1 介绍](https://www.youtube.com/watch?v=m1CH-mgpdYg)
[^dex]: **灵巧性（dexterity）** — 手指级的精细·灵活操作能力。其接触物理远比行走复杂，被视为机器人学习中最难的轴。
[^simbench]: **LIBERO · RoboCasa · SIMPLER** — 无需真机即可比较 VLA/操作策略性能的标准仿真基准套件。仿真分数并不保证真机性能。
[^smoke]: **冒烟测试（smoke test）** — 只确认"基本能跑"的小规模运行，不是完整验证。n=5 这样的样本无法支撑统计意义上的性能主张。
[^droid]: **DROID** — 由 13 家机构用 Franka 机械臂采集的大规模开放真实世界操作数据集，被广泛用作操作策略预训练·微调的材料。
[^lbm]: **Large Behavior Models (LBM)** — LLM 的"机器人行为"版：Toyota Research Institute 用该术语指代用大规模示范数据训练、以单一模型执行多种操作任务的机器人基础模型。
[^diffpol]: **Diffusion Policy** — 用图像生成中的扩散（diffusion）模型来生成机器人动作序列的策略架构。它能稳定学习包含多种有效做法的示范数据，已成为模仿学习的事实标准。
[^eef]: **末端执行器（end-effector）** — 安装在机械臂末端的作业工具（夹爪·多指手·专用工具）。选用哪种末端执行器决定数据·策略的兼容性。
[^umi]: **UMI (Universal Manipulation Interface)** — 无需机器人、由人手持带相机的便携夹爪采集示范数据的方式。可以在不投入机器人的情况下大量获取真实世界数据。
