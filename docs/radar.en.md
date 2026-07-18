---
ko_hash: a0371a51b08ec4fdde1085e51939e6ee9a061ec9
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

## 🆕 Latest scan intake (2026-07 · public research — pending primary verification)

<!-- Intake from automated scan (arXiv/web). All 🔵/⚪/🟡 unverified — do not use in customer proposals until they pass THE FILTER. See scripts/radar_scan.md for the periodic refresh. -->

| Item | Label | Why waiting | Promotion criteria |
|---|---|---|---|
| **AgiBot 15,000th unit total + Longcheer line deployment** | 🟡 Pilot | ⚠️ "15,000 units mass-produced" is inaccurate — actually the **15,000th robot delivered overall (own factories)** + **8 G2 robots on one Longcheer line** `[3]`. The 6-day 99.99% demo (64,828 operations) is real but not independently validated; dataset licensing → [pillar-1](pillar-1.md) | Independent productivity validation + line expansion |
| **DSWAM** (Dual-System World Action Foundation Model) | 🔵 Research | 2026-07 preprint, single lab. Claims a dual-system architecture for fine-grained manipulation `[4]` | peer review + reproduction |
| **Actuator Reality Shaping** (zero-shot sim-to-real) | 🔵 Research | 2026-07 preprint, claims to close the actuator-dynamics gap (legged robots and humanoids) `[4]` | peer review + reproduction |
| **Kairos** (regret-aware world-action model stack) | 🔵 Research | 2026-06 preprint, claims a full-stack Physical AI approach `[4]` | primary confirmation + independent reproduction |
| **1X NEO 25-DoF tendon-driven hand** | 🟡 Pre-order | Hand is real `[3]`; claims pre-orders sold out (10k in 5 days) but **0 verified customer deliveries** — currently pre-order ($20k / $499-mo), consumer shipments "planned" for late 2026. "Shipping" wording is marketing | Verified deliveries + validated autonomous manipulation case |
| **ULTRA** (unified multimodal humanoid whole-body loco-manipulation) | 🔵 Research | 2026-03 preprint, claims perception-driven behavior generation without predefined motion references `[4]` | peer review + reproduction |

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
