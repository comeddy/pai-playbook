---
ko_hash: 9fe285bbff72c7e9e5f35f761991bd3297d745ae
---
# Customer conversation guide — for AWS staff

_Last updated: 2026-09 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: Establish task, cost, and operating requirements before helping choose technology. This public guide contains no confidential customer or sales records. Show the [Executive Brief](exec.md) and complete [Start](start.md) with the customer.

## 1. Meeting flow

1. **Task**: identify repetitive work whose time, failures, or interventions should decrease.
2. **Alternatives**: compare existing automation, products, robot SI, and model adaptation.
3. **Experiment**: confirm rights, staffing, and limits; test one bottleneck.
4. **Exit conditions**: agree on success, stopping, handover, and evidence for the next meeting.

## 2. Key questions

| Question | Include in the answer | Tool |
|---|---|---|
| ROI? | Total hardware/SI/data/staff/safety/operations cost and realizable benefit, beyond GPU | [ROI](start.md#roi) |
| Why AWS? | Reuse of existing infrastructure, measured bottlenecks, needed services/support boundaries | [Decisions](decisions.md) |
| Staffing? | Robotics, ML, cloud, and site safety roles; partner/SI scope for gaps | [Owners](operations.md#layers) |
| When will we see results? | Range based on readiness/evaluation; no universal one-day or 12–24-month promise | [Execution](execution.md) |
| Safety? | Tool permissions plus independent physical safety, local control, cancellation/recovery tests, site approval | [Operations](operations.md) |
| Processing within Korea? | Check storage, inference, Memory/Evaluations, and external-tool routes separately | [Evidence](evidence.md#agentcore-residency) |
| Are open models commercial? | Version-specific code, weight, base-model, and dataset terms | [P2](pillar-2.md) |
| Partner selection? | Comparable site outcomes, robot support, integration/safety responsibility, recovery/maintenance scope | [Pilot card](start.md#pilot) |

## 3. Handover and support

AWS staff clarify service architecture, quotas, pricing, and service support. Robotics/ML teams own data, model/device compatibility, and evaluation. SI/site teams own process integration, safety, and operating recovery. Do not assume sample maintainers offer a customer operations SLA. Record owners and unresolved items.

## 4. Promises to avoid

| Avoid | Say instead |
|---|---|
| “Seoul GA means no residency problem” | “We will inspect storage and processing per feature/model” |
| “OpenVLA is MIT, so commercial use is allowed” | “We will check code and weight terms separately” |
| “100 demos gives 80% in one day” | “We will measure data/time needs under fixed evaluation conditions” |
| “Cedar guarantees robot safety” | “Independent safety, local control, and site validation are also required” |
| “Open models eliminate lock-in” | “We will compare migration costs for models, data, and operating tools” |

**➡️ Next action**: share a one-page decision, spend/time caps, owners, and evidence required for the next stage.

_owner: Youngjin · updated: 2026-09 · volatility: medium_
