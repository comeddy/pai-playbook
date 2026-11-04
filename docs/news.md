# 새 소식

_owner: Youngjin · updated: 2026-11 · volatility: 높음_

> **L0 TL;DR**: AWS Physical AI 공식 글에서 새로 읽을 자료를 골라 기존 필러와 연결한다. 아래 날짜는 **원문 발행일**, 목록 확인일은 **2026-11-04**다. 새로운 발표를 찾은 뒤 [워크숍·자료](workshops.md)에서 실습 경로를 고를 수 있다.

공식 원문을 읽어 요약했으며 성능 수치를 독립 재현한 목록은 아니다. 미검증 기술 후보는 기존 [Radar](radar.md)에서 계속 관리한다.

> **re:Invent 2026 (11/30–12/4, 라스베이거스)**: 전체 세션 카탈로그에서 Physical AI·시뮬레이션·모델 학습·데이터·엣지·AgentCore 세션 45개를 [골라 두었다](#reinvent-2026).

## 최근 자료 한눈에

| 발행일 | 자료 | 연결 |
|---|---|---|
| 2026-11-03 | [NVIDIA CloudXR 6 on AWS — 디지털 트윈을 XR 헤드셋으로 스트리밍](#cloudxr-6) | [P1](pillar-1.md) · [P3](pillar-3.md) |
| 2026-10-28 | [Archetype AI Newton — 산업 센서 데이터를 운영 인텔리전스로](#archetype-newton) | [P4](pillar-4.md) · [P5](pillar-5.md) |
| 2026-10-28 | [AWS × RLWRLD — 내일의 인력을 위한 Physical AI](#aws-rlwrld-workforce) | [Radar](radar.md) · [P2](pillar-2.md) |
| 2026-10-28 | [Visual Asset Management System 2.6 공개](#vams-2-6) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-07 | [AWS Physical AI Toolchain 공개](#toolchain) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md) |
| 2026-10-06 | [3D Gaussian Splatting 산업 활용 사례](#gaussian-splatting) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-10-02 | [Isaac Lab on AWS — 시뮬레이션에서 정책 등록까지](#isaac-lab-aws) | [P3](pillar-3.md) · [Isaac Lab](workshops.md#isaac-lab) |
| 2026-09-28 | [NVIDIA Cosmos 3 on AWS](#cosmos-3) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) |
| 2026-09-10 | [π0 파인튜닝 on SageMaker HyperPod EKS](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence의 DreamZero 실험](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics의 태양광 패널 설치 AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics의 휴머노이드 도구 사용 학습](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD·SDMA 산업용 디지털 트윈 구현](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-17 | [Edge Impulse와 AWS — 엣지 추론과 클라우드 지능 결합](#edge-impulse-aws) | [P4](pillar-4.md) · [P5](pillar-5.md) |
| 2026-07-15 | [Config의 로봇 학습 데이터 증강](#config) | [P1](pillar-1.md) |

## NVIDIA CloudXR 6 on AWS — 디지털 트윈을 XR 헤드셋으로 스트리밍 { #cloudxr-6 }

**발행일: 2026-11-03 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/streaming-physical-ai-digital-twins-and-immersive-experiences-to-xr-headsets-with-nvidia-cloudxr-6-on-aws/) `[4]` · ⏳ owner 원문 대조 대기 (로컬 세션 2026-11-04 RSS 본문 확인)**

GPU 렌더링한 OpenXR 콘텐츠를 경량 XR 헤드셋으로 스트리밍하는 NVIDIA CloudXR 6를 Amazon EC2 GPU 인스턴스에서 돌리는 AWS 샘플([aws-samples/sample-cloudxr6-on-aws](https://github.com/aws-samples/sample-cloudxr6-on-aws))을 소개한다. Physical AI 쪽 용도는 디지털 트윈[^dtwin] 리뷰, 시뮬레이션 장면 검증, 시뮬레이션 속 텔레옵으로 정책 학습용 시연 데이터 수집이며, NVIDIA Isaac GR00T 엔드투엔드 워크플로의 Isaac Sim XR 텔레옵 예시를 함께 언급한다. 구성은 CloudFront(진입점·CloudXR.js 웹 클라이언트) → ECS Fargate 시그널링 프록시(Cognito 인증, DynamoDB 인스턴스 레지스트리) → Local Zone 또는 리전의 EC2 GPU 풀이고, 미디어는 헤드셋과 GPU 인스턴스 사이를 UDP로 직접 흐른다. 클라이언트는 Apple Vision Pro(네이티브)와 Meta Quest·Pico(브라우저 WebRTC) 두 경로를 지원한다.

**읽을 때 확인할 범위**: AWS 샘플 공개 글(아키텍처·배포 가이드). 지연 수치는 AWS 자체 테스트 1건 — 로스앤젤레스 Local Zone의 g7e 인스턴스에서 같은 LA 지역 Meta Quest 3로 약 90 FPS, pose-to-render 지연[^p2r] 약 35 ms(네트워크 왕복 약 8–9 ms)였다. NVIDIA 목표치(20–30 ms)보다는 높고 상한(100 ms)보다는 낮다. 한국에서 재현하려면 서울 리전 또는 가까운 Local Zone의 GPU 인스턴스 가용성과 실측 지연을 따로 확인해야 한다. 고객 프로덕션 사례는 글에 없다.

**다음 액션**: P1 텔레옵 데이터 수집 · P3 디지털 트윈 리뷰 — [P1](pillar-1.md) · [P3](pillar-3.md).

## Archetype AI Newton — 산업 센서 데이터를 운영 인텔리전스로 { #archetype-newton }

**발행일: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/industrial-sensor-data-to-operational-intelligence-with-archetype-ai-on-aws/) `[4]` · ⏳ owner 원문 대조 대기 (로컬 세션 2026-11-04 RSS 본문 확인)**

Archetype AI의 물리 월드 모델 Newton을 AWS에 배포해 진동·압력·온도·전류·레이더·영상 같은 멀티모달 센서 신호에서 이상 탐지·상태 모니터링·작업 검증을 하는 파트너 소개 글이다. Newton은 80억(8B) 파라미터 모델이며, 엣지용으로 8,500만(85M) 파라미터 모델로 증류할 수 있다고 설명한다. 플랫폼은 [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-pjqoobj6vnbhm)에서 고객 계정의 전용 VPC로 배포되고 Amazon EKS(CPU·GPU 노드 그룹), S3·Aurora PostgreSQL·ElastiCache 위에서 돈다. 엣지 에이전트는 온프레미스·산업용 엣지 하드웨어에 배포하며 AWS IoT Greengrass·Outposts를 선택적으로 쓴다. 클라우드 수집 경로는 IoT Core·Kinesis Data Streams·MSK다.

**읽을 때 확인할 범위**: 파트너(Archetype AI) 솔루션 소개 글. 성능 수치는 모두 벤더 자체 발표로 독립 실측이 아니다 — 펌프 상태 탐지 "최대 90% 정확도(소수 라벨 예시)", 기어박스 결함 탐지 "99% 정확도·기존 방식 대비 80% 빠른 배포", 건설 현장 영상 12,000시간 분석 사례가 모두 고객명 없이 제시된다. "과업별 학습 없이 바로 동작(zero-shot)"도 벤더 주장이다. 로봇 정책이 아니라 산업 설비 센서 해석 모델이라 플레이북의 로봇 학습 축보다는 엣지 운영·모니터링 축에 가깝다.

**다음 액션**: P4 엣지 배포(Greengrass·Outposts) · P5 운영 모니터링 — [P4](pillar-4.md) · [P5](pillar-5.md).

## AWS × RLWRLD — 내일의 인력을 위한 Physical AI { #aws-rlwrld-workforce }

**발행일: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/aws-rlwrld-building-the-workforce-of-tomorrow-with-physical-ai/) `[4]` · ⏳ 원문 대조 대기 (자동 스캔 2026-11-02)**

AWS와 RLWRLD의 Physical AI 협업을 다루는 시리즈 2편으로, 2026-06-22 1편("Putting Dexterous Robots to Work")의 후속이다. RLWRLD가 AWS Validated Partner로 등재되고 AWS Marketplace에 제품 2종을 올렸다고 소개하며, 박스 집기·상품 피킹·진열 보충 같은 인력난 대응 PoC 계획과 AWS Physical AI 로드쇼를 통한 고객 파이프라인 형성을 다룬다. RLDX-1이 선두 파운데이션 모델 대비 약 20%의 학습 컴퓨트로 비슷한 성능에 도달했다는 주장도 인용한다.

**읽을 때 확인할 범위**: AWS·RLWRLD 공식 파트너십 시리즈 글(고객 협업 소개 성격). "AWS Validated Partner"·Marketplace 등재는 파트너 프로그램 지위이지 실배포 성과가 아니다. 박스 집기·피킹·진열 보충 PoC는 원문에서 계획(planned) 단계로 서술되며 실가동 사례가 아니다. "약 20% 컴퓨트로 동급 성능" 주장은 RLWRLD 자체 기술 블로그를 인용한 벤더 자체 표현이며, 기존 [Radar](radar.md)의 RLDX-1 항목에 있는 자체 공표 벤치마크와 같은 성격 — 독립 실측이 아니다. 이번 세션은 전역 egress 차단으로 aws.amazon.com 원문에 직접 접속하지 못해 복수의 독립 검색 결과(제목·날짜·핵심 서술 일치)로 교차 확인했다 — 세부 수치는 owner의 원문 대조가 필요하다.

**다음 액션**: 기존 RLDX-1 Radar 항목과 연결 · P2 모델 학습 — [Radar](radar.md) · [P2](pillar-2.md).

## Visual Asset Management System 2.6 공개 { #vams-2-6 }

**발행일: 2026-10-28 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/visual-asset-management-system-2-6-release/) `[4]` · ⏳ 원문 대조 대기 (자동 스캔 2026-11-02)**

VAMS는 AWS Physical AI·PACE 팀이 만든 오픈소스 3D/공간 자산 관리 액셀러레이터로, 2.6은 2.0(2024-06) 이후 "가장 큰 업데이트"라고 소개한다. 오케스트레이션 레이어를 다시 설계해 멀티파일·멀티에셋 실행, 전역 실행 뷰, 업로드 트리거 자동 워크플로를 추가했고, AWS European Sovereign Cloud 배포 템플릿, Amazon Cognito OIDC 연동, 세분화된 IAM 역할 커스터마이징, 기본 차단형 WAF, 자산 생애주기·버전별 변경 이력 추적 기능을 더했다. 데모로는 시맨틱 검색, 브라우저 내 SuperSplat(가우시안 스플랫[^3dgs]) 편집기, IFC BIM 뷰어, 지리공간 지도 검색, NVIDIA Cosmos text-to-world 워크플로를 소개한다. 코드는 [GitHub awslabs/visual-asset-management-system](https://github.com/awslabs/visual-asset-management-system)에 공개된 오픈소스다.

**읽을 때 확인할 범위**: 공식 오픈소스 솔루션 업데이트 글. "2.0 이후 가장 큰 업데이트"는 AWS 측 자체 표현이며, 실제 고객 프로덕션 도입 성과나 성능 수치는 글에서 제시되지 않는다. 공개 저장소이지 계정팀 전용 경로가 아니다 — 누구나 GitHub에서 받아 쓸 수 있다. 이번 세션은 전역 egress 차단으로 aws.amazon.com 원문에 직접 접속하지 못해 검색 스니펫과 GitHub 릴리스 태그(2.6.0 2026-09-11 ~ 2.6.6 2026-10-30)로 교차 확인했다 — 발행일(2026-10-28)도 검색 스니펫 기준이며 owner의 원문 대조가 필요하다.

**다음 액션**: P3 디지털 트윈·씬 재구성 · P4 real-to-sim 후보 — [P3](pillar-3.md) · [P4](pillar-4.md).

## AWS Physical AI Toolchain 공개 { #toolchain }

**발행일: 2026-10-07 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/introducing-aws-physical-ai-toolchain/) `[3]`**

데이터 수집부터 합성 데이터, 학습, 시뮬레이션 검증, 엣지 배포까지 Physical AI 개발 주기를 AWS에서 돌리기 위한 레퍼런스 아키텍처·IaC·배포 자동화 모음이다. NVIDIA GR00T(VLA[^vla] 학습)·Isaac Sim·Isaac Lab·Cosmos·OSMO를 S3·EKS·AWS Batch·SageMaker·EC2·IoT Greengrass(Jetson 배포)에 연결하고, 구성 요소별 Terraform 모듈을 하나씩 도입할 수 있다. 데이터는 Zarr→LeRobot, 엣지는 ONNX·ROS 2 같은 공개 포맷을 쓴다. 코드: [aws-samples 저장소](https://github.com/aws-samples/sample-the-physical-ai-toolchain-on-aws).

**읽을 때 확인할 범위**: 공식 레퍼런스 아키텍처. 글 스스로 "완성된 로봇 동작이 아니라 인프라 패턴"이라고 밝힌다. GR00T 예제는 UR3 pick-and-place 시연 27개로 동작 확인용이며, "몇 주가 아니라 몇 시간"은 AWS 측 설명이다. GPU 할당량(SageMaker·EC2), NGC API 키, Hugging Face 토큰이 필요하고 실습 후 정리(tear down)를 해야 비용이 멈춘다.

**다음 액션**: 병목 단계 하나부터 도입 — P1 데이터 · P2 학습 · P3 시뮬레이션 · P5 오케스트레이션(Strands 에이전트 계층) · Radar 대기 항목 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P5](pillar-5.md) · [Radar](radar.md).

## 3D Gaussian Splatting 산업 활용 사례 { #gaussian-splatting }

**발행일: 2026-10-06 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/3d-gaussian-splatting-in-practice-industry-use-cases/) `[3]`**

사진·영상으로 실사 3D 장면을 만드는 3DGS를 오픈소스 Splat Toolbox([AWS Solutions Library 가이던스](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws))로 처리하는 5단계 파이프라인(입력→전처리→재구성→학습→후처리)과 미디어·로보틱스·건설·제조·부동산 활용을 소개한다. Step Functions·Lambda·AWS Batch/ECS와 EC2 Spot을 쓴다.

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

**읽을 때 확인할 범위**: 공식 구현 가이드. 보고된 평가는 n=5 open-loop[^openloop]이며 실기 태스크 성공률이 아니다. 본문의 코드 링크는 404다 — 코드가 main에 병합되지 않고 [미병합 PR #1174](https://github.com/awslabs/awsome-distributed-ai/pull/1174)에 있다(2026-10-14 확인). 우선 블로그 본문을 안내한다.

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

## Edge Impulse와 AWS — 엣지 추론과 클라우드 지능 결합 { #edge-impulse-aws }

**발행일: 2026-07-17 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/edge-impulse-and-aws-combining-edge-inference-with-cloud-intelligence-for-physical-ai/) `[4]` · ⏳ 원문 대조 대기 (자동 스캔 2026-10-16)**

Qualcomm 자회사 Edge Impulse와 AWS가 함께 쓴 글로, 창고 설비 위치 추적을 예시로 한 하이브리드 엣지-클라우드 아키텍처를 소개한다. 카메라 엣지 디바이스에서 Edge Impulse YOLO Pro 객체 탐지와 Qwen2-VL 8B 비전-언어 모델로 1차 판단을 하고, 확정된 감지만 클라우드로 올려 Amazon Bedrock AgentCore(Nova Lite)가 "지게차가 어디 있나" 같은 자연어 질의에 답한다. AWS IoT Core가 디바이스 연결·MQTT 메시징을, Greengrass가 엣지 모델 배포·관리를, S3가 재학습용 이미지 저장을 맡는다.

**읽을 때 확인할 범위**: AWS·Edge Impulse 공동 파트너 소개 글. 공개 저장소 경로가 원문에 명확히 적혀 있지 않아 공개 샘플인지 계정팀 경로인지 추가 확인이 필요하다. "지연시간·대역폭 감소"는 엣지 우선 처리 설계의 이점 서술이며 수치화된 벤치마크가 아니다 — 벤더 설명과 실측을 구분해서 읽는다.

**다음 액션**: P4 엣지 추론 배포 · P5 에이전트 오케스트레이션(Bedrock AgentCore) — [P4](pillar-4.md) · [P5](pillar-5.md).

## Config의 로봇 학습 데이터 증강 { #config }

**발행일: 2026-07-15 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/how-config-scales-robot-training-data-without-scaling-data-collection/) `[3]`**

이미 수집한 로봇 시연의 시각적 다양성을 늘리는 흐름이다. S3, Bedrock 설명 생성, Cosmos 기반 변환, HyperPod/EC2를 조합한다.

**읽을 때 확인할 범위**: 고객 공동 기술 글. 증강 후 영상 품질과 로봇 정책의 실제 개선을 각각 평가할 때 참고한다.

**다음 액션**: P1 데이터 수집·처리 — [P1](pillar-1.md).

## re:Invent 2026 — Physical AI 관련 세션 { #reinvent-2026 }

**행사: 2026-11-30 ~ 12-04 · [re:Invent 2026 이벤트 카탈로그](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog) `[3]` · 카탈로그 확인일: 2026-11-02**

카탈로그의 전체 2,415개 세션(반복 회차 포함)을 받아, 제목·초록에서 Physical AI·로보틱스·월드 모델·시뮬레이션·디지털 트윈·모델 학습(HyperPod·Trainium)·학습 데이터·엣지·AgentCore 키워드로 1차 추린 뒤 필러와 직접 연결되는 45개를 골랐다. AgentCore는 제목에 들어간 세션만 60개가 넘어 프로덕션 운영 패턴과 제조·현장 사례 위주로 남겼다. 세션 코드를 누르면 카탈로그 검색 결과로 이동한다. 시간은 현지(PT) 기준이고, 같은 세션의 다른 회차는 "반복"으로 적었다. 형식: Workshop 120분 실습 · Builders' session 60분 소규모 실습 · Chalk talk 60분 화이트보드 토론 · Code talk 60분 라이브 코딩 · Lightning talk 20분.

**키노트·패널**

| 일시 (PT) | 세션 | 형식 | 볼 포인트 |
|---|---|---|---|
| 12/1(화) 08:30 | [KEY002](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY002) CEO Keynote | Keynote | AI 인프라·추론·에이전트 플랫폼 신규 발표 — Physical AI 관련 발표 여부 확인용 |
| 12/2(수) 08:30 | [KEY003](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY003) Data & AI Keynote | Keynote | 에이전트가 데이터에 닿는 방식·가치 측정·한계 설정 — P1 데이터·P5 에이전트 관점 |
| 12/2(수) 14:00 | [SUP201](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=SUP201) Training and simulation turn robot capabilities into useful products | Breakout session | NEURA Robotics·1X·Highlanders 패널 — 학습·시뮬레이션·데이터 파이프라인을 제품으로 연결 |
| 12/3(목) 08:30 | [KEY005](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=KEY005) Technical Innovations Keynote | Keynote | Graviton·Trainium·네트워크·스토리지 내부 구조 — 학습 인프라 선택의 배경 |
| 12/3(목) 10:00 | [AIM2215](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2215) World Models & Physical AI: The next frontier in intelligent systems | Breakout session | 월드 모델 패널 — 연구자·고객의 프로덕션 배포 경험과 기술 과제 |
| 12/3(목) 13:30 | [AIM2213](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM2213) How leading AI builders push the frontier with AWS Trainium | Breakout session | 월드 모델·Physical AI 등 4개 고객의 Trainium 사용 사례 패널 |

**Physical AI 파이프라인 — P1·P2·P3·P5**

| 일시 (PT) | 세션 | 형식 | 볼 포인트 |
|---|---|---|---|
| 11/30(월) 10:00 | [IND3338-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3338-R) Accelerate Physical AI development with NVIDIA on AWS | Chalk talk | AWS Physical AI Toolchain으로 합성 데이터→학습→sim-to-real→HIL 검증 전 주기 |
| 11/30(월) 12:00 | [AIM449](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM449) One agent, any robot: building physical AI with Strands Robots | Chalk talk | Strands Robots SDK — MuJoCo 시뮬레이션과 실기를 파라미터 하나로 전환, GR00T·Cosmos 3·LeRobot 정책, IoT 브리지 플릿 |
| 11/30(월) 15:00 | [IND389](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND389) Physical AI for MedTech: From Intelligent Devices to Business Impact | Chalk talk | 의료기기 Physical AI 스택 — SageMaker 학습, Greengrass 엣지 추론, 규제 대응 OTA |
| 12/1(화) 13:30<br>반복 12/1(화) 15:00 | [IND322-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND322-R) Physical AI in Telecom: A Framework for Workload Placement | Chalk talk | Physical AI 워크로드 배치 기준 — 리전·Local Zones·Outposts·셀 사이트 선택 |
| 12/1(화) 16:30 | [AIM413](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM413) Build a Physical AI Model Factory on SageMaker HyperPod | Chalk talk | 합성 시나리오→사후 학습→평가 데이터 플라이휠을 HyperPod EKS 이기종 GPU 풀에서 운영 |
| 12/2(수) 08:30<br>반복 12/3(목) 14:30 | [CMP407-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP407-R) Orchestrating Physical AI workloads on AWS: Compute and pipeline patterns | Chalk talk | Batch(병렬 시뮬레이션)·EKS+Karpenter(학습)·HyperPod 비교, Capacity Blocks·Spot 비용 전략 |
| 12/2(수) 12:30 | [AIM458-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM458-S) The Physical AI Blueprint: A Full-Stack Solution with AWS and NVIDIA (sponsored by NVIDIA) | Workshop | 실습: Isaac Sim 합성 데이터, GR00T·Cosmos 학습, Omniverse 트윈, Greengrass 배포, AgentCore 다중 로봇 오케스트레이션 |

**시뮬레이션·디지털 트윈 — P3**

| 일시 (PT) | 세션 | 형식 | 볼 포인트 |
|---|---|---|---|
| 11/30(월) 13:30 | [CMP408](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CMP408) The cloud holodeck: Stream NVIDIA Omniverse, scale headless sim on AWS | Chalk talk | DCV로 Omniverse·Isaac Sim 워크스테이션 스트리밍 + Batch 헤드리스 대량 렌더링, VAMS 관리 |
| 12/1(화) 15:00 | [IND102-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND102-S) Accelerating with NVIDIA Omniverse: VW’s Battery Manufacturing Digital Twin (sponsored by NVIDIA) | Breakout session | 폭스바겐 배터리 공장 OpenUSD 디지털 트윈 — 가상 시운전·합성 검사 데이터 |
| 12/1(화) 16:00<br>반복 12/2(수) 09:00 | [IND401-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND401-R) Build, simulate, and validate physical AI-driven robotic systems | Builders' session | 실습: 가상 PLC·필드버스·Omniverse 물리 시뮬레이션으로 다중 로봇 셀 디지털 트윈 구성 |
| 12/2(수) 16:30 | [CON409](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=CON409) ML, automotive, and robotics simulations at scale on AWS Batch | Breakout session | 자동차·로보틱스 시뮬레이션 → 데이터 레이크 → GPU 학습 루프를 Batch로 오케스트레이션 |
| 12/3(목) 16:30 | [IND3355](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND3355) Building Worlds for Machines: VAMS and 3DGS for Autonomy | Lightning talk | 현장 센서 데이터 → 3DGS 재구성 → 시뮬레이션용 환경 (20분 라이트닝) |

**월드 모델·로봇 학습 연구 — P2**

| 일시 (PT) | 세션 | 형식 | 볼 포인트 |
|---|---|---|---|
| 11/30(월) 13:00<br>반복 12/2(수) 12:00 | [AIM305-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM305-R) Hands-on training world models and deploying agents for Physical AI | Builders' session | 실습: Trainium·Neuron으로 트랜스포머 월드 모델 파인튜닝(PEFT) 후 에이전트 배포 |
| 11/30(월) 16:00 | [AIM323](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM323) Serving world models on AWS Trainium with native PyTorch | Code talk | torch.compile·커스텀 커널로 월드 모델 추론을 Trainium에서 서빙 |
| 11/30(월) 16:30 | [INV531](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV531) Visual reasoning will be bigger than language reasoning | Chalk talk | UW Ranjay Krishna — 점·궤적·깊이 같은 시각 표현으로 추론하는 로봇 파운데이션 모델 |
| 12/1(화) 11:30<br>반복 12/3(목) 13:30 | [AIM304-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM304-R) Deploy and optimize world models with agentic AI workflows | Builders' session | 실습: 실시간 영상 월드 모델을 Trainium에 배포, Neuron 에이전트 스킬로 커널 최적화 |
| 12/2(수) 10:30 | [INV527](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV527) World models for indoor robots: what breaks and why | Chalk talk | Diligent Robotics 병원 로봇용 라이다 월드 모델 — 트랜스포머의 기하 추론이 깨지는 지점 |
| 12/2(수) 13:30 | [INV537](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=INV537) No torque sensors, no problem: learning safe physical interaction for humanoids | Chalk talk | Fauna Robotics — 토크 센서 없는 휴머노이드의 순응(compliant) 제어 학습 |

**모델 학습·데이터 인프라 — P1·P2**

| 일시 (PT) | 세션 | 형식 | 볼 포인트 |
|---|---|---|---|
| 11/30(월) 08:30 | [AIM406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM406) End-to-end foundation model pipelines on SageMaker HyperPod with EKS | Workshop | 실습: HyperPod EKS에서 데이터 준비→분산 파인튜닝→같은 클러스터 추론 |
| 11/30(월) 15:00 | [AIM318](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM318) Resilient VLM Training at Scale on Amazon SageMaker HyperPod | Workshop | 실습: VLM 학습 중 노드 장애를 일부러 일으키고 자동 복구·체크포인트로 이어 가기 |
| 11/30(월) 15:00 | [AIM433](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM433) Maximize GPU utilization across training and inference on HyperPod | Chalk talk | HyperPod을 데이터 처리·학습·추론 공용 GPU 풀로 — 팀 간 스케줄링 |
| 12/1(화) 12:00<br>반복 12/3(목) 08:00 | [AIM334-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM334-R) Hands-on distributed training with AWS Trainium and PyTorch | Workshop | 실습: TorchTitan으로 Trainium 분산 학습 — 병렬화 전략·성능 튜닝 |
| 12/1(화) 14:30 | [AIM362](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM362) Which customization compute? A decision approach for model fine-tuning | Chalk talk | 파인튜닝 컴퓨팅 선택 기준 — 서버리스 커스터마이징·학습 잡·HyperPod |
| 12/2(수) 15:00 | [AIM3308](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM3308) What's new: SageMaker HyperPod, with learnings from Multiverse | Breakout session | SageMaker HyperPod 신규 기능(EKS·Slurm) — 월드 모델 등 대규모 학습·서빙 |
| 12/2(수) 15:30<br>반복 12/3(목) 08:00 | [AIM434-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM434-R) From raw data to custom model: Dataset prep with Amazon SageMaker AI | Workshop | 실습: 데이터셋 프로파일링·자동 라벨링·사람 검토·합성 데이터로 학습 데이터 준비 |

**현장 운영·엣지 — P4**

| 일시 (PT) | 세션 | 형식 | 볼 포인트 |
|---|---|---|---|
| 11/30(월) 10:00 | [DVT210-S](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=DVT210-S) When Telemetry Steers the Robot: Observability for Physical AI (sponsored by groundcover) | Breakout session | Path Robotics 용접 로봇·사족 로봇의 관측성(observability) 사례 (스폰서 세션) |
| 11/30(월) 15:00<br>반복 12/1(화) 12:30 | [IND402-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND402-R) Agentic AI for manufacturing: Build a cross-domain digital thread | Workshop | 실습: Neptune·AgentCore·IoT SiteWise로 OT·IT 데이터를 잇는 제조 디지털 스레드 |
| 12/1(화) 12:30<br>반복 12/3(목) 08:30 | [HMC403-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC403-R) Self-managed agentic AI at the hybrid edge | Workshop | 실습: Local Zones·Outposts에서 자체 관리형 에이전트 AI 실행 (데이터 상주·저지연) |
| 12/2(수) 16:30 | [IND378](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND378) How Mercedes-Benz accelerates engineering and production with AI | Breakout session | 메르세데스-벤츠 — AgentCore 엔지니어링 에이전트와 클라우드 네이티브 MES·디지털 트윈 |
| 12/3(목) 08:30 | [HMC406](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=HMC406) How Amazon Robotics runs AWS Outposts across hundreds of fulfillment centers | Code talk | Amazon Robotics가 수백 개 물류센터에서 Outposts를 운영하는 방식 — 격리·장애 조치 |
| 12/3(목) 09:00 | [IND384](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND384) Inside T-Mobile's Kinetic Edge: Real-Time Physical AI at Scale | Breakout session | T-Mobile Kinetic Edge — Outposts·SageMaker·AgentCore로 네트워크 엣지 실시간 Physical AI |
| 12/4(금) 08:30 | [IND345](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=IND345) Human+AI Collaboration: How Amazon Deploys Autonomous Operations on AWS | Breakout session | Amazon 물류 현장의 휴머노이드·사족·AMR·드론 혼합 플릿 오케스트레이션 아키텍처 |

**AgentCore — P5**

| 일시 (PT) | 세션 | 형식 | 볼 포인트 |
|---|---|---|---|
| 11/30(월) 08:30<br>반복 12/2(수) 08:00 | [AIM439-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM439-R) Getting Started with AgentCore: ship an agent to production in 2 hours | Workshop | 실습 2시간: AgentCore CLI로 런타임·메모리·게이트웨이·ID·정책·관측성·평가를 차례로 추가 |
| 11/30(월) 10:00<br>반복 12/2(수) 15:00 | [AIM436-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM436-R) Scale production agents reliably with AgentCore | Chalk talk | 세션 10개→1만 개 확장 패턴 — microVM 격리, 도구 호출 실패·타임아웃 대응 |
| 11/30(월) 14:00<br>반복 12/3(목) 08:00 | [TNC331-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=TNC331-R) Ship AI Agents Faster with AgentCore Harness | Lab | 실습: AgentCore Harness — 설정만으로 에이전트 루프 실행, 도구·스킬 추가, 버전 엔드포인트 |
| 11/30(월) 14:30 | [AIM370](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM370) Trusting agents in production: end-to-end security with AgentCore | Breakout session | AgentCore 종단 보안 — microVM 격리, ID 전파, Gateway 정책, Cedar 최소 권한 |
| 12/2(수) 11:30 | [AIM450-R](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM450-R) Context engineering for production agents on AgentCore | Chalk talk | 컨텍스트 엔지니어링 — 시스템 프롬프트·스킬·도구 정의·메모리 배분 |
| 12/2(수) 15:00 | [AIM212](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM212) Best practices for production agents on AgentCore, with Nasdaq | Breakout session | AgentCore 프로덕션 모범 사례 + Nasdaq의 멀티 계정 격리·에이전트 ID 운영 |
| 12/3(목) 14:30 | [AIM452](https://registration.awsevents.com/flow/awsevents/reinvent2026/eventcatalog/page/eventcatalog?search=AIM452) Build long-running agents that persist for days on AgentCore | Chalk talk | 며칠씩 지속되는 에이전트 — Runtime 내구 실행·Memory·사람 승인 일시정지/재개 |

**읽을 때 확인할 범위**: 세션 초록(사전 공지)이며 발표 내용이 아니다. 일정·장소는 바뀔 수 있으니 현장 앱에서 다시 확인한다. "35주→3.5주"(IND378), "수 주→수 시간"(IND401) 같은 수치는 발표자 측 주장이다. AIM305·AIM304는 Trainium에서 월드 모델을 학습·서빙하는 실습을 예고한다 — [P2](pillar-2.md)의 "Trainium으로 VLA를 학습한 공개 사례 없음" 판단은 세션 자료가 공개되고 재현이 확인된 뒤 다시 검토한다.

**다음 액션**: 담당 필러별로 세션을 고른다 — [P1](pillar-1.md) · [P2](pillar-2.md) · [P3](pillar-3.md) · [P4](pillar-4.md) · [P5](pillar-5.md). 행사 후 키노트 발표와 녹화·발표 자료가 공개되면 해당 행을 원문 링크로 바꾸고, 새 서비스·기능은 [Radar](radar.md) 경로로 올린다.

## 계속 확인할 곳

공식 [Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/)와 [RSS](https://aws.amazon.com/blogs/physical-ai/feed/)에서 후속 글을 확인한다. 새 항목은 발행일·원문·적용 범위·필러 연결을 함께 갱신한다. 일간 자동 스캔이 이 페이지에 없는 글을 `[4]` · ⏳ 원문 대조 대기 표시로 먼저 추가하고, owner가 원문을 대조한 뒤 `[3]`으로 바꾼다. 또한 기술의 필러 승격은 기존 [유지보수 규칙](maintenance.md)을 따른다.

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — 영상과 언어 지시를 입력받아 로봇 동작을 출력하는 모델.
[^openloop]: **Open-loop 평가** — 기록된 관측·행동을 이용한 예측 오차 평가. 정책을 실제로 실행하며 다음 관측을 받는 closed-loop 태스크 성공 평가와 다르다.
[^3dgs]: **3D Gaussian Splatting (3DGS)** — 여러 장의 사진·영상에서 수많은 3D 가우시안(타원형 점)을 맞춰 실사 장면을 실시간 렌더링하는 3D 재구성 기법. 실제 현장을 시뮬레이션 배경으로 옮기는 real-to-sim에 쓰인다.
[^wfm]: **월드 파운데이션 모델(WFM, World Foundation Model)** — 물리 세계의 다음 장면을 예측·생성하도록 학습된 대형 모델. 텍스트·영상 프롬프트로 물리적으로 그럴듯한 영상·시나리오를 만들어 로봇 학습 데이터를 증강한다. 🎥 [NVIDIA Cosmos 소개](https://www.youtube.com/watch?v=9Uch931cDx8)
[^wam]: **월드-액션 모델(WAM, World Action Model)** — 미래 장면 예측과 로봇 동작 생성을 한 모델에서 함께 수행하는 모델. 영상만 만드는 월드 모델과 달리 관절 각도·그리퍼 명령 같은 실행 가능한 동작을 출력한다.
[^dtwin]: **디지털 트윈(digital twin)** — 실제 공장·창고·로봇을 물리적으로 충실하게 본뜬 가상 복제본. 실환경을 건드리지 않고 정책 학습·검증·시나리오 실험을 할 수 있게 한다.
[^p2r]: **pose-to-render 지연** — 사용자가 머리를 움직인 순간부터 그에 맞는 프레임이 헤드셋에 표시될 때까지의 시간. 길어지면 보이는 화면과 몸의 감각이 어긋나 멀미가 생기므로 XR 스트리밍 품질의 핵심 지표다.
