---
ko_hash: 026bab16f8923b50ce259438e0b8e935060a9b0c
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

## 🆕 Latest scan intake (2026-07-25 · primary verification completed 2026-07-21)

<!-- Intake from automated scan (arXiv/web). Primary-source verification completed 2026-07-21 (4 verification agents, cross-checked against official announcements and arXiv originals) — 0 promoted, 6 corrected. Do not use in customer proposals until they pass THE FILTER. See scripts/radar_scan.md for the periodic refresh. -->

| Item | Label | Why waiting | Promotion criteria |
|---|---|---|---|
| **RLWRLD RLDX-1** (dexterity-first foundation model) | 🟡 Preview | Weight release is real but ⚠️ not open source — RLWRLD Model License v1.0 (non-commercial, commercial distribution prohibited) `[3]`; a 7–9B family (flagship 8.1B). RoboCasa/LIBERO/SIMPLER SOTA is self-reported, no independent reproduction ([aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws) provides measured n=5 smoke runs on EC2 — not a full benchmark reproduction). AWS connection is limited to simulation benchmarking (a use the non-commercial license explicitly permits; no commercial positioning) — "no connection" wording updated (2026-07). 0 real customer deployments | Independent benchmark reproduction + validated deployment case |
| **NEURA Robotics × AWS strategic collaboration** | ⚪ Hype/roadmap | Confirmed via official AWS press release, 2026-04-21 `[1]` — AWS as primary cloud, Neuraverse hosting + NEURA Gym/SageMaker integration stated explicitly. But the fulfillment-center wording is "explore opportunities to deploy" — 0 live deployments | Public case of actual AWS infra use + validated fulfillment-center deployment |
| **TACO** (Tactile World Model as Self-Corrector for VLA post-training) | 🔵 Research | Existence confirmed (arXiv 2607.02840, 2026-07-03) `[1]` — 4-institution collaboration ("single lab" corrected), real-robot Franka experiments on 6 tasks, +44%p absolute. Not peer-reviewed | peer review + independent reproduction |
| **MotionWAM** (foundation world-action model for real-time humanoid loco-manipulation) | 🔵 Research | Existence confirmed (arXiv 2606.09215, 2026-06-08) `[1]` — 3-institution collaboration ("single lab" corrected), real Unitree G1 experiments on 9 tasks at 76.1% (+32%p absolute over GR00T-N1.7). Not peer-reviewed | peer review + independent reproduction |
| **Kairos** (regret-aware native world-action model stack) | 🔵 Research | Existence confirmed (arXiv 2606.16533, 2026-06-15) `[1]`, code released. ⚠️ "Full stack" is an overstatement — no real-robot closed-loop validation (the authors themselves list it as future work); simulation and benchmarks only | Real-robot closed-loop validation + independent reproduction |
| **Actuator Reality Shaping** (zero-shot sim-to-real) | 🔵 Research | Existence confirmed (arXiv 2607.02205, 2026-07-02) `[1]` — validated on 4 real hardware platforms (including humanoid walking); the summary matches the abstract (no corrections). Not peer-reviewed | peer review + independent reproduction |
| **AgiBot 15,000th unit total + Longcheer line deployment** | 🟡 Pilot | Cumulative **15,000 units off the production line**, and the 15,000th was **delivered to customer Longcheer's factory** ("own factories" corrected) + 8 G2 robots on one quality-inspection line `[3]`. The 6-day 99.99% demo (64,828 operations, 17,625 products) is real but vendor-controlled, no independent validation; dataset licensing → [pillar-1](pillar-1.md) | Independent productivity validation + line expansion |
| **1X NEO 25-DoF tendon-driven hand** | 🟡 Pre-order | Hand specs (25 DoF, tendon-driven, tactile skin) officially confirmed `[3]`; "10k pre-orders sold out in 5 days" is 1X's own claim, not independently verified. **0 verified consumer deliveries** ($20k or $499/mo; shipments planned for late 2026) — early home placements are teleop pilots, and the autonomy rate is 1X's own estimate of 60–70% | Verified deliveries + validated autonomous manipulation case |
| **Anthropic × Physical Intelligence acquisition rumor** | ⚪ Hype/roadmap | Social rumor (Scoble tweet) broke 2026-07-19 → The Information reported "acquisition talks did happen in spring 2026," but no actual acquisition; PI CEO Karol Hausman denied it internally on Slack `[4]` — secondary reporting only, no primary confirmation from either party. PI runs on GCP (see pillar-2) and is an OpenAI portfolio company, so a deal would matter for the cloud/competitive landscape | Official statement from either party (deal completed or explicitly off) |
| **AXIS** (community-driven, growable robot-manipulation data engine) | 🔵 Research | Existence confirmed (arXiv 2607.21588, 2026-07-23) `[4]` — 8 universities + Axis Robotics; crowdsourced via browser-based MuJoCo-WASM teleoperation, then augmented in IsaacSim. Simulation-only on a Franka arm (207 tasks, 50k+ trajectories); reports +4.9pp on LIBERO-Plus from π0.5 continual pretraining (self-reported benchmark, no independent reproduction). Authors themselves list sim-to-real as future work — unvalidated on real hardware | peer review + real-hardware sim-to-real validation |

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
