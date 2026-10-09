---
ko_hash: 65b0be28854136a23f62fbfab4bfa425d2c947db
---
# Radar — 队列 / 观察列表

_最终更新: 2026-09 · owner: Youngjin · volatility: 高_
[← 返回 index](index.md)

> **L0 TL;DR**: 需要进一步原文、复现或现场验证的候选。晋升需满足全部[收录条件](maintenance.md#纳入标准-the-filter)并由 owner 审查用途，扫描不能批准。
>
> ⚠️ **不要把这里的条目当作"成熟能力"用于客户提案。** 华丽的演示常常掩盖可部署性。

---

> **复核范围**：页面修改日不代表所有技术条目已重验。核心修正日期、复现/人工状态见[证据](evidence.md)，旧条目仍使用各自确认日期。

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

## 🆕 最新扫描流入（2026-10-09 · 链接与一手来源核对 2026-09-27）

<!-- 自动扫描（arXiv/网络）流入项。2026-09-27 全部链接存活确认（20/20 HTTP 200）+ 10 项对照一手来源 —— 晋升 0 项，更正 6 项（RLDX 基准差距 +11.1 分、更换 KIMM 链接、更换 OpenAI 链接并将引语标为二手、反映 Skild 自报基准、Figure Index 数字单独注明来源、删除 NEURA IFA 实机展示说法）。按流入政策等级保持 [4]（自行公布、无独立验证）。在通过 THE FILTER 之前禁止用于客户提案。定期刷新参见 scripts/radar_scan.md。 -->

| 条目 | 标签 | 要点 | 晋升条件 |
|---|---|---|---|
| **[NEURA Robotics 4NE1 / Neuraverse × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale)**（德国全栈机器人公司，与 AWS 战略合作） | ⚪ 路线图 | ✨ **为何关注**：AWS 作为 Neuraverse 的主要云服务商托管平台，NEURA Gym 训练管道与 SageMaker 集成，NEURA 通过 AWS 合作伙伴网络（APN）拓展市场 —— 明确列出服务名的 AWS 合作，是 Radar 中的欧洲人形机器人赛道<br>⏳ **为何等待**：AWS·NEURA 官方发布（2026-04-21，press.aboutamazon.com）`[4]` —— Amazon 履约中心部署在原文中仅为"explore opportunities"（探索），并非实际部署。[最高 14 亿美元的 C 轮](https://neura-robotics.com/record-series-c/)（2026-06-10，Amazon、NVIDIA、Tether 等参与，公司自称"全栈机器人公司史上最大"）与 [IFA 2026 柏林主题演讲](https://www.ifa-berlin.com/press-releases/ifa-2026-neura)（2026-09-05）带来新话题，无第三方验证。🔗 链接 200 · 一手来源核对 2026-09-27。**AWS 角度：官方合作（明确 SageMaker·APN）** | 公开 Amazon 履约中心等实际部署案例 + 独立性能验证 |
| **[RLWRLD RLDX-1](https://arxiv.org/abs/2605.03269)**（81 亿参数的灵巧操作[^dext]基础模型，在 AWS 上训练） | 🔵 Research | ✨ **为何关注**：KAIST 出身的首尔初创公司的开放机器人基础模型，由 [AWS Physical AI 博客](https://aws.amazon.com/blogs/physical-ai/putting-dexterous-robots-to-work-how-rlwrld-builds-physical-ai-with-aws/)（2026-06-22）直接介绍 —— 使用 EC2 p5e/p5en（H200）、ParallelCluster、FSx for Lustre 训练，专注五指手精细操作，代码与权重[在 GitHub 公开](https://github.com/RLWRLD/RLDX-1)（CC BY 4.0）—— 与 NEURA 同为 Radar 中的 AWS 官方合作案例，也是韩国发起的赛道<br>⏳ **为何等待**：arXiv 技术报告（2026-05-05）+ AWS 博客 `[4]` —— 6 套仿真基准与 3 个实机平台的自测数据（GR-1 Tabletop 58.7 vs GR00T N1.6 47.6 = +11.1 分，表 1(b)；ALLEX 实机 86.8% vs π0.5·GR00T N1.6 约 40%；SIMPLER 81.5% 为 AWS 博客引用），无独立复现与同行评审 —— **自行公布数据，禁止向客户引用**。与 AWS 的关系处于训练基础设施 + Generative AI Accelerator 参与（2025-10）阶段，实际部署目标为乐天酒店及度假村 2030 年（以安全验证为前提）。🔗 链接 200 · 一手来源核对 2026-09-27。**AWS 角度：AWS 博客案例（EC2·ParallelCluster·FSx）· 🇰🇷 韩国触点** | 独立基准复现 + 公开实际部署案例 |
| **[Figure Index → Helix 2.5](https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization)**（以众包人类视频数据预训练的人形机器人神经网络，在 30 个未见过的家庭中零样本验证） | 🟡 Preview | ✨ **为何关注**：Figure 将以众包数据（Index）预训练的单一策略在不采集数据、不微调的情况下部署到湾区 30 个真实家庭（全部未见过），完成整理客厅、叠毛巾、整理床铺 3 项任务 —— 宣称仅靠 Index 预训练就使零样本整任务成功率从 9% 升至 56%，是众包数据管道转化为真实策略性能的首个定量主张<br>⏳ **为何等待**：Figure 官方发布（2026-09-17，figure.ai）`[4]` —— 9%→56% 为 Figure 内部盲测的**自测数据，禁止向客户引用**（420 次试验中 237 次仅见于二手媒体，原文页面文本中未确认；Index 报酬 1,500 万美元出自 [Index 发布](https://www.figure.ai/news/introducing-index)，2026-08-25），无独立复现或第三方验证。🔗 链接 200 · 一手来源核对 2026-09-27。**AWS 角度：无** | 独立复现与第三方基准验证 + 扩大家庭与任务范围的实证 |
| **[KIMM 凯洛斯（KAIROS）V0.7](https://www.kimm.re.kr/sub0504/view/id/21372)**（K-Moonshot 国家战略技术项目的韩国国产 AI 人形机器人） | ⚪ 路线图 | ✨ **为何关注**：韩国机械研究院（KIMM）作为科技信息通信部支持的"AI 人形机器人全球顶尖研究团"开发的国家项目人形机器人 —— 2026-09-07 在"2026 全球机械技术论坛"公开 V0.7，演示假面舞、国民体操等全身动作（4 月建院 50 周年首次公开的 V0.5 仅能握手、挥手）—— 韩国客户对话中可能出现的"国家研究机构"人形机器人赛道<br>⏳ **为何等待**：KIMM 官方新闻（2026-09-07）`[4]` —— 演示为自家 demo，无自主性能数据。V1.0 公开目标 2027-04 与约 30 亿韩元追加开发费不在 KIMM 原文中，出自 [edaily](https://www.edaily.co.kr/News/Read?newsId=03883526645577824)·[Newspim](https://www.newspim.com/news/view/20260907001070) 报道（二手）。无商业化与自主性能，处于 demo 阶段。🔗 链接 200（原 4 月新闻稿链接已替换为 09-07 官方新闻）· 一手来源核对 2026-09-27。**AWS 角度：无 · 🇰🇷 韩国触点** | 公开 V1.0 + 公开汽车装配或家用实证案例 |
| **[XPENG IRON](https://www.xpeng.com/news/01a080371029a057bc8e8a02a2c6012b)**（中国电动车企业小鹏的人形机器人，首台成品机器人自行走下汽车级量产线） | ⚪ 路线图 | ✨ **为何关注**：整车企业将自身 EV 生产经验（核心工序自动化 80%+）直接移植到人形机器人量产线 —— 公开了成品机器人自行走下产线的画面（全身 76 自由度，每只手 21 自由度）—— 韩国客户对话中"中国 EV 出身人形机器人"的竞争赛道<br>⏳ **为何等待**：小鹏官方发布（2026-09-08，xpeng.com）`[4]` —— 按原文，"进入量产"是 2026 年底目标，初期商业投放在自家门店与园区，中国及海外正式上市与交付计划在 2027 年。自由度与自动化率为自行公布，无独立性能与安全验证。🔗 链接 200 · 一手来源核对 2026-09-27。**AWS 角度：无** | 实际量产出货开始 + 第三方安全与性能验证 |
| **[Skild AI S1](https://skild.ai/blogs/s1)**（仅凭单个人类演示视频、无需微调即可执行最长 10 分钟长程任务的上下文学习机器人基础模型） | 🟡 Preview | ✨ **为何关注**：以 1 个人类演示视频作为"视觉提示"，无需微调或改动权重即可执行最长 10 分钟、数十步的未见过长程任务 —— [NVIDIA 官方博客](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/)（2026-09-10）介绍了 Skild·NVIDIA·富士康在 NVIDIA Blackwell 系统装配线的部署（安装母线排与限位块、拧紧 16 颗螺钉）以及"60 多个部署合作"—— 从"少数合作伙伴部署"宣言阶段迈入工业营收阶段的早期案例<br>⏳ **为何等待**：NVIDIA·Skild AI 官方发布（2026-09-10）`[4]` —— [Skild 自家文章](https://www.skild.ai/blogs/skild-crosses-100m-arr)中的 ARR 1 亿美元（首次商业部署后 10 个月）、已确认营收 5,000 万美元、60 多个付费客户，以及 S1 博客（2026-08）中已见任务 96%、未见任务 66% 的成功率，均为**自行公布数据，禁止向客户引用**（无第三方审计或独立验证）。无 AWS 映射或首尔区域关联案例。🔗 链接 200 · 一手来源核对 2026-09-27。**AWS 角度：无（NVIDIA 技术栈）** | 独立性能与营收验证（第三方审计）+ 公开 AWS 映射案例 |
| **[Intrinsic Core](https://www.intrinsic.ai/blog/posts/introducing-intrinsic-core)**（Alphabet 机器人子公司 Intrinsic 开源其工业机器人技术栈 —— 实时控制、基于 NVIDIA FoundationPose 的位姿估计、运动/抓取规划、基于 Gazebo 的仿真、相机标定、ROS 兼容驱动） | 🟢 GA（开源） | ✨ **为何关注**：Intrinsic 在 ROSCon 2026（多伦多）以 Apache 2.0 整体公开了与其自身制造部署所用相同的技术栈（[GitHub](https://github.com/intrinsic-ai/intrinsic-core)）—— 在 Isaac 生态一家独大的格局中首次出现 Alphabet 出身的替代技术栈，为 Radar 🖥️ 仿真/工具轴（Isaac/MuJoCo/Newton）新增竞争观察对象<br>⏳ **为何等待**：Intrinsic 官方博客（2026-09-22）`[4]` —— 代码已公开，但没有 Intrinsic 之外的独立采用案例（原文仅提及 FANUC·UR 兼容与挑战赛参与人数），也无 AWS 映射案例。🔗 链接 200 · 一手来源核对 2026-09-27。**AWS 角度：无（竞争技术栈）** | 公开外部独立采用案例 + 验证 AWS 基础设施映射 |
| **[Agility Robotics Digit 5](https://www.agilityrobotics.com/content/agility-unveils-digit-5-humanoid-robot-built-for-cooperatively-safe-work-at-scale)**（相较现有 Digit@GXO，具备近距离协作安全架构与 90 分钟续航电池的第五代通用人形机器人） | 🟡 Preview | ✨ **为何关注**：已在 pillar-4 中列为"验证最充分的付费人形机器人"的 Agility Digit（@GXO）的下一代机型 —— 检测到碰撞风险时回避、停止或坐下，并以视听信号与人近距离协作的安全设计，90 分钟续航、9 分钟充电，并宣布以 CE 标志进入欧盟与英国的计划<br>⏳ **为何等待**：Agility 官方发布（2026-09-15，agilityrobotics.com）`[4]` —— 3 亿美元以上的多年订单为"截至 2026-05，以合同里程碑为前提"，Digit 5 实际运行为 0（既有 65,000 小时以上的成绩属于 Digit 4）。早期访问计划在 2027 年上半年，面向制造与仓储客户的 GA 预计 2027 年底。🔗 链接 200 · 一手来源核对 2026-09-27。**AWS 角度：无** | 公开 Digit 5 实际运行客户案例（欧盟/北美）+ 安全架构第三方验证 |
| **[Dyna Robotics DYNA-2 / DYNA 2.1](https://www.prnewswire.com/news-releases/dyna-robotics-launches-dyna-2-1-physical-agent-a-semi-humanoid-robot-that-completes-full-workflows-such-as-a-commercial-laundry-shift-302892411.html)**（完全不使用机器人实机数据、仅以 100 万+小时第一人称人类视频预训练的世界-动作模型，加上已在洗衣、酒店客房清洁、餐饮服务等完整工作流中实际部署的半人形 physical agent） | 🟡 Preview | ✨ **为何关注**：世界-动作模型（DYNA-2）完全不使用机器人实机数据、仅以人类第一人称视频预训练，再通过少量机器人数据微调，延伸为已在酒店、餐厅、洗衣店实际部署的半人形机器人（DYNA 2.1）—— "人类数据→机器人规模法则"的主张，为 Radar 🔬 World-action models 轴新增数据管道视角（无机器人数据预训练）的案例<br>⏳ **为何等待**：Dyna Robotics 官方发布（PR Newswire，DYNA-2 更正版 2026-08-10·DYNA 2.1 2026-09-29）`[4]` —— 成功率 20%→80~90%、相对 DYNA-1 提升 1.55 倍、客户现场 87% vs 46% 等数字均为**自行公布数据，禁止向客户引用**，无独立验证或同行评审。模型权重与 API 未公开（仅能通过自家运营的硬件接触）。⚠️ 本次执行环境的 egress 限制阻止了对 prnewswire.com 的人工 curl 200 验证（见提交信息/issue）。**AWS 角度：无（Amazon Industrial Innovation Fund 仅作为 2025-09 A 轮投资方参与，非基础设施合作）** | 独立性能验证（第三方审计）+ 公开更多实际部署案例 |
| **[Magic-W0](https://arxiv.org/abs/2609.39870)**（Magiclab Robotics，将 3D 几何、运动与未来语义构成的结构化世界表示与动作生成双向耦合的世界-动作基础模型） | 🔵 Research | ✨ **为何关注**：以第一人称人类操作视频、真实机器人轨迹与仿真数据大规模预训练，自称在 RoboDojo-Sim 基准上排名第一 —— 为 Radar 🔬 World-action models 轴（DreamZero→GR00T N2）新增一个公开代码（GitHub）的中国机器人创业公司实现案例<br>⏳ **为何等待**：arXiv 预印本（2026-09-30 提交·v2 2026-10-03）`[4]` —— 以 RoboDojo-Sim·LIBERO 自测基准与自测实机测试为主，无同行评审或独立复现。代码已公开（MagiclabRobotics/Magic-W0），但训练权重是否公开尚不明确。⚠️ 本次执行环境的 egress 限制阻止了对 arxiv.org·github.com 的人工 curl 200 验证（见提交信息/issue）。**AWS 角度：无** | 同行评审 + 独立复现 + 实机部署案例 |

## 终止或限制 — 分别确认 { #-已废弃--禁止提议存档保留 }

| 条目 | 状态 | 替代 |
|---|---|---|
| **[AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)** | 不接受新客户，现有客户可继续 `[1]` | 不用于新机器人默认方案 — [证据](evidence.md#fleetwise-new-customers) |
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 终止 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 终止 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 终止 (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 无公开案例 `[4]` | 当前为 CUDA/NVIDIA（提议时明示风险） |

> ⚠️ **传闻警戒（并非事实）**: "AWS IoT TwinMaker 废弃"是**误信息** —— TwinMaker 是 GA·对新客户开放（低速度）。是与 SiteWise 维护混淆的第三方博客主张。禁止重复。→ [pillar-3](pillar-3.md)。

---

## 晋升流程（摘要）

1. **捕获**: 用指定频道/表情收集候选
2. **过滤**：满足全部[收录条件](maintenance.md#纳入标准-the-filter)，区分发布、证据、用途和支持。
3. **通过时**: 由负责的支柱 owner 用[标准模板](maintenance.md#标准模板)编入，并从 Radar 移除
4. **未达时**: 在此保留一句话，明示晋升条件

完整管道 → [maintenance](maintenance.md#playbook-晋升管道)。

---
_owner: Youngjin · updated: 2026-09 · volatility: 高（Radar 本质上快速变化 —— 建议月度评审）_

<!-- 용어 각주 -->

[^wfm]: **世界基础模型（WFM, World Foundation Model）** — 为预测·生成物理世界的下一场景而训练的大型模型。通过文本·视频提示生成物理上合理的视频·场景，用于增强机器人学习数据。🎥 [NVIDIA Cosmos 介绍](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **系统辨识（SysID, System Identification）** — 测量真实机器人的物理参数（摩擦·质量·电机响应），把仿真器校准到与实物一致的工作。
[^s2r]: **sim-to-real** — 把在仿真中训练的策略迁移到真实机器人上，或指其方法论。由于仿真与现实的物理·视觉差异（域间差异），直接迁移会导致性能崩溃。🎥 [NVIDIA sim-to-real 机器人展示](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **物理引擎（physics engine）** — 数值计算刚体动力学·接触·摩擦·碰撞的仿真器核心软件。引擎的精度·速度权衡左右着仿真器的选择（Isaac/MuJoCo/Genesis）。
[^mcp]: **MCP（Model Context Protocol）** — 连接智能体与工具·数据源的开放标准协议。常被比作"智能体的 USB-C"，把机器人技能暴露为 MCP 服务器的实验正在增多。
[^ros]: **ROS 2（Robot Operating System 2）** — 机器人软件事实上的标准开源中间件。传感器·控制节点通过话题（topic）通信的分布式架构，是工业·研究机器人栈的公共基础。
[^agent]: **LLM 智能体** — 大语言模型自行制定计划、挑选并调用工具（API·机器人技能）、执行多步任务的软件。与简单问答不同，关键在于它有"行动"。
[^dext]: **灵巧操作（dexterity）** — 机器人手·臂像人手一样精细·灵巧地操纵物体的能力。与简单夹爪的抓取·放置不同，指用五指手转动物体或操作工具等接触密集、复杂的操作。
