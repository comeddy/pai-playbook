# 새 소식

_owner: Youngjin · updated: 2026-09 · volatility: 높음_

> **L0 TL;DR**: AWS Physical AI 공식 글에서 새로 읽을 자료를 골라 기존 필러와 연결한다. 아래 날짜는 **원문 발행일**, 목록 확인일은 **2026-09-19**다. 새로운 발표를 찾은 뒤 [워크숍·자료](workshops.md)에서 실습 경로를 고를 수 있다.

공식 원문을 읽어 요약했으며 성능 수치를 독립 재현한 목록은 아니다. 미검증 기술 후보는 기존 [Radar](radar.md)에서 계속 관리한다.

## 최근 자료 한눈에

| 발행일 | 자료 | 연결 |
|---|---|---|
| 2026-09-10 | [π0 파인튜닝 on SageMaker HyperPod EKS](#pi0-hyperpod) | [P2](pillar-2.md) · [π0](workshops.md#pi0-guide) |
| 2026-09-09 | [Telexistence의 DreamZero 실험](#telexistence-dreamzero) | [P1](pillar-1.md) · [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-08-12 | [Luminous Robotics의 태양광 패널 설치 AI](#luminous) | [P3](pillar-3.md) · [P4](pillar-4.md) |
| 2026-08-10 | [WIRobotics의 휴머노이드 도구 사용 학습](#wirobotics) | [P2](pillar-2.md) · [P4](pillar-4.md) |
| 2026-07-31 | [OpenUSD·SDMA 산업용 디지털 트윈 구현](#openusd) | [P3](pillar-3.md) · [OpenUSD](workshops.md#spatial) |
| 2026-07-15 | [Config의 로봇 학습 데이터 증강](#config) | [P1](pillar-1.md) |

## π0 파인튜닝 on SageMaker HyperPod EKS { #pi0-hyperpod }

**발행일: 2026-09-10 · [AWS Physical AI](https://aws.amazon.com/blogs/physical-ai/fine-tuning-%CF%800-pi-zero-for-robotic-manipulation-on-amazon-sagemaker-hyperpod-eks/) `[3]`**

DROID·LIBERO 데이터를 이용한 π0 VLA[^vla] 학습·평가 과정을 소개한다. HyperPod EKS, FSx for Lustre와 학습 잡 구성을 연결해 볼 수 있다.

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

공식 [Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/)와 [RSS](https://aws.amazon.com/blogs/physical-ai/feed/)에서 후속 글을 확인한다. 새 항목은 발행일·원문·적용 범위·필러 연결을 함께 갱신하고, 기술의 필러 승격은 기존 [유지보수 규칙](maintenance.md)을 따른다.

<!-- 용어 각주 -->

[^vla]: **VLA (Vision-Language-Action)** — 영상과 언어 지시를 입력받아 로봇 동작을 출력하는 모델.
[^openloop]: **Open-loop 평가** — 기록된 관측·행동을 이용한 예측 오차 평가. 정책을 실제로 실행하며 다음 관측을 받는 closed-loop 태스크 성공 평가와 다르다.
