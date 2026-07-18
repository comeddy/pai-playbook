---
ko_hash: bf3dbec91ebf5416ed0579ee049bd62bb700c305
---
# Pillar 3 — 仿真 (Simulation)

_最终更新: 2026-07 · owner: comeddy · volatility: 高（版本·实例经常变动）_
_除非另有标注，各条目继承页面元数据（owner/updated/volatility）。按条目指定 owner 时在条目页脚补充。_
[← 返回 index](index.md)

> **L0 TL;DR**: 机器人策略在仿真中比在真实机体上训练快数千倍且更安全。AWS 上的正解栈是 **EC2 G6e/G7e(RTX GPU) + NVIDIA Isaac Sim AMI(GUI) + AWS Batch(无头大规模 RL)**。⚠️ **AWS RoboMaker 已于 2025-09-10 终止** —— 绝对不要提议。Isaac Sim 最新 GA 为 **5.1.0**，6.0 仍为 Preview。

---

## 本支柱中客户最常问的问题 Top 3

1. **"Isaac Sim/Lab 在 AWS 上怎么跑？用哪种实例？"** → [Isaac on AWS](#1-isaac-sim--isaac-lab-on-aws--ga)
2. **"数千~数万环境的并行 RL 在云上怎么扩展？"** → [大规模并行 RL](#2-大规模并行-rl-仿真--ga)
3. **"必须全押 NVIDIA 吗？开源替代方案呢？"** → [开源替代方案](#3-开源仿真器替代方案--ga---部分-hype)、[decisions](decisions.md)

> **稳定原理（几乎不变）**: 仿真的价值在于 (1) **并行性**（一张 GPU 上同时数千~8 千环境），(2) **安全**（无需损坏真实机体即可探索危险策略），(3) **自动标注**（完美的 ground truth）。渲染**必须用 RTX(RT Core) GPU**，所以 A100/H100（计算 GPU）无法用于 Isaac Sim 渲染 —— 这是左右实例选择的不变约束。

---

## 1. Isaac Sim & Isaac Lab on AWS  🟢 GA

**L0 TL;DR**: 在 AWS EC2 GPU 上运行 NVIDIA Isaac Sim（仿真器）+ Isaac Lab（RL 框架）的正统路径。Marketplace 上有**免费 AMI**，进入很容易。

**客户需求/问题**: "本地工作站 GPU 不够。想在云上用 GUI 使用 Isaac Sim，训练则以无头方式大规模跑。"

**解决方案概览** `[1]`:

- **版本**: Isaac Sim 最新 **GA = 5.1.0(2025-10-30)**。**6.0 为 Preview**（"Early Developer Release", GTC'26）—— 即便 GitHub 补丁标签被错误标为 "GA"，也**不要把 6.0 说成 GA**。Isaac Lab 稳定版 2.3.x，3.0 为 beta（引入 Newton 物理引擎）。
- **许可证**: Isaac Sim **源码为 Apache 2.0**（商用免费）。但若将 **Omniverse Kit 运行时**做第三方再分发/SaaS 提供/交钥匙安装，则**需要 NVIDIA AI Enterprise 许可证**。内部 R&D 或仅销售产出物则无需。Isaac Lab 为 BSD-3。
- **GPU 需求**: **必须 RTX(RT Core)**。最低 RTX 4080(16GB)，理想为 RTX PRO 6000 Blackwell(48GB)。**不支持 A100/H100**（无 RT Core）。

**AWS 映射** `[1]`:

- **实例**: G6e(L40S 48GB) / **G7e(RTX PRO 6000 Blackwell 96GB, 2026-01 GA)**。官方 **Isaac Sim Development Workstation AMI**(build 2026.1.1, Ubuntu 24.04, 免费) 支持 G6e·G7e，推荐 `g6e.4xlarge`。
- **接入**: 用 NICE DCV(=Amazon DCV) 客户端/网页进行远程 GUI 流传输。
- **参考架构**: **AWS Solutions Guidance "Physical AI for Robotics on AWS"**(Isaac Sim on GPU EC2 + Isaac Lab + SageMaker + IoT Greengrass 边缘)。AWS 上存在 **Physical AI 专属博客频道**(aws.amazon.com/blogs/physical-ai/)。

**决策标准**:

- GUI 场景编辑·SDG → G6e（成本）或 G7e（性能·大场景）。
- 大规模无头 RL → 第 2 项（AWS Batch）。
- 开源是否够用 → 第 3 项 / [decisions](decisions.md)。

**客户案例**: 案例待定（Unitree H1 训练见 [pillar-2](pillar-2.md) 的 AWS 博客）。

**➡️ SA 后续行动**: **将"在 g6e.4xlarge 上启动 Marketplace Isaac Sim AMI 并用 NICE DCV 接入的 30 分钟 hands-on"作为首个提议**，随后以 **[pai-sim-isaaclab 端到端实操](https://github.com/comeddy/pai-sim-isaaclab)**（Terraform 预置 g6e → Isaac Lab 四足 PPO 无头训练 → 策略导出，约 2 小时/$12）衔接到无头训练。出现许可证问题则准确说明"源码 Apache，但再分发/SaaS 需 AI Enterprise"。

**🔗 相关资产**: [pillar-2 训练栈](pillar-2.md) · [pillar-1 合成数据](pillar-1.md) · [decisions](decisions.md) · [NVIDIA Isaac Lab on AWS 研讨会（Batch MNP 无头 RL）](https://catalog.us-east-1.prod.workshops.aws/workshops/075ce3fe-6888-4ea9-986e-5bdd1b767ef7/en-US)

<details markdown="1"><summary>🔄 易变数据（版本 —— 2026-07 确认，部分年份需在 GitHub 再确认）</summary>

| 组件 | 状态 | 备注 |
|---|---|---|
| Isaac Sim 5.1.0 | 🟢 GA (2025-10-30) | 最新 GA |
| Isaac Sim 6.0 | 🟡 Preview | Early Dev Release, PhysX+Newton 多后端 |
| Isaac Lab 2.3.x | 🟢 GA | 兼容 Isaac Sim 5.1 |
| Isaac Lab 3.0 | 🟡 beta | Newton 物理引擎 |
| Isaac Sim AMI | 🟢 GA | build 2026.1.1, G6e/G7e |
</details>

---

## 2. 大规模并行 RL 仿真  🟢 GA

**L0 TL;DR**: Isaac Lab 在**一张 GPU 上同时仿真数千~8,192 个环境**。在 AWS 上进行无头大规模 RL 的官方路径是 **AWS Batch(Multi-Node Parallel)**。

**客户需求/问题**: "训练一个策略要好几天。想大量并行化环境并用多节点扩展。"

**解决方案概览** `[1]/[3]`:

- Isaac Lab 在**一张 GPU 上同时仿真数千~8 千环境**，并可随多节点近乎线性扩展（具体数值见下方折叠块 —— 引用时务必并列注明测量条件）。
- **AWS Batch Multi-Node Parallel Jobs** 是 AWS 推荐的编排器（也是 RoboMaker 的迁移路径）。AWS HPC/Physical AI 博客中存在 Isaac Lab on G6e + Batch MNP + EFS + ECR 的参考。

<details markdown="1"><summary>🔄 易变数据（基准 —— NVIDIA 官方性能基准, "with training" 为准, 2026-07 确认）</summary>

| 任务 | 环境数 | GPU | 吞吐量 |
|---|---|---|---|
| Cartpole-Direct | 4,096 | 1×RTX 4090 | 510,000 FPS |
| 人形(Velocity-Rough-G1) | 4,096 | 1×RTX 4090 | 82,000 FPS |
| Cartpole-Direct | 4,096 | 16×L40 (4 节点) | 3,500,000 FPS |
| 精密操作(Repose-Cube-Shadow) | 8,192 | 1×RTX 4090 | 170,000 FPS |

_来源: isaac-sim.github.io/IsaacLab performance benchmarks `[1]`_
</details>

**AWS 映射** `[1]`: **AWS Batch(MNP)** + EFS（共享存储）+ ECR（容器）+ G6e/G5。NVIDIA 侧用 OSMO 做多节点编排。⚠️ **没有面向 EKS·ParallelCluster 的 Isaac 官方参考架构** —— Batch 是有文档的路径。

**决策标准**:

- 单 GPU 数千环境即够（多数 locomotion）→ EC2 单实例。
- 需要多节点（超大型·像素观测）→ **AWS Batch MNP**。
- 想用 SageMaker 整合训练循环 → [pillar-2](pillar-2.md) 的 Isaac Lab on SageMaker 博客。

**客户案例**: **Unitree H1 RL(Isaac Lab on SageMaker)** —— 见 [pillar-2](pillar-2.md)。

**➡️ SA 后续行动**: **画出"用 AWS Batch MNP 扩展 Isaac Lab 并行 RL"架构**，用客户任务是像素观测（→ 需要多节点）还是状态观测（→ 单 GPU 即够）来判断扩展。引用基准时务必并列注明测量条件（环境数·GPU）。

**🔗 相关资产**: [pillar-2 HyperPod](pillar-2.md) · [decisions: GPU 获取](decisions.md)

---

## 3. 开源仿真器替代方案  🟢 GA / ⚪ 部分 Hype

**L0 TL;DR**: 不喜欢 NVIDIA 全栈，或特定工作负载用开源更好。**MuJoCo(+MJX)** 是最可信的替代（Unitree 实际使用），**Gazebo** 是 ROS 原生标准，**Genesis** 则话题性高于验证（著名的 "430,000 倍" 主张已被反驳）。

**客户需求/问题**: "NVIDIA 依赖有负担" / "ROS 整合优先" / "需要可微分物理"。

**解决方案概览** `[1]`:

- **MuJoCo / MJX** —— C 引擎 GA(v3.10)，**MJX-JAX** 是成熟的 RL 主力（可微分、跨厂商），**MuJoCo Warp 为 Alpha**（非生产）。**Unitree 为 Go2/G1/H1 的 RL 维护自有 MuJoCo 仓库 = 实际厂商采用**。MuJoCo Playground 经 RSS 2025 验证，6 个平台 sim-to-real。
- **Gazebo** —— 最新 LTS **Jetty**(2025-09)，**Harmonic** 部署最广。ROS 2 原生。⚠️ **Gazebo Classic 11 于 2025-01 EOL** —— 新项目禁用 Classic。基于 CPU，不适合 GPU 并行 RL（是 Isaac 的补充）。
- **Genesis** —— Apache 2.0，活跃但**"43M FPS/430,000 倍"主张在现实工作负载中被反驳**（在接触多的操作中反而比 ManiSkill 慢 3~10 倍）。作为 Isaac 替代未获验证 → **⚪ 注意夸大**。

**AWS 映射**: 全部可在 EC2 上运行。MuJoCo/MJX(JAX) **也可利用 A100/H100(P4/P5)**（无需 RTX 渲染）—— 与 Isaac 不同，能用计算 GPU 是其优势。大规模用 AWS Batch。

**决策标准**（详情 → [decisions](decisions.md)）:

- 照片级渲染·SDG·全栈 → **Isaac Sim**。
- 可微分·轻量·跨厂商 GPU·快速 RL 迭代 → **MuJoCo/MJX**。
- ROS 2 整合·CPU·传统机器人 → **Gazebo**。
- Genesis → 仅限 PoC/实验，禁止生产依赖。

**客户案例**: **Unitree**（MuJoCo，训练生产 HW）。

**➡️ SA 后续行动**: 对担心"NVIDIA 依赖"的客户提出**"AWS 对 Isaac、MuJoCo/Gazebo 都能跑好 —— 按工作负载选即可"**的中立立场。若用 MuJoCo，强调可复用计算 GPU(P5) 的成本优势。

**🔗 相关资产**: [decisions: NVIDIA vs 开源](decisions.md)

---

## 4. NVIDIA Cosmos 3（世界基础模型）  🟢 GA · ⚠️ AWS 未托管

**L0 TL;DR**: 生成·推理·仿真物理世界的基础模型。**可商用(OpenMDW-1.1)**。⚠️ 但 **AWS 未被列为官方 Cosmos 3 云托管方**（Azure/CoreWeave/Baseten 等为托管方）—— 这是 SA 应了解的竞争现实。

**客户需求/问题**: "想生成多样的现实场景用于训练/评估。"（数据生成视角见 [pillar-1](pillar-1.md)）

**解决方案概览** `[1]`: **Cosmos 3**(2026-05-31 GTC Taipei GA) 是当前旗舰 —— Reasoner(VLM) + Generator(diffusion)，MoT 架构。**Super 64B**（数据中心）、**Nano 16B**（RTX PRO 6000，实时机器人，含 Nano-Policy-DROID）、**Edge**（Jetson，计划中 —— 参数未公开）。许可证 **OpenMDW-1.1（可商用）**。HF/GitHub/NGC 分发。⚠️ 旧的 Predict/Transfer/Reason 系列进入维护模式（建议迁移到 Cosmos 3）。

**AWS 映射**: **直接映射较弱** —— Cosmos 3 不以 AWS 为指定托管方。但因是开放权重(HF/GitHub)，**可在 EC2 G7e(Nano 16B, RTX PRO 6000) 上自托管**。这就是 AWS 的角度: "即便不是托管主机，也能用最佳 GPU 自行运行"。

**决策标准**: 需要托管 Cosmos NIM → 其他云。开放权重自托管·数据主权·整合既有 AWS 栈 → EC2 G7e。

**客户案例**（⚠️ 仅为公布，未经生产验证）: 作为 Cosmos 3 采用方，**Doosan Robotics、LG Electronics、Samsung Electronics** 等多家韩国企业已公布 —— 国内相关性高，但为"已公布的采用"而非经过验证的生产。

**➡️ SA 后续行动**: 国内客户对 Cosmos 3 感兴趣 → **以"在 AWS G7e 上自托管 Cosmos 3 Nano" PoC 应对**（把缺乏托管服务转化为自托管+数据主权的优势）。

**🔗 相关资产**: [pillar-1 Cosmos 数据生成](pillar-1.md) · [pillar-4 sim-to-real](pillar-4.md)

---

## 5. 数字孪生 — IoT TwinMaker & Omniverse on AWS  🟢 GA（低速度）

**L0 TL;DR**: **AWS IoT TwinMaker 并未被废弃**（第三方"discontinued"主张是误信息 —— 与 SiteWise 的维护混淆）。它是 GA 且对新客户开放，但**新功能推进缓慢**（低速度）。Omniverse 也以 AWS Marketplace AMI 形式 GA。

**客户需求/问题**: "想制作设备/工厂数字孪生，并与机器人仿真·监控连接。"

**解决方案概览** `[1]`:

- **AWS IoT TwinMaker** —— GA，官方产品页面有效，无废弃横幅（2026-07-11 确认）。⚠️ innfactory.de/oneuptime.com 等的 "discontinued" 主张是**未经验证的传闻**，禁止重复。但 2025~26 无重大新功能，故为**低速度**。
- **NVIDIA Omniverse on AWS** —— Marketplace AMI(Developer/Production, Linux/Windows)。运行于 **EC2 G6e/G7e**。Production AMI 是捆绑 AI Enterprise 许可证 + 支持的付费订阅。⚠️ **没有专用的 "OVX" 实例家族** —— Omniverse on AWS = G6e/G7e + AMI。托管的 "Omniverse Enterprise on AWS" 无明确依据。

<details markdown="1"><summary>🔄 易变数据（AMI 版本·价格 —— 2026-07 确认）</summary>

| 项目 | 值 |
|---|---|
| 最新 AMI | 2026.1.0 (Ubuntu 24.04, 2026 Q1 Refresh) |
| Production AMI 订阅 | ~$1.00/hr（Marketplace 标示价，含 AI Enterprise + 支持） |
</details>

**AWS 映射**: IoT TwinMaker + IoT SiteWise + Omniverse AMI(G6e/G7e)。

**决策标准**: 设备数据整合·轻量孪生 → TwinMaker（但需考虑低速度）。照片级仿真·USD 协作 → Omniverse AMI。

**客户案例**: 案例待定。

**➡️ SA 后续行动**: 客户问"听说 TwinMaker 死了？"时**立即更正**（"GA、对新客户开放，只是低速度"）。想整合孪生+仿真则连接到 Omniverse AMI。问"有 OVX 吗"则准确回答"没有，是 G6e/G7e + AMI"。

**🔗 相关资产**: [pillar-1](pillar-1.md) · （内部数字孪生研讨会 —— 需确认 ⚠️）

---

## 本支柱的诚实现实（SA 必读）

- **AWS RoboMaker 已死（2025-09-10 支持终止）。** 绝对禁止作为选项提出。后续栈 = EC2 G6e/G7e + Isaac Sim AMI + AWS Batch MNP。
- **Isaac Sim 6.0 不是 GA（Preview）。** 最新 GA 是 5.1.0。不要被 GitHub 补丁标签迷惑。
- **AWS 不是 Cosmos 3 的指定托管方**（Azure/CoreWeave 为托管方）。以自托管(G7e)应对才是诚实的角度。
- **A100/H100 无法用于 Isaac Sim 渲染**（无 RT Core）。渲染用 G6e/G7e，计算型 RL 也可用 P5（MuJoCo）。
- **TwinMaker 废弃说是传闻** —— 更正的同时诚实承认"低速度"。
- **Genesis "430,000 倍"已被反驳**，**MuJoCo Warp 为 Alpha**，**Unity Robotics Hub 实际处于放置状态（2022 年以后）**，**Habitat 在 v0.3.4 之后停止维护** —— 禁止夸大开源成熟度。

---
_owner: comeddy · updated: 2026-07 · volatility: 高（版本·实例在折叠块中管理）· sources: [1] 官方/论文, [3] 厂商, [4] 未经验证。建议再确认部分 GitHub 发布年份。_
