---
ko_hash: d9f429a22b7169dd04e5a4022773ba6fa3f7bf9f
---
# Radar — Queue / Watchlist

_Last updated: 2026-07 · owner: comeddy · volatility: high_
[← back to index](index.md)

> **L0 TL;DR**: Things **worth watching** that have not yet passed the inclusion criteria ([2.5 THE FILTER](maintenance.md#inclusion-criteria-the-filter)). Each item is one line — a maturity label + **why it is on hold**. Once it clears the gate (2 of 4), the owning pillar's owner promotes it using the standard template.
>
> ⚠️ **Do not present items here as "mature capabilities" in customer proposals.** A flashy demo often masks how deployable something actually is.

---

## 🔬 Models / algorithms (awaiting validation)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| Physical Intelligence **π0.7** | 🔵 Research | Secondary sources only `[4]`, no primary PI confirmation | Official PI release + performance validation |
| **GR00T N1.6 / N1.7 commercial license** | 🟡→ | Commercial-use claim is secondary-source only `[4]` (N1.5 is clearly non-commercial per model card `[1]`) | License confirmed on live model card |
| **World-action models** (DreamZero → GR00T N2) | 🟡 Preview | GR00T N2 "expected end of year," DreamZero is research | GA + real deployment case |
| Google DeepMind **Genie 3** (world model for robot learning) | 🟡 Preview | The world model itself is preview; applying it to robot learning is research | Validated case of robot policy learning |
| **VLM-based SysID** (Vid2Sid, Swim2Real) | 🔵 Research | 2026 preprints, single lab | peer-review + reproduction |
| **VIRAL / VideoMimic / Real2Render2Real** (visual sim-to-real at scale) | 🔵 Research | CVPR/CoRL research, not production | Evidence of production deployment |
| **Robbyant LingBot-VLA / UnifoLM-VLA-0** | 🔵 Research | Secondary sources, no validation | Primary confirmation + AWS mapping |

## 🖥️ Simulation / tools (awaiting maturity)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| **Genesis** physics engine | ⚪ Hype | "430,000×" refuted `[1]`, slow on contact-rich manipulation | Independent benchmark + production adoption |
| **MuJoCo Warp** | 🟡 Alpha | PyPI classifier "3-Alpha" `[1]`, not production | Beta/GA transition |
| **NVIDIA Newton** physics engine | 🟡 Preview | Experimental backend in Isaac Sim 6.0 | GA + official in Isaac Lab 3.0 |
| **Isaac Sim 6.0** | 🟡 Preview | "Early Developer Release," API in flux (latest GA is 5.1) | 6.x GA declaration |
| **Cosmos 3 as sim-to-real training source** | 🟢 GA(model)/🔵(in practice) | Model is GA, but "training deployable policies from world-model data" is early-adopter only. ⚠️ **not hosted on AWS** | Stronger AWS mapping + training validation |

## 🤖 Hardware / deployment (roadmap / demo)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | Musk claims only, production not started | Validated deployment |
| **Hyundai·BD electric Atlas** | ⚪ Roadmap | Electric Atlas product version unveiled (2026-07, BD official `[3]`). Deployment 25k+ units & 30k/yr capacity both **start 2028**; ~0 in live production today. 2026 is a small pilot only (Hyundai RMAC + Google DeepMind). ⚠️ "Gen 5" is a misnomer | Verified real-operation shipments begin |
| **Apptronik Apollo 2 + Robot Park** | 🟡 Pilot | Operational pilots at Mercedes-Benz & GXO `[3]` + Google DeepMind Gemini Robotics data partnership (90k sq ft). Autonomy/commercial scale unverified. AWS mapping is generic (data→S3/SageMaker); the partnership itself is Google `[4]` | Commercial deployment scale + validated autonomy |
| **1X Neo** autonomy | 🟡 Preview | Product shipped but autonomy ~60–70%, rest is VR teleoperation | Validation of true autonomy |
| **Figure 03 "8-hour autonomous shift"** | ⚪ Hype | CEO tweet, no independent validation (Figure 02@BMW is a validated pilot) | Third-party autonomy audit |
| **Cosmos 3 adoption** (Doosan/LG/Samsung) | 🟢 GA(announced) | Adoption is "announced," not production-validated | Public production case |

## 🔗 Agents / connectivity (early)

| Item | Label | Why on hold | Promotion condition |
|---|---|---|---|
| **MCP for robotics** (ros-mcp-server, etc.) | 🔵 Research | 50+ servers exist but open-source/demo, none in production (safety, latency, determinism unvalidated) | Production-hardening case |
| **ROS 2 + LLM agents** (NASA JPL ROSA, RAI) | 🔵 Research | ROSA (JPL) is the strongest real case but mock-ops. Field deployment limited | Field production deployment |
| **Agent physical-safety standards** (RoboGuard, etc.) | 🔵 Research | ISO covers physical only; no standard for LLM semantic risk | Progress on standardization |
| **AgentCore Payments / Agent Registry (Seoul)** | 🟡 Preview/unavailable | Not available in Seoul region (Tokyo Agent Registry ✅) | Seoul region expansion |

## 🆕 Latest scan intake (2026-07-29 · primary verification completed 2026-07-21)

<!-- Intake from automated scan (arXiv/web). Primary-source verification completed 2026-07-21 (4 verification agents, cross-checked against official announcements and arXiv originals) — 0 promoted, 6 corrected. Do not use in customer proposals until they pass THE FILTER. See scripts/radar_scan.md for the periodic refresh. -->

| Item | Label | Why waiting | Promotion criteria |
|---|---|---|---|
| **RLWRLD RLDX-1** (dexterity-first foundation model) | 🟡 Preview | Weight release is real but ⚠️ not open source — RLWRLD Model License v1.0 (non-commercial, commercial distribution prohibited) `[3]`; a 7–9B family (flagship 8.1B). RoboCasa/LIBERO/SIMPLER SOTA is self-reported, no independent reproduction ([aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws) provides measured n=5 smoke runs on EC2 — not a full benchmark reproduction). AWS connection is limited to simulation benchmarking (a use the non-commercial license explicitly permits; no commercial positioning) — "no connection" wording updated (2026-07). 0 real customer deployments | Independent benchmark reproduction + validated deployment case |
| **NEURA Robotics × AWS strategic collaboration** | ⚪ Hype/roadmap | Confirmed via official AWS press release, 2026-04-21 `[1]` — AWS as primary cloud, Neuraverse hosting + NEURA Gym/SageMaker integration stated explicitly. But the fulfillment-center wording is "explore opportunities to deploy" — 0 live deployments. The NEURA Gym RWTH Aachen training-network expansion (announced 2026-07-22) makes no mention of AWS — tracked as a separate thread | Public case of actual AWS infra use + validated fulfillment-center deployment |
| **Actuator Reality Shaping** (zero-shot sim-to-real) | 🔵 Research | Existence confirmed (arXiv 2607.02205, 2026-07-02) `[1]` — validated on 4 real hardware platforms (including humanoid walking); the summary matches the abstract (no corrections). Not peer-reviewed | peer review + independent reproduction |
| **AgiBot 15,000th unit total + Longcheer line deployment** | 🟡 Pilot | Cumulative **15,000 units off the production line**, and the 15,000th was **delivered to customer Longcheer's factory** ("own factories" corrected) + 8 G2 robots on one quality-inspection line `[3]`. The 6-day 99.99% demo (64,828 operations, 17,625 products) is real but vendor-controlled, no independent validation; dataset licensing → [pillar-1](pillar-1.md) | Independent productivity validation + line expansion |
| **AgiBot World 2026** (open-source real-world robot manipulation dataset, phased 5-track release) | 🔵 Research | AgiBot official release (HuggingFace `agibot-world/AgiBotWorld2026`, 2026-07) `[4]` — 100% real-world data captured on the AgiBot G2 platform, 5 research tracks (imitation learning, etc.) to be released in phases; the first tranche covers several hundred hours from commercial/service environments. License and commercial-use terms unconfirmed; no independent benchmark or training-validation case yet. Distinct from the "AgiBot 15,000th unit" row above (production volume) — this covers only the data track | License confirmed + independent training validation (SOTA reproduction) case |
| **AXIS** (community-driven, growable robot-manipulation data engine) | 🔵 Research | Existence confirmed (arXiv 2607.21588, 2026-07-23) `[4]` — 8 universities + Axis Robotics; crowdsourced via browser-based MuJoCo-WASM teleoperation, then augmented in IsaacSim. Simulation-only on a Franka arm (207 tasks, 50k+ trajectories); reports +4.9pp on LIBERO-Plus from π0.5 continual pretraining (self-reported benchmark, no independent reproduction). Authors themselves list sim-to-real as future work — unvalidated on real hardware | peer review + real-hardware sim-to-real validation |
| **AMD Ryzen AI Embedded X100 + Kria AI SoM** (robot edge compute, positioned against NVIDIA Jetson Thor) | ⚪ Hype/roadmap | AMD official announcement `[4]` (2026-07-24) — Zen 5 CPU, RDNA 3.5 iGPU, XDNA 2 NPU with unified memory (up to 128GB); claims 3x FP32 over Jetson Thor and 2.1x multithread over Intel (self-reported benchmarks, no independent validation). SOM mass production planned for Q4 2026 (Arbor, Congatec, etc.); 0 robot edge deployments today | Independent benchmark + real robot edge-deployment case |
| **NVIDIA Cosmos 3 Edge** (Cosmos 3-family, on-device 4B world model + policy) | 🟡 Preview | NVIDIA official announcement `[4]` (2026-07-21, HuggingFace/developer blog) — on-device inference on Jetson Thor for real-time 15Hz robot policy control (self-reported benchmark, no independent validation); Cosmos 3 Edge Policy (DROID) supports pick-and-place fine-tuning. Distinct from the existing "Cosmos 3 as sim-to-real training source" entry (🖥️ section) — this covers only the edge-deployment track; watch alongside AMD Ryzen AI Embedded X100 (this table) as a competing approach. 0 production robot deployments today | Independent benchmark + real production robot-deployment case |
| **Mistral AI Robostral Navigate** (8B single-RGB-camera robot navigation VLA) | 🟡 Preview | Mistral official announcement (2026-07-08) `[4]` — a foundation-model lab's new entry into Physical AI (watch as a competitive-landscape signal). Trained entirely in simulation (~400k trajectories, 6k scenes); navigates from a single RGB camera + language instruction with no LiDAR/depth sensor; R2R-CE unseen 76.6% is self-reported, no independent reproduction. 0 real-world deployments or customer cases; AWS Bedrock connection unconfirmed | Independent real-hardware validation + confirmed AWS mapping (e.g. Bedrock) + real deployment case |
| **NVIDIA Halos for Robotics** (full-stack robot safety system) | 🟡 Preview | NVIDIA official announcement `[1]` (2026-06-23) — IGX Thor + Holoscan Sensor Bridge + Halos OS + ANAB-accredited Inspection Lab. First adopter Agility is deploying it at Amazon, GXO, Schaeffler, and Toyota sites `[4]` (adoption is per NVIDIA/Agility announcements only; no completed third-party safety certification yet — the Inspection Lab is at the "certification-readiness support" stage). Distinct from the existing "agent physical-safety standards" entry (🔗 section, focused on LLM semantic risk) — this covers only the hardware functional-safety axis. No direct AWS connection announced (Amazon here is Agility's end customer, not an AWS service tie-in) | Verified third-party certification case (TÜV, etc.) + confirmed AWS infrastructure connection |

## ⚰️ Retired — do not propose (kept for the record)

| Item | Status | Replacement |
|---|---|---|
| **AWS RoboMaker** | 🔴 Discontinued (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **SageMaker Edge Manager** | 🔴 Discontinued (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **IoT Greengrass V1** | 🔴 Discontinued (2026-06-01) `[1]` | Greengrass V2 |
| **Gazebo Classic 11** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ No public case `[4]` | Currently CUDA/NVIDIA (state the risk when proposing) |

> ⚠️ **Rumor watch (not true)**: "AWS IoT TwinMaker discontinued" is **misinformation** — TwinMaker is GA and open to new customers (low velocity). It is a third-party blog claim confused with SiteWise maintenance. Do not repeat. → [pillar-3](pillar-3.md).

---

## Promotion procedure (summary)

1. **Capture**: collect candidates via a designated channel/emoji
2. **Filter**: apply the [2.5 gate](maintenance.md#inclusion-criteria-the-filter) (2 or more of 4)
3. **If it passes**: the owning pillar's owner incorporates it via the [standard template](maintenance.md#standard-template) and removes it from the Radar
4. **If it falls short**: keep it here as a one-liner, with the promotion condition stated

Full pipeline → [maintenance](maintenance.md#playbook-promotion-pipeline).

---
_owner: comeddy · updated: 2026-07 · volatility: high (the Radar changes fast by nature — monthly review recommended)_
