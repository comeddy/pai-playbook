# 워크숍·자료

_owner: Youngjin · updated: 2026-11 · volatility: 중간_

> **L0 TL;DR**: 상시 열람할 수 있는 공개 워크숍·구현 가이드·샘플을 한 곳에 모았다. **마지막 확인: 2026-11-04**. 자료 제목에서 원문으로 이동하고, 관련 필러에서 아키텍처 배경을 확인한다.

워크숍 완료 시간과 비용은 선택 모듈·계정 준비·GPU 가용성에 따라 달라진다. 시작 전 원문의 Prerequisites·Cleanup, 계정 권한과 모델 사용 조건을 확인한다. 이 목록은 원문 열람 확인이며 실습 전체 재실행 기록은 아니다.

## 목적별로 고르기

| 하고 싶은 일 | 자료 | 관련 필러 |
|---|---|---|
| 시뮬레이션 학습 입문 | [NVIDIA Isaac Lab on AWS](#isaac-lab) | [P3](pillar-3.md) |
| 한국어로 RL부터 VLA[^vla]까지 | [Physical AI E2E 워크숍](#physical-ai-e2e) | [P2](pillar-2.md) |
| 에이전트 구성요소 입문 | [Getting Started with Amazon Bedrock AgentCore](#agentcore-start) | [P5](pillar-5.md) |
| AgentCore 심화·적용 | [Diving Deep with Amazon Bedrock AgentCore](#agentcore-deep) | [P5](pillar-5.md) |
| π0 학습 구성·평가 읽기 | [π0 파인튜닝 on SageMaker HyperPod EKS](#pi0-guide) | [P2](pillar-2.md) |
| 3D 자산·센서·예측 연결 | [OpenUSD 산업용 디지털 트윈 샘플](#spatial) | [P3](pillar-3.md) |
| 로봇 없이 시뮬레이션 결과 보기 | [VLA Simulator on AWS](#vla-simulator) | [P4](pillar-4.md) |
| 실로봇 시연 데이터 수집 | [LeRobot 데이터 수집 on Greengrass](#lerobot-collection) | [P1](pillar-1.md) |
| 말로 계획하고 물리 시뮬레이션으로 검증 | [Robot Atlas Physical AI 로봇 워크숍](#robot-atlas) | [P5](pillar-5.md) |

## NVIDIA Isaac Lab on AWS { #isaac-lab }

**[NVIDIA Isaac Lab on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/075ce3fe-6888-4ea9-986e-5bdd1b767ef7/en-US) · AWS 공식 워크숍 · English**

**내용**: EC2에서 Isaac Lab 실행 → AWS Batch 확장 → Isaac Sim에서 모델 확인 → 정리.

**시작 전 확인**: AWS 계정·권한, 컨테이너 기초, GPU 할당량을 준비한다. 실습은 시뮬레이션 기준이다.

**관련 필러**: [P3](pillar-3.md).

## Physical AI E2E 워크숍 { #physical-ai-e2e }

**[Physical AI E2E 워크숍](https://hi-space.gitbook.io/physical-ai-on-aws/guide/e2e-workshop) · 커뮤니티 제작 가이드 · 한국어**

**내용**: Isaac Lab RL, GR00T VLA, Batch·SageMaker, 시뮬레이션 평가를 모듈별로 실습한다.

**시작 전 확인**: CDK·Docker·GPU 환경과 모델 접근 권한을 확인한다. 첫 실행은 필요한 트랙부터 선택한다.

**관련 필러**: [P2](pillar-2.md).

## Getting Started with Amazon Bedrock AgentCore { #agentcore-start }

**[Getting Started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US) · AWS 공식 워크숍 · English**

**내용**: 에이전트 프로토타입, Memory, Gateway, 관측·평가, Policy 등을 순서대로 살펴본다.

**시작 전 확인**: AWS 계정과 사용할 모델·서비스 권한을 확인한다. 로봇 연결은 별도 통합이 필요하다.

**관련 필러**: [P5](pillar-5.md).

## Diving Deep with Amazon Bedrock AgentCore { #agentcore-deep }

**[Diving Deep with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-deep-dive/en-US) · AWS 공식 워크숍 · English**

**내용**: Feature Deep Dive 또는 Build with Skills 트랙에서 기능 조합과 보안·관측을 학습한다.

**시작 전 확인**: 공식 안내는 Getting Started 선행 학습을 요구한다. 개발 환경은 원문의 Prerequisites를 따른다.

**관련 필러**: [P5](pillar-5.md).

## π0 파인튜닝 on SageMaker HyperPod EKS { #pi0-guide }

**[π0 파인튜닝 on SageMaker HyperPod EKS](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) · AWS 구현 글 · English**

**내용**: HyperPod EKS에서 데이터·학습·평가·정리를 연결하는 새 가이드. 2026-09-10 발행.

**시작 전 확인**: 고급 구성. 본문은 공개되지만 본문의 코드 링크(`awsome-distributed-ai/…/3.test_cases/pytorch/pi0-lerobot`)는 404다 — 해당 코드가 main에 병합되지 않고 [미병합 PR #1174](https://github.com/awslabs/awsome-distributed-ai/pull/1174)에 머물러 있다(2026-10-14 확인, PR 최종 갱신 2026-07-30). 병합 전 코드는 검토되지 않은 상태이므로 읽기 자료로 사용한다.

**관련 필러**: [P2](pillar-2.md).

## OpenUSD 산업용 디지털 트윈 샘플 { #spatial }

**[OpenUSD 산업용 디지털 트윈 샘플](https://github.com/aws-samples/sample-physical-ai-spatial-intelligence) · aws-samples · English**

**내용**: L1 정적 장면 → L2 센서 오버레이 → L3 예측 → L4 재보정. 로컬 실행과 AWS 배포 경로를 제공한다.

**시작 전 확인**: Python·Node.js·Docker 등 원문 준비 사항을 따른다. README 복제 예시의 내부 주소 대신 여기 연결한 공개 GitHub 주소를 사용한다.

**관련 필러**: [P3](pillar-3.md).

## VLA Simulator on AWS { #vla-simulator }

**[VLA Simulator on AWS](https://github.com/aws-samples/sample-vla-simulator-on-aws) · aws-samples · English**

**내용**: 여러 VLA와 시뮬레이션 조합을 실행하고 영상·요약 결과를 S3로 모으는 샘플이다.

**시작 전 확인**: CDK·GPU 할당량·모델별 라이선스를 확인한다. 소규모 데모 성공률을 고객 배포 성능으로 인용하지 않는다.

**관련 필러**: [P4](pillar-4.md).

## LeRobot 데이터 수집 on Greengrass { #lerobot-collection }

**[LeRobot 데이터 수집 on Greengrass](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass) · aws-samples · English/한국어**

**내용**: SO-ARM101 리더/팔로워·카메라의 데이터를 LeRobot 형식으로 기록하고 S3에 업로드한다.

**시작 전 확인**: 실로봇·카메라·Greengrass 장치가 필요하다. README는 교육·데모용으로 명시하며 바로 프로덕션에 사용하는 자료가 아니다.

**관련 필러**: [P1](pillar-1.md).

## Robot Atlas Physical AI 로봇 워크숍 { #robot-atlas }

**[Robot Atlas Physical AI 로봇 워크숍](https://robot-atlas.whchoi.net/workshop/) · 커뮤니티 제작 워크숍 · 한국어/English/日本語/中文** · [라이브 데모](https://robot-atlas.whchoi.net/)

**내용**: 3개 트랙, 19개 장이다. 참가자 기본(00~04, 약 110분)은 MuJoCo[^mujoco]에서 집기·쌓기를 재생하고 Bedrock 작업 계획으로 새 배치를 실행한다. 참가자 AWS 배포(05~13, 약 280분)는 AgentCore Runtime 작업 플래너, Private Fargate 물리 엔진, CloudFront·WAF 경로를 구성한다. 진행자 트랙(14~18, 약 195분)은 EKS Auto Mode의 g6e·g7e Spot에서 Isaac Sim RTX 카메라·체크포인트 재개를 다룬다. 라이브 데모에서 로봇 팔·다섯 손가락 손·양팔 옷 접기 시연을 볼 수 있다.

**시작 전 확인**: 교재는 준비된 EC2 VSCode Server와 계정을 전제한다(교재 기준일 2026-09-13). 원문이 밝힌 범위대로 AI는 고수준 계획만 만들고 역기구학·관절 제어기가 로봇을 움직이며, 운동 정책 학습과 실물 로봇 실험은 포함하지 않는다. Isaac Sim 옷 접기는 원문에서 "검증 중"이다. GPU 트랙은 Spot 비용과 정리 절차를 먼저 확인한다.

**관련 필러**: [P5](pillar-5.md) — 계획(System 2)과 제어(System 1)의 분리, [P3](pillar-3.md) — 시뮬레이션 운영.

## 추천 학습 순서

처음 시뮬레이션을 다루면 **Isaac Lab → 한국어 E2E의 필요한 트랙 → VLA Simulator** 순으로 본다. 에이전트는 **AgentCore Getting Started → Deep Dive**로 이어가고, 에이전트 계획을 로봇 시뮬레이션에 연결해 보려면 **Robot Atlas 기본 트랙**을 이어서 본다. 디지털 트윈은 **OpenUSD 샘플의 로컬 실행 → 필요한 AWS 단계**를 선택한다.

## 자료 갱신

신규 자료는 제공자·언어·목적·준비 조건·관련 필러·확인일을 기록한다. 링크가 열리는 것과 실습이 현재 환경에서 재현되는 것은 별도로 확인한다. 신규 발표는 [새 소식](news.md), 검증 대기 기술은 [Radar](radar.md)에 연결한다.

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — 영상과 언어 지시를 입력받아 로봇 동작을 출력하는 모델.
[^mujoco]: **MuJoCo** — 접촉·마찰 계산이 빠른 오픈소스 물리 시뮬레이터. 로봇 조작 연구와 강화학습 벤치마크에서 널리 쓰인다.
