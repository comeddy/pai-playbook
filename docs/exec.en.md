---
ko_hash: 31a7299c4c1d83b76d8c7996a7b2032c7473f488
---
# Executive Brief — business value and investment approval

_Last updated: 2026-09 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: Choose one business task and compare existing automation and products. Expand investment after a bounded experiment establishes benefit, total cost, and operability.

## ① Why now?

Public models and simulation/training assets can be evaluated, but product releases and service GA do not establish customer profitability. Connect [model choices](pillar-2.md), [execution paths](execution.md), and [evidence](evidence.md) to form a hypothesis for your environment.

## ② What does this mean for our industry?

| Example task | Measure first | Alternatives |
|---|---|---|
| Manufacturing inspection/part handling | Defects, rework, cycle time, interventions | Existing vision/control improvements, commercial cells, SI |
| Logistics transport/loading | Throughput, downtime/recovery, environmental changes | Existing AMR/fleet products, process improvements |
| Robot product development | Data preparation/training/evaluation time, physical failures | Existing development-stack improvements, cloud experiments |

These are discovery examples. A particular model or humanoid is not the default answer for every task.

## ③ What is real and what is hype?

| Decision | Required conditions | Action |
|---|---|---|
| Bounded experiment | Measurable baseline, usage rights, owners, spending cap | Approve the [pilot card](start.md#pilot) |
| Site pilot | Improvement on separate evaluation; latency/safety/recovery test plan | Limited scope under supervision |
| Expand operations | Site outcomes, actual operating cost, interventions/recovery, support owners | Expand in stages |
| Hold/alternative | Unclear rights/safety ownership, more economical alternatives, repeated missed targets | Resolve gaps or choose another approach |

Do not use a generic “invest now because GA” or “results in 12–24 months” timetable. Separate product release, reproduction, and customer-site validation.

## ④ Where do we start?

Complete the [eight discovery questions](start.md#fit) and compare the current approach. If learning is needed, choose data collection, simulation, or fine-tuning for the present bottleneck. Separate preparation time from training runtime.

**Calculate ROI on total cost**: initial hardware, integration, data, staff, and safety validation; recurring maintenance, interventions, and cloud. Check payback in low/base/high scenarios using the [ROI worksheet](start.md#roi).

## ⑤ Why work with AWS?

Assess reuse of existing AWS data, security, and operations; measure small, then add services only as needed. [Decisions](decisions.md) covers single-GPU, managed, and multi-node choices. Assign cloud support, model-provider support, and robot/SI site responsibility separately.

Seoul availability does not guarantee Korea-only processing ([AgentCore evidence](evidence.md#agentcore-residency)). Code licenses alone do not establish commercial weight rights ([OpenVLA evidence](evidence.md#openvla-license)). Evaluate portability without promising “no lock-in.”

## To begin

The business owner, technical team, and AWS contact complete the [pilot approval card](start.md#pilot): **one task, baseline, spending/time caps, operations/safety owners, success/stop criteria**. Then follow [execution paths](execution.md) and [release gates](operations.md#release).

_owner: Youngjin · updated: 2026-09 · volatility: medium_
