---
ko_hash: b883f09cce87a233271097a1c5160900d47f325f
---
# Physical AI Playbook — Introduction

_Last updated: 2026-07 · owner: Youngjin · status: initial build in progress_

> **L0 TL;DR**: A reference asset that lets you answer a customer's Physical AI question with **architecture direction, AWS mapping, and next actions in under 5 minutes from this single playbook** — no digging through Slack. This is neither a paper-summary collection nor a news archive.

<!-- 임시 숨김(2026-08-07): 비공식 자료 박스 — 복원하려면 주석 해제
!!! info "Unofficial"
    This site is a personally maintained reference asset and is **not official AWS (Amazon Web Services) documentation or an official AWS position.** Service specifications, pricing, and regional availability on this site must always be re-verified against the [official AWS documentation](https://docs.aws.amazon.com/).
-->


---

## How to read this document (30 seconds)

1. **In a hurry**: jump straight to the relevant item in [Top 20 Frequently Asked Questions](#top-20-frequently-asked-questions) below.
2. **Once the topic is clear**: enter one of the 5 pillars. Each item is layered as **L0 (1–2 sentences) → L1 (1 page) → L2 (deep-dive links)** — reading only the top gives you direction.
3. **At a crossroads**: [Decision trees](decisions.md) — Cloud vs Edge, NVIDIA vs open source, securing GPUs, Build vs Buy.
4. **"Why isn't this here?"**: check the [Radar](radar.md) first. Items that fell short of the inclusion criteria and are on hold live there. Submit new candidates via the promotion pipeline in the [maintenance guide](maintenance.md).

### How to read the labels

| Maturity | Meaning |
|---|---|
| 🟢 GA | Generally available, usable in production |
| 🟡 Preview | Public preview / clear GA roadmap |
| 🔵 Research-only | Paper/research stage, do not use in customer proposals |
| ⚪ Hype | Demo only. "Impressive demo" ≠ "deployable" |

| Source grade | Meaning |
|---|---|
| [1] | Official docs / papers |
| [2] | AWS internal validation (we ran it ourselves) |
| [3] | Vendor official blog |
| [4] | Unverified (Slack/rumor) — always re-confirm when citing |

---

## The 5 pillars

| # | Pillar | L0 one-liner | Go to |
|---|---|---|---|
| 1 | **Data Collection & Processing** | The bottleneck in robot learning is not the model but the data — how to process teleoperation[^teleop], open datasets, and synthetic data through AWS pipelines | [pillar-1](pillar-1.md) |
| 2 | **Model Training (VLA)** | How to design VLA[^vla] / robot foundation model training, starting from GPU scale and whether it is fine-tuning[^ft] or pretraining[^pretrain] | [pillar-2](pillar-2.md) |
| 3 | **Simulation** | Choosing Isaac Sim/Lab vs open source, and patterns for running large-scale parallel simulation on AWS | [pillar-3](pillar-3.md) |
| 4 | **Sim-to-Real** | Proven methodologies for transferring simulation-trained policies to real hardware, and edge inference deployment paths | [pillar-4](pillar-4.md) |
| 5 | **Agentic Orchestration** | The layer where an LLM planner (System 2[^sys]) directs the robot controller (System 1) and the fleet[^fleet] — centered on Bedrock AgentCore | [pillar-5](pillar-5.md) |

> The pillars carry equal weight. Within each pillar, items are ordered by **actual customer demand × production-readiness**, with a "Top 3 questions customers ask most in this pillar" at the top.

---

## Top 20 Frequently Asked Questions

<!-- 1-10: initial seed (master-prompt examples + IA structure). 11-20: deep research of public community/blogs (2026-07). ⚠️ Neither is an actual SA inquiry log; re-rank by frequency once Slack inquiry history is available. -->

| # | Question | Where to | Source |
|---|---|---|---|
| 1 | "How do I run Isaac Sim / Isaac Lab on AWS?" | [pillar-3](pillar-3.md) | seed ⚠️ |
| 2 | "How should I set up the infrastructure for VLA model training (fine-tuning)?" | [pillar-2](pillar-2.md) | seed ⚠️ |
| 3 | "I can't get GPUs — should I use On-Demand, Capacity Blocks, or an alternative?" | [decisions](decisions.md) | seed ⚠️ |
| 4 | "How do you actually overcome the sim-to-real[^s2r] gap? Are there proven methods?" | [pillar-4](pillar-4.md) | seed ⚠️ |
| 5 | "It's real-time robot control (30–100 Hz) — can I put inference in the cloud?" | [decisions](decisions.md) | seed ⚠️ |
| 6 | "Should I fine-tune a foundation model (GR00T/π0, etc.) or train my own?" | [decisions](decisions.md) | seed ⚠️ |
| 7 | "How do I collect robot learning data and where should I store it? (teleoperation / synthetic data)" | [pillar-1](pillar-1.md) | seed ⚠️ |
| 8 | "How locked in am I to the NVIDIA full stack? What about open-source alternatives?" | [decisions](decisions.md) | seed ⚠️ |
| 9 | "How do I connect edge deployment (Jetson, etc.) with AWS?" | [pillar-4](pillar-4.md) | seed ⚠️ |
| 10 | "Does an architecture where an LLM agent[^agent] directs robots/equipment actually work?" | [pillar-5](pillar-5.md) | seed ⚠️ |
| 11 | "How much will all this GPU compute cost? How do I budget for it?" | [decisions](decisions.md) | [AWS Embodied AI blog](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "How do I connect my existing ROS 2[^ros] stack / rosbag[^rosbag] data to AWS?" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac blog](https://aws.amazon.com/blogs/robotics/) |
| 13 | "How do I scale training across multiple nodes? AWS Batch vs SageMaker HyperPod?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "How do I validate/benchmark whether a policy actually works before real deployment?" | [pillar-4](pillar-4.md) | [NVIDIA policy evaluation](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "Our robot/factory data is sensitive — is cloud training OK for compliance? On-prem/hybrid?" | [decisions](decisions.md) | [AWS AI sovereignty](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "How do I version, reproduce, and recover checkpoints for trained policies?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Can I use Isaac Sim / open models in a commercial product? When do I need NVIDIA AI Enterprise?" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "How do I optimize policy inference for real-time (low latency)? TensorRT / quantization[^quant] / action chunking[^chunk]?" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "How do I build an equipment/factory digital twin[^dtwin] and connect it to robot simulation? TwinMaker / Omniverse?" | [pillar-3](pillar-3.md) | [AWS Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "We have no ML experts — where do we start? How to design a minimal PoC?" | [decisions](decisions.md) | [AWS Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) |

---

## Page list

- [guide — how this playbook is built and maintained (the full verification pipeline)](guide.md)
- [Executive Brief — a 5-minute judgment frame for executives (now/soon/not-yet matrix)](exec.md)
- [Executive Conversation Guide — SA prep for executive meetings (pitches, top-10 Q&A, forbidden claims)](exec-guide.md)
- [pillar-1 — Data Collection & Processing](pillar-1.md)
- [pillar-2 — Model Training (VLA)](pillar-2.md)
- [pillar-3 — Simulation](pillar-3.md)
- [pillar-4 — Sim-to-Real](pillar-4.md)
- [pillar-5 — Agentic Orchestration](pillar-5.md)
- [decisions — Cross-cutting decision trees](decisions.md)
- [radar — Queue / watchlist](radar.md)
- [maintenance — Ownership · update rules · promotion pipeline](maintenance.md)

---

## What this playbook does not cover

- **Items that fall short of the inclusion criteria**: ⓐ production-validated ⓑ mappable to AWS ⓒ actual inquiry history ⓓ GA (or roadmap) — if **fewer than 2** of these hold, it is not in the body. It exists only as a one-liner in the [Radar](radar.md).
- **Breaking news**: "it just came out" is not a reason for inclusion.
- **Items that end at conceptual explanation**: every item ends with "➡️ Next action." If there is no action, it is incomplete.

---

_owner: Youngjin · updated: 2026-07 · volatility: low (structural page — only the FAQ Top 20 ranking is reviewed quarterly)_

<!-- 용어 각주 -->

[^teleop]: **Teleoperation** — a data-collection method in which a human remotely operates a robot with VR controllers, leader arms, etc., recording demonstration motions. Quality is the highest, but human time translates directly into cost. 🎥 [Stanford Mobile ALOHA teleoperation demo](https://www.youtube.com/watch?v=mnLVbwxSdNM)
[^vla]: **VLA (Vision-Language-Action)** — a foundation model that takes camera images (Vision) and natural-language instructions (Language) as input and directly outputs robot actions (Action). Say "pick up the cup" and it generates the joint motions. 🎥 [NVIDIA Isaac GR00T N1 introduction](https://www.youtube.com/watch?v=m1CH-mgpdYg)
[^ft]: **fine-tuning** — additionally training a model pretrained on large-scale data with a small amount of data from your own task/robot. Saves tens to hundreds of times the data and GPU compared to training from scratch.
[^pretrain]: **pre-training** — training a model from scratch on large-scale general-purpose data to build its base capabilities; it is then adapted to a specific task by fine-tuning on a small amount of data. Frontier VLA pre-training is the domain of a tiny handful of organizations.
[^sys]: **System 2 / System 1** — the cognitive-science "slow thinking / fast reaction" distinction applied to robot architecture. System 2 is a slow large model that plans (5~10Hz); System 1 is a small policy that runs real-time control (50~200Hz). This becomes the criterion for whether inference goes to the cloud or the edge.
[^fleet]: **Fleet coordination** — scheduling and route allocation for a large group of robots as one system. Already production-proven at the hundreds-to-thousands scale, as with warehouse robots.
[^s2r]: **sim-to-real** — transferring a policy trained in simulation to a real robot, or the methodology for doing so. The physical and visual differences between simulation and reality (the domain gap) mean a naive transfer collapses performance. 🎥 [NVIDIA sim-to-real robotics showcase](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM agent** — software in which a large language model plans on its own, selects and calls tools (APIs, robot skills), and carries out multi-step tasks. Unlike simple Q&A, the key point is that it "acts."
[^ros]: **ROS 2 (Robot Operating System 2)** — the de facto standard open-source middleware for robot software. A distributed architecture in which sensor and control nodes communicate over topics; the shared foundation of industrial and research robot stacks.
[^rosbag]: **ROS bag (rosbag2)** — the standard log format in which the robot operating system ROS 2 records topics (sensor/command streams) wholesale. The de facto default form of robot companies' raw data, but it cannot be used for training as-is and requires conversion.
[^quant]: **Quantization** — a lightweighting technique that converts model weights and operations to lower precision, e.g. FP16→INT8/FP4, cutting memory and compute. A key means of meeting latency budgets on edge devices, managed as a trade-off against accuracy loss.
[^chunk]: **action chunking** — predicting a chunk of several future action steps at once instead of one action per step. Reduces the number of inference calls, making it easier to meet real-time control frequencies.
[^dtwin]: **Digital twin** — A physically faithful virtual replica of a real factory, warehouse, or robot. Enables policy training, validation, and scenario experiments without touching the real environment.
