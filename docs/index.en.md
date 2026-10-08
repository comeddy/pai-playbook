---
ko_hash: 88810e6a4d48cdc1304577555aa665bc9fd2690b
---
# Physical AI Playbook

_Last updated: 2026-09 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: A guide to deciding which technology fits a customer's robotics task and moving through AWS experiments, evaluation, and operations. Start with business fit, total cost, and execution requirements.

!!! info "Unofficial reference"
    This personal reference is not official AWS documentation or an AWS position. Check linked primary sources and dates for technology, licenses, pricing, and Regions. Sample code and service GA do not guarantee customer-site outcomes.

## Start by role

| I am… | Path | Output |
|---|---|---|
| Customer decision maker | [Start/ROI](start.md) → [Executive Brief](exec.md) | Task, alternatives, budget, pilot approval conditions |
| Customer engineer | [Execution](execution.md) → relevant pillar → [Operations](operations.md) | Results, cost, deployment/recovery evidence |
| AWS staff | [Conversation guide](exec-guide.md) → [Decisions](decisions.md) | Discovery, fit assessment, partner handover |

## Technical reference — five pillars

| Pillar | Coverage |
|---|---|
| [P1 Data](pillar-1.md) | Collection, rights, formats, quality, training pipeline |
| [P2 Training](pillar-2.md) | Model selection, licensing, sizing, evaluation |
| [P3 Simulation](pillar-3.md) | Environments, tools, parallel execution, costs |
| [P4 Sim-to-Real](pillar-4.md) | Physical transfer, edge deployment, validation, safety |
| [P5 Orchestration](pillar-5.md) | Business planning, robot skills, permissions, fleet connectivity |

## Labels and verification scope

GA/Preview/Research describe **release status**. Check source comparison, reproduction, site validation, intended use, and support separately. `[1]` official documents/papers, `[2]` recorded reproduction, `[3]` vendor announcements, `[4]` unverified are source types, not AWS endorsement. See [Evidence](evidence.md) and [Maintenance](maintenance.md).

The questions below are discovery examples, not measured inquiry-frequency rankings. Start with a question, then check the [pilot card](start.md#pilot) before making a proposal.

## Top 20 Frequently Asked Questions

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
| 11 | "How much will all this GPU compute cost? How do I budget for it?" | [start](start.md) | [AWS Embodied AI blog](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "How do I connect my existing ROS 2[^ros] stack / rosbag[^rosbag] data to AWS?" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac blog](https://aws.amazon.com/blogs/robotics/) |
| 13 | "How do I scale training across multiple nodes? AWS Batch vs SageMaker HyperPod?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "How do I validate/benchmark whether a policy actually works before real deployment?" | [pillar-4](pillar-4.md) | [NVIDIA policy evaluation](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "Our robot/factory data is sensitive — is cloud training OK for compliance? On-prem/hybrid?" | [decisions](decisions.md) | [AWS AI sovereignty](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "How do I version, reproduce, and recover checkpoints for trained policies?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Can I use Isaac Sim / open models in a commercial product? When do I need NVIDIA AI Enterprise?" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "How do I optimize policy inference for real-time (low latency)? TensorRT / quantization[^quant] / action chunking[^chunk]?" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "How do I build an equipment/factory digital twin[^dtwin] and connect it to robot simulation? TwinMaker / Omniverse?" | [pillar-3](pillar-3.md) | [AWS Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "We have no ML experts — where do we start? How to design a minimal PoC?" | [start](start.md) | [AWS Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) |

---

## Page list

- [Start and ROI](start.md)
- [Execution paths](execution.md)
- [Operations and recovery](operations.md)
- [Usage guide](guide.md)
- [News — recent official articles and pillar links](news.md)
- [Workshops & Resources — public workshops, guides, and samples](workshops.md)
- [Executive Brief](exec.md)
- [AWS staff conversation guide](exec-guide.md)
- [P1 Data](pillar-1.md)
- [P2 Training](pillar-2.md)
- [P3 Simulation](pillar-3.md)
- [P4 Sim-to-Real](pillar-4.md)
- [P5 Orchestration](pillar-5.md)
- [Decisions](decisions.md)
- [Radar](radar.md)
- [Evidence](evidence.md)
- [Maintenance](maintenance.md)
- [Settings · MCP Connection](mcp.md)

_owner: Youngjin · updated: 2026-09 · volatility: medium_

<!-- 용어 각주 -->

[^s2r]: **sim-to-real** — transferring a policy trained in simulation to a real robot, or the methodology for doing so. The physical and visual differences between simulation and reality (the domain gap) mean a naive transfer collapses performance. 🎥 [NVIDIA sim-to-real robotics showcase](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM agent** — software in which a large language model plans on its own, selects and calls tools (APIs, robot skills), and carries out multi-step tasks. Unlike simple Q&A, the key point is that it "acts."
[^ros]: **ROS 2 (Robot Operating System 2)** — the de facto standard open-source middleware for robot software. A distributed architecture in which sensor and control nodes communicate over topics; the shared foundation of industrial and research robot stacks.
[^rosbag]: **ROS bag (rosbag2)** — the standard log format in which the robot operating system ROS 2 records topics (sensor/command streams) wholesale. The de facto default form of robot companies' raw data, but it cannot be used for training as-is and requires conversion.
[^quant]: **Quantization** — a lightweighting technique that converts model weights and operations to lower precision, e.g. FP16→INT8/FP4, cutting memory and compute. A key means of meeting latency budgets on edge devices, managed as a trade-off against accuracy loss.
[^chunk]: **Action chunking** — Generating several future actions per inference. Execution rate differs from response to fresh observations; validate horizons, transitions, and latency per model.
[^dtwin]: **Digital twin** — A physically faithful virtual replica of a real factory, warehouse, or robot. Enables policy training, validation, and scenario experiments without touching the real environment.
