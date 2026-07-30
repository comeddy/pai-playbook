---
ko_hash: 62cdee875eec2ac591bec215c23b02eed13b0298
---
# Executive Brief — Physical AI: What to Do and What to Wait On

_Last updated: 2026-07 · owner: Youngjin · volatility: medium_
[← to index](index.md)

> **L0 TL;DR**: Robotics is meeting foundation models, putting the industry at an inflection point. But **what to invest in now differs from what to watch**. This page draws that line without the hype — 5 minutes.

## ① Why now

Three verification signals have stacked up. First, Agility Digit has run for pay under a multi-year RaaS contract at GXO logistics sites, logging more than 65,000 hours as of 2025-11 with customer cross-confirmation — the best-verified paid humanoid work to date. Second, Figure 02 ran a verification pilot on a BMW line (whereas Figure 03's "8-hour autonomous shift" is only a CEO tweet with no independent verification). Third, open foundation models such as Physical Intelligence's π0 have been released under Apache-2.0, making commercial fine-tuning possible. That said, no independent third-party autonomy audit of humanoids exists anywhere yet ([pillar-4](pillar-4.md)), so large-scale deployment forecasts remain items to watch, grounded only in vendor and customer PR.

## ② What it means for our industry

**Manufacturing**: A path has opened to fine-tune open VLA models to your own tasks. Rather than training from scratch, the realistic approach is to teach a specific process with a small number of real demonstrations ([pillar-2](pillar-2.md)).
**Logistics**: Locomotion-based (walking) robots are already deployed at paid commercial sites. Precision manipulation, by contrast, is still at the research/preview stage, so task scope must be kept narrow ([pillar-4](pillar-4.md)).
**Automotive**: The training pipeline for moving policies trained at scale in simulation to real hardware has matured. Parallel simulation on cloud GPUs lowers the barrier to entry ([pillar-3](pillar-3.md)).

## ③ What is real and what is hype

| Verdict | Meaning | Representative areas |
|---|---|---|
| 🟢 **Invest now** | Verified foundational capabilities | Robot data pipelines · simulation infrastructure · synthetic data |
| 🟡 **Soon (12–24 months)** | Worth a pilot | VLA fine-tuning capability · edge inference stack · agent orchestration |
| ⚪ **Not yet** | Items to watch | Large-scale humanoid adoption · fully autonomous shifts |

This distinction is not arbitrary. 🟢 holds because data pipelines and synthetic data ([pillar-1](pillar-1.md)) and simulation infrastructure ([pillar-3](pillar-3.md)) are GA and usable in production. 🟡 reflects that VLA fine-tuning is GA but lacks public real-world cases ([pillar-2](pillar-2.md)), and that edge/agents ([pillar-5](pillar-5.md)) are early in verification. ⚪ comes from the verdict that large-scale humanoid adoption such as Optimus and Figure 03 remains at the demo/roadmap stage ([radar](radar.md#-hardware--deployment-roadmap--demo)). This verdict is not made once and left alone — a continuous verification system that scans every week ([radar](radar.md)) updates it through promotions and demotions.

## ④ So what do we do first

The honest answer is "data first." The bottleneck in robot learning is not the model but the data, and the real-world recipe is almost always a three-stage mix of **open-dataset pretraining → synthetic data augmentation → fine-tuning on a small number of real demonstrations** ([pillar-1](pillar-1.md)). Set the order as three steps. (1) Stand up the data pipeline first to accumulate assets, (2) secure low-cost, high-diversity data with a simulation PoC, and (3) on top of that, verify a VLA fine-tuning pilot on a narrow task. LoRA fine-tuning is possible with a single GPU, so the pilot entry cost is low ([pillar-2](pillar-2.md)).

## ⑤ Why do it with AWS

Three verified facts are enough. First, there is an official AWS blog case that trained Unitree H1 humanoid RL on Isaac Lab + SageMaker HyperPod (noting explicitly that this is RL locomotion, not VLA) ([pillar-2](pillar-2.md)). Second, Amazon Bedrock AgentCore is GA with full support in the Seoul region, so you can put agent orchestration on it without data residency concerns ([pillar-5](pillar-5.md)). Third, you can self-host open models such as π0 (Apache-2.0) and OpenVLA (MIT) and use them freely without vendor lock-in ([pillar-2](pillar-2.md)).

## If you want to start a review

**1-day architecture workshop**: We recommend a diagnosis of your data assets plus applying the judgment matrix above to your situation. Reach out via your AWS SA or [GitHub](https://github.com/comeddy/pai-playbook).

---
**Go deeper**: [Technical Guide](guide.md) · [P1 Data](pillar-1.md) · [P3 Simulation](pillar-3.md) · [Decision Tree](decisions.md)

_owner: Youngjin · updated: 2026-07 · volatility: medium (the judgment matrix is updated on radar promotions/demotions)_
