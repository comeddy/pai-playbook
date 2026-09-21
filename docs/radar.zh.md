---
ko_hash: cb3a2208556aff13b0fc6b017aad6c0af32cec7e
---
# Radar — 队列 / 观察列表

_最终更新: 2026-08 · owner: Youngjin · volatility: 高_
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

## 🆕 最新扫描流入（2026-09-21 · 一手验证完成 2026-07-21）

<!-- 自动扫描（arXiv/网络）流入项。2026-07-21 完成一手来源验证（4 个验证代理，对照官方发布与 arXiv 原文）—— 晋升 0 项，更正 6 项。在通过 THE FILTER 之前禁止用于客户提案。定期刷新参见 scripts/radar_scan.md。 -->

| 项目 | 标签 | 要点 | 晋升条件 |
|---|---|---|---|
| **[NEURA Robotics 4NE1 / Neuraverse × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale)**（德国全栈机器人公司，AWS 战略合作） | ⚪ 路线图 | ✨ **关注**：AWS 成为 Neuraverse 的主要云服务商，把 Gym 训练环境与 SageMaker 集成，NEURA 加入 AWS Partner Network —— 服务名称具体明确的 AWS 合作，是 Radar 中映射最具体的"AWS 自家"物理 AI 案例之一，一条值得关注的欧洲人形机器人赛道<br>⏳ **待定**：AWS·NEURA 官方公布（2026-04-21，press.aboutamazon.com）`[4]` —— 在 Amazon 履约中心的部署仅处于"探讨中"阶段，并非实际部署。因最高 14 亿美元的 C 轮融资（2026-06-10，Amazon·NVIDIA·Tether 等参与，全栈机器人公司史上最大融资）与 IFA 柏林 2026 主题演讲（2026-09-05，4NE1 实机展示）而重新引发关注，无第三方验证。⚠️ 链接为 press.aboutamazon.com 官方发布稿，但本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 公开部署案例（如 Amazon 履约中心）+ 独立性能验证 |
| **[RLWRLD RLDX-1](https://arxiv.org/abs/2605.03269)**（81 亿参数的灵巧操作[^dext]基础模型，AWS Generative AI Accelerator 参与项目） | 🔵 Research | ✨ **关注**：一家 KAIST 背景的首尔初创公司利用 AWS Generative AI Accelerator 算力训练的开源机器人基础模型，被 AWS 官方博客直接报道 —— 专攻五指手精细操作，自报在基准测试上优于 GR00T N1.6·π0.5，是韩国发起的"AWS 自家"合作案例（与 NEURA 同为 Radar 中的官方 AWS 合作案例）<br>⏳ **待定**：RLWRLD 官方发布 + arXiv 技术报告（2026-05，arXiv 2605.03269）`[4]` —— 8 项公开基准的自测数据（如 GR-1 Tabletop 得分 58.7，比 GR00T N1.6 高 10.7 个百分点），无独立复现·同行评审。与 AWS 的关系仍处于 accelerator 参与阶段，实际部署目标为 2030 年与乐天酒店及度假村合作（早期阶段）。⚠️ 链接为 arXiv 原文，但本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 独立基准复现 + 实际部署案例 |
| **[Figure Index → Helix 2.5](https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization)**（基于众包人类视频数据预训练的人形机器人神经网络，在 30 个未见过的家庭中完成零样本验证） | 🟡 Preview | ✨ **关注**：Figure 将同一个基于 Index 预训练的策略部署到 30 个从未采集数据的湾区真实家庭，在无需现场数据采集或微调的情况下完成客厅整理、毛巾折叠、整理床铺三项任务 —— 仅凭 Index 预训练，零样本整体任务成功率就由 9% 提升到 56%（420 次中 237 次成功），首次给出众包数据管道能转化为实际策略性能的量化证据，满足了该流入项此前晋升条件中"公开实测数据"的部分<br>⏳ **待定**：Figure 官方公布（2026-09-17，figure.ai）`[4]` —— 仅为自测数据（9%→56%，30 个家庭，420 次试验），无独立复现或第三方验证。Index 应用自身的报酬发放（1,500 万美元）与质量管控方式同样仍是自报口径。⚠️ 本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 独立复现·第三方基准验证 + 更多家庭与任务场景的扩展实证 |
| **[KIMM KAIROS V0.7](https://www.kimm.re.kr/eng/sub011001/view/id/1565)**（K-Moonshot 国家战略技术课题下的国产 AI 人形机器人） | ⚪ 路线图 | ✨ **关注**：韩国机械研究院（KIMM）作为科技情通部支持的"AI 人形机器人全球顶尖研究团"开发的国策人形机器人 —— 2026-09-07 在"2026 全球机械技术论坛"上公开 V0.7，已能完成国民体操、传统假面舞（탈춤）等动作（4 月的 V0.5 仅能握手·挥手）—— 韩国客户对话中可能被提及的"国策研究机构发"人形机器人赛道（与现代·BD Atlas 角度不同）<br>⏳ **待定**：KIMM 官方公布 `[4]`（二手：多家韩国国内媒体交叉确认——体操·假面舞演示为自报。⚠️ 本次运行环境的出网限制导致未能对 kimm.re.kr 执行人工 curl 200 检查，详见提交说明/issue）—— V1.0 公开目标为 2027-04，据报道 KIMM 需要约 30 亿韩元的额外开发经费。商业化·自主性能尚为 0，仍处演示阶段 | V1.0 公开 + 汽车装配·家用场景实证案例公开 |
| **[Generalist AI GEN-1.5](https://generalistai.com/blog/gen-1.5)**（基于物理交互数据预训练 8 个月以上的具身基础模型；仅凭单次 3~12 秒示范即可立即执行新任务，无需梯度更新或微调的单样本学习） | 🔵 Research | ✨ **关注**：把 3~12 秒示范视频作为"物理提示"插入上下文，无需微调即可立即尝试新任务 —— 有望降低 VLA 对逐任务微调的依赖，多家媒体称其为机器人领域的"GPT-3 时刻"<br>⏳ **待定**：仅有公司官方发布（2026-08-19，generalistai.com）`[4]` —— 10 项任务的自测基准（单样本平均成功率 59%，追加 5 分钟数据+10 步梯度更新后升至 83%），无独立复现·同行评审。⚠️ 本次运行环境的出网限制导致未能对 generalistai.com 执行人工 curl 200 检查（详见提交说明/issue） | 独立基准复现 + 多样任务·硬件验证 |
| **[TANGO](https://arxiv.org/abs/2609.09158)**（直接预测关节空间动作的全身控制型人形机器人导航 VLA） | 🔵 Research | ✨ **关注**：不同于预测 2D 路点，该全身（whole-body）VLA 直接预测 29 自由度的关节空间动作，在障碍物密集的室内环境中根据语言指令自主决定弯身·侧移·跨越障碍 —— 使用自研仿真数据管道（Plan-Edit-Track，6.46 万条轨迹）训练后，在 Unitree G1 上实现零样本 sim-to-real[^s2r] 迁移，是同时触及 VLA 与 sim-to-real 两条主线的学术案例<br>⏳ **待定**：arXiv 预印本（2026-09-08，UC Berkeley·Peking Univ·Tsinghua·HKU·Princeton 联合）`[4]` —— 仅有自测基准（成功率/SPL/碰撞率），无同行评审·独立复现。数据管道·模型·检查点计划开源但尚未发布。⚠️ 本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 同行评审 + 开源后独立复现 |
| **[Skild AI S1](https://skild.ai/blogs/s1)**（仅凭单个人类示范视频、无需微调即可执行最长 10 分钟长时任务的上下文学习机器人基础模型） | 🟡 Preview | ✨ **关注**：Skild AI 以 1 个人类示范视频作为"视觉提示"，无需微调·权重不变即可执行未学习长时任务 —— [NVIDIA 官方博客](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/)（2026-09-10）确认 Skild·NVIDIA·Foxconn 已在 NVIDIA Blackwell 系统组装线（安装busbar和limit block、拧紧16颗螺丝等）实际部署，付费客户超 60 家，首次商业部署仅 10 个月即达成年化经常性收入（ARR）1 亿美元 —— 从"启动向少数合作伙伴部署"的宣告阶段，升级为实际产生产业收入的早期案例<br>⏳ **待定**：NVIDIA·Skild AI 官方公布（2026-09-10）`[4]` —— 营收·客户数为公司自报数据，无第三方审计或独立性能验证（通用任务成功率等细节未公开）。无 AWS 映射·首尔区域关联案例。⚠️ 本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 独立性能·营收审计（第三方）+ 公开 AWS 映射案例 |
| **[Strands Robots](https://strandsagents.com/blog/robots-working-together-model-hardware-standard-strands-robots/)**（AWS 开源智能体框架 Strands Agents 的机器人·物理硬件自然语言控制扩展，具备 Zenoh 网状网络 + AWS IoT Core 机群连接） | 🟡 Preview | ✨ **关注**：AWS 自家的开源智能体框架 Strands Agents 发布了可用自然语言直接控制机器人的扩展 —— 每个 `Robot()`/`Simulation()` 实例都自动成为 Zenoh 网状网络的节点，在本地网络中互相发现·控制，并可通过 AWS IoT Core 连接地理分布的机群，同时仍能原样观测·指挥现有 ROS 2 计算图 —— 是 Radar 🔗 智能体/连接主线（MCP for robotics、AgentCore Payments/Registry）中首个 AWS 自家机器人智能体案例<br>⏳ **待定**：strands-labs/robots 开源仓库（2026-08，v0.5.x）+ strandsagents.com 官方博客 `[4]` —— 尚未作为 GA 服务在 docs.aws.amazon.com 上正式文档化，仍处于社区/开源阶段，同期发布的"Model Hardware Standard"为限量研究预览。⚠️ 本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 官方服务 GA 文档化 + 公开实际机器人机群生产案例 |
| **[WholeBodyWAM](https://arxiv.org/abs/2609.16644)**（将预训练世界-动作模型扩展为基于 whole-body controller 的全身控制人形机器人 loco-manipulation 框架） | 🔵 Research | ✨ **关注**：在保留以操作为中心预训练的世界-动作模型（WAM）知识的同时，为异构的全身控制器（whole-body controller）语义提供接地，泛化到包含行走的全身协同 loco-manipulation —— 仿真综合成功率达 91.9%，是把 Radar 🔬 世界-动作模型主线（DreamZero→GR00T N2）从操作扩展到全身控制的最新学术案例<br>⏳ **待定**：arXiv 预印本（2026-09-17）`[4]` —— 仅有自测仿真基准，无实机验证·同行评审·独立复现。⚠️ 本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 实机（sim-to-real）验证 + 同行评审 + 独立复现 |
| **[OpenAI 确认研发人形机器人](https://sources.news/p/introducing-the-sources-podcast-with)**（Sam Altman 在 Sources 播客中直接确认公司正在研发自家人形机器人） | ⚪ Hype·路线图 | ✨ **关注**：OpenAI CEO 首次直接表态"我们肯定会做人形机器人"—— 暗示将正式扩展到机器人硬件形态，是 OpenAI 首次进入 Radar 的竞争对手人形机器人观察清单（与 Tesla/Figure/1X/Google 并列），也可能是客户对话中话题度最高的项目之一<br>⏳ **待定**：仅有 2026-09-01 Sources 播客节目中的一句表态 `[4]` —— 未披露任何原型机·上市时间表·制造合作伙伴（Forbes 等已确认），同时提及数据中心等"其他形态"，也让人形机器人是否为专门战略仍不明确。⚠️ 本次运行环境的出网限制导致未能执行人工 curl 200 检查（详见提交说明/issue） | 官方公布原型机·制造合作伙伴·上市时间表 |

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
_owner: Youngjin · updated: 2026-08 · volatility: 高（Radar 本质上快速变化 —— 建议月度评审）_

<!-- 용어 각주 -->

[^wfm]: **世界基础模型（WFM, World Foundation Model）** — 为预测·生成物理世界的下一场景而训练的大型模型。通过文本·视频提示生成物理上合理的视频·场景，用于增强机器人学习数据。🎥 [NVIDIA Cosmos 介绍](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **系统辨识（SysID, System Identification）** — 测量真实机器人的物理参数（摩擦·质量·电机响应），把仿真器校准到与实物一致的工作。
[^s2r]: **sim-to-real** — 把在仿真中训练的策略迁移到真实机器人上，或指其方法论。由于仿真与现实的物理·视觉差异（域间差异），直接迁移会导致性能崩溃。🎥 [NVIDIA sim-to-real 机器人展示](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **物理引擎（physics engine）** — 数值计算刚体动力学·接触·摩擦·碰撞的仿真器核心软件。引擎的精度·速度权衡左右着仿真器的选择（Isaac/MuJoCo/Genesis）。
[^mcp]: **MCP（Model Context Protocol）** — 连接智能体与工具·数据源的开放标准协议。常被比作"智能体的 USB-C"，把机器人技能暴露为 MCP 服务器的实验正在增多。
[^ros]: **ROS 2（Robot Operating System 2）** — 机器人软件事实上的标准开源中间件。传感器·控制节点通过话题（topic）通信的分布式架构，是工业·研究机器人栈的公共基础。
[^agent]: **LLM 智能体** — 大语言模型自行制定计划、挑选并调用工具（API·机器人技能）、执行多步任务的软件。与简单问答不同，关键在于它有"行动"。
[^dext]: **灵巧操作（dexterity）** — 机器人手·臂像人手一样精细·灵巧地操纵物体的能力。与简单夹爪的抓取·放置不同，指用五指手转动物体或操作工具等接触密集、复杂的操作。
