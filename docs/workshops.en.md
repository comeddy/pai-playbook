---
ko_hash: 6cf05e14af012d3be0a4976f990bab5cc6bf2d36
---
# Workshops & Resources

_owner: Youngjin · updated: 2026-11 · volatility: medium_

> **L0 TL;DR**: Public self-paced workshops, implementation guides, and samples in one place. **Last checked: 2026-11-04**. Open each title for the source and use the related pillar for architecture context.

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
| Plan in natural language, verify in physics simulation | [Robot Atlas Physical AI robot workshop](#robot-atlas) | [P5](pillar-5.md) |

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

**Before starting**: Advanced setup. The article is public, but its code link (`awsome-distributed-ai/…/3.test_cases/pytorch/pi0-lerobot`) returns 404 — the code was never merged to main and sits in [unmerged PR #1174](https://github.com/awslabs/awsome-distributed-ai/pull/1174) (checked 2026-10-14; PR last updated 2026-07-30). Unmerged code is unreviewed, so use this as reading material.

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

## Robot Atlas Physical AI robot workshop { #robot-atlas }

**[Robot Atlas Physical AI robot workshop](https://robot-atlas.whchoi.net/workshop/) · Community-built workshop · Korean/English/Japanese/Chinese** · [Live demo](https://robot-atlas.whchoi.net/)

**What it covers**: 3 tracks, 19 chapters. The participant basics track (00–04, about 110 min) replays pick-and-stack runs in MuJoCo[^mujoco] and runs new layouts from Bedrock task plans. The participant AWS deployment track (05–13, about 280 min) builds an AgentCore Runtime task planner, a private Fargate physics engine, and the CloudFront·WAF path. The facilitator track (14–18, about 195 min) covers Isaac Sim RTX cameras and checkpoint resume on g6e·g7e Spot in EKS Auto Mode. The live demo shows a robot arm, a five-finger hand, and bimanual shirt folding.

**Before you start**: The material assumes a prepared EC2 VSCode Server and account (material dated 2026-09-13). As the source states, the AI produces only high-level plans while inverse kinematics and joint controllers move the robot; motion-policy training and physical-robot experiments are not included. Isaac Sim cloth folding is marked "under validation" in the source. For the GPU track, check Spot cost and cleanup steps first.

**Related pillars**: [P5](pillar-5.md) — separating planning (System 2) from control (System 1), [P3](pillar-3.md) — simulation operations.

## Suggested learning order

For simulation, start with **Isaac Lab → the relevant E2E track → VLA Simulator**. For agents, follow **AgentCore Getting Started → Deep Dive**, then try the **Robot Atlas basics track** to connect agent planning to robot simulation. For digital twins, start with **local OpenUSD execution → the AWS levels you need**.

## Maintaining this list

Record provider, language, goal, prerequisites, related pillar, and check date for new resources. Link availability and lab reproducibility are separate checks. Use [News](news.md) for announcements and [Radar](radar.md) for technology awaiting validation.

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — A model that turns visual observations and language instructions into robot actions.
[^mujoco]: **MuJoCo** — An open-source physics simulator with fast contact and friction computation, widely used in robot-manipulation research and RL benchmarks.
