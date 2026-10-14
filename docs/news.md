# 새 소식

_owner: Youngjin · updated: 2026-10 · volatility: 높음_

> **L0 TL;DR**: AWS Physical AI 공식 글에서 새로 읽을 자료를 골라 기존 필러와 연결한다. 아래 날짜는 **원문 발행일**, 목록 확인일은 **2026-10-14**다. 새로운 발표를 찾은 뒤 [워크숍·자료](workshops.md)에서 실습 경로를 고를 수 있다.

공식 원문을 읽어 요약했으며 성능 수치를 독립 재현한 목록은 아니다. 미검증 기술 후보는 기존 [Radar](radar.md)에서 계속 관리한다.

## 최근 자료 한눈에

| 발행일 | 자료 | 연결 |
|---|---|---|
| 2026-10-07 | [AWS Physical AI Toolchain 공개](#toolchain) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md) |
| 2026-10-06 | [3D Gaussian Splatting 산업 활용 사례](#gaussian-splatting) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-02 | [Isaac Lab on AWS — 시뮬레이션에서 정책 등록까지](#isaac-lab-aws) | [P3](pillar-3.md) · [Isaac Lab](workshops.md#isaac-lab) |
| 2026-09-28 | [NVIDIA Cosmos 3 on AWS](#cosmos-3) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) |
| 2026-09-10 | [π0 파인튜닝 on SageMaker HyperPod EKS](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence의 DreamZero 실험](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics의 태양광 패널 설치 AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics의 휴머노이드 도구 사용 학습](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD·SDMA 산업용 디지털 트윈 구현](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-15 | [Config의 로봇 학습 데이터 증강](#config) | [P1](pillar-1.md) |

## AWS Physical AI Toolchain 공개 { #toolchain }

**발행일: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

데이터 수집부터 합성 데이터, 학습, 시뮬레이션 검증, 엣지 배포까지 Physical AI 개발 주기를 AWS에서 돌리기 위한 레퍼런스 아키텍처·IaC·배포 자동화 모음이다. NVIDIA GR00T(VLA[^vla] 학습)·Isaac Sim·Isaac Lab·Cosmos·OSMO를 S3·EKS·AWS Batch·SageMaker·EC2·IoT Greengrass(Jetson 배포)에 연결하고, 구성 요소별 Terraform 모듈을 하나씩 도입할 수 있다. 데이터는 Zarr→LeRobot, 엣지는 ONNX·ROS 2 같은 공개 포맷을 쓴다. 코드: [aws-samples 저장소](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws).

**읽을 때 확인할 범위**: 공식 레퍼런스 아키텍처. 글 스스로 "완성된 로봇 동작이 아니라 인프라 패턴"이라고 밝힌다. GR00T 예제는 UR3 pick-and-place 시연 27개로 동작 확인용이며, "몇 주가 아니라 몇 시간"은 AWS 측 설명이다. GPU 할당량(SageMaker·EC2), NGC API 키, Hugging Face 토큰이 필요하고 실습 후 정리(tear down)를 해야 비용이 멈춘다.

**다음 액션**: 병목 단계 하나부터 도입 — P1 데이터 · P2 학습 · P3 시뮬레이션 · P5 오케스트레이션(Strands 에이전트 계층) · Radar 대기 항목 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting 산업 활용 사례 { #gaussian-splatting }

**발행일: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

사진·영상으로 실사 3D 장면을 만드는 3DGS[^3dgs]를 오픈소스 Splat Toolbox([AWS Solutions Library 가이던스](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws))로 처리하는 5단계 파이프라인(입력→전처리→재구성→학습→후처리)과 미디어·로보틱스·건설·제조·부동산 활용을 소개한다. Step Functions·Lambda·AWS Batch/ECS와 EC2 Spot을 쓴다.

**읽을 때 확인할 범위**: 산업 활용 개요. 로보틱스 항목(합성 학습 데이터, sim-to-real 격차 축소, 경로 계획)은 활용 방향 설명이며 정책 성능 실측은 없다. 현재 결과물은 정적 3D이고 4D(시간축) 자산은 로드맵이다. "최대 50% 절감"은 Spot과 온디맨드의 컴퓨팅 단가 비교다.

**다음 액션**: P3 디지털 트윈·씬 재구성 · P4 real-to-sim 후보 — [P3](pillar-3.md) · [P4](pillar-4.md).

## Isaac Lab on AWS — 시뮬레이션에서 정책 등록까지 { #isaac-lab-aws }

**발행일: 2026-10-02 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/isaac-lab-on-aws-from-simulation-to-registered-policy/) `[3]`**

Isaac Sim 5.1.0·Isaac Lab v2.3.2·NVIDIA 드라이버·Amazon DCV를 미리 구운 골든 AMI, 개인용 Instance 모드와 다중 사용자 Fleet 모드(Cognito MFA·자동 확장), SageMaker 학습 잡과 관리형 MLflow 모델 레지스트리를 한 번에 배포하는 AWS CDK 솔루션이다. 데스크톱에서 만든 프로젝트를 이미지 재빌드 없이 학습 잡으로 보내고, 학습된 정책은 MLflow에 자동 등록된다. 샘플은 SO-ARM101 RL·원격조작 데이터 수집, Unitree H1 보행 3종이다.

**읽을 때 확인할 범위**: 공개 저장소가 아니다 — 글 기준으로 **AWS 계정팀을 통해 제공**된다. 레지스트리는 정책을 기록·라벨링할 뿐 서빙하지 않으며, 배포 연결은 팀이 직접 구성해야 한다. 공개 실습이 필요하면 별도의 Isaac Lab 워크숍을 쓴다.

**다음 액션**: P3 시뮬레이션 · 공개 워크숍 [Isaac Lab](workshops.md#isaac-lab) — [P3](pillar-3.md).

## NVIDIA Cosmos 3 on AWS { #cosmos-3 }

**발행일: 2026-09-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/nvidia-cosmos-3-on-aws-omnimodal-world-models-for-physical-ai/) `[3]`**

Cosmos 3(2026-05 공개)는 이전의 Predict·Transfer·Reason 3개 모델을 Mixture-of-Transformers 하나로 합친 모델로, 한 번의 추론에서 장면 이해, 미래 영상 생성(WFM[^wfm]), 로봇 동작 궤적(WAM[^wam])을 함께 낸다. 크기는 Super 64B·Nano 16B·Edge 4B다. AWS 쪽은 데이터 큐레이션(Batch), HyperPod 사후 학습, EKS+NIM 또는 SageMaker JumpStart 추론, Greengrass로 Jetson 엣지 배포까지의 레퍼런스 아키텍처와 인스턴스 권장안을 제시한다.

**읽을 때 확인할 범위**: "최초의 완전 개방 옴니 모델"은 NVIDIA 측 표현이다. 전체 체크포인트는 BF16 기준으로 테스트됐고, 글 스스로 인스턴스별 성능 주장 전에 런타임 구성을 검증하라고 한다. 로봇 동작 출력은 실기 성공률 근거가 아니다.

**다음 액션**: P1 합성 데이터 · P2 모델 학습 · P3 시뮬레이션 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md).

## π0 파인튜닝 on SageMaker HyperPod EKS { #pi0-hyperpod }

**발행일: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

DROID·LIBERO 데이터를 이용한 π0 VLA 학습·평가 과정을 소개한다. HyperPod EKS, FSx for Lustre와 학습 잡 구성을 연결해 볼 수 있다.

**읽을 때 확인할 범위**: 공식 구현 가이드. 보고된 평가는 n=5 open-loop[^openloop]이며 실기 태스크 성공률이 아니다. 연결된 코드 경로는 2026-09-19 공개 접근 확인에 실패해, 우선 블로그 본문을 안내한다.

**다음 액션**: P2 모델 학습 · 워크숍의 π0 읽기 경로 — [P2](pillar-2.md) · [π0](workshops.md#pi0-guide).

## Telexistence의 DreamZero 실험 { #telexistence-dreamzero }

**발행일: 2026-09-09 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/bringing-a-frontier-world-model-to-the-convenience-store-inside-telexistences-dreamzero-experiment-on-aws/) `[3]`**

매장 로봇의 데이터 변환·정제, DreamZero 파인튜닝, 시뮬레이션·실기 평가 과정을 다룬다. EC2와 S3를 사용하는 고객 공동 실험 사례다.

**읽을 때 확인할 범위**: 고객 실험/PoC. 기존 매장 로봇의 운영 실적과 DreamZero 실험의 성과를 구분해서 읽는다.

**다음 액션**: P1 데이터 · P2 학습 · P4 평가 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md).

## Luminous Robotics의 태양광 패널 설치 AI { #luminous }

**발행일: 2026-08-12 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/teaching-robots-to-see-how-luminous-robotics-is-accelerating-energy-infrastructure-construction-with-vision-action-ai/) `[3]`**

태양광 패널 배치에서 사람 확인이 필요한 부분을 줄이기 위한 시각 기반 정책 실험이다. Isaac Sim 데이터와 EC2·S3 학습 흐름을 소개한다.

**읽을 때 확인할 범위**: 고객 기술 사례. 시뮬레이션·오프라인 평가와 현장 도입 범위를 구분한다.

**다음 액션**: P3 시뮬레이션 · P4 Sim-to-Real — [P3](pillar-3.md) · [P4](pillar-4.md).

## WIRobotics의 휴머노이드 도구 사용 학습 { #wirobotics }

**발행일: 2026-08-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-wirobotics-is-teaching-humanoid-robots-to-use-human-tools-with-aws-and-nvidia/) `[3]`**

한국 로봇 기업의 드릴 조작 학습 사례다. AWS·NVIDIA 협업에서 데이터 품질, 학습 설정, 실제 로봇 평가를 어떻게 연결했는지 소개한다.

**읽을 때 확인할 범위**: 고객 협업 사례. 특정 도구·태스크의 관찰 결과를 범용 휴머노이드 성능으로 확대하지 않는다.

**다음 액션**: P2 모델 학습 · P4 실기 평가 — [P2](pillar-2.md) · [P4](pillar-4.md).

## OpenUSD·SDMA 산업용 디지털 트윈 구현 { #openusd }

**발행일: 2026-07-31 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/build-l1-4-industrial-digital-twins-with-openusd-and-sdma-on-aws/) `[3]`**

정적 3D 장면에서 센서 정보·예측·재보정으로 확장하는 단계별 구현 글이다. OpenUSD 레이어와 S3·Kinesis·Lambda·Batch를 연결한다.

**읽을 때 확인할 범위**: 참조 구현. 가이드의 합성 센서 입력과 실제 설비 연결을 구분하고 필요한 단계부터 검토한다.

**다음 액션**: P3 디지털 트윈 · 워크숍의 OpenUSD 자료 — [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial).

## Config의 로봇 학습 데이터 증강 { #config }

**발행일: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

이미 수집한 로봇 시연의 시각적 다양성을 늘리는 흐름이다. S3, Bedrock 설명 생성, Cosmos 기반 변환, HyperPod/EC2를 조합한다.

**읽을 때 확인할 범위**: 고객 공동 기술 글. 증강 후 영상 품질과 로봇 정책의 실제 개선을 각각 평가할 때 참고한다.

**다음 액션**: P1 데이터 수집·처리 — [P1](pillar-1.md).

## 계속 확인할 곳

공식 [Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/)와 [RSS](https://aws.amazon.com/blogs/physical-ai/feed/)에서 후속 글을 확인한다. 새 항목은 발행일·원문·적용 범위·필러 연결을 함께 갱신한다. 일간 자동 스캔이 이 페이지에 없는 글을 `[4]` · ⏳ 원문 대조 대기 표시로 먼저 추가하고, owner가 원문을 대조한 뒤 `[3]`으로 바꾼다. 또한 기술의 필러 승격은 기존 [유지보수 규칙](maintenance.md)을 따른다.

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — 영상과 언어 지시를 입력받아 로봇 동작을 출력하는 모델.
[^openloop]: **Open-loop 평가** — 기록된 관측·행동을 이용한 예측 오차 평가. 정책을 실제로 실행하며 다음 관측을 받는 closed-loop 태스크 성공 평가와 다르다.
[^3dgs]: **3D Gaussian Splatting (3DGS)** — 여러 장의 사진·영상에서 수많은 3D 가우시안(타원형 점)을 맞춰 실사 장면을 실시간 렌더링하는 3D 재구성 기법. 실제 현장을 시뮬레이션 배경으로 옮기는 real-to-sim에 쓰인다.
[^wfm]: **월드 파운데이션 모델(WFM, World Foundation Model)** — 물리 세계의 다음 장면을 예측·생성하도록 학습된 대형 모델. 텍스트·영상 프롬프트로 물리적으로 그럴듯한 영상·시나리오를 만들어 로봇 학습 데이터를 증강한다. 🎥 [NVIDIA Cosmos 소개](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **월드-액션 모델(WAM, World Action Model)** — 미래 장면 예측과 로봇 동작 생성을 한 모델에서 함께 수행하는 모델. 영상만 만드는 월드 모델과 달리 관절 각도·그리퍼 명령 같은 실행 가능한 동작을 출력한다.
