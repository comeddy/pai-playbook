---
ko_hash: 6c812de4981e09fc57a08d454791c78c874795a4
---
# Workshops & Resources

_owner: Youngjin · updated: 2026-09 · volatility: medium_

> **L0 TL;DR**: Public self-paced workshops, implementation guides, and samples in one place. **Last checked: 2026-09-19**. Open each title for the source and use the related pillar for architecture context.

Duration and cost depend on modules, account readiness, and GPU availability. Check source Prerequisites/Cleanup, permissions, and model terms before starting. This list records source inspection, not a full rerun of every lab.

## Choose by goal

| Goal | Resource | Related pillar |
|---|---|---|
| Start simulation training | [NVIDIA Isaac Lab on AWS](#isaac-lab) | [P3](pillar-3.md) |
| RL to VLA[^vla] in Korean | [Physical AI E2E workshop](#physical-ai-e2e) | [P2](pillar-2.md) |
| Agent component fundamentals | [Getting Started with Amazon Bedrock AgentCore](#agentcore-start) | [P5](pillar-5.md) |
| Advanced AgentCore application | [Diving Deep with Amazon Bedrock AgentCore](#agentcore-deep) | [P5](pillar-5.md) |
| Read π0 training/evaluation setup | [π0 fine-tuning on SageMaker HyperPod EKS](#pi0-guide) | [P2](pillar-2.md) |
| Connect 3D assets, sensors, and prediction | [OpenUSD industrial digital-twin sample](#spatial) | [P3](pillar-3.md) |
| Inspect simulation results without a robot | [VLA Simulator on AWS](#vla-simulator) | [P4](pillar-4.md) |
| Collect physical robot demonstrations | [LeRobot data collection on Greengrass](#lerobot-collection) | [P1](pillar-1.md) |

## NVIDIA Isaac Lab on AWS { #isaac-lab }

**[NVIDIA Isaac Lab on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/075ce3fe-6888-4ea9-986e-5bdd1b767ef7/en-US) · Official AWS workshop · English**

**Content**: Run Isaac Lab on EC2, scale with AWS Batch, inspect the model in Isaac Sim, then clean up.

**Before starting**: Prepare AWS access, container basics, and GPU quota. The exercise is simulation-based.

**Related pillar**: [P3](pillar-3.md).

## Physical AI E2E workshop { #physical-ai-e2e }

**[Physical AI E2E workshop](https://hi-space.gitbook.io/physical-ai-on-aws/guide/e2e-workshop) · Community-authored guide · Korean**

**Content**: Modular exercises for Isaac Lab RL, GR00T VLA, Batch/SageMaker, and simulation evaluation.

**Before starting**: Check CDK, Docker, GPU setup, and model access. Choose the needed track first.

**Related pillar**: [P2](pillar-2.md).

## Getting Started with Amazon Bedrock AgentCore { #agentcore-start }

**[Getting Started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US) · Official AWS workshop · English**

**Content**: Progress through an agent prototype, Memory, Gateway, observability/evaluation, and Policy.

**Before starting**: Check AWS account and model/service access. Robot connectivity needs separate integration.

**Related pillar**: [P5](pillar-5.md).

## Diving Deep with Amazon Bedrock AgentCore { #agentcore-deep }

**[Diving Deep with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-deep-dive/en-US) · Official AWS workshop · English**

**Content**: Explore composition, security, and observability through Feature Deep Dive or Build with Skills.

**Before starting**: The workshop requires Getting Started first; follow its development-environment prerequisites.

**Related pillar**: [P5](pillar-5.md).

## π0 fine-tuning on SageMaker HyperPod EKS { #pi0-guide }

**[π0 fine-tuning on SageMaker HyperPod EKS](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) · AWS implementation article · English**

**Content**: New guide connecting data, training, evaluation, and cleanup on HyperPod EKS; published 2026-09-10.

**Before starting**: Advanced setup. The article is public, but its linked code path returned 404 at review. Use as reading material until code access is resolved.

**Related pillar**: [P2](pillar-2.md).

## OpenUSD industrial digital-twin sample { #spatial }

**[OpenUSD industrial digital-twin sample](https://github.com/aws-samples/sample-physical-ai-spatial-intelligence) · aws-samples · English**

**Content**: L1 static scene, L2 sensor overlays, L3 prediction, and L4 recalibration; local and AWS execution paths.

**Before starting**: Follow Python/Node.js/Docker prerequisites. Clone from the public GitHub URL linked here instead of the internal address in the README example.

**Related pillar**: [P3](pillar-3.md).

## VLA Simulator on AWS { #vla-simulator }

**[VLA Simulator on AWS](https://github.com/aws-samples/sample-vla-simulator-on-aws) · aws-samples · English**

**Content**: Runs supported VLA/simulator combinations and collects videos and summaries in S3.

**Before starting**: Check CDK, GPU quota, and per-model licenses. Small demo success rates do not establish customer deployment performance.

**Related pillar**: [P4](pillar-4.md).

## LeRobot data collection on Greengrass { #lerobot-collection }

**[LeRobot data collection on Greengrass](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass) · aws-samples · English/Korean**

**Content**: Records SO-ARM101 leader/follower and camera data in LeRobot format and uploads it to S3.

**Before starting**: Requires robot hardware, cameras, and a Greengrass device. The README marks it educational/demo code, not ready for production.

**Related pillar**: [P1](pillar-1.md).

## Suggested learning order

For simulation, start with **Isaac Lab → the relevant E2E track → VLA Simulator**. For agents, follow **AgentCore Getting Started → Deep Dive**. For digital twins, start with **local OpenUSD execution → the AWS levels you need**.

## Maintaining this list

Record provider, language, goal, prerequisites, related pillar, and check date for new resources. Link availability and lab reproducibility are separate checks. Use [News](news.md) for announcements and [Radar](radar.md) for technology awaiting validation.

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — A model that turns visual observations and language instructions into robot actions.
