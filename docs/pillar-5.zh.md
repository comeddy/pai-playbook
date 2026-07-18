---
ko_hash: 80b7b2fd7ad0574df30285a2af0e3ae1450c3213
---
# Pillar 5 — 智能体编排 (Agentic Orchestration)

_最终更新: 2026-07 · owner: comeddy · volatility: 高（AgentCore 功能·区域经常扩展）_
_除非另有标注，各条目继承页面元数据（owner/updated/volatility）。按条目指定 owner 时在条目页脚补充。_
[← 返回 index](index.md)

> **L0 TL;DR**: LLM 智能体指挥机器人·设备的层。这里是 **AWS 最强的支柱** —— **Amazon Bedrock AgentCore 已 GA(2025-10) 且首尔区域完全支持**，实时拦截工具调用的 **Policy(Cedar) 也已 GA(2026-03)**。结构上以 **System 2（慢速 LLM 规划器，云）+ System 1（快速控制，边缘）** 分离为正统。⚠️ Amazon DeepFleet 不是"LLM 智能体"，而是仓库机器人协调的基础模型，切勿混淆。

---

## 本支柱中客户最常问的问题 Top 3

1. **"用 LLM 智能体指挥机器人/设备实际可行吗？AWS 上有什么？"** → [Bedrock AgentCore](#1-amazon-bedrock-agentcore--ga)
2. **"实时机器人上怎么用智能体？能在边缘离线运行吗？"** → [边缘智能体编排](#3-边缘智能体编排--preview参考架构)
3. **"智能体控制物理系统时，安全怎么保证？"** → [安全 & 护栏](#5-安全--护栏--ga智能体层--未解决物理-语义-gap)

> **稳定原理（几乎不变）**: 智能体不"直接实时控制"机器人。**高层规划·工具选择(System 2) 由智能体承担，低层实时控制(System 1) 由边缘策略承担**（→ [pillar-2](pillar-2.md)、[pillar-4](pillar-4.md)）。生产中真正跑起来的是 (1) **仓库机群协调**(DeepFleet, CoEvolution) 与 (2) **开发/数据工作负载编排**(OSMO)，而人形全栈智能体或 MCP-机器人连接大多为研究/演示。

---

## 1. Amazon Bedrock AgentCore  🟢 GA

**L0 TL;DR**: 面向生产智能体的托管栈 —— Runtime、Memory、Gateway（工具连接）、Identity、Observability，以及 **Policy（基于 Cedar 的实时工具调用门禁）**。**首尔区域完全支持**。框架免费，仅按资源用量计费。

**客户需求/问题**: "想把智能体从 PoC 推进到生产。不想每次都自己搭建会话管理、工具连接、权限·安全、可观测性。"

**解决方案概览** `[1]`:
- **GA 历程**: 预览 2025-07 → **GA 2025-10-13**。组件: **Runtime、Memory、Gateway、Identity、Observability、Built-in Tools（Browser·Code Interpreter）**。re:Invent 2025-12 新增 Policy·Evaluations 预览、episodic Memory GA、面向语音的双向流式 Runtime GA。**Policy 于 2026-03-03 GA**。
- **Policy（核心）**: 与 Gateway 整合，**实时拦截所有 智能体→工具 调用**，以 ms 级评估策略(allow/deny)。用自然语言编写 → 编译为 **Cedar**（AWS 开源策略语言）。**含首尔在内 13 个区域 GA**。→ 约束物理系统工具调用的直接原语（第 5 项安全）。
- **Strands Agents SDK**（配套）: 模型·云中立的编排 SDK，**已达 1.0（GA 级）**。Amazon Q Developer·Glue 内部使用。与 AgentCore 配对。（版本·指标见折叠块）
- **Nova Act**（相关）: 浏览器/UI 自动化智能体，re:Invent 2025 **GA**。厂商声称高任务可靠性（数值见折叠块 —— 测量条件未公开）。

**AWS 映射**: 服务本身即映射。将机器人技能作为工具注册到 Gateway → 智能体以自然语言计划调用，用 Policy 门控，用 Memory 维持会话，用 Observability 追踪。

**决策标准**:
- 生产智能体（需要会话·工具·权限·可观测性）→ **AgentCore Runtime + Gateway + Policy**。
- 简单一次性推理 → 直接调用 Bedrock 即够，AgentCore 过重。
- 多智能体·A2A → Strands 1.0。
- 需要离线·低延迟边缘 → 第 3 项（边缘）。

**客户案例**: **AWS×SoftServe 自主生产线**(AgentCore + IoT Greengrass + Nova Pro + Jetson Thor) —— Hannover Messe 2026 **演示/展示**([1]/[3])。

**➡️ SA 后续行动**: 先让国内客户确认 **"AgentCore 在首尔区域 GA —— 无数据驻留问题"**（更正过时的"首尔不支持"信息），再提议把机器人技能注册为 Gateway 工具的 PoC。价格以"框架免费，仅按资源计费"来安心。

**🔗 相关资产**: [pillar-4 边缘](pillar-4.md) · （内部 AgentCore 研讨会 —— 需确认 ⚠️）

<details markdown="1"><summary>🔄 易变数据（组件·区域·价格 —— 2026-07 确认）</summary>

| 组件 | 状态 | 首尔 |
|---|---|---|
| Runtime / Memory / Gateway / Identity / Observability / Built-in Tools | 🟢 GA | ✅ |
| Policy (Cedar 工具门禁) | 🟢 GA (2026-03) | ✅ |
| Evaluations | 🟡 Preview→ | ✅ |
| Payments | 🟡 Preview | ❌ |
| Agent Registry | — | ❌（东京 ✅） |

**价格**: 框架免费，仅按资源。Runtime/Browser/Code Interpreter = $0.0895/vCPU-hr + $0.00945/GB-hr（按秒）。Gateway $0.005/1,000 次调用。Memory 短期 $0.25/1,000 事件，长期存储 $0.75/1,000 记录·月。
**区域**: 首尔(ap-northeast-2) 全部核心+Policy+Evaluations ✅。东京(ap-northeast-1) + Agent Registry ✅。（AWS 官方区域表 `[1]`，2026-07 直接确认）
**Strands**: Python 1.0(2026-05-21)、TS 1.0(2026-04-30)、~16.7M 下载/月(2026-06, `[3]`)。
**Nova Act**: "90%+ 任务可靠性" —— Amazon 公布数值，测量条件未公开(2025-12, `[3]`)。禁止无条件断言引用。
</details>

---

## 2. System 2 + System 1 编排模式  🟢 GA（稳定原理）

**L0 TL;DR**: 智能体编排的架构骨架。**重型 VLM/LLM 以 5~10Hz 规划·重规划(System 2)**，**轻量策略以 50~200Hz 执行(System 1)**。这种分离决定了"什么放云、什么放边缘"。

**客户需求/问题**: "大型推理模型和实时控制怎么放进一个系统？"

**解决方案概览** `[1]/[4]`: 从 SayCan/PaLM-E(2022~23 研究) 谱系演进。当前主导模式 = 高层规划器（任务分解·工具调用，慢）+ 低层动作策略（快）。示例数值（厂商公开，用于建立量级感）: Figure Helix S2 7~9Hz + S1 200Hz(Figure, 2025)、GR00T N1 S1 diffusion ~10ms(NVIDIA, 2025)。⚠️ **模式本身是标准，但全身人形全栈大多为试点/演示**。

**AWS 映射**: **System 2 = 云端 Bedrock AgentCore**（规划·工具编排·护栏），**System 1 = 边缘 Jetson**（实时控制，→ [pillar-4](pillar-4.md)）。能容忍延迟则 System 2 放云上，否则边缘板载。

**决策标准**: 参见 [decisions Cloud vs Edge](decisions.md)。实时控制回路 → 无条件边缘。规划·重规划 → 可放云/异步。

**客户案例**: Figure、GR00T（开放）。经过验证的生产环境有限。

**➡️ SA 后续行动**: 针对"智能体实时控制机器人吗？"的误解，**用"智能体做规划，实时控制交给边缘策略"来理清图示**。提出 AgentCore（规划）+ Jetson（控制）的组合。

**🔗 相关资产**: [pillar-2 VLA 结构](pillar-2.md) · [pillar-4 边缘](pillar-4.md) · [decisions](decisions.md)

---

## 3. 边缘智能体编排  🟡 Preview（参考架构）

**L0 TL;DR**: 在离线·低延迟现场把智能体部署到边缘设备的模式。AWS **Solutions Guidance("AI Agents to Device Fleets via IoT Greengrass")** 是真实存在的参考架构 —— 但**不是 GA 产品，而是指南/示例代码**。

**客户需求/问题**: "工厂离线/低带宽。想让智能体不依赖云也能在现场做判断。"

**解决方案概览** `[1]/[3]`: AWS Guidance = **在 IoT Greengrass 设备上部署 Strands Agents + 本地 SLM(Ollama)**。把 GGUF 模型推送到 S3，用 IoT Core MQTT 查询，Orchestrator Agent 向专门智能体（文档·OPC-UA 等）扇出。联网后切换到 Bedrock 云模型。目标行业明示含**机器人**。2026 模式: 训练模型 → 用 Greengrass 部署到 Jetson Thor，通过 VDA 5050 协议转换协调 AMR 机群。

**AWS 映射**: IoT Greengrass V2 + Strands + 本地 SLM(Ollama) + IoT Core(MQTT) + S3（模型）。在线时晋升到 Bedrock/AgentCore。

**决策标准**: 离线·数据主权·低延迟 → 边缘智能体。始终联网·复杂推理 → 云端 AgentCore。

**客户案例**: AWS×SoftServe（上方第 1 项，演示）。

**➡️ SA 后续行动**: 向离线客户**以 AWS Greengrass 智能体 Guidance + 示例代码作为起点**提出（诚实说明不是 GA 产品）。设计在线/离线混合（边缘 SLM ↔ 云端 AgentCore）。

**🔗 相关资产**: [pillar-4 边缘部署](pillar-4.md) · [pillar-1](pillar-1.md)

---

## 4. 机群编排  🟢 GA（部分）/ mixed

**L0 TL;DR**: 协调多个机器人的层。**真正的生产是仓库机群协调**(Amazon DeepFleet, CoEvolution) 与 **开发工作负载编排**(NVIDIA OSMO)。⚠️ DeepFleet 不是 LLM 智能体，而是多机器人协调基础模型。

**客户需求/问题**: "怎么从中央协调·监控数百~数千台机器人？"

**解决方案概览** `[1]/[3]`:
- **Amazon DeepFleet** 🟢 —— Amazon 仓库机器人机群协调的生成式基础模型（"交通管制"），移动时间效率提升 ~10%，与第 100 万台机器人一同公布(2025-07)。**生产（Amazon 内部）**。⚠️ **不是 LLM 智能体编排器** —— 是多机器人 RL 意义上的"多智能体"。禁止错误归类。
- **NVIDIA Isaac OSMO** 🟢 —— 机器人**开发/数据/训练工作负载**编排（合成数据·训练·RL·SIL）。GTC 2026 整合编码智能体(Claude Code/Codex/Cursor)。⚠️ **不是现场机器人机群的实时控制** —— 是开发管道编排。
- **Formant** 🟡 —— 机群管理 SaaS。在数百个组织中运行但规模较小（具体指标以 `[3]` PitchBook/Crunchbase 为准 —— 644 个组织·<$5M ARR, 2026-05, 变动频繁），未被收购。
- **CoEvolution** —— Lotte Global Logistics 417 家超级门店的多机群协调，声称 30% 效率（⚠️ 单一 [3] 来源，需再确认）。

**AWS 映射**: IoT Core/Greengrass（机群连接）+ AgentCore（编排逻辑）+ IoT FleetWise/SiteWise（遥测）。DeepFleet 式协调模型用 SageMaker 训练。

**决策标准**: 仓库/AMR 机群协调 → 已验证领域（参考 DeepFleet 式方法）。人形智能体机群 → 仍处早期。开发工作负载 → OSMO(NVIDIA) 或 AWS Batch/Step Functions。

**客户案例**（⚠️ 国内为早期/演示/公布）: **Lotte Global Logistics×CoEvolution**(30%，单一来源)、**LG CNS** 仓库演示（人形+机器狗+移动）、**Naver** AI Agent Platform 计划于 2026 下半年（NVIDIA 蓝图）。

**➡️ SA 后续行动**: 向机群客户**以"协调逻辑用 AgentCore，连接用 IoT，训练用 SageMaker"三层来梳理**。准确说明，避免把 DeepFleet 误解为 LLM 智能体。

**🔗 相关资产**: [pillar-2 训练](pillar-2.md) · [pillar-3 OSMO](pillar-3.md)

---

## 5. 安全 & 护栏  🟢 GA（智能体层）/ 🔵 未解决（物理-语义 gap）

**L0 TL;DR**: 智能体控制物理系统时，安全靠**分层防御**。**AgentCore Policy(Cedar) 门控 智能体→工具 调用**，机器人层则由 **ISO 确定性安全层**承担。⚠️ 现有标准(ISO) 只涵盖物理安全，**尚无覆盖 LLM 语义风险（幻觉·越狱）的标准** —— 诚实的开放问题。

**客户需求/问题**: "智能体判断错误导致机器人做出危险行为怎么办？怎么阻止？"

**解决方案概览** `[1]/[4]`:
- **智能体层（AWS 原生）**: **AgentCore Policy** —— 用 Cedar 实时 allow/deny 所有 智能体→工具 调用(ms)。约束物理动作工具调用的实用层。**Bedrock Guardrails** —— 过滤 LLM 输入输出（内容·主题·PII）（本身不是执行动作）。
- **机器人层（功能安全）**: **ISO 10218-1/2**（机器人·集成系统）、**ISO/TS 15066**（协作机器人）、**ISO 13482**（个人辅助机器人）。⚠️ 这些**只涉及物理安全** —— 不覆盖 LLM 语义滥用/幻觉。
- **研究**: RoboGuard（安全规则 grounding）、BadRobot（嵌入式 LLM 越狱攻击）、LLM 语义 DoS —— 🔵 研究阶段。标准无法连接功能安全(ISO) 与 LLM 风险的**开放 gap**。

**AWS 映射**: AgentCore Policy(Cedar) + Bedrock Guardrails（智能体层）+ 机器人板载确定性安全（依据 ISO，在 AWS 之外）。

**决策标准**: 物理动作智能体 → **必须分层防御**（用 AgentCore Policy 做工具门控 + 机器人板载 ISO 安全层）。仅靠任一方都不够。禁止"智能体会自己保证安全"。

**客户案例**: （生产安全案例为非公开/早期）

**➡️ SA 后续行动**: 对安全问题**提出"智能体层用 AgentCore Policy/Cedar 门控工具调用，机器人层用 ISO 确定性安全 —— 双重防御"**。诚实承认"LLM 语义风险标准尚不存在"，并以分层防御来补足的角度。

**🔗 相关资产**: [pillar-4 边缘](pillar-4.md) · （内部智能体安全指南 —— 新建需要 ⚠️）

---

## 本支柱的诚实现实（SA 必读）

- **AgentCore 首尔区域完全支持**（含 Policy·Evaluations）。"首尔不支持"是 GA 初期的说法 —— 现在已错。让客户对数据驻留放心。
- **Policy 已 GA(2026-03)** —— 不要称其为"预览"。
- **DeepFleet ≠ LLM 智能体编排器。** 是仓库机器人协调基础模型（多机器人 RL）。禁止错误归类。
- **真正的生产是机群协调(DeepFleet/CoEvolution) 与开发工作负载(OSMO)。** MCP-机器人连接与人形全栈智能体大多为研究/演示。
- **没有 LLM 语义安全标准。** ISO 只管物理。分层防御(Cedar Policy + ISO 机器人层) 才是诚实的答案。
- **Lotte 30% 等国内数值为单一来源** —— 硬引用前需再确认。

---
_owner: comeddy · updated: 2026-07 · volatility: 高（AgentCore 功能·区域在折叠块中管理）· sources: [1] 官方, [3] 厂商/press, [4] 研究/社区_
