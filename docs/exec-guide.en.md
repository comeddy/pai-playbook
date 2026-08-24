---
ko_hash: 2ce31417f5c626dbd06c8a584b1cdd3ea96dd2f6
---
# Executive Conversation Guide — For SAs

_Last updated: 2026-08 · owner: Youngjin · volatility: medium_
[← to index](index.md)

> **L0 TL;DR**: A practical asset to skim 30 minutes before an executive meeting. If the [Executive Brief](exec.md) is what you "show," this page is how you "say" it.

## 1. Three elevator pitches

- **30 seconds (hallway)**: "Robotics is meeting foundation models and the industry is at an inflection point. But **what to invest in now differs from what to watch.** What's verified is data and simulation infrastructure; large-scale humanoid adoption is still an item to watch."
- **2 minutes (meeting opener)**: Add the three pieces of evidence above — Digit has run for 65,000+ hours under a multi-year paid contract at GXO, open VLA (π0 = Apache-2.0) has made commercial fine-tuning possible, and yet no independent autonomy audit of humanoids exists yet ([pillar-4](pillar-4.md), [pillar-2](pillar-2.md)). "So our proposal is **data first**."
- **5 minutes (whiteboard)**: Pull up the [Executive Brief](exec.md) and walk it in h2 order — [① Why now](exec.md#①-why-now) → [② Industry meaning](exec.md#②-what-it-means-for-our-industry) → [③ The matrix](exec.md#③-what-is-real-and-what-is-hype) → [④ What first](exec.md#④-so-what-do-we-do-first) → [⑤ Why AWS](exec.md#⑤-why-do-it-with-aws) → [If you want to start a review](exec.md#if-you-want-to-start-a-review). Stop at the matrix and ask "where are you?" — that opens the conversation.

## 2. Top 10 anticipated executive questions

| # | Question | Answer summary | Basis |
|---|---|---|---|
| 1 | ROI/cost? | LoRA is possible with a single GPU, so pilot entry cost is low. Building assets from data/sim PoCs first keeps the initial investment small | [pillar-2](pillar-2.md) |
| 2 | Why AWS (vs. NVIDIA)? | AWS is a neutral position that runs both NVIDIA and open source. There is an official case that trained Unitree H1 RL on Isaac Lab + HyperPod | [decisions](decisions.md) |
| 3 | Competitors? | Foundation labs and humanoid vendors look ahead, but most are pilots/demos. Gemini Robotics-ER is also Preview | [pillar-2](pillar-2.md), [radar](radar.md) |
| 4 | Are we late? | The bottleneck is not the model but the data. Data assets must be built now to stay ahead — models keep coming out as open releases | [pillar-1](pillar-1.md) |
| 5 | How much does it cost? | A single G7e LoRA 1-day PoC is the basic entry. Unless it's very large pretraining, large-scale GPUs are unnecessary | [decisions](decisions.md) |
| 6 | Staffing? | You can start with open-model fine-tuning and sim PoCs even without ML experts | [index FAQ](index.md#top-20-frequently-asked-questions) |
| 7 | When are results? | Data/sim now, VLA pilot in 12–24 months, large-scale humanoid adoption TBD | [exec ③](exec.md#③-what-is-real-and-what-is-hype) |
| 8 | Risks? | Manipulation sim-to-real is unsolved, and humanoid "production" metrics are mostly vendor PR. Manage with narrow tasks | [pillar-4](pillar-4.md) |
| 9 | Partner criteria? | License (commercially viable) and data sovereignty. π0 and OpenVLA are commercially friendly; for GR00T, checking the model card is a must | [pillar-2](pillar-2.md) |
| 10 | First project? | Data pipeline → sim PoC → narrow VLA fine-tuning. Diagnose data assets in a 1-day workshop | [exec ④](exec.md#④-so-what-do-we-do-first) |

## 3. Handling pushback and concerns

**Three beats: acknowledge → reframe → verified next step.**

- **"Isn't this just a humanoid demo?"** — True, there are many demos → but locomotion is already deployed for pay (Digit@GXO) → our proposal is the data/sim infrastructure beneath it ([pillar-4](pillar-4.md)).
- **"What about safety and regulation?"** — Important → that's why 30–100 Hz control must be at the edge, with only planning in the cloud → AgentCore Policy (Cedar) gates tool calls at the millisecond level ([pillar-5](pillar-5.md)).
- **"What about the workforce-replacement debate?"** — Sensitive → what's verified is narrow, repetitive tasks (tote moving), not general-purpose replacement → start narrow from the angle of hazardous/assistive work ([pillar-4](pillar-4.md)).
- **"Isn't this hype?"** — There's a lot of hype → that's why a continuous verification system that scans every week separates real from hype → [Radar](radar.md) shows the maturity labels as-is.
- **"What about vendor lock-in?"** — A legitimate concern → AWS runs both NVIDIA and open source → self-hosting π0/OpenVLA means freedom without lock-in ([decisions](decisions.md)).

## 4. Industry angles

| Industry | Hook | Verified case | First proposal |
|---|---|---|---|
| Manufacturing | A path has opened to fine-tune open VLA to your own process | Figure 02@BMW verification pilot ([radar](radar.md#-hardware--deployment-roadmap--demo)) | Verify a narrow task with a single G7e LoRA 1-day PoC |
| Logistics | Locomotion robots are already at paid commercial sites | Digit@GXO 65,000+ operating hours ([pillar-4](pillar-4.md)) | Scope to narrow, structured movement tasks |
| Automotive | The training pipeline for moving policies trained in sim to real hardware has matured | Zoox HyperPod training (⚠️ AV, 64+ GPUs at 95% utilization — [pillar-2](pillar-2.md)) | Lower the barrier with a cloud parallel-sim PoC |

## 5. ⚠️ Phrases to avoid or handle with care in front of executives

| ❌ Don't say this | ⭕ Say this instead |
|---|---|
| "Optimus goes into mass production soon" | "Humanoids are at the verification-pilot stage. Our proposal is the earlier stage — data/sim infrastructure" |
| (Citing radar ⚪/🔵 items as if they were mature capabilities) | (Maturity label as-is: "It was announced, but it's not yet production-verified") |
| "Figure 03 runs an 8-hour autonomous shift" | "That's a CEO tweet with no independent verification. What's verified is the Figure 02@BMW pilot" ([radar](radar.md#-hardware--deployment-roadmap--demo)) |
| "1X Neo does household chores fully autonomously" | "The 1X CEO openly acknowledges it runs on mixed autonomy + VR teleoperation. Even the '60–70% autonomy' figure has no primary source" ([radar](radar.md#-hardware--deployment-roadmap--demo)) |
| "Simulation alone completes a manipulation policy" | "Manipulation sim-to-real is still unsolved. Fine-tuning on real data is essential" ([pillar-4](pillar-4.md)) |

Always check the maturity labels in [Radar](radar.md) for the latest status before you speak.

_owner: Youngjin · updated: 2026-08 · volatility: medium_
