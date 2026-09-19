# 워크숍·자료

_owner: Youngjin · updated: 2026-09 · volatility: 중간_

> **L0 TL;DR**: 상시 열람할 수 있는 공개 워크숍·구현 가이드·샘플을 한 곳에 모았다. **마지막 확인: 2026-09-19**. 자료 제목에서 원문으로 이동하고, 관련 필러에서 아키텍처 배경을 확인한다.

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

**시작 전 확인**: 고급 구성. 본문은 공개되지만 연결된 코드 경로는 확인일에 404였다. 코드 접근을 확보하기 전에는 읽기 자료로 사용한다.

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

## 추천 학습 순서

처음 시뮬레이션을 다루면 **Isaac Lab → 한국어 E2E의 필요한 트랙 → VLA Simulator** 순으로 본다. 에이전트는 **AgentCore Getting Started → Deep Dive**로 이어간다. 디지털 트윈은 **OpenUSD 샘플의 로컬 실행 → 필요한 AWS 단계**를 선택한다.

## 자료 갱신

신규 자료는 제공자·언어·목적·준비 조건·관련 필러·확인일을 기록한다. 링크가 열리는 것과 실습이 현재 환경에서 재현되는 것은 별도로 확인한다. 신규 발표는 [새 소식](news.md), 검증 대기 기술은 [Radar](radar.md)에 연결한다.

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — 영상과 언어 지시를 입력받아 로봇 동작을 출력하는 모델.
