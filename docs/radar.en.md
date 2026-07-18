---
ko_hash: 0f25aef6b593147b074982f677925d5b0fae9c1f
---
# Radar — Queue / Watchlist

_Last updated: 2026-07 · owner: TBD ⚠️ · volatility: high_
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
| **Hyundai 25,000 Atlas** | ⚪ Roadmap | 2028 start target, 0 units operating, union opposition | Real operation begins |
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

Full pipeline → [maintenance](maintenance.md#slack--playbook-promotion-pipeline).

---
_owner: TBD ⚠️ · updated: 2026-07 · volatility: high (the Radar changes fast by nature — monthly review recommended)_
