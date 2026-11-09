---
ko_hash: 248931244fee0386e2cf7fac8c357a66618fa72c
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

Before the pilot starts, answer the 10 questions below together with the customer. **If any field is still empty, it is not yet time to start.** The examples are hypothetical values for illustration. Duration, demonstration counts, and success rates are customer-specific agreements, not universal promises.

| # | Field | In plain words | Example (hypothetical) |
|---|---|---|---|
| 1 | Task / exclusions | What exactly will the robot do? What will it **not** do this time? | Pick parts from mixed bins into trays. Damaged-part handling and night shifts excluded |
| 2 | Current approach / alternatives / baseline measurement period | How is it done today, and how well? Will you also compare non-robot options (existing automation, off-the-shelf products)? How many days will you measure today's performance as the baseline? | 2 operators, 300 parts/hour, 2% errors. Compared with a quote for a commercial picking cell. Measured for 2 weeks |
| 3 | Target metric / minimum improvement / measurement conditions | What defines success? What is the smallest improvement that matters? Under which conditions is it measured? | Success rate and hourly throughput. At least 20% more throughput than the baseline. Measured at real line speed and lighting |
| 4 | Evaluation sample size / repeated runs / unseen environments | How many trials? Are results similar when repeated? Does it work on objects and layouts not seen in training? | 200 attempts, repeated over 3 days, including 5 part types absent from training |
| 5 | Data, code, and weight usage rights | Who owns the collected data, the code, and the trained model files (weights), and can they be used commercially? | Data owned by the customer. Confirm the open model's license allows commercial use |
| 6 | Owners | Is there one named owner per area? | One each for site operations, robotics/SI, ML, cloud, and safety |
| 7 | Cost | What is the upfront cost, the experiment-period cost, and the monthly cost once running? Give low, base, and high values | Initial / experiment / monthly operations, each as low-base-high |
| 8 | Limits | How much can be spent, and until when? Who approves an extension? | Spending cap, end date, extension approved by the business-unit head |
| 9 | Stop conditions | When will you stop? Decide before starting | Minimum improvement missed by the end date, spending cap exceeded, or emergency-stop/recovery test failed |
| 10 | Next-stage evidence / approver | What must be shown to move to the next stage, and who approves it? | Evaluation report, actual costs, safety checklist → plant manager approval |

Copy the block below into the project document and fill it in.

```text
1. Task: what the robot will do / what is excluded this time:
2. Baseline: current approach and performance / alternatives to compare / measurement period:
3. Target: success metric / minimum improvement / measurement conditions:
4. Evaluation: number of trials / repetitions / environments unseen in training:
5. Rights: ownership and permitted use of data, code, and model (weights):
6. Owners: site / robotics-SI / ML / cloud / safety:
7. Cost (low-base-high): initial / experiment / monthly operations:
8. Limits: maximum spend / end date / extension approver:
9. Stop conditions: target missed / budget exceeded / safety-recovery test failed:
10. Next stage: evidence to show / approver:
```

**Stage gates**: establish a baseline → [isolated experiment](execution.md) → [limited site validation](operations.md) → expand operations. Review metrics, cost, interventions, and recovery at every gate. A technology's GA status or a generic ‘12–24 months’ forecast does not approve the next stage.

**➡️ Next action**: complete one card in the next customer meeting and decide proceed, hold, or an alternative. If proceeding, select just one of the [three execution paths](execution.md) for the current bottleneck.

<!-- 용어 각주 -->
[^si]: **SI (System Integrator)** — A provider integrating robots, equipment, controls, and software at the customer's site. Cloud service support and responsibility for cell integration/safety must be assigned separately.

_owner: Youngjin · updated: 2026-11 · volatility: medium_
