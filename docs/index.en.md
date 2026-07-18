---
ko_hash: c6c614576fad53450cec520e227f48064ee2f1c7
---
# Physical AI Playbook — AWS Korea SA

_Last updated: 2026-07 · owner: comeddy · status: initial build in progress_

> **L0 TL;DR**: A reference asset that lets you answer a customer's Physical AI question with **architecture direction, AWS mapping, and next actions in under 5 minutes from this single playbook** — no digging through Slack. This is neither a paper-summary collection nor a news archive.

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
| 1 | **Data Collection & Processing** | The bottleneck in robot learning is not the model but the data — how to process teleoperation, open datasets, and synthetic data through AWS pipelines | [pillar-1](pillar-1.md) |
| 2 | **Model Training (VLA)** | How to design VLA / robot foundation model training, starting from GPU scale and whether it is fine-tuning or pretraining | [pillar-2](pillar-2.md) |
| 3 | **Simulation** | Choosing Isaac Sim/Lab vs open source, and patterns for running large-scale parallel simulation on AWS | [pillar-3](pillar-3.md) |
| 4 | **Sim-to-Real** | Proven methodologies for transferring simulation-trained policies to real hardware, and edge inference deployment paths | [pillar-4](pillar-4.md) |
| 5 | **Agentic Orchestration** | The layer where an LLM planner (System 2) directs the robot controller (System 1) and the fleet — centered on Bedrock AgentCore | [pillar-5](pillar-5.md) |

> The pillars carry equal weight. Within each pillar, items are ordered by **actual customer demand × production-readiness**, with a "Top 3 questions customers ask most in this pillar" at the top.

---

## Top 20 Frequently Asked Questions

<!-- 1-10: initial seed (master-prompt examples + IA structure). 11-20: deep research of public community/blogs (2026-07). ⚠️ Neither is an actual SA inquiry log; re-rank by frequency once Slack inquiry history is available. -->

| # | Question | Where to | Source |
|---|---|---|---|
| 1 | "How do I run Isaac Sim / Isaac Lab on AWS?" | [pillar-3](pillar-3.md) | seed ⚠️ |
| 2 | "How should I set up the infrastructure for VLA model training (fine-tuning)?" | [pillar-2](pillar-2.md) | seed ⚠️ |
| 3 | "I can't get GPUs — should I use On-Demand, Capacity Blocks, or an alternative?" | [decisions](decisions.md) | seed ⚠️ |
| 4 | "How do you actually overcome the sim-to-real gap? Are there proven methods?" | [pillar-4](pillar-4.md) | seed ⚠️ |
| 5 | "It's real-time robot control (30–100 Hz) — can I put inference in the cloud?" | [decisions](decisions.md) | seed ⚠️ |
| 6 | "Should I fine-tune a foundation model (GR00T/π0, etc.) or train my own?" | [decisions](decisions.md) | seed ⚠️ |
| 7 | "How do I collect robot learning data and where should I store it? (teleoperation / synthetic data)" | [pillar-1](pillar-1.md) | seed ⚠️ |
| 8 | "How locked in am I to the NVIDIA full stack? What about open-source alternatives?" | [decisions](decisions.md) | seed ⚠️ |
| 9 | "How do I connect edge deployment (Jetson, etc.) with AWS?" | [pillar-4](pillar-4.md) | seed ⚠️ |
| 10 | "Does an architecture where an LLM agent directs robots/equipment actually work?" | [pillar-5](pillar-5.md) | seed ⚠️ |
| 11 | "How much will all this GPU compute cost? How do I budget for it?" | [decisions](decisions.md) | [AWS Embodied AI blog](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "How do I connect my existing ROS 2 stack / rosbag data to AWS?" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac blog](https://aws.amazon.com/blogs/robotics/) |
| 13 | "How do I scale training across multiple nodes? AWS Batch vs SageMaker HyperPod?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "How do I validate/benchmark whether a policy actually works before real deployment?" | [pillar-4](pillar-4.md) | [NVIDIA policy evaluation](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "Our robot/factory data is sensitive — is cloud training OK for compliance? On-prem/hybrid?" | [decisions](decisions.md) | [AWS AI sovereignty](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "How do I version, reproduce, and recover checkpoints for trained policies?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Can I use Isaac Sim / open models in a commercial product? When do I need NVIDIA AI Enterprise?" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "How do I optimize policy inference for real-time (low latency)? TensorRT / quantization / action chunking?" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "How do I build an equipment/factory digital twin and connect it to robot simulation? TwinMaker / Omniverse?" | [pillar-3](pillar-3.md) | [AWS Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "We have no ML experts — where do we start? How to design a minimal PoC?" | [decisions](decisions.md) | [AWS Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) |

---

## Page list

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
- **Items that end at conceptual explanation**: every item ends with "➡️ SA next action." If there is no action, it is incomplete.

---

_owner: comeddy · updated: 2026-07 · volatility: low (structural page — only the FAQ Top 20 ranking is reviewed quarterly)_
