---
ko_hash: 62cd1ee818e1aa36c2df871bece506e62dd803f7
---
# News

_owner: Youngjin · updated: 2026-09 · volatility: high_

> **L0 TL;DR**: Selected new AWS Physical AI articles, linked to the existing pillars. Dates below are **publication dates**; this list was checked on **2026-09-19**. Follow [Workshops & Resources](workshops.md) for learning paths.

Summaries are based on official articles, not independent reproduction of their performance claims. Unverified technology candidates remain in [Radar](radar.md).

## Recent resources at a glance

| Published | Resource | Connects to |
|---|---|---|
| 2026-09-10 | [π0 fine-tuning on SageMaker HyperPod EKS](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence’s DreamZero experiment](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics: AI for solar-panel placement](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics: teaching humanoids to use tools](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [Industrial digital twins with OpenUSD and SDMA](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-15 | [Config: augmenting robot training data](#config) | [P1](pillar-1.md) |

## π0 fine-tuning on SageMaker HyperPod EKS { #pi0-hyperpod }

**Published: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

Walks through π0 VLA[^vla] training/evaluation on DROID and LIBERO, connecting HyperPod EKS, FSx for Lustre, and training-job configuration.

**Scope to check**: Official implementation guide. Reported evaluation is n=5 open-loop[^openloop], not physical task success. The linked code path was not publicly accessible on 2026-09-19; start with the article.

**Next action**: P2 Training · π0 reading path — [P2](pillar-2.md) · [π0](workshops.md#pi0-guide).

## Telexistence’s DreamZero experiment { #telexistence-dreamzero }

**Published: 2026-09-09 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/bringing-a-frontier-world-model-to-the-convenience-store-inside-telexistences-dreamzero-experiment-on-aws/) `[3]`**

Covers retail-robot data conversion/curation, DreamZero adaptation, and simulation/physical evaluation in a customer experiment using EC2 and S3.

**Scope to check**: Customer experiment/PoC. Distinguish existing retail-robot operations from the DreamZero experiment’s results.

**Next action**: P1 Data · P2 Training · P4 Evaluation — [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md).

## Luminous Robotics: AI for solar-panel placement { #luminous }

**Published: 2026-08-12 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/teaching-robots-to-see-how-luminous-robotics-is-accelerating-energy-infrastructure-construction-with-vision-action-ai/) `[3]`**

Explores vision-based policies for solar-panel placement to reduce operator confirmations, using Isaac Sim data with EC2 and S3.

**Scope to check**: Customer technical case. Separate simulation/offline evaluation from field deployment scope.

**Next action**: P3 Simulation · P4 Sim-to-Real — [P3](pillar-3.md) · [P4](pillar-4.md).

## WIRobotics: teaching humanoids to use tools { #wirobotics }

**Published: 2026-08-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-wirobotics-is-teaching-humanoid-robots-to-use-human-tools-with-aws-and-nvidia/) `[3]`**

A Korean robotics company’s drill-use learning project, connecting data quality, training settings, and physical evaluation with AWS and NVIDIA.

**Scope to check**: Customer collaboration. Observations on a particular tool/task do not establish general humanoid capability.

**Next action**: P2 Training · P4 Physical Evaluation — [P2](pillar-2.md) · [P4](pillar-4.md).

## Industrial digital twins with OpenUSD and SDMA { #openusd }

**Published: 2026-07-31 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/build-l1-4-industrial-digital-twins-with-openusd-and-sdma-on-aws/) `[3]`**

A staged implementation from static 3D scenes to sensor overlays, prediction, and recalibration, using OpenUSD layers with S3, Kinesis, Lambda, and Batch.

**Scope to check**: Reference implementation. Distinguish synthetic sensor inputs from real equipment integration; start at the needed level.

**Next action**: P3 Digital Twins · OpenUSD resources — [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial).

## Config: augmenting robot training data { #config }

**Published: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

Expands visual diversity in existing demonstrations with S3, Bedrock captioning, Cosmos-based transformation, and HyperPod/EC2.

**Scope to check**: Joint customer technical article. Useful for separately evaluating augmented-video quality and actual policy improvement.

**Next action**: P1 Data Collection and Processing — [P1](pillar-1.md).

## Keep following

Follow the official [Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) and [RSS](https://aws.amazon.com/blogs/physical-ai/feed/). Update publication date, source, scope, and pillar links together; technology promotion follows existing [maintenance rules](maintenance.md).

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — A model that turns visual observations and language instructions into robot actions.
[^openloop]: **Open-loop evaluation** — Prediction-error evaluation on recorded observations/actions, distinct from task-success evaluation with the policy interacting with an environment.
