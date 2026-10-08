---
ko_hash: 5a3463b7c8a1274dfa99487730b7b3dc561aaea2
---
# Execution paths — data, simulation, and fine-tuning

_Last updated: 2026-09 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: Complete the [pilot card](start.md#pilot), then choose one path for the current bottleneck. These guides are based on **pinned public sample commits**. Sources and commands were compared on 2026-09-15; no AWS resources or physical robots were run during this playbook revision. Sample-author results are separate from playbook reproduction.

## Shared prerequisites and run record { #prepare }

Assign AWS/IAM/data and robotics/ML owners, plus a site safety owner for physical trials. Check GPU quota, Region, licenses, and data-processing locations; set runtime and spending limits. Budget alerts alone do not stop workloads: assign a stop owner and procedure.

```text
repo commit / container digest / dependency versions:
region / AZ / instance type / instance count:
dataset version / robot-camera configuration / train-eval split:
start-end time / setup-training-evaluation hours / actual cost:
success numerator-denominator / cycle time / interventions / latency:
failure evidence / cleanup result / operator / reviewer:
```

## A. Collect robot data and check quality { #data }

**For** teams collecting demonstrations with SO-ARM101 leader/follower arms and dual cameras. **Other robots and ROS bag conversion require adapter work**; this sample does not automatically solve them.

**Prerequisites and version**: [Pinned sample](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) `[1]` (MIT-0, education/demo). The author reports Jetson AGX Thor/JetPack 7 validation. Requires a HEALTHY Greengrass V2 device, Docker/NVIDIA runtime, calibrated robot/cameras, and an S3 bucket/IoT thing group in the same Region.

```bash
git clone https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass.git
cd sample-lerobot-data-collection-on-aws-iot-greengrass
git checkout 6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e
```

**Run**: follow sections 0–0.2 of the pinned `DEPLOYMENT_GUIDE.md` for devices, permissions, and authentication → deploy CloudFormation → upload `collect.py` → register/deploy the matching `recipe.yaml` version → record a short web-console session → Save & Next → End Session → inspect S3 output and episode replay. Substitute the guide's environment placeholders in its AWS commands.

**Output and pass criteria**: a versioned dataset, episode manifest, and checks for camera/action alignment, missing frames, units, and success/failure labels. Meet the agreed data contract and recover interrupted uploads. Successful recording does not guarantee training quality.

**Cost and stop conditions**: device/operator time, S3, optional KVS video/transfer, logs, and web resources. Estimate with the [budget worksheet](start.md#roi). Stop collecting when alignment, calibration, permissions, or safety conditions fail.

**Cleanup**: stop recording/video streams and remove the component from Greengrass deployment. Decide retention first, then inspect CloudFormation resources, IoT certificates/policies, KVS, logs, and buckets created for this experiment. Separate shared resources from experiment resources.

## B. Simulation training and evaluation { #simulation }

**For** teams learning cloud training and policy export with an ANYmal-C locomotion example. Synthetic imagery and other robot tasks require separate experiments.

**Prerequisites and version**: [Pinned sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) `[1]` (MIT, educational). **Isaac Lab v2.1.0 + Isaac Sim 4.5.0**, default `us-east-1`, `g6e.4xlarge`. These differ from the pillar's latest-version table; do not mix versions arbitrarily. Requires Terraform ≥1.5, AWS CLI, NGC access, GPU quota, and an SSH key.

```bash
git clone https://github.com/aws-samples/sample-issac-lab-on-aws.git
cd sample-issac-lab-on-aws
git checkout 50ea76d87d873c1d69bed92c450ab144894f437e
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform validate
terraform plan
```

Set Region, allowed SSH addresses, key, storage, and other variables; review the plan before `terraform apply`. The sample stores the NGC key in state/user data; change secret handling first for shared or long-lived environments. Follow the README's **bootstrap → core-package installation → container launch**. Inside the prepared container at `/workspace/isaaclab`:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py   --task Isaac-Velocity-Rough-Anymal-C-v0 --headless
```

**Output and pass criteria**: configuration, training logs, checkpoint, video from a separate evaluation, and exported `.pt`/`.onnx`. Measure failures and tracking error on agreed terrain, as well as reward. Successful export does not pass physical deployment.

**Cost and stop conditions**: the author's roughly 2-hour/$12 figure is a workshop estimate, not Seoul g6e.xlarge pricing combined with the ETH paper's 4–20-minute result. Account for full setup/training/evaluation instance time, EBS, S3, public IPv4, and logs. Stop on bootstrap failure, insufficient memory, or the cap.

**Cleanup**: preserve results separately, review `terraform plan -destroy`, then run `terraform destroy` in that experiment's working directory. Check retained S3 objects, snapshots, logs, and IPs for ongoing charges. Physical trials are a separate stage governed by [release gates](operations.md#release).

## C. Fine-tuning and limited edge evaluation { #finetuning }

**For** teams with separated training/evaluation data and defined robot observations/actions. This is not foundation-model pretraining.

**Prerequisites and evidence scope**: [Pinned sample](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac) `[1]` (MIT-0). The author reports a completed **IL Pattern A (Batch)** run. B/C (SageMaker/HyperPod) lack deployment validation, RL has not run on a GPU, and a forced Spot interruption/recovery has not been demonstrated. Requires Node/npm/CDK, Python (`boto3`, `sagemaker`), S3 data, model/base-model access and licenses, and GPU quota.

```bash
git clone https://github.com/aws-samples/sample-vla-finetuning.git
cd sample-vla-finetuning
git checkout f21e4a9bf0ec11f40c2298a85951690b61efeaac
npm ci
npm run build
export PAI_AWS_REGION=us-west-2
npm run cdk -- synth PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

The example uses `us-west-2`; change it to an approved Region that meets processing and capacity requirements. Use the same value for CDK and the CLI.

Complete the sample's bootstrap, image preparation, and account setup; review the resources before deploying Pattern A.

```bash
npm run cdk -- deploy PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

Then activate the Python environment and run:

```bash
cd containers/vla-ft
python vla_ft_cli.py --help
python vla_ft_cli.py --quickstart --backend batch --region "$PAI_AWS_REGION" --dry-run
```

Dry-run can query account/capacity but submits no training job. **Default quickstart may select Pattern B; `--backend batch` limits this path's scope.** Check model, batch, memory, and estimated cost; to run the bundled-data experiment, replace `--dry-run` with `--yes` on that command. For customer data, replace `--quickstart` with `--dataset s3://... --model ...` and follow `--help`.

**Output and pass criteria**: lineage from data/base checkpoint/configuration to the new checkpoint, baseline-model evaluation under identical conditions, success numerator/denominator, repeated/unseen conditions, cycle time, and interventions. Demonstration counts do not guarantee success rates or completion dates.

**Edge handover**: the training sample does not complete physical deployment. Validate model-specific export/serving, observation order/normalization, action units, device compatibility, and observation-to-action latency. Connect [P4 deployment assets](pillar-4.md) and [release gates](operations.md#release) for a supervised limited trial.

**Cost, stop, and cleanup**: record estimates and actual charges separately. Stop for memory failure, stalled evaluation, or budget/time limits. Preserve checkpoints, inspect active Batch jobs/compute environments, and remove experiment-only CDK stacks. EFS, S3, NAT, and logs can still cost money at zero GPU capacity. Check shared stacks with their owner.

**➡️ Next action**: record preparation, execution, evaluation, and cleanup; decide the next gate using the [pilot card](start.md#pilot). Add actual reproduction evidence to [evidence records](evidence.md).

_owner: Youngjin · updated: 2026-09 · volatility: medium_
