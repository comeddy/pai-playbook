---
ko_hash: c52bf32e3cb8f788b6384f47337ac5a43f993bf1
---
# Evidence — per-claim dates, scope, and review status

_Last updated: 2026-09 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: A page edit date does not revalidate every claim. These seven records cover the core corrections in this review. Other legacy claims are not yet migrated; this is not a full factual audit.

`source-checked` means compared with the named primary sources; `withdrawn` removes an earlier generalization/promise; `reproduction-pending` awaits execution. All records are **pending human review**, not official AWS approval or guarantees. Source comparison, experimental reproduction, and site release approval are separate stages.

The source data is [claims.json](assets/claims.json). These blocks are generated from it. CI checks required fields, all languages, affected pages, dates, and rendering consistency, and warns on overdue review. It does not judge source truth or fitness for a customer site.

<!-- evidence:start -->

### openvla-license { #openvla-license }

OpenVLA distinguishes MIT code from Llama-2-derived pretrained weights subject to the Llama Community License. Check the selected weights, base model, and data terms; the code LICENSE alone does not decide commercial use.

- Checked: 2026-09-15 · Status: `source-checked` · Review interval (days): 30
- Compared by: Codex (source comparison) · Human review: pending
- Affected pages: [pillar-2](pillar-2.md) · [decisions](decisions.md) · [exec](exec.md)
- Sources: [OpenVLA README](https://github.com/openvla/openvla#pretrained-vlas)

### agentcore-residency { #agentcore-residency }

AgentCore availability, storage, and inference-processing Regions differ. Memory can infer across APAC Regions; Evaluations originating in Seoul uses global cross-region inference. Assess Korea-only processing per feature, model, and route.

- Checked: 2026-09-15 · Status: `source-checked` · Review interval (days): 30
- Compared by: Codex (source comparison) · Human review: pending
- Affected pages: [pillar-5](pillar-5.md) · [decisions](decisions.md) · [exec](exec.md) · [operations](operations.md)
- Sources: [AWS cross-region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html) · [AWS Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-cross-region-inference.html)

### fleetwise-new-customers { #fleetwise-new-customers }

IoT FleetWise is closed to new customers; existing customers can continue using it. Do not describe it as terminated or make it a default for new robot-fleet architectures.

- Checked: 2026-09-15 · Status: `source-checked` · Review interval (days): 30
- Compared by: Codex (source comparison) · Human review: pending
- Affected pages: [pillar-5](pillar-5.md) · [radar](radar.md)
- Sources: [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)

### action-chunking { #action-chunking }

Action output count is not the frequency of responding to new observations. Inference Hz times chunk length is not feedback-control frequency. PI treats transitions and latency separately; Helix S1/S2 are both onboard, not evidence for cloud placement.

- Checked: 2026-09-15 · Status: `source-checked` · Review interval (days): 90
- Compared by: Codex (source comparison) · Human review: pending
- Affected pages: [pillar-2](pillar-2.md) · [pillar-4](pillar-4.md) · [pillar-5](pillar-5.md) · [decisions](decisions.md) · [operations](operations.md)
- Sources: [PI real-time chunking](https://www.physicalintelligence.company/research/real_time_chunking) · [Figure Helix](https://www.figure.ai/news/helix)

### simulation-cost { #simulation-cost }

Withdraw the generalized “Seoul g6e.xlarge + 4–20 minutes = $11–12 per training run.” $0.98/hour for 4–20 minutes gives only an arithmetic $0.07–0.33, not a measurement on that instance. The sample author’s roughly 2-hour/$12 estimate uses a different setup.

- Checked: 2026-09-15 · Status: `withdrawn` · Review interval (days): 30
- Compared by: Codex (source comparison) · Human review: pending
- Affected pages: [pillar-3](pillar-3.md) · [execution](execution.md) · [exec](exec.md)
- Sources: [Pinned simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [ETH parallel RL paper](https://arxiv.org/abs/2109.11978)

### finetuning-outcomes { #finetuning-outcomes }

Withdraw universal promises of “100–500 demonstrations → 80%+ success” or a one-day result from 100 demos. Success and duration require experiments with specified data, task, model, training, and evaluation conditions.

- Checked: 2026-09-15 · Status: `withdrawn` · Review interval (days): 90
- Compared by: Codex (source comparison) · Human review: pending
- Affected pages: [pillar-2](pillar-2.md) · [exec-guide](exec-guide.md) · [decisions](decisions.md) · [execution](execution.md)
- Sources: [OpenVLA fine-tuning](https://github.com/openvla/openvla#fine-tuning-openvla-via-lora)

### execution-samples { #execution-samples }

Compared commits, READMEs, and commands for three samples; no AWS or robot execution in this revision. The training author reports a completed Pattern A run; B/C, RL, and forced interruption/recovery must not be presented as equally validated.

- Checked: 2026-09-15 · Status: `reproduction-pending` · Review interval (days): 30
- Compared by: Codex (source comparison) · Human review: pending
- Affected pages: [execution](execution.md) · [pillar-1](pillar-1.md) · [pillar-2](pillar-2.md) · [pillar-3](pillar-3.md)
- Sources: [Data sample](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) · [Simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [Training sample](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac)

<!-- evidence:end -->

## Updating and assigning review { #review }

Owner Youngjin assigns review work. Human reviewers for licensing, AWS services/Regions, robot control/safety, and reproduction are **not yet assigned**; do not invent names. Record source comparers; set `human_review: complete` only with the actual named human reviewer.

When a claim changes, update affected originals, summaries, and translations listed in `pages`, and its check date/evidence. Run `python3 scripts/check_evidence.py --render`, update translation hashes, then run all checks. HTTP 200, successful builds, and translation hashes do not replace factual verification.

_owner: Youngjin · updated: 2026-09 · volatility: medium_
