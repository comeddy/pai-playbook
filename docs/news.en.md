---
ko_hash: 6d385b283f526caca083d3149b2aa9ee357e351f
---
# News

_owner: Youngjin · updated: 2026-11 · volatility: high_

> **L0 TL;DR**: Selected new AWS Physical AI articles, linked to the existing pillars. Dates below are **publication dates**; this list was checked on **2026-10-14**. Follow [Workshops & Resources](workshops.md) for learning paths.

Summaries are based on official articles, not independent reproduction of their performance claims. Unverified technology candidates remain in [Radar](radar.md).

> **re:Invent 2026 (Nov 30–Dec 4, Las Vegas)**: 45 Physical AI, simulation, model training, data, edge and AgentCore sessions [picked from the full session catalog](#reinvent-2026).

## Recent resources at a glance

| Published | Resource | Connects to |
|---|---|---|
| 2026-10-28 | [AWS × RLWRLD — Building the Workforce of Tomorrow with Physical AI](#aws-rlwrld-workforce) | [Radar](radar.md) · [P2](pillar-2.md) |
| 2026-10-28 | [Visual Asset Management System 2.6 released](#vams-2-6) | [P3](pillar-3.md) · [P4](pillar-4.md) |
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

## AWS × RLWRLD — Building the Workforce of Tomorrow with Physical AI { #aws-rlwrld-workforce }

**Published: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/aws-rlwrld-building-the-workforce-of-tomorrow-with-physical-ai/) `[4]` · ⏳ awaiting source check (auto-scan 2026-11-02)**

The second installment in the AWS × RLWRLD Physical AI collaboration series, following the 2026-06-22 first post ("Putting Dexterous Robots to Work"). It introduces RLWRLD as a newly listed AWS Validated Partner with two offerings on AWS Marketplace, and covers planned PoCs for labor-shortage use cases (box picking, product picking, shelf replenishment) plus customer pipeline activity from AWS Physical AI roadshows. It also cites a claim that RLDX-1 reaches comparable performance using roughly 20% of the training compute of leading foundation models.

**Scope to check**: An official AWS×RLWRLD partnership-series article (a customer-collaboration introduction). "AWS Validated Partner" and the Marketplace listing are partner-program status, not a live-deployment result. The box picking/product picking/shelf replenishment PoC is described in the article as "planned," not already operating. The "~20% compute for comparable performance" claim is RLWRLD's own vendor wording, citing its own technical blog — the same category as the self-reported benchmark already noted on the Radar's RLDX-1 item, not an independent measurement. This session could not reach aws.amazon.com directly due to a blanket egress block, so it was cross-checked against multiple independent search results (matching title, date, and key claims) instead — the owner should verify specific figures against the original.

**Next action**: Connects to the existing RLDX-1 Radar item · P2 Training — [Radar](radar.md) · [P2](pillar-2.md).

## Visual Asset Management System 2.6 released { #vams-2-6 }

**Published: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/visual-asset-management-system-2-6-release/) `[4]` · ⏳ awaiting source check (auto-scan 2026-11-02)**

VAMS is an open-source 3D/spatial-asset-management accelerator from the AWS Physical AI and PACE teams; 2.6 is described as the largest update since 2.0 (2024-06). It rebuilds the orchestration layer to add multi-file/multi-asset execution, a global execution view, and upload-triggered automatic workflows, plus an AWS European Sovereign Cloud deployment template, Amazon Cognito OIDC federation, finer-grained IAM role customization, a deny-by-default WAF, and asset provenance tracking (lifecycle and per-version change history). Demos include semantic search, an in-browser SuperSplat (Gaussian splat[^3dgs]) editor, an IFC BIM viewer, geospatial map search, and an NVIDIA Cosmos text-to-world workflow. The code is open source on [GitHub (awslabs/visual-asset-management-system)](https://github.com/awslabs/visual-asset-management-system).

**Scope to check**: An official open-source solution update post. "Largest update since 2.0" is AWS's own description; the post gives no live customer production-adoption results or performance figures. It's a public repository, not an account-team-only path — anyone can get it from GitHub. This session could not reach aws.amazon.com directly due to a blanket egress block, so it was cross-checked against search snippets and GitHub release tags (2.6.0 on 2026-09-11 through 2.6.6 on 2026-10-30) instead — the publication date (2026-10-28) is also based on search snippets and needs the owner's check against the original.

**Next action**: P3 Digital twins and scene reconstruction · P4 real-to-sim candidate — [P3](pillar-3.md) · [P4](pillar-4.md).

## AWS Physical AI Toolchain released { #toolchain }

**Published: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

A collection of reference architectures, IaC, and deployment automation for running the Physical AI lifecycle on AWS — data collection, synthetic data, training, simulation validation, and edge deployment. It connects NVIDIA GR00T (VLA[^vla] training), Isaac Sim, Isaac Lab, Cosmos, and OSMO to S3, EKS, AWS Batch, SageMaker, EC2, and IoT Greengrass (Jetson deployment), with one Terraform module per component that can be adopted one at a time. Open formats are used: Zarr→LeRobot for data, ONNX and ROS 2 at the edge. Code: [aws-samples repository](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws).

**Scope to check**: Official reference architecture. The article itself says it provides "infrastructure patterns, not finished robot behaviors." The GR00T example uses 27 UR3 pick-and-place demonstrations as a smoke test, and "hours rather than weeks" is AWS's own claim. Requires GPU quota (SageMaker and EC2), an NGC API key, and a Hugging Face token; tear down after the lab to stop costs.

**Next action**: Adopt one bottleneck stage first — P1 Data · P2 Training · P3 Simulation · P5 Orchestration (Strands agentic layer) · Radar queue entry — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting industry use cases { #gaussian-splatting }

**Published: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

Introduces a five-stage pipeline (input → pre-processing → reconstruction → training → post-processing) for 3DGS, which builds photorealistic 3D scenes from photos and video, using the open-source Splat Toolbox ([AWS Solutions Library guidance](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws)), plus uses in media, robotics, construction, manufacturing, and real estate. Built on Step Functions, Lambda, AWS Batch/ECS, and EC2 Spot.

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

## re:Invent 2026 — Physical AI sessions { #reinvent-2026 }

**Event: 2026-11-30 to 12-04 · [re:Invent 2026 event catalog](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog) `[3]` · catalog checked: 2026-11-02**

We pulled all 2,415 sessions in the catalog (repeats included), filtered titles and abstracts for Physical AI, robotics, world models, simulation, digital twins, model training (HyperPod, Trainium), training data, edge and AgentCore, then kept the 45 that connect directly to the pillars. AgentCore alone has more than 60 sessions with it in the title, so we kept production-operations patterns and manufacturing/field cases. Each session code opens the catalog search result. Times are local (PT); other runs of the same session are listed as "repeat". Formats: Workshop 120-min hands-on · Builders' session 60-min small-group hands-on · Chalk talk 60-min whiteboard discussion · Code talk 60-min live coding · Lightning talk 20 min.

**Keynotes and panels**

| When (PT) | Session | Format | What to look for |
|---|---|---|---|
| Tue 12/1 08:30 | [KEY002](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY002) CEO Keynote | Keynote | New announcements on AI infrastructure, inference and agent platforms — check for Physical AI-related launches |
| Wed 12/2 08:30 | [KEY003](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY003) Data & AI Keynote | Keynote | How agents reach data, measure value and set limits — P1 data and P5 agent angle |
| Wed 12/2 14:00 | [SUP201](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=SUP201) Training and simulation turn robot capabilities into useful products | Breakout session | NEURA Robotics, 1X and Highlanders panel — turning training, simulation and data pipelines into products |
| Thu 12/3 08:30 | [KEY005](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY005) Technical Innovations Keynote | Keynote | Inside Graviton, Trainium, networking and storage — background for training-infrastructure choices |
| Thu 12/3 10:00 | [AIM2215](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2215) World Models & Physical AI: The next frontier in intelligent systems | Breakout session | World-model panel — researchers and customers on production deployment and open technical problems |
| Thu 12/3 13:30 | [AIM2213](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2213) How leading AI builders push the frontier with AWS Trainium | Breakout session | Panel of four customers using Trainium, including world models and Physical AI |

**Physical AI pipeline — P1·P2·P3·P5**

| When (PT) | Session | Format | What to look for |
|---|---|---|---|
| Mon 11/30 10:00 | [IND3338-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3338-R) Accelerate Physical AI development with NVIDIA on AWS | Chalk talk | Full lifecycle with the AWS Physical AI Toolchain: synthetic data → training → sim-to-real → hardware-in-the-loop |
| Mon 11/30 12:00 | [AIM449](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM449) One agent, any robot: building physical AI with Strands Robots | Chalk talk | Strands Robots SDK — switch between MuJoCo sim and real hardware with one parameter; GR00T, Cosmos 3, LeRobot policies; IoT-bridged fleet |
| Mon 11/30 15:00 | [IND389](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND389) Physical AI for MedTech: From Intelligent Devices to Business Impact | Chalk talk | Physical AI stack for medical devices — SageMaker training, Greengrass edge inference, regulated OTA |
| Tue 12/1 13:30<br>repeat Tue 12/1 15:00 | [IND322-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND322-R) Physical AI in Telecom: A Framework for Workload Placement | Chalk talk | Placement framework for Physical AI workloads — Region, Local Zones, Outposts or cell site |
| Tue 12/1 16:30 | [AIM413](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM413) Build a Physical AI Model Factory on SageMaker HyperPod | Chalk talk | Run the synthetic-scenario → post-training → evaluation data flywheel on heterogeneous GPU pools in HyperPod EKS |
| Wed 12/2 08:30<br>repeat Thu 12/3 14:30 | [CMP407-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP407-R) Orchestrating Physical AI workloads on AWS: Compute and pipeline patterns | Chalk talk | Batch (parallel simulation) vs EKS + Karpenter (training) vs HyperPod; Capacity Blocks and Spot cost strategy |
| Wed 12/2 12:30 | [AIM458-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM458-S) The Physical AI Blueprint: A Full-Stack Solution with AWS and NVIDIA (sponsored by NVIDIA) | Workshop | Hands-on: Isaac Sim synthetic data, GR00T/Cosmos training, Omniverse twin, Greengrass deployment, AgentCore multi-robot orchestration |

**Simulation and digital twins — P3**

| When (PT) | Session | Format | What to look for |
|---|---|---|---|
| Mon 11/30 13:30 | [CMP408](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP408) The cloud holodeck: Stream NVIDIA Omniverse, scale headless sim on AWS | Chalk talk | Stream Omniverse/Isaac Sim workstations over DCV + headless rendering at scale on Batch, managed by VAMS |
| Tue 12/1 15:00 | [IND102-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND102-S) Accelerating with NVIDIA Omniverse: VW’s Battery Manufacturing Digital Twin (sponsored by NVIDIA) | Breakout session | Volkswagen battery plant OpenUSD digital twin — virtual commissioning and synthetic inspection data |
| Tue 12/1 16:00<br>repeat Wed 12/2 09:00 | [IND401-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND401-R) Build, simulate, and validate physical AI-driven robotic systems | Builders' session | Hands-on: build a multi-robot cell digital twin with virtual PLCs, fieldbus and Omniverse physics |
| Wed 12/2 16:30 | [CON409](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CON409) ML, automotive, and robotics simulations at scale on AWS Batch | Breakout session | Orchestrate the automotive/robotics simulation → data lake → GPU training loop with Batch |
| Thu 12/3 16:30 | [IND3355](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3355) Building Worlds for Machines: VAMS and 3DGS for Autonomy | Lightning talk | Field sensor capture → 3DGS reconstruction → simulation-ready environments (20-min lightning talk) |

**World models and robot learning research — P2**

| When (PT) | Session | Format | What to look for |
|---|---|---|---|
| Mon 11/30 13:00<br>repeat Wed 12/2 12:00 | [AIM305-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM305-R) Hands-on training world models and deploying agents for Physical AI | Builders' session | Hands-on: fine-tune a transformer world model on Trainium/Neuron (PEFT), then deploy agents |
| Mon 11/30 16:00 | [AIM323](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM323) Serving world models on AWS Trainium with native PyTorch | Code talk | Serve world-model inference on Trainium with torch.compile and custom kernels |
| Mon 11/30 16:30 | [INV531](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV531) Visual reasoning will be bigger than language reasoning | Chalk talk | UW's Ranjay Krishna — robot foundation models that reason through points, trajectories and depth |
| Tue 12/1 11:30<br>repeat Thu 12/3 13:30 | [AIM304-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM304-R) Deploy and optimize world models with agentic AI workflows | Builders' session | Hands-on: deploy a real-time video world model on Trainium and optimize kernels with Neuron agent skills |
| Wed 12/2 10:30 | [INV527](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV527) World models for indoor robots: what breaks and why | Chalk talk | Lidar world model for Diligent Robotics' hospital robots — where transformer geometric reasoning breaks |
| Wed 12/2 13:30 | [INV537](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV537) No torque sensors, no problem: learning safe physical interaction for humanoids | Chalk talk | Fauna Robotics — learning compliant control for a humanoid without torque sensors |

**Model training and data infrastructure — P1·P2**

| When (PT) | Session | Format | What to look for |
|---|---|---|---|
| Mon 11/30 08:30 | [AIM406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM406) End-to-end foundation model pipelines on SageMaker HyperPod with EKS | Workshop | Hands-on: data prep → distributed fine-tuning → inference on the same HyperPod EKS cluster |
| Mon 11/30 15:00 | [AIM318](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM318) Resilient VLM Training at Scale on Amazon SageMaker HyperPod | Workshop | Hands-on: inject node failures during VLM training and recover with auto-healing and checkpoints |
| Mon 11/30 15:00 | [AIM433](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM433) Maximize GPU utilization across training and inference on HyperPod | Chalk talk | HyperPod as a shared GPU pool for data processing, training and inference — cross-team scheduling |
| Tue 12/1 12:00<br>repeat Thu 12/3 08:00 | [AIM334-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM334-R) Hands-on distributed training with AWS Trainium and PyTorch | Workshop | Hands-on: distributed training on Trainium with TorchTitan — parallelism strategy and tuning |
| Tue 12/1 14:30 | [AIM362](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM362) Which customization compute? A decision approach for model fine-tuning | Chalk talk | Choosing fine-tuning compute — serverless customization, training jobs or HyperPod |
| Wed 12/2 15:00 | [AIM3308](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM3308) What's new: SageMaker HyperPod, with learnings from Multiverse | Breakout session | What's new in SageMaker HyperPod (EKS and Slurm) — large-scale training and serving including world models |
| Wed 12/2 15:30<br>repeat Thu 12/3 08:00 | [AIM434-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM434-R) From raw data to custom model: Dataset prep with Amazon SageMaker AI | Workshop | Hands-on: prepare training data with profiling, auto-labeling, human review and synthetic data |

**Field operations and edge — P4**

| When (PT) | Session | Format | What to look for |
|---|---|---|---|
| Mon 11/30 10:00 | [DVT210-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=DVT210-S) When Telemetry Steers the Robot: Observability for Physical AI (sponsored by groundcover) | Breakout session | Observability for Path Robotics' welding and quadruped robots (sponsored session) |
| Mon 11/30 15:00<br>repeat Tue 12/1 12:30 | [IND402-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND402-R) Agentic AI for manufacturing: Build a cross-domain digital thread | Workshop | Hands-on: manufacturing digital thread joining OT and IT data with Neptune, AgentCore and IoT SiteWise |
| Tue 12/1 12:30<br>repeat Thu 12/3 08:30 | [HMC403-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC403-R) Self-managed agentic AI at the hybrid edge | Workshop | Hands-on: run self-managed agentic AI on Local Zones and Outposts (data residency, low latency) |
| Wed 12/2 16:30 | [IND378](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND378) How Mercedes-Benz accelerates engineering and production with AI | Breakout session | Mercedes-Benz — AgentCore engineering agents plus a cloud-native MES and digital twins |
| Thu 12/3 08:30 | [HMC406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC406) How Amazon Robotics runs AWS Outposts across hundreds of fulfillment centers | Code talk | How Amazon Robotics runs Outposts across hundreds of fulfillment centers — isolation and failover |
| Thu 12/3 09:00 | [IND384](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND384) Inside T-Mobile's Kinetic Edge: Real-Time Physical AI at Scale | Breakout session | T-Mobile Kinetic Edge — real-time Physical AI at the network edge with Outposts, SageMaker and AgentCore |
| Fri 12/4 08:30 | [IND345](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND345) Human+AI Collaboration: How Amazon Deploys Autonomous Operations on AWS | Breakout session | Amazon's fulfillment floor — orchestrating a mixed fleet of humanoids, quadrupeds, AMRs and drones |

**AgentCore — P5**

| When (PT) | Session | Format | What to look for |
|---|---|---|---|
| Mon 11/30 08:30<br>repeat Wed 12/2 08:00 | [AIM439-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM439-R) Getting Started with AgentCore: ship an agent to production in 2 hours | Workshop | 2-hour hands-on: add runtime, memory, gateway, identity, policy, observability and evaluation step by step with the AgentCore CLI |
| Mon 11/30 10:00<br>repeat Wed 12/2 15:00 | [AIM436-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM436-R) Scale production agents reliably with AgentCore | Chalk talk | Scaling from 10 to 10,000 sessions — microVM isolation, handling tool-call failures and timeouts |
| Mon 11/30 14:00<br>repeat Thu 12/3 08:00 | [TNC331-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=TNC331-R) Ship AI Agents Faster with AgentCore Harness | Lab | Lab: AgentCore Harness — declare the agent loop in config, add tools and skills, publish versioned endpoints |
| Mon 11/30 14:30 | [AIM370](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM370) Trusting agents in production: end-to-end security with AgentCore | Breakout session | End-to-end AgentCore security — microVM isolation, identity propagation, Gateway policies, Cedar least privilege |
| Wed 12/2 11:30 | [AIM450-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM450-R) Context engineering for production agents on AgentCore | Chalk talk | Context engineering — budgeting system prompts, skills, tool definitions and memory |
| Wed 12/2 15:00 | [AIM212](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM212) Best practices for production agents on AgentCore, with Nasdaq | Breakout session | AgentCore production best practices + Nasdaq on multi-account isolation and agent identity |
| Thu 12/3 14:30 | [AIM452](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM452) Build long-running agents that persist for days on AgentCore | Chalk talk | Agents that persist for days — durable Runtime execution, Memory, human-in-the-loop pause/resume |

**Scope to check when reading**: These are session abstracts (advance notices), not the talks themselves. Schedules and rooms can change — re-check in the event app. Figures such as "35 weeks → 3.5" (IND378) and "weeks → hours" (IND401) are the presenters' claims. AIM305 and AIM304 announce hands-on training and serving of world models on Trainium — the [P2](pillar-2.md) call "no public case of training VLA on Trainium" will be revisited once session materials are public and reproduced.

**Next action**: Pick sessions by the pillar you own — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P4](pillar-4.md) · [P5](pillar-5.md). After the event, replace rows with links to recordings and slides once published, and route new services or features through [Radar](radar.md).

## Keep following

Follow the official [Physical AI blog](https://aws.amazon.com/blogs/physical-ai/) and [RSS](https://aws.amazon.com/blogs/physical-ai/feed/). Update publication date, source, scope, and pillar links together. The daily auto-scan first adds posts missing from this page marked `[4]` · ⏳ awaiting source check, and the owner switches them to `[3]` after checking the original; technology promotion follows existing [maintenance rules](maintenance.md).

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — A model that turns visual observations and language instructions into robot actions.
[^openloop]: **Open-loop evaluation** — Prediction-error evaluation on recorded observations/actions, distinct from task-success evaluation with the policy interacting with an environment.
[^3dgs]: **3D Gaussian Splatting (3DGS)** — A 3D reconstruction technique that fits many 3D Gaussians (ellipsoidal points) to a set of photos or video and renders photorealistic scenes in real time. Used for real-to-sim: bringing a real site into simulation as the background.
[^wfm]: **World Foundation Model (WFM)** — a large model trained to predict/generate the next scenes of the physical world. From text/video prompts it creates physically plausible video and scenarios to augment robot training data. 🎥 [NVIDIA Cosmos introduction](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **World Action Model (WAM)** — A model that predicts future scenes and generates robot actions together. Unlike a world model that only produces video, it outputs executable actions such as joint angles and gripper commands.
