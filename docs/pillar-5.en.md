---
ko_hash: 301fcc497bdcab115a9021056c5f9f79cba38358
---
# Pillar 5 — Agentic Orchestration

_Last updated: 2026-09 · owner: Youngjin · volatility: high (AgentCore features/regions expand often)_
_Unless separately noted, each item inherits the page metadata (owner/updated/volatility). When an item has its own owner, add an item footer._
[← back to index](index.md)

> **L0 TL;DR**: Separate business planning, robot skill calls, and fleet connectivity requirements. Use AgentCore selectively for needed agent functions; [validate control, safety, and data-processing locations separately](operations.md).

---

> **Review scope**: the page edit date does not revalidate every technical item. See [Evidence](evidence.md) for core corrections, check dates, and reproduction/human review status; legacy item dates still apply.

## Top 3 questions customers ask most in this pillar

> These are discovery examples, not a measured ranking of customer inquiries.

1. **"Does directing robots/equipment with an LLM agent actually work? What does AWS have?"** → [Bedrock AgentCore](#1-amazon-bedrock-agentcore--ga)
2. **"How do you put an agent on a real-time robot? Even offline at the edge?"** → [Edge agentic orchestration](#3-edge-agentic-orchestration--preview-reference-architecture)
3. **"When an agent controls a physical system, how is safety guaranteed?"** → [Safety & guardrails](#5-safety--guardrails--ga-agent-layer---unsolved-physical-semantic-gap)

> **L0/L1**: Business planning, observation-based policies, low-level control, and independent safety are separate responsibilities. Distinguish service release from customer-site validation.

---

## 1. Amazon Bedrock AgentCore  🟢 GA

**L0 TL;DR**: AgentCore provides agent execution, tool access, identity, and observability. **Separate service GA from robot-site validation, and Seoul availability from Korea-only processing.**

| Component | Role to assess | Limit |
|---|---|---|
| Runtime | Business-planning agent execution | Not a real-time robot controller |
| Gateway/Identity | Connect/authenticate permitted robot skill APIs | Completion, cancellation, and deduplication need implementation |
| Policy | Policy checks for tool calls through Gateway | Does not replace physical-state checks or independent safety |
| Memory/Evaluations | Context and evaluation | Check storage and inference processing separately |
| Observability | Trace tasks/tool calls | Correlate with device/control/safety logs |

**Region/data correction** `[1]`: Seoul availability alone does not settle data residency. [AWS cross-region inference documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html) states Memory and other inputs/outputs may be processed outside the primary Region. Seoul-origin Evaluations uses global cross-region inference. Record processing countries per feature, model, and external tool ([evidence](evidence.md#agentcore-residency)).

**Decision criteria**: consider direct model calls for single inference. Select AgentCore components when persistent sessions, tool permissions, or tracing are needed. Check feature-specific [Regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) and [pricing](https://aws.amazon.com/bedrock/agentcore/pricing/), including model/API, network, and log costs. “Free harness” is not a total-cost estimate.

**Customer case**: the existing AWS/SoftServe reference is a demo/showcase, not proof of customer production-line operation.

**➡️ Next action**: define robot skill inputs, permissions, completion/cancellation, and processing routes; connect [operations/recovery tests](operations.md).

**🔗 Related assets**:

- Playbook: [pillar-4 edge](pillar-4.md)
- [Getting started with AgentCore workshop](https://catalog.workshops.aws/agentcore-getting-started/en-US) · [AgentCore Deep Dive workshop](https://catalog.workshops.aws/agentcore-deep-dive/en-US)
- [AgentCore retail agent workshop "Build! Deploy! Observe!"](https://catalog.us-east-1.prod.workshops.aws/workshops/3cab1e1f-1dfa-42e0-959c-6e2e0a072ea3/ko-KR) — Korean. Retail-domain examples, but covers all seven AgentCore services (Gateway · Runtime · Observability · Code Interpreter · Memory · Policy · Browser) in a three-phase hands-on — the Policy guardrail/escalation lab connects to item 5 (Safety & guardrails). Guide: [workshop site](https://dxdbmmdwak6t8.cloudfront.net/) (event-scoped CloudFront deployment — link persistence unconfirmed ⚠️)
- (internal AgentCore workshop — confirm needed ⚠️)
- [AWS Physical AI Toolchain](https://github.com/aws-samples/sample-aws-physical-ai-toolchain) — aws-samples. 4-pillar flywheel reference architecture. ⚠️ Only NVIDIA OSMO 6.3 on EKS orchestration is Available; Cosmos·Isaac Lab·GR00T·Strands+AgentCore agentic layer are Planned
- [Self-improving Physical AI](https://github.com/aws-samples/sample-self-improving-physical-AI) — aws-samples. Bedrock agents control Isaac Sim and real robots SO-ARM101/XGO2/Zumi via IoT, iterative sim-to-real learning with agent memory
- [Agentic AI Robot — industrial safety monitoring](https://github.com/aws-samples/sample-agentic-ai-robot) — aws-samples. AgentCore+IoT+robot autonomous patrol and edge inference demo, shown at AWS AI x Industry Week 2025, Korean README. ⚠️ Explicitly experimental/educational — not for production
- [Smart Machines — hybrid Physical AI for industrial equipment](https://github.com/aws-samples/sample-smart-machines-physical-hybrid-ai) — aws-samples. Full-stack demo where agents detect fleet telemetry anomalies → diagnose root causes → create tickets and adjust machine parameters (multi-agent chat, natural-language scenario builder, KVS video → Bedrock analysis, Jetson YOLOWorld+VLM edge monitoring). ⚠️ README-stated demo — only excavators (simulated telemetry) fully work today; robot arms are WIP

---

## 2. Separate business planning and robot control { #2-system-2--system-1-orchestration-pattern--ga-stable-principle }

**L0 TL;DR**: Separate business-planning agents from robot execution, control, and safety without treating this as a model's internal System 1/2 split.

**Placement**: first set allowable cloud delay, outage duration, and processing countries. Place observation-based policies, local control, and independent safety according to deadlines/risk assessment. Both Helix models are onboard; see [P2](pillar-2.md) and [evidence](evidence.md#action-chunking).

**AWS mapping**: AgentCore is an option for eligible business planning. Skill calls need IDs, expiry, preconditions, and completion checks. Action chunking alone solves neither network latency nor safety.

**➡️ Next action**: use the four-layer diagram and failure matrix in [Operations](operations.md) to assign ownership, cancellation, and recovery.

**🔗 Related assets**: [pillar-2 VLA structure](pillar-2.md) · [pillar-4 edge](pillar-4.md) · [decisions](decisions.md)

---

## 3. Edge agentic orchestration  🟡 Preview (reference architecture)

**L0 TL;DR**: A pattern for deploying agents to edge devices in offline/low-latency field settings. AWS's **Solutions Guidance ("AI Agents to Device Fleets via IoT Greengrass")** is a real reference architecture — but it is **guidance/sample code, not a GA product**.

**Customer need/problem**: "The factory is offline/low-bandwidth. We want the agent to make decisions in the field even without the cloud."

**Solution overview** `[1]/[3]`: The AWS Guidance = deploy **Strands Agents + a local SLM ([Ollama](https://ollama.com/)) to [IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) devices**. Push a GGUF model to S3, query over IoT Core MQTT, and an Orchestrator Agent fans out to specialist agents (documents, OPC-UA, etc.). When connected, switch to a Bedrock cloud model. **Robotics** is explicitly listed among target industries. 2026 pattern: trained model → deployed to Jetson Thor via Greengrass, coordinating AMR fleets via VDA 5050 protocol conversion.

**AWS mapping**: IoT Greengrass V2 + Strands + local SLM (Ollama) + IoT Core (MQTT) + S3 (models). When online, promote to Bedrock/AgentCore.

**Decision criteria**: offline · data sovereignty · low latency → edge agent. Always-connected · complex reasoning → cloud AgentCore.

**Customer case**: AWS×SoftServe (item 1 above, demo).

**➡️ Next action**: for offline customers, **present the AWS Greengrass agent Guidance + sample code as a starting point** (honestly, not a GA product). Design an on/offline hybrid (edge SLM ↔ cloud AgentCore).

**🔗 Related assets**: [pillar-4 edge deployment](pillar-4.md) · [pillar-1](pillar-1.md) · [MCP+MQTT on AWS IoT Core pattern](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/) — official blog. A practical pattern weaving Physical AI agents that treat robots/edge devices like MCP tools on top of IoT Core (MQTT) — the current standard path linking edge operations (P4) and multi-device coordination (P5)

---

## 4. Fleet operations — product, control, and cloud boundaries { #4-fleet-orchestration--ga-partly--mixed }

**L0 TL;DR**: Fleet task/traffic coordination, device operations, and development-job scheduling are different problems. Compare fleet products, SI, and custom logic against requirements.

**Reference scope**: [Amazon DeepFleet](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) is an internal Amazon coordination case, not a customer-purchasable AgentCore feature `[3]`. [NVIDIA OSMO](https://developer.nvidia.com/osmo) schedules development/data/training workloads, not site traffic.

**AWS mapping**: design IoT Core/Greengrass connectivity/state collection and needed storage/analytics. Consider AgentCore only when business planning needs an agent. Assign collision avoidance, task allocation, and offline recovery to defined robot/fleet solution responsibilities.

**FleetWise correction** `[1]`: [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html) is **closed to new customers**. Existing customers may continue, but it is not a default for new robot architectures ([evidence](evidence.md#fleetwise-new-customers)).

**Customer case**: [Certis patrol robots](https://aws.amazon.com/blogs/physical-ai/how-certis-achieved-autonomous-robot-security-patrols-with-aws/) is a public AWS case, not a guarantee of equivalent outcomes elsewhere.

**➡️ Next action**: record product boundaries, completion, outages, intervention, and recovery in the [pilot card](start.md#pilot); perform [failure tests](operations.md#failure).

**🔗 Related assets**: [pillar-2 training](pillar-2.md) · [pillar-3 OSMO](pillar-3.md)

---

## 5. Safety & guardrails  🟢 GA (agent layer) / 🔵 unsolved (physical-semantic gap)

**L0 TL;DR**: When an agent controls a physical system, safety is by **layered defense**. **AgentCore Policy (Cedar) gates agent→tool calls**, and the robot layer is handled by an **ISO deterministic safety layer**. ⚠️ Existing standards (ISO) cover physical safety only, and **there is not yet a standard covering LLM semantic risk (hallucination/jailbreak)** — an honest open problem.

**Customer need/problem**: "What if the agent misjudges and the robot takes a dangerous action? How do we prevent it?"

**Solution overview** `[1]/[4]`:

- **Agent layer (AWS-native)**: **AgentCore Policy** — real-time allow/deny (ms) via Cedar on each agent→tool call through Gateway. A practical layer for constraining physical-action tool calls. **[Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)** — filters LLM input/output (content · topic · PII) (not the actuation itself).
- **Robot layer (functional safety)**: **[ISO 10218-1/2](https://www.iso.org/standard/73933.html)** (robots · integrated systems), **ISO/TS 15066** (collaborative robots), **ISO 13482** (personal care robots). ⚠️ These cover **physical safety only** — LLM semantic misuse/hallucination is not covered.
- **Research**: RoboGuard (safety-rule grounding), BadRobot (embedded-LLM jailbreak attacks), LLM semantic DoS — 🔵 research stage. An **open gap** where standards don't bridge functional safety (ISO) and LLM risk.

**AWS mapping**: AgentCore Policy (Cedar) + Bedrock Guardrails (agent layer) + robot on-board deterministic safety (ISO-conformant, outside AWS).

**Decision criteria**: physical-action agent → **layered defense is mandatory** (tool gating with AgentCore Policy + on-board robot ISO safety layer). Either alone is insufficient. "The agent will keep itself safe" is forbidden.

**Customer case**: (production safety cases are undisclosed/early)

**➡️ Next action**: for safety questions, present **"the agent layer gates tool calls with AgentCore Policy/Cedar, the robot layer has ISO deterministic safety — double defense."** Honestly acknowledge "there's no standard for LLM semantic risk yet," and take the angle of complementing it with layered defense.

**🔗 Related assets**: [pillar-4 edge](pillar-4.md) · (internal agent safety guide — newly needed ⚠️)

---

## 6. Agent standards for the physical world — Anthropic MHS & AWS Strands Robots  🟡 Research Preview

**L0 TL;DR**: On 2026-08-27 Anthropic opened the research preview of the **[Model Hardware Standard (MHS)](https://www.anthropic.com/news/model-hardware-standard-research-preview)** — a shared specification that lets AI agents operate physical devices (microscopes, liquid handlers, robot arms) through a **standardized driver (read/write primitives)** and orchestrate many devices in parallel. The hardware counterpart to what MCP did for data and tools. **AWS supports MHS through Strands Robots** (a private pre-release for preview participants), and **Doosan Robotics (Korea) is a launch partner**. ⚠️ Research preview — do not propose for customer production; directional indicator only.

**Customer need/problem**: "We keep repeating bespoke integration (weeks~months) per device. Is there no standard for agent-hardware connection?"

**Solution overview** `[1]/[3]`:

- **How it works**: a **standard driver** exposing each device as a set of read (e.g., get temperature) / write (set temperature) primitives, plus a reference file generated from natural-language tags (listing what the device can measure/adjust and the **enforced safety limits**). The agent controls hardware through three mechanisms (MCP · CLI · code files/APIs), sequencing steps, monitoring results, and adjusting parameters in real time. Model-agnostic — the core claim is that integration drops from weeks~months to hours~minutes.
- **AWS's place**: the Anthropic announcement states "AWS will support MHS through **Strands Robots**, the library for connecting AI agents to physical devices." It connects to the public [strands-labs/robots](https://github.com/strands-labs/robots) (Apache-2.0 — a robot-control library integrating Strands Agents + GR00T VLA + LeRobot), but ⚠️ **the public package itself does not mention MHS** — the MHS-enabled build is a separate private pre-release.
- **Korean relevance** `[3]`: Doosan Robotics is a launch partner, testing MHS for automated quality inspection (QA) on robot arms and multi-robot coordination (alongside Universal Robots, Tecan, QIAGEN, and others).
- **Honest limits**: LLMs learn the physical world through text and images, so **spatial/physical reasoning still needs expert supervision** — Anthropic itself cites Genentech researchers having to teach Claude that "sample foaming is a physical failure, not a software bug." Open-sourcing is planned.

**AWS mapping**: the picture is AgentCore (item 1) providing the agent runtime and Policy gate, with MHS/Strands Robots providing the device-connection standard — one more layer, **"device driver + safety limits,"** appears beneath the "tool gate" of the item-5 layered defense.

**Decision criteria**: not something to put in today's designs (research preview). But for customers with a large device-integration backlog (lab automation, high-mix cells), flag it as **#1 on the watch list**.

**Customer case**: Doosan Robotics (launch partner, testing stage) `[3]`.

**➡️ Next action**: introduce it to customers already using MCP with the frame **"MCP: data & tools ↔ MHS: hardware,"** and once it opens, set up a validation PoC via the Strands Robots path. Until then, the current alternative is the [MCP+MQTT on IoT Core pattern](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/) (item-3 related assets).

**🔗 Related assets**: [strands-labs/robots](https://github.com/strands-labs/robots) · [pillar-4 edge](pillar-4.md)

---

## The honest reality of this pillar (SA must-read)

- **Separate Seoul availability from processing location.** Check [cross-region inference](evidence.md#agentcore-residency) per feature, model, and route.
- **Policy is GA (2026-03)** — do not call it "preview."
- **DeepFleet ≠ LLM agent orchestrator.** A warehouse robot coordination foundation model (multi-robot RL). No misclassification.
- **Real production is fleet coordination (DeepFleet/CoEvolution) and development workloads (OSMO).** MCP-robot connections and full-stack humanoid agents are mostly research/demo.
- **There is no LLM semantic safety standard.** ISO covers physical only. Layered defense (Cedar Policy + ISO robot layer) is the honest answer.
- **Korean figures like Lotte 30% are single-source** — re-confirm before hard citation.

---
_owner: Youngjin · updated: 2026-09 · volatility: high (AgentCore features · regions are managed in the collapsed block) · sources: [1] official, [3] vendor/press, [4] research/community_

<!-- 용어 각주 -->
