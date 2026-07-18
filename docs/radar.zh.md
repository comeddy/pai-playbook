---
ko_hash: 0f25aef6b593147b074982f677925d5b0fae9c1f
---
# Radar — 队列 / 观察列表

_最终更新: 2026-07 · owner: 待定 ⚠️ · volatility: 高_
[← 返回 index](index.md)

> **L0 TL;DR**: 尚未通过纳入标准（[2.5 THE FILTER](maintenance.md#纳入标准-the-filter)）但**值得关注**的东西。每个条目一句话 —— 成熟度标签 + **为何待定**。一旦通过门禁（4 项中 2 项），由负责的支柱 owner 用标准模板晋升。
>
> ⚠️ **不要把这里的条目当作"成熟能力"用于客户提案。** 华丽的演示常常掩盖可部署性。

---

## 🔬 模型 / 算法（待验证）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| Physical Intelligence **π0.7** | 🔵 Research | 仅二手来源 `[4]`，无 PI 一手确认 | PI 官方发布 + 性能验证 |
| **GR00T N1.6 / N1.7 商业许可证** | 🟡→ | 允许商用的说法仅来自二手来源 `[4]`（N1.5 在模型卡上明确为非商业 `[1]`） | 在实时模型卡确定许可证 |
| **World-action models**（DreamZero → GR00T N2） | 🟡 Preview | GR00T N2 "计划年底"，DreamZero 为研究 | GA + 实际部署案例 |
| Google DeepMind **Genie 3**（用于机器人学习的世界模型） | 🟡 Preview | 世界模型本身为预览，用于机器人学习为研究 | 机器人策略学习验证案例 |
| **基于 VLM 的 SysID**（Vid2Sid, Swim2Real） | 🔵 Research | 2026 预印本，单一实验室 | peer-review + 复现 |
| **VIRAL / VideoMimic / Real2Render2Real**（visual sim-to-real at scale） | 🔵 Research | CVPR/CoRL 研究，非生产 | 生产部署证据 |
| **Robbyant LingBot-VLA / UnifoLM-VLA-0** | 🔵 Research | 二手来源，无验证 | 一手确认 + AWS 映射 |

## 🖥️ 仿真 / 工具（待成熟）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| **Genesis** 物理引擎 | ⚪ Hype | "430,000 倍"已被反驳 `[1]`，接触操作中慢 | 独立基准 + 生产采用 |
| **MuJoCo Warp** | 🟡 Alpha | PyPI classifier "3-Alpha" `[1]`，非生产 | Beta/GA 转换 |
| **NVIDIA Newton** 物理引擎 | 🟡 Preview | 在 Isaac Sim 6.0 中为 experimental 后端 | GA + Isaac Lab 3.0 正式 |
| **Isaac Sim 6.0** | 🟡 Preview | "Early Developer Release"，API 变动（最新 GA 为 5.1） | 6.x GA 宣布 |
| **Cosmos 3 作为 sim-to-real 学习源** | 🟢 GA（模型）/🔵（实战） | 模型 GA，但"用世界模型数据训练可实际部署策略"仅早期采用者。⚠️ **AWS 未托管** | 强化 AWS 映射 + 学习验证 |

## 🤖 硬件 / 部署（路线图·演示）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | 仅 Musk 的主张，生产未启动 | 经过验证的部署 |
| **Hyundai 25,000 Atlas** | ⚪ 路线图 | 目标 2028 启动，0 台运行，工会反对 | 实际运行启动 |
| **1X Neo** 自主性 | 🟡 Preview | 已发布产品但自主 ~60~70%，其余为 VR 远程操作 | 真正自主的验证 |
| **Figure 03 "8 小时自主班次"** | ⚪ Hype | CEO 推文，无独立验证（Figure 02@BMW 为已验证试点） | 第三方自主性审计 |
| **Cosmos 3 采用**（Doosan/LG/Samsung） | 🟢 GA（公布） | 采用为"公布"而非生产验证 | 公开生产案例 |

## 🔗 智能体 / 连接（早期）

| 条目 | 标签 | 为何待定 | 晋升条件 |
|---|---|---|---|
| **MCP for robotics**（ros-mcp-server 等） | 🔵 Research | 有 50+ 服务器但为开源/演示，无生产（安全·延迟·确定性未验证） | 生产硬化案例 |
| **ROS 2 + LLM 智能体**（NASA JPL ROSA, RAI） | 🔵 Research | ROSA(JPL) 为最强实例但为 mock-ops。现场部署有限 | 现场生产部署 |
| **智能体物理安全标准**（RoboGuard 等） | 🔵 Research | ISO 只管物理，缺乏 LLM 语义风险标准 | 标准化进展 |
| **AgentCore Payments / Agent Registry（首尔）** | 🟡 Preview/未提供 | 首尔区域未提供（东京 Agent Registry ✅） | 首尔区域扩展 |

## ⚰️ 已废弃 — 禁止提议（存档保留）

| 条目 | 状态 | 替代 |
|---|---|---|
| **AWS RoboMaker** | 🔴 终止 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **SageMaker Edge Manager** | 🔴 终止 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **IoT Greengrass V1** | 🔴 终止 (2026-06-01) `[1]` | Greengrass V2 |
| **Gazebo Classic 11** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 无公开案例 `[4]` | 当前为 CUDA/NVIDIA（提议时明示风险） |

> ⚠️ **传闻警戒（并非事实）**: "AWS IoT TwinMaker 废弃"是**误信息** —— TwinMaker 是 GA·对新客户开放（低速度）。是与 SiteWise 维护混淆的第三方博客主张。禁止重复。→ [pillar-3](pillar-3.md)。

---

## 晋升流程（摘要）

1. **捕获**: 用指定频道/表情收集候选
2. **过滤**: 应用 [2.5 门禁](maintenance.md#纳入标准-the-filter)（4 项中 2 项以上）
3. **通过时**: 由负责的支柱 owner 用[标准模板](maintenance.md#标准模板)编入，并从 Radar 移除
4. **未达时**: 在此保留一句话，明示晋升条件

完整管道 → [maintenance](maintenance.md#slack--playbook-晋升管道)。

---
_owner: 待定 ⚠️ · updated: 2026-07 · volatility: 高（Radar 本质上快速变化 —— 建议月度评审）_
