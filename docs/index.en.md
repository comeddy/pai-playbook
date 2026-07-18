---
ko_hash: 969975d261010e3f546159b61168181016c9d474
---
# Physical AI Playbook — AWS Korea SA

_Last updated: 2026-07 · owner: TBD ⚠️ · status: initial build in progress_

> **L0 TL;DR**: A reference asset that lets you answer a customer's Physical AI question with **architecture direction, AWS mapping, and next actions in under 5 minutes from this single playbook** — no digging through Slack. This is neither a paper-summary collection nor a news archive.

---

## How to read this document (30 seconds)

1. **In a hurry**: jump straight to the relevant item in [Top 10 Frequently Asked Questions](#top-10-frequently-asked-questions) below.
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

## Top 10 Frequently Asked Questions

<!-- ⚠️ Initial seed: replace/re-rank with actual SA inquiry history. Tighten links to section anchors once pillar pages are built. -->

| # | Question | Where to |
|---|---|---|
| 1 | "How do I run Isaac Sim / Isaac Lab on AWS?" | [pillar-3](pillar-3.md) |
| 2 | "How should I set up the infrastructure for VLA model training (fine-tuning)?" | [pillar-2](pillar-2.md) |
| 3 | "I can't get GPUs — should I use On-Demand, Capacity Blocks, or an alternative?" | [decisions](decisions.md) |
| 4 | "How do you actually overcome the sim-to-real gap? Are there proven methods?" | [pillar-4](pillar-4.md) |
| 5 | "It's real-time robot control (30–100 Hz) — can I put inference in the cloud?" | [decisions](decisions.md) |
| 6 | "Should I fine-tune a foundation model (GR00T/π0, etc.) or train my own?" | [decisions](decisions.md) |
| 7 | "How do I collect robot learning data and where should I store it? (teleoperation / synthetic data)" | [pillar-1](pillar-1.md) |
| 8 | "How locked in am I to the NVIDIA full stack? What about open-source alternatives?" | [decisions](decisions.md) |
| 9 | "How do I connect edge deployment (Jetson, etc.) with AWS?" | [pillar-4](pillar-4.md) |
| 10 | "Does an architecture where an LLM agent directs robots/equipment actually work?" | [pillar-5](pillar-5.md) |

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

_owner: TBD ⚠️ · updated: 2026-07 · volatility: low (structural page — only the FAQ Top 10 ranking is reviewed quarterly)_
