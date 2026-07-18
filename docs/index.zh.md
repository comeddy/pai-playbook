---
ko_hash: 969975d261010e3f546159b61168181016c9d474
---
# Physical AI Playbook — AWS Korea SA

_最终更新: 2026-07 · owner: 待定 ⚠️ · 状态: 初期构建中_

> **L0 TL;DR**: 当客户抛出 Physical AI 问题时，无需翻查 Slack，**仅凭这一份 playbook 就能在 5 分钟内**给出架构方向、AWS 映射与后续行动的参考资产。它既不是论文摘要集，也不是新闻归档。

---

## 如何阅读本文档（30 秒）

1. **赶时间**：直接跳到下方 [常见问题 Top 10](#常见问题-top-10) 中对应的条目。
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
| 1 | **数据采集 & 处理** | 机器人学习的瓶颈不是模型而是数据 —— 如何用 AWS 管道处理遥操作、开放数据集与合成数据 | [pillar-1](pillar-1.md) |
| 2 | **模型训练 (VLA)** | 如何从 GPU 规模、以及是微调还是预训练入手，来设计 VLA/机器人基础模型的训练 | [pillar-2](pillar-2.md) |
| 3 | **仿真** | Isaac Sim/Lab vs 开源的选择，以及在 AWS 上运行大规模并行仿真的模式 | [pillar-3](pillar-3.md) |
| 4 | **Sim-to-Real** | 将仿真中训练的策略迁移到真实机体的经过验证的方法论，以及边缘推理的部署路径 | [pillar-4](pillar-4.md) |
| 5 | **智能体编排** | LLM 规划器（System 2）指挥机器人控制器（System 1）与机群的层 —— 以 Bedrock AgentCore 为中心 | [pillar-5](pillar-5.md) |

> 各支柱之间权重均等。每个支柱内部按 **客户实际需求 × production-readiness** 排序，顶部有"本支柱中客户最常问的问题 Top 3"。

---

## 常见问题 Top 10

<!-- ⚠️ 初期种子: 需用 SA 实际咨询记录替换/重新排序。支柱页面生成后需将链接收紧到章节锚点。 -->

| # | 问题 | 前往何处 |
|---|---|---|
| 1 | "Isaac Sim / Isaac Lab 在 AWS 上怎么跑？" | [pillar-3](pillar-3.md) |
| 2 | "VLA 模型训练（微调）的基础设施该怎么搭？" | [pillar-2](pillar-2.md) |
| 3 | "GPU 拿不到 —— On-Demand、Capacity Blocks、替代方案中该用哪个？" | [decisions](decisions.md) |
| 4 | "sim-to-real gap 实际上怎么克服？有经过验证的方法吗？" | [pillar-4](pillar-4.md) |
| 5 | "机器人实时控制（30–100Hz），推理能放到云上吗？" | [decisions](decisions.md) |
| 6 | "基础模型（GR00T/π0 等）是微调好，还是自行训练好？" | [decisions](decisions.md) |
| 7 | "机器人学习数据怎么采集、该存到哪里？（遥操作/合成数据）" | [pillar-1](pillar-1.md) |
| 8 | "对 NVIDIA 全栈的依赖有多深？开源替代方案呢？" | [decisions](decisions.md) |
| 9 | "边缘部署（Jetson 等）与 AWS 怎么连接？" | [pillar-4](pillar-4.md) |
| 10 | "用 LLM 智能体指挥机器人/设备的架构实际可行吗？" | [pillar-5](pillar-5.md) |

---

## 页面列表

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
- **止于概念说明的条目**: 每个条目都以"➡️ SA 后续行动"结尾。没有行动就是未完成。

---

_owner: 待定 ⚠️ · updated: 2026-07 · volatility: 低（结构性页面 —— 仅 FAQ Top 10 排名按季度复核）_
