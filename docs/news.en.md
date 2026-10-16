---
ko_hash: 97764a94d9bc250fc42d34b6187d4215bf85efa7
---
# News

_owner: Youngjin · updated: 2026-10 · volatility: high_

> **L0 TL;DR**: Selected new AWS Physical AI articles, linked to the existing pillars. Dates below are **publication dates**; this list was checked on **2026-10-14**. Follow [Workshops & Resources](workshops.md) for learning paths.

Summaries are based on official articles, not independent reproduction of their performance claims. Unverified technology candidates remain in [Radar](radar.md).

## Recent resources at a glance

| Published | Resource | Connects to |
|---|---|---|
| 2026-10-07 | [AWS Physical AI Toolchain released](#toolchain) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md) |
| 2026-10-06 | [3D Gaussian Splatting industry use cases](#gaussian-splatting) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-02 | [Isaac Lab on AWS — from simulation to registered policy](#isaac-lab-aws) | [P3](pillar-3.md) · [Isaac Lab](workshops.md#isaac-lab) |
| 2026-09-28 | [NVIDIA Cosmos 3 on AWS](#cosmos-3) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) |
| 2026-09-10 | [π0 fine-tuning on SageMaker HyperPod EKS](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence’s DreamZero experiment](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics: AI for solar-panel placement](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics: teaching humanoids to use tools](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [Industrial digital twins with OpenUSD and SDMA](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-17 | [Edge Impulse and AWS — combining edge inference with cloud intelligence](#edge-impulse-aws) | [P4](pillar-4.md) · [P5](pillar-5.md) |
| 2026-07-15 | [Config: augmenting robot training data](#config) | [P1](pillar-1.md) |

## AWS Physical AI Toolchain released { #toolchain }

**Published: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

A collection of reference architectures, IaC, and deployment automation for running the Physical AI lifecycle on AWS — data collection, synthetic data, training, simulation validation, and edge deployment. It connects NVIDIA GR00T (VLA[^vla] training), Isaac Sim, Isaac Lab, Cosmos, and OSMO to S3, EKS, AWS Batch, SageMaker, EC2, and IoT Greengrass (Jetson deployment), with one Terraform module per component that can be adopted one at a time. Open formats are used: Zarr→LeRobot for data, ONNX and ROS 2 at the edge. Code: [aws-samples repository](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws).

**Scope to check**: Official reference architecture. The article itself says it provides "infrastructure patterns, not finished robot behaviors." The GR00T example uses 27 UR3 pick-and-place demonstrations as a smoke test, and "hours rather than weeks" is AWS's own claim. Requires GPU quota (SageMaker and EC2), an NGC API key, and a Hugging Face token; tear down after the lab to stop costs.

**Next action**: Adopt one bottleneck stage first — P1 Data · P2 Training · P3 Simulation · P5 Orchestration (Strands agentic layer) · Radar queue entry — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting industry use cases { #gaussian-splatting }

**Published: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

Introduces a five-stage pipeline (input → pre-processing → reconstruction → training → post-processing) for 3DGS[^3dgs], which builds photorealistic 3D scenes from photos and video, using the open-source Splat Toolbox ([AWS Solutions Library guidance](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws)), plus uses in media, robotics, construction, manufacturing, and real estate. Built on Step Functions, Lambda, AWS Batch/ECS, and EC2 Spot.

**Scope to check**: Industry overview. The robotics items (synthetic training data, narrowing the sim-to-real gap, path planning) describe directions, with no measured policy results. Output today is static 3D; 4D (time-axis) assets are on the roadmap. "Up to 50% savings" compares Spot with On-Demand compute pricing.

**Next action**: P3 digital twins and scene reconstruction · P4 real-to-sim candidate — [P3](pillar-3.md) · [P4](pillar-4.md).

## Isaac Lab on AWS — from simulation to registered policy { #isaac-lab-aws }

**Published: 2026-10-02 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/isaac-lab-on-aws-from-simulation-to-registered-policy/) `[3]`**

An AWS CDK solution that deploys, in one go, a golden AMI pre-baked with Isaac Sim 5.1.0, Isaac Lab v2.3.2, the NVIDIA driver, and Amazon DCV; a single-user Instance mode and a multi-user Fleet mode (Cognito MFA, auto scaling); and SageMaker training jobs with a managed MLflow model registry. Projects built on the desktop go to training jobs without an image rebuild, and trained policies are registered in MLflow automatically. Samples: SO-ARM101 RL, SO-ARM101 teleoperation data capture, and Unitree H1 locomotion.

**Scope to check**: Not a public repository — per the article it is **available through your AWS account team**. The registry records and labels policies but does not serve them; wiring deployment is the team's job. For a public hands-on path, use the separate Isaac Lab workshop.

**Next action**: P3 Simulation · public [Isaac Lab](workshops.md#isaac-lab) workshop — [P3](pillar-3.md).

## NVIDIA Cosmos 3 on AWS { #cosmos-3 }

**Published: 2026-09-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/nvidia-cosmos-3-on-aws-omnimodal-world-models-for-physical-ai/) `[3]`**

Cosmos 3 (released 2026-05) merges the earlier Predict, Transfer, and Reason models into a single Mixture-of-Transformers model that produces scene understanding, future video (WFM[^wfm]), and robot action trajectories (WAM[^wam]) in one inference. Sizes: Super 64B, Nano 16B, Edge 4B. On the AWS side the post gives a reference architecture — data curation (Batch), HyperPod post-training, EKS+NIM or SageMaker JumpStart inference, and Jetson edge deployment via Greengrass — plus instance recommendations.

**Scope to check**: "First fully open omni-model" is NVIDIA's description. Full checkpoints are tested in BF16, and the article itself says to validate the runtime layout before making per-instance performance claims. Action outputs are not evidence of physical task success.

**Next action**: P1 Synthetic data · P2 Training · P3 Simulation — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md).

## π0 fine-tuning on SageMaker HyperPod EKS { #pi0-hyperpod }

**Published: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

Walks through π0 VLA training/evaluation on DROID and LIBERO, connecting HyperPod EKS, FSx for Lustre, and training-job configuration.

**Scope to check**: Official implementation guide. Reported evaluation is n=5 open-loop[^openloop], not physical task success. The article's code link returns 404 — the code was never merged and sits in [unmerged PR #1174](https://github.com/awslabs/awsome-distributed-ai/pull/1174) (checked 2026-10-14); start with the article.

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

## Edge Impulse and AWS — combining edge inference with cloud intelligence { #edge-impulse-aws }

**Published: 2026-07-17 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/edge-impulse-and-aws-combining-edge-inference-with-cloud-intelligence-for-physical-ai/) `[4]` · ⏳ awaiting source check (auto-scan 2026-10-16)**

A joint post from Edge Impulse (a Qualcomm company) and AWS describing a hybrid edge-to-cloud architecture, using warehouse asset tracking as the example. Camera edge devices make a first pass with Edge Impulse YOLO Pro object detection and a Qwen2-VL 8B vision-language model, and only confirmed detections go to the cloud, where Amazon Bedrock AgentCore (Nova Lite) answers natural-language queries such as "where is the forklift." AWS IoT Core handles device connectivity and MQTT messaging, Greengrass deploys and manages the edge models, and S3 stores images for retraining.

**Scope to check**: A joint AWS×Edge Impulse partner-introduction article. The article does not clearly state where the code sample lives, so whether it's a public repository or an account-team path needs further confirmation. "Reduced latency and bandwidth" describes the benefit of the edge-first design, not a measured benchmark — separate vendor description from measurement.

**Next action**: P4 Edge inference deployment · P5 Agentic orchestration (Bedrock AgentCore) — [P4](pillar-4.md) · [P5](pillar-5.md).

## Config: augmenting robot training data { #config }

**Published: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

Expands visual diversity in existing demonstrations with S3, Bedrock captioning, Cosmos-based transformation, and HyperPod/EC2.

**Scope to check**: Joint customer technical article. Useful for separately evaluating augmented-video quality and actual policy improvement.

**Next action**: P1 Data Collection and Processing — [P1](pillar-1.md).

## Keep following

Follow the official [Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) and [RSS](https://aws.amazon.com/blogs/physical-ai/feed/). Update publication date, source, scope, and pillar links together. The daily auto-scan first adds posts missing from this page marked `[4]` · ⏳ awaiting source check, and the owner switches them to `[3]` after checking the original; technology promotion follows existing [maintenance rules](maintenance.md).

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — A model that turns visual observations and language instructions into robot actions.
[^openloop]: **Open-loop evaluation** — Prediction-error evaluation on recorded observations/actions, distinct from task-success evaluation with the policy interacting with an environment.
[^3dgs]: **3D Gaussian Splatting (3DGS)** — A 3D reconstruction technique that fits many 3D Gaussians (ellipsoidal points) to a set of photos or video and renders photorealistic scenes in real time. Used for real-to-sim: bringing a real site into simulation as the background.
[^wfm]: **World Foundation Model (WFM)** — a large model trained to predict/generate the next scenes of the physical world. From text/video prompts it creates physically plausible video and scenarios to augment robot training data. 🎥 [NVIDIA Cosmos introduction](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **World Action Model (WAM)** — A model that predicts future scenes and generates robot actions together. Unlike a world model that only produces video, it outputs executable actions such as joint angles and gripper commands.
