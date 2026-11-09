---
ko_hash: 445c03453543105e049a872bd347a312022be139
---
# Start — business fit, ROI, and pilot approval

_Last updated: 2026-11 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: Start with the work, not the technology. Write down which task you want to improve and how well it runs today. Then check whether existing automation, a commercial product, or a system integrator (SI)[^si] can already solve it. Only when something is left that the robot has to learn do you look at data, simulation, or a VLA. Customers and AWS staff fill in this worksheet together.

## Paths by role { #roles }

| Role | Read first | Meeting output |
|---|---|---|
| Customer decision maker | This page → [Executive Brief](exec.md) | One task, spending cap, proceed/hold criteria |
| Customer engineering team | [Execution paths](execution.md) → relevant pillar → [Operations and recovery](operations.md) | Prerequisites, experiment plan, owners |
| AWS staff | [Conversation guide](exec-guide.md) → [Decisions](decisions.md) | Discovery questions, alternatives, support/partner roles |

Staff guidance is also public. Do not record internal contacts or confidential customer material on this site.

## Business fit — eight discovery questions { #fit }

| Question | Complete with the customer |
|---|---|
| What task needs improvement? | Process, objects, environment, and start/completion conditions in one sentence |
| How well does it work today? | Completions/hour, cycle time, failure/rework rate, human interventions |
| Why is the current approach insufficient? | Compare rule-based automation, controller improvements, products, and SI quotes |
| Which variation needs learning? | Object, lighting, layout, or instruction changes and their actual frequency |
| What is already available? | Robot, sensors, logs, demonstrations, CAD, usage rights, staff |
| What constrains the site? | Human access, outages, latency, power, countries processing data |
| Who operates and recovers it? | Named site, robotics/SI, ML, and cloud owners |
| What would stop the pilot? | Budget/time caps, minimum improvement over baseline, safety/recovery conditions |

**Proceed** when the task and baseline are measurable and there is an improvement hypothesis, experimental capacity, and an operating owner. **Hold** when rights, site responsibility, or spending limits are unresolved. **Choose an alternative** when a product or existing automation meets the need at lower total cost. Record the choice in [Build vs Buy](decisions.md#4-build-vs-buy-foundation-models).

## Total cost and ROI — beyond the GPU quote { #roi }

Model **low/base/high scenarios**. Mark unknown costs as ‘quote pending’, not zero. Enter quantities, rates, and the period in the calculator below; results update instantly, and you can download the inputs and results as CSV to attach to project documents (USD worksheet, not a price list).

| Cost group | Include |
|---|---|
| Initial fixed | Robot, gripper, sensors, installation/SI, data collection/cleaning, environment creation, safety review/validation |
| Experiment variable | GPU instance hours, storage/transfer/logs, models/APIs, failed runs/retries, engineering time |
| Recurring operations | Maintenance, parts, supervision, interventions, inference/connectivity, retraining/site revalidation |
| Expected benefit | Actual reductions in rework/downtime, realizable throughput value, staff time that can be reassigned |

| Metric | How to calculate | How to read it |
|---|---|---|
| **Initial investment** | Initial fixed + experiment variable | One-time spend from pilot start until validation is done |
| **Period operating cost** | Monthly recurring ops × period (months) | Ongoing spend over the analysis period |
| **Period benefit** | Monthly expected benefit × period (months) | Value actually realized over the analysis period |
| **Period net benefit** | Period benefit − period operating cost | What operations leave over — before subtracting the initial investment |
| **Payback period** | Initial investment ÷ monthly net benefit | Months needed to earn back the initial investment. If monthly net benefit (monthly benefit − monthly ops) is zero or less: ‘no payback’ |
| **Period ROI** | (Period benefit − initial investment − period operating cost) ÷ (initial investment + period operating cost) | Return on everything spent. Below 0% means a loss within the analysis period |

<div class="pai-roi-calc"><noscript><p>The calculator needs JavaScript. Without it, calculate with the table above.</p></noscript></div>

Simulation can reduce experimentation costs, but does not eliminate environment creation, calibration, or physical validation. Do not count productivity and labor savings twice for the same benefit. Record sources and check dates for estimates and benefit assumptions.

## Pilot approval card { #pilot }

Copy this block into the project document. Duration, demonstration counts, and success rates are customer-specific agreements, not universal promises.

```text
Task / exclusions:
Current approach / alternatives / baseline measurement period:
Target metric / minimum improvement / measurement conditions:
Evaluation sample size / repeated runs / unseen environments:
Data, code, and weight usage rights:
Owners: site / robotics-SI / ML / cloud / safety:
Cost: initial / experiment / monthly operations / low-base-high:
Limits: maximum spend / end date / extension approver:
Stop: target missed / budget exceeded / safety-recovery test failed:
Evidence and approver required for the next stage:
```

**Stage gates**: establish a baseline → [isolated experiment](execution.md) → [limited site validation](operations.md) → expand operations. Review metrics, cost, interventions, and recovery at every gate. A technology's GA status or a generic ‘12–24 months’ forecast does not approve the next stage.

**➡️ Next action**: complete one card in the next customer meeting and decide proceed, hold, or an alternative. If proceeding, select just one of the [three execution paths](execution.md) for the current bottleneck.

<!-- 용어 각주 -->
[^si]: **SI (System Integrator)** — A provider integrating robots, equipment, controls, and software at the customer's site. Cloud service support and responsibility for cell integration/safety must be assigned separately.

_owner: Youngjin · updated: 2026-11 · volatility: medium_
