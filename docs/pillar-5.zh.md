---
ko_hash: 301fcc497bdcab115a9021056c5f9f79cba38358
---
# Pillar 5 — 智能体编排 (Agentic Orchestration)

_最终更新: 2026-09 · owner: Youngjin · volatility: 高（AgentCore 功能·区域经常扩展）_
_除非另有标注，各条目继承页面元数据（owner/updated/volatility）。按条目指定 owner 时在条目页脚补充。_
[← 返回 index](index.md)

> **L0 TL;DR**: 区分业务规划、机器人技能调用、机群连接。按需选择 AgentCore 功能；控制、安全和数据处理位置需[单独验证](operations.md)。

---

> **复核范围**：页面修改日不代表所有技术条目已重验。核心修正日期、复现/人工状态见[证据](evidence.md)，旧条目仍使用各自确认日期。

## 本支柱中客户最常问的问题 Top 3

> 以下为探索问题示例，不是已验证的客户咨询频率排名。

1. **"用 LLM 智能体指挥机器人/设备实际可行吗？AWS 上有什么？"** → [Bedrock AgentCore](#1-amazon-bedrock-agentcore--ga)
2. **"实时机器人上怎么用智能体？能在边缘离线运行吗？"** → [边缘智能体编排](#3-边缘智能体编排--preview参考架构)
3. **"智能体控制物理系统时，安全怎么保证？"** → [安全 & 护栏](#5-安全--护栏--ga智能体层--未解决物理-语义-gap)

> **L0/L1**: 业务规划、观测策略、底层控制和独立安全职责不同。区分服务发布与客户现场验证。

---

## 1. Amazon Bedrock AgentCore  🟢 GA

**L0 TL;DR**: AgentCore 提供智能体运行、工具访问、身份与观测。**区分服务 GA 和机器人现场验证，以及首尔可用和韩国境内处理。**

| 组件 | 应评估的职责 | 限制 |
|---|---|---|
| Runtime | 业务规划智能体运行 | 不是保证机器人控制时限的实时控制器 |
| Gateway/Identity | 连接认证允许的机器人技能 API | 完成、取消、去重需另行实现 |
| Policy | 检查通过 Gateway 的工具调用策略 | 不替代物理状态检查及独立安全 |
| Memory/Evaluations | 上下文与评估 | 分别确认存储及推理处理地点 |
| Observability | 任务及工具追踪 | 需关联设备、控制、安全日志 |

**区域/数据修正** `[1]`：首尔可用不自动解决数据驻留。[AWS 跨区域推理文档](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html)说明 Memory 等输入输出可在主区域之外处理。首尔发起的 Evaluations 使用全球跨区域推理。按功能、模型、外部工具记录处理国家（[证据](evidence.md#agentcore-residency)）。

**决策标准**：单次推理先考虑直接模型调用，需要持续会话、工具权限、追踪时选择 AgentCore 组件。核对功能[区域表](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)及[价格](https://aws.amazon.com/bedrock/agentcore/pricing/)，计入模型/API、网络、日志费用。“harness 免费”不是总成本估算。

**客户案例**：已有 AWS×SoftServe 材料是演示展示，不证明客户生产线运营。

**➡️ 后续行动**：定义技能输入、权限、完成取消契约、数据处理路径，连接[运营恢复测试](operations.md)。

**🔗 相关资产**:

- Playbook: [pillar-4 边缘](pillar-4.md)
- [AgentCore 入门研讨会](https://catalog.workshops.aws/agentcore-getting-started/en-US) · [AgentCore Deep Dive 研讨会](https://catalog.workshops.aws/agentcore-deep-dive/en-US)
- [AgentCore 零售智能体研讨会 "Build! Deploy! Observe!"](https://catalog.us-east-1.prod.workshops.aws/workshops/3cab1e1f-1dfa-42e0-959c-6e2e0a072ea3/ko-KR) —— 韩语。虽以零售场景为例，但以三阶段动手实验覆盖 AgentCore 全部 7 个服务（Gateway·Runtime·Observability·Code Interpreter·Memory·Policy·Browser）—— Policy 护栏·升级规则实验与第 5 项（安全 & 护栏）相衔接。指南: [研讨会站点](https://dxdbmmdwak6t8.cloudfront.net/)（面向活动的 CloudFront 部署 —— 链接持久性待确认 ⚠️）
- （内部 AgentCore 研讨会 —— 需确认 ⚠️）
- [AWS Physical AI Toolchain](https://github.com/aws-samples/sample-aws-physical-ai-toolchain) —— aws-samples。4 支柱飞轮参考架构。⚠️ 目前仅 NVIDIA OSMO 6.3 on EKS 编排为 Available，Cosmos·Isaac Lab·GR00T·Strands+AgentCore 智能体层均为 Planned
- [Self-improving Physical AI](https://github.com/aws-samples/sample-self-improving-physical-AI) —— aws-samples。Bedrock 智能体通过 IoT 控制 Isaac Sim 与实体机器人 SO-ARM101/XGO2/Zumi，借助智能体记忆进行 sim-to-real 迭代学习
- [Agentic AI Robot — 工业安全监控](https://github.com/aws-samples/sample-agentic-ai-robot) —— aws-samples。AgentCore+IoT+机器人自主巡逻·边缘推理演示，曾在 AWS AI x Industry Week 2025 展示，含韩语 README。⚠️ 明确标注为实验·教育用途 —— 非生产环境
- [Smart Machines — 工业设备混合 Physical AI](https://github.com/aws-samples/sample-smart-machines-physical-hybrid-ai) —— aws-samples。智能体完成机群遥测异常检测→根因诊断→建单·调整设备参数的全栈演示（多智能体对话·自然语言场景构建器·KVS 视频→Bedrock 分析·Jetson YOLOWorld+VLM 边缘监控）。⚠️ README 明示为演示 —— 目前仅挖掘机（模拟遥测）完整可用，机械臂为 WIP

---

## 2. 业务规划与机器人控制分离 { #2-system-2--system-1-编排模式--ga稳定原理 }

**L0 TL;DR**: 区分业务规划智能体、机器人执行、控制及安全，不将其等同于模型内部 System 1/2。

**部署**：先定义可接受的云延迟、断网时间及处理国家，再按时限和风险评估部署观测策略、本地控制、独立安全。Helix 两个模型都在板载，见 [P2](pillar-2.md)及[证据](evidence.md#action-chunking)。

**AWS 映射**：AgentCore 是满足条件的业务规划选项。技能调用需 ID、过期、前置条件及完成检查，action chunking 本身不解决网络延迟和安全。

**➡️ 后续行动**：使用[运营](operations.md)的四层图和故障表设计负责人、取消及恢复。

**🔗 相关资产**: [pillar-2 VLA 结构](pillar-2.md) · [pillar-4 边缘](pillar-4.md) · [decisions](decisions.md)

---

## 3. 边缘智能体编排  🟡 Preview（参考架构）

**L0 TL;DR**: 在离线·低延迟现场把智能体部署到边缘设备的模式。AWS **Solutions Guidance("AI Agents to Device Fleets via IoT Greengrass")** 是真实存在的参考架构 —— 但**不是 GA 产品，而是指南/示例代码**。

**客户需求/问题**: "工厂离线/低带宽。想让智能体不依赖云也能在现场做判断。"

**解决方案概览** `[1]/[3]`: AWS Guidance = **在 [IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) 设备上部署 Strands Agents + 本地 SLM([Ollama](https://ollama.com/))**。把 GGUF 模型推送到 S3，用 IoT Core MQTT 查询，Orchestrator Agent 向专门智能体（文档·OPC-UA 等）扇出。联网后切换到 Bedrock 云模型。目标行业明示含**机器人**。2026 模式: 训练模型 → 用 Greengrass 部署到 Jetson Thor，通过 VDA 5050 协议转换协调 AMR 机群。

**AWS 映射**: IoT Greengrass V2 + Strands + 本地 SLM(Ollama) + IoT Core(MQTT) + S3（模型）。在线时晋升到 Bedrock/AgentCore。

**决策标准**: 离线·数据主权·低延迟 → 边缘智能体。始终联网·复杂推理 → 云端 AgentCore。

**客户案例**: AWS×SoftServe（上方第 1 项，演示）。

**➡️ 后续行动**: 向离线客户**以 AWS Greengrass 智能体 Guidance + 示例代码作为起点**提出（诚实说明不是 GA 产品）。设计在线/离线混合（边缘 SLM ↔ 云端 AgentCore）。

**🔗 相关资产**: [pillar-4 边缘部署](pillar-4.md) · [pillar-1](pillar-1.md) · [MCP+MQTT on AWS IoT Core 模式](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/) —— 官方博客。在 IoT Core(MQTT) 上把机器人·边缘设备当作 MCP 工具来驱动 Physical AI 智能体的实战模式 —— 连接边缘运营(P4)与多设备协调(P5)的现行标准路径

---

## 4. 机群运营 — 产品、控制与云的边界 { #4-机群编排--ga部分-mixed }

**L0 TL;DR**: 现场任务/交通协调、设备运营、开发任务调度是不同问题。按需求比较机群产品、SI 和自研逻辑。

**参考范围**：[Amazon DeepFleet](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) 是 Amazon 内部协调案例，不是客户可购买的 AgentCore 功能 `[3]`。[NVIDIA OSMO](https://developer.nvidia.com/osmo) 调度开发/数据/训练工作负载，不是现场交通控制。

**AWS 映射**：设计 IoT Core/Greengrass 连接状态采集及所需存储分析。仅在业务规划需要智能体时考虑 AgentCore。明确机器人/机群方案的避碰、任务分配、离线恢复职责。

**FleetWise 修正** `[1]`：[AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html) **不接受新客户**。现有客户可继续使用，但不作为新机器人架构的默认方案（[证据](evidence.md#fleetwise-new-customers)）。

**客户案例**：[Certis 巡逻机器人](https://aws.amazon.com/blogs/physical-ai/how-certis-achieved-autonomous-robot-security-patrols-with-aws/) 是 AWS 公开案例，不保证其他客户获得相同结果。

**➡️ 后续行动**：在[试点卡](start.md#pilot)记录产品边界、完成、断网、介入、恢复要求，执行[故障测试](operations.md#failure)。

**🔗 相关资产**: [pillar-2 训练](pillar-2.md) · [pillar-3 OSMO](pillar-3.md)

---

## 5. 安全 & 护栏  🟢 GA（智能体层）/ 🔵 未解决（物理-语义 gap）

**L0 TL;DR**: 智能体控制物理系统时，安全靠**分层防御**。**AgentCore Policy(Cedar) 门控 智能体→工具 调用**，机器人层则由 **ISO 确定性安全层**承担。⚠️ 现有标准(ISO) 只涵盖物理安全，**尚无覆盖 LLM 语义风险（幻觉·越狱）的标准** —— 诚实的开放问题。

**客户需求/问题**: "智能体判断错误导致机器人做出危险行为怎么办？怎么阻止？"

**解决方案概览** `[1]/[4]`:

- **智能体层（AWS 原生）**: **AgentCore Policy** —— 用 Cedar 实时 allow/deny 所有 智能体→工具 调用(ms)。约束物理动作工具调用的实用层。**[Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)** —— 过滤 LLM 输入输出（内容·主题·PII）（本身不是执行动作）。
- **机器人层（功能安全）**: **[ISO 10218-1/2](https://www.iso.org/standard/73933.html)**（机器人·集成系统）、**ISO/TS 15066**（协作机器人）、**ISO 13482**（个人辅助机器人）。⚠️ 这些**只涉及物理安全** —— 不覆盖 LLM 语义滥用/幻觉。
- **研究**: RoboGuard（安全规则 grounding）、BadRobot（嵌入式 LLM 越狱攻击）、LLM 语义 DoS —— 🔵 研究阶段。标准无法连接功能安全(ISO) 与 LLM 风险的**开放 gap**。

**AWS 映射**: AgentCore Policy(Cedar) + Bedrock Guardrails（智能体层）+ 机器人板载确定性安全（依据 ISO，在 AWS 之外）。

**决策标准**: 物理动作智能体 → **必须分层防御**（用 AgentCore Policy 做工具门控 + 机器人板载 ISO 安全层）。仅靠任一方都不够。禁止"智能体会自己保证安全"。

**客户案例**: （生产安全案例为非公开/早期）

**➡️ 后续行动**: 对安全问题**提出"智能体层用 AgentCore Policy/Cedar 门控工具调用，机器人层用 ISO 确定性安全 —— 双重防御"**。诚实承认"LLM 语义风险标准尚不存在"，并以分层防御来补足的角度。

**🔗 相关资产**: [pillar-4 边缘](pillar-4.md) · （内部智能体安全指南 —— 新建需要 ⚠️）

---

## 6. 物理世界的智能体标准 — Anthropic MHS & AWS Strands Robots  🟡 Research Preview

**L0 TL;DR**: 2026-08-27 Anthropic 公开了 **[Model Hardware Standard(MHS)](https://www.anthropic.com/news/model-hardware-standard-research-preview)** research preview —— 让 AI 智能体通过**标准化驱动（read/write primitive）**操作物理设备（显微镜·liquid handler·机械臂）并并行编排多台设备的共享规格。相当于 MCP 之于数据·工具的硬件版。**AWS 通过 Strands Robots 支持 MHS**（面向 preview 参与者的 private pre-release），**Doosan Robotics（韩国）为发布合作伙伴**。⚠️ research preview —— 禁止向客户做生产提议，仅作方向指标。

**客户需求/问题**: "每台设备都在重复定制集成（数周~数月）。智能体-硬件连接没有标准吗？"

**解决方案概览** `[1]/[3]`:

- **工作方式**: 将设备暴露为 read（例: get temperature）/write（set temperature）primitive 集合的**标准驱动** + 由自然语言标签生成的 reference file（记载该设备可测量·可调整的项目与**强制执行的安全限值（safety limits）**）。智能体通过三种机制（MCP·CLI·code files/API）控制设备，编排步骤、观测结果并实时调整参数。model-agnostic —— 核心主张是把集成周期从数周~数月缩短到数小时~数分钟。
- **AWS 的位置**: Anthropic 公告明示 "AWS will support MHS through **Strands Robots**, the library for connecting AI agents to physical devices"。它与公开的 [strands-labs/robots](https://github.com/strands-labs/robots)（Apache-2.0 —— Strands Agents + GR00T VLA + LeRobot 整合机器人控制库）相衔接，但 ⚠️ **公开包本身并未提及 MHS** —— 支持 MHS 的构建是单独的 private pre-release。
- **韩国相关性** `[3]`: Doosan Robotics 作为发布合作伙伴，正在机械臂的自动质检（QA）·多机器人协作上测试 MHS（与 Universal Robots·Tecan·QIAGEN 等一道）。
- **诚实的局限**: LLM 通过文本·图像学习物理世界，**空间·物理推理仍需专家监督** —— Anthropic 自己举例: Genentech 研究人员不得不教 Claude "样品起泡（foaming）不是软件 bug 而是物理失败"。已计划开源。

**AWS 映射**: AgentCore（第 1 节）负责智能体运行时·Policy 门控，MHS/Strands Robots 负责设备连接标准 —— 相当于在第 5 节分层防御的"工具门禁"之下再加一层**"设备驱动 + safety limits"**。

**决策标准**: 还不到写进今天设计的阶段（research preview）。但对设备集成积压大的客户（实验室自动化·多品种单元），应作为**观察清单第一位**进行引导。

**客户案例**: Doosan Robotics（发布合作伙伴，测试阶段）`[3]`。

**➡️ 后续行动**: 向已在用 MCP 的客户以 **"MCP 管数据·工具，MHS 管硬件"** 的框架介绍；一旦公开，就以 Strands Robots 路径安排验证 PoC。在那之前的现行替代方案是 [MCP+MQTT on IoT Core 模式](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/)（第 3 节相关资产）。

**🔗 相关资产**: [strands-labs/robots](https://github.com/strands-labs/robots) · [pillar-4 边缘](pillar-4.md)

---

## 本支柱的诚实现实（SA 必读）

- **区分首尔可用和处理地点。** 按功能、模型、路径检查[跨区域推理](evidence.md#agentcore-residency)。
- **Policy 已 GA(2026-03)** —— 不要称其为"预览"。
- **DeepFleet ≠ LLM 智能体编排器。** 是仓库机器人协调基础模型（多机器人 RL）。禁止错误归类。
- **真正的生产是机群协调(DeepFleet/CoEvolution) 与开发工作负载(OSMO)。** MCP-机器人连接与人形全栈智能体大多为研究/演示。
- **没有 LLM 语义安全标准。** ISO 只管物理。分层防御(Cedar Policy + ISO 机器人层) 才是诚实的答案。
- **Lotte 30% 等韩国数值为单一来源** —— 硬引用前需再确认。

---
_owner: Youngjin · updated: 2026-09 · volatility: 高（AgentCore 功能·区域在折叠块中管理）· sources: [1] 官方, [3] 厂商/press, [4] 研究/社区_

<!-- 용어 각주 -->
