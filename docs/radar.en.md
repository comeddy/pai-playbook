---
ko_hash: a2d03f03e5c3e2bcd5e406fdd7f1e97a78d7c727
---
# Radar — Queue / Watchlist

_Last updated: 2026-07 · owner: Youngjin · volatility: high_
[← back to index](index.md)

> **L0 TL;DR**: Things **worth watching** that have not yet passed the inclusion criteria ([2.5 THE FILTER](maintenance.md#inclusion-criteria-the-filter)). Each item is one line — a maturity label + **why it is on hold**. Once it clears the gate (2 of 4), the owning pillar's owner promotes it using the standard template.
>
> ⚠️ **Do not present items here as "mature capabilities" in customer proposals.** A flashy demo often masks how deployable something actually is.

---

## 🔬 Models / algorithms (awaiting validation)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| Physical Intelligence **[π0.7](https://www.physicalintelligence.company/)** | 🔵 Research | Secondary sources only `[4]`, no primary PI confirmation | Official PI release + performance validation |
| **[GR00T N1.6 / N1.7](https://github.com/NVIDIA/Isaac-GR00T) commercial license** | 🟡→ | Commercial-use claim is secondary-source only `[4]` (N1.5 is clearly non-commercial per model card `[1]`) | License confirmed on live model card |
| **[World-action models](https://developer.nvidia.com/isaac/gr00t)** (DreamZero → GR00T N2) | 🟡 Preview | GR00T N2 "expected end of year," DreamZero is research | GA + real deployment case |
| Google DeepMind **[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)** (world model[^wfm] for robot learning) | 🟡 Preview | The world model itself is preview; applying it to robot learning is research | Validated case of robot policy learning |
| **VLM-based SysID[^sysid]** ([Vid2Sid](https://arxiv.org/abs/2602.19359), [Swim2Real](https://arxiv.org/abs/2603.20827)) | 🔵 Research | 2026 preprints, single lab | peer-review + reproduction |
| **VIRAL / [VideoMimic](https://www.videomimic.net/) / [Real2Render2Real](https://real2render2real.com/)** (visual sim-to-real[^s2r] at scale) | 🔵 Research | CVPR/CoRL research, not production | Evidence of production deployment |
| **Robbyant [LingBot-VLA](https://huggingface.co/robbyant) / [UnifoLM-VLA-0](https://huggingface.co/unitreerobotics)** | 🔵 Research | Secondary sources, no validation | Primary confirmation + AWS mapping |

## 🖥️ Simulation / tools (awaiting maturity)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** physics engine[^physeng] | ⚪ Hype | "430,000×" refuted `[1]`, slow on contact-rich manipulation | Independent benchmark + production adoption |
| **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** | 🟡 Alpha | PyPI classifier "3-Alpha" `[1]`, not production | Beta/GA transition |
| **[NVIDIA Newton](https://github.com/newton-physics/newton)** physics engine | 🟡 Preview | Experimental backend in Isaac Sim 6.0 | GA + official in Isaac Lab 3.0 |
| **[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)** | 🟡 Preview | "Early Developer Release," API in flux (latest GA is 5.1) | 6.x GA declaration |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) as sim-to-real training source** | 🟢 GA(model)/🔵(in practice) | Model is GA, but "training deployable policies from world-model data" is early-adopter only. ⚠️ **not hosted on AWS** | Stronger AWS mapping + training validation |

## 🤖 Hardware / deployment (roadmap / demo)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | Musk claims only, production not started | Validated deployment |
| **Hyundai·BD electric [Atlas](https://bostondynamics.com/atlas/)** | ⚪ Roadmap | Electric Atlas product version unveiled (2026-07, BD official `[3]`). Deployment 25k+ units & 30k/yr capacity both **start 2028**; ~0 in live production today. 2026 is a small pilot only (Hyundai RMAC + Google DeepMind). ⚠️ "Gen 5" is a misnomer | Verified real-operation shipments begin |
| **[Apptronik Apollo 2 + Robot Park](https://apptronik.com/)** | 🟡 Pilot | Operational pilots at Mercedes-Benz & GXO `[3]` + Google DeepMind Gemini Robotics data partnership (90k sq ft). Autonomy/commercial scale unverified. AWS mapping is generic (data→S3/SageMaker); the partnership itself is Google `[4]` | Commercial deployment scale + validated autonomy |
| **[1X Neo](https://www.1x.tech/neo)** autonomy | 🟡 Preview | Mixed autonomy + VR teleoperation (Expert Mode) — acknowledged by the CEO directly ([Engadget](https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html) `[3]`). The "60–70% autonomy" figure has no primary source `[4]` | Validation of true autonomy |
| **[Figure 03](https://www.figure.ai/) "8-hour autonomous shift"** | ⚪ Hype | CEO tweet, no independent validation (Figure 02@BMW is a validated pilot) | Third-party autonomy audit |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) adoption** (Doosan/LG/Samsung) | 🟢 GA(announced) | Adoption is "announced," not production-validated | Public production case |

## 🔗 Agents / connectivity (early)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| **MCP[^mcp] for robotics** ([ros-mcp-server](https://github.com/lpigeon/ros-mcp-server), etc.) | 🔵 Research | 50+ servers exist but open-source/demo, none in production (safety, latency, determinism unvalidated) | Production-hardening case |
| **ROS 2[^ros] + LLM agents[^agent]** (NASA JPL [ROSA](https://github.com/nasa-jpl/rosa), [RAI](https://github.com/RobotecAI/rai)) | 🔵 Research | ROSA (JPL) is the strongest real case but mock-ops. Field deployment limited | Field production deployment |
| **Agent physical-safety standards** ([RoboGuard](https://arxiv.org/abs/2503.07885), etc.) | 🔵 Research | ISO covers physical only; no standard for LLM semantic risk | Progress on standardization |
| **[AgentCore Payments / Agent Registry](https://aws.amazon.com/bedrock/agentcore/) (Seoul)** | 🟡 Preview/unavailable | Not available in Seoul region (Tokyo Agent Registry ✅) | Seoul region expansion |

## 🆕 Latest scan intake (2026-08-08 · primary verification completed 2026-07-21)

<!-- Intake from automated scan (arXiv/web). Primary-source verification completed 2026-07-21 (4 verification agents, cross-checked against official announcements and arXiv originals) — 0 promoted, 6 corrected. Do not use in customer proposals until they pass THE FILTER. See scripts/radar_scan.md for the periodic refresh. -->

| Item | Label | Why waiting | Promotion criteria |
|---|---|---|---|
| **[RLWRLD RLDX-1](https://huggingface.co/RLWRLD)** (dexterity-first foundation model) | 🟡 Preview | Weight release is real but ⚠️ not open source — RLWRLD Model License v1.0 (non-commercial, commercial distribution prohibited) `[3]`; a 7–9B family (flagship 8.1B). RoboCasa/LIBERO/SIMPLER SOTA is self-reported, no independent reproduction ([aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws) provides measured n=5 smoke runs on EC2 — not a full benchmark reproduction). AWS connection is limited to simulation benchmarking (a use the non-commercial license explicitly permits; no commercial positioning) — "no connection" wording updated (2026-07). 0 real customer deployments | Independent benchmark reproduction + validated deployment case |
| **[NEURA Robotics × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale) strategic collaboration** | ⚪ Hype/roadmap | Confirmed via official AWS press release, 2026-04-21 `[1]` — AWS as primary cloud, Neuraverse hosting + NEURA Gym/SageMaker integration stated explicitly. But the fulfillment-center wording is "explore opportunities to deploy" — 0 live deployments. The NEURA Gym RWTH Aachen training-network expansion (announced 2026-07-22) makes no mention of AWS — tracked as a separate thread | Public case of actual AWS infra use + validated fulfillment-center deployment |
| **[Actuator Reality Shaping](https://arxiv.org/abs/2607.02205)** (zero-shot sim-to-real) | 🔵 Research | Existence confirmed (arXiv 2607.02205, 2026-07-02) `[1]` — validated on 4 real hardware platforms (including humanoid walking); the summary matches the abstract (no corrections). Not peer-reviewed | peer review + independent reproduction |
| **[AgiBot World 2026](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)** (open-source real-world robot manipulation dataset, phased 5-track release) | 🔵 Research | AgiBot official release (HuggingFace `agibot-world/AgiBotWorld2026`, 2026-07) `[4]` — 100% real-world data captured on the AgiBot G2 platform, 5 research tracks (imitation learning, etc.) to be released in phases; the first tranche covers several hundred hours from commercial/service environments. License and commercial-use terms unconfirmed; no independent benchmark or training-validation case yet | License confirmed + independent training validation (SOTA reproduction) case |
| **[AXIS](https://arxiv.org/abs/2607.21588)** (community-driven, growable robot-manipulation data engine) | 🔵 Research | Existence confirmed (arXiv 2607.21588, 2026-07-23) `[4]` — 8 universities + Axis Robotics; crowdsourced via browser-based MuJoCo-WASM teleoperation, then augmented in IsaacSim. Simulation-only on a Franka arm (207 tasks, 50k+ trajectories); reports +4.9pp on LIBERO-Plus from π0.5 continual pretraining (self-reported benchmark, no independent reproduction). Authors themselves list sim-to-real as future work — unvalidated on real hardware | peer review + real-hardware sim-to-real validation |
| **[NVIDIA Cosmos 3 Edge](https://www.nvidia.com/en-us/ai/cosmos/)** (Cosmos 3-family, on-device 4B world model + policy) | 🟡 Preview | NVIDIA official announcement `[4]` (2026-07-21, HuggingFace/developer blog) — on-device inference on Jetson Thor for real-time 15Hz robot policy control (self-reported benchmark, no independent validation); Cosmos 3 Edge Policy (DROID) supports pick-and-place fine-tuning. Distinct from the existing "Cosmos 3 as sim-to-real training source" entry (🖥️ section) — this covers only the edge-deployment track; watch alongside AMD Ryzen AI Embedded X100 (this table) as a competing approach. 0 production robot deployments today | Independent benchmark + real production robot-deployment case |
| **[Walden Robotics](https://www.waldenrobotics.com/news/walden-robotics-launches-from-stealth)** (Toyota Research Institute spinout, Large Behavior Models humanoid) | 🟡 Pilot | Official company announcement (2026-07-15) `[4]` — spun out of TRI in 2026-01 (founder Russ Tedrake, former TRI SVP); $300M seed co-led by Toyota and Deviation Capital, with NVIDIA, Boeing, Samsung Ventures, etc. participating ($1.1B valuation). Humanoid upper body on a wheeled mobile base, running Diffusion Policy / Large Behavior Models; claims a pilot-to-"production" transition at a North American Toyota plant starting 2026-02, no third-party validation | Third-party audit / independent validation + expanded deployment scale |
| **[Generalist AI GEN-1](https://generalistai.com/blog/gen-1)** (embodied foundation model supporting a broad range of end effectors) | 🟡 Preview | Generalist AI official blog post (2026-07) `[4]` — pretrained on ~9,000 end-effector variants (5-finger hands to specialized tools) and 500k+ hours of real interaction data; claims 99% task success and 3x speed (self-reported, no independent reproduction). Generalist AI is already mentioned in [pillar-1](pillar-1.md) as a Cosmos WFM data-generation user, but the GEN-1 model itself is a distinct new item | Independent benchmark reproduction + real deployment case |
| **[Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)** (VLA foundation model, 100k+ hours of real-world UMI trajectories) | 🔵 Research | Xiaomi official arXiv release (2607.15330, 2026-07-16) `[4]` — Qwen3-VL-based MoT (VLM+DiT), self-reported SOTA on four benchmarks: RoboCasa365 (57.4%, up from prior SOTA 46.6%), RoboDojo (20.07, up from 13.07), VLABench, and RoboCasa (compared against RLDX-1 and GR00T N1.6 among others; no independent reproduction). Code/weights are "to be released," but the GitHub repo currently holds only a README — release not yet confirmed (as of 2026-08-01) | Confirmed code/weight release + independent benchmark reproduction |
| **[Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)** (Google DeepMind, whole-body-control VLA[^vla]) | 🟡 Preview | Official announcement (2026-07-30) `[4]` — extends prior upper-body-only control to whole-body control (walking, bending, two-hand coordination); launched alongside a reasoning model, Gemini Robotics ER 2, and an edge model, On-Device 2. Demoed on Apptronik Apollo 2 (92% success unscrewing a light bulb), self-reported benchmark, no independent validation. Only ER 2 has a public preview (AI Studio/Enterprise Agent Platform); VLA and On-Device 2 are early-access-partner only. ⚠️ [pillar-2](pillar-2.md)'s "Gemini Robotics" competitor-stack section is a pre-announcement snapshot (confirmed 2026-07, covers ER 1.6/On-Device/1.5) — needs a pillar-owner refresh | Early access ends, GA release + independent benchmark validation |

## ⚰️ Retired — do not propose (kept for the record)

| Item | Status | Replacement |
|---|---|---|
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 Discontinued (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 Discontinued (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 Discontinued (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA[^vla]** | ⚪ No public case `[4]` | Currently CUDA/NVIDIA (state the risk when proposing) |

> ⚠️ **Rumor watch (not true)**: "AWS IoT TwinMaker discontinued" is **misinformation** — TwinMaker is GA and open to new customers (low velocity). It is a third-party blog claim confused with SiteWise maintenance. Do not repeat. → [pillar-3](pillar-3.md).

---

## Promotion procedure (summary)

1. **Capture**: collect candidates via a designated channel/emoji
2. **Filter**: apply the [2.5 gate](maintenance.md#inclusion-criteria-the-filter) (2 or more of 4)
3. **If it passes**: the owning pillar's owner incorporates it via the [standard template](maintenance.md#standard-template) and removes it from the Radar
4. **If it falls short**: keep it here as a one-liner, with the promotion condition stated

Full pipeline → [maintenance](maintenance.md#playbook-promotion-pipeline).

---
_owner: Youngjin · updated: 2026-07 · volatility: high (the Radar changes fast by nature — monthly review recommended)_

<!-- 용어 각주 -->

[^wfm]: **World Foundation Model (WFM)** — a large model trained to predict/generate the next scenes of the physical world. From text/video prompts it creates physically plausible video and scenarios to augment robot training data. 🎥 [NVIDIA Cosmos introduction](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **SysID (System Identification)** — measuring the real robot's physical parameters (friction, mass, motor response) to calibrate the simulator to the real hardware.
[^s2r]: **sim-to-real** — transferring a policy trained in simulation to a real robot, or the methodology for doing so. The physical and visual differences between simulation and reality (the domain gap) mean a naive transfer collapses performance. 🎥 [NVIDIA sim-to-real robotics showcase](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **Physics engine** — the core software of a simulator that numerically computes rigid-body dynamics, contact, friction, and collision. An engine's accuracy-speed trade-off drives the choice of simulator (Isaac/MuJoCo/Genesis).
[^mcp]: **MCP (Model Context Protocol)** — an open standard protocol connecting agents to tools and data sources. Often likened to "USB-C for agents"; experiments exposing robot skills as MCP servers are growing.
[^ros]: **ROS 2 (Robot Operating System 2)** — the de facto standard open-source middleware for robot software. A distributed architecture in which sensor and control nodes communicate over topics; the shared foundation of industrial and research robot stacks.
[^agent]: **LLM agent** — software in which a large language model plans on its own, selects and calls tools (APIs, robot skills), and carries out multi-step tasks. Unlike simple Q&A, the key point is that it "acts."
[^vla]: **VLA (Vision-Language-Action)** — a foundation model that takes camera images (Vision) and natural-language instructions (Language) as input and directly outputs robot actions (Action). Say "pick up the cup" and it generates the joint motions. 🎥 [NVIDIA Isaac GR00T N1 introduction](https://www.youtube.com/watch?v=m1CH-mgpdYg)
