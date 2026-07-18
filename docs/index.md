# Physical AI Playbook — AWS Korea SA

_최종 갱신: 2026-07 · owner: comeddy · 상태: 초기 구축 중_

> **L0 TL;DR**: 고객이 Physical AI 질문을 던졌을 때, 슬랙을 뒤지지 않고 **이 playbook 하나로 아키텍처 방향 · AWS 매핑 · 다음 액션을 5분 안에** 제시하기 위한 참조 자산이다. 논문 요약집도, 뉴스 아카이브도 아니다.

---

## 이 문서를 읽는 법 (30초)

1. **급하면**: 아래 [자주 묻는 질문 Top 20](#자주-묻는-질문-top-20)에서 바로 해당 항목으로 이동.
2. **주제가 잡히면**: 5개 필러 중 하나로 진입. 각 항목은 **L0(1~2문장) → L1(1페이지) → L2(deep-dive 링크)** 로 계층화되어 있다 — 상단만 읽어도 방향이 잡힌다.
3. **갈림길에 섰으면**: [의사결정 트리](decisions.md) — Cloud vs Edge, NVIDIA vs 오픈소스, GPU 확보, Build vs Buy.
4. **"이거 왜 없어요?"**: [Radar](radar.md)를 먼저 확인. 포함 기준 미달로 대기 중인 항목이 거기 있다. 새 후보 제보는 [유지보수 가이드](maintenance.md)의 승격 파이프라인으로.

### 라벨 읽는 법

| 성숙도 | 의미 |
|---|---|
| 🟢 GA | 정식 출시, 프로덕션 사용 가능 |
| 🟡 Preview | 공개 프리뷰 / 명확한 GA 로드맵 |
| 🔵 Research-only | 논문·연구 단계, 고객 제안에 사용 금지 |
| ⚪ Hype | 데모만 존재. "인상적 데모" ≠ "배포 가능" |

| 출처 등급 | 의미 |
|---|---|
| [1] | 공식 문서 / 논문 |
| [2] | AWS 내부 검증 (직접 돌려봄) |
| [3] | 벤더 공식 블로그 |
| [4] | 미검증 (슬랙/소문) — 인용 시 반드시 재확인 |

---

## 5개 필러

| # | 필러 | L0 한 줄 | 바로가기 |
|---|---|---|---|
| 1 | **데이터 수집 & 처리** | 로봇 학습의 병목은 모델이 아니라 데이터다 — 텔레옵·오픈 데이터셋·합성 데이터를 AWS 파이프라인으로 처리하는 법 | [pillar-1](pillar-1.md) |
| 2 | **모델 학습 (VLA)** | VLA/로봇 파운데이션 모델을 어느 규모의 GPU로, 파인튜닝인지 사전학습인지부터 갈라서 설계하는 법 | [pillar-2](pillar-2.md) |
| 3 | **시뮬레이션** | Isaac Sim/Lab vs 오픈소스 선택과 AWS 위에서의 대규모 병렬 시뮬레이션 실행 패턴 | [pillar-3](pillar-3.md) |
| 4 | **Sim-to-Real** | 시뮬레이션에서 학습한 정책을 실기체로 옮기는 검증된 방법론과 엣지 추론 배포 경로 | [pillar-4](pillar-4.md) |
| 5 | **에이전트 오케스트레이션** | LLM 플래너(System 2)가 로봇 컨트롤러(System 1)와 플릿을 지휘하는 계층 — Bedrock AgentCore 중심 | [pillar-5](pillar-5.md) |

> 필러 간 비중은 균등. 각 필러 내부는 **고객 실제 수요 × production-readiness** 순으로 정렬되어 있고, 상단에 "이 필러에서 고객이 가장 자주 묻는 질문 Top 3"가 있다.

---

## 자주 묻는 질문 Top 20

<!-- 1~10: 초기 시드(마스터 프롬프트 예시 + IA 구조). 11~20: 공개 커뮤니티/블로그 심화 조사(2026-07). ⚠️ 둘 다 SA 실제 문의 로그가 아니므로, Slack 문의 이력 확보 시 빈도순 재정렬할 것. -->

| # | 질문 | 어디로 | 출처 |
|---|---|---|---|
| 1 | "Isaac Sim / Isaac Lab을 AWS에서 어떻게 돌리나요?" | [pillar-3](pillar-3.md) | 시드 ⚠️ |
| 2 | "VLA 모델 학습(파인튜닝) 인프라는 어떻게 잡아야 하나요?" | [pillar-2](pillar-2.md) | 시드 ⚠️ |
| 3 | "GPU를 못 구합니다 — On-Demand, Capacity Blocks, 대안 중 뭘 써야 하나요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 4 | "sim-to-real gap은 실제로 어떻게 극복하나요? 검증된 방법이 있나요?" | [pillar-4](pillar-4.md) | 시드 ⚠️ |
| 5 | "로봇 실시간 제어(30–100Hz)인데 추론을 클라우드에 둘 수 있나요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 6 | "파운데이션 모델(GR00T/π0 등)을 파인튜닝할까요, 자체 학습할까요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 7 | "로봇 학습 데이터를 어떻게 모으고 어디에 쌓아야 하나요? (텔레옵/합성 데이터)" | [pillar-1](pillar-1.md) | 시드 ⚠️ |
| 8 | "NVIDIA 풀스택에 얼마나 종속되나요? 오픈소스 대안은요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 9 | "엣지 배포(Jetson 등)와 AWS를 어떻게 연결하나요?" | [pillar-4](pillar-4.md) | 시드 ⚠️ |
| 10 | "LLM 에이전트로 로봇/설비를 지휘하는 아키텍처가 실제로 되나요?" | [pillar-5](pillar-5.md) | 시드 ⚠️ |
| 11 | "이거 다 돌리면 GPU 비용이 얼마나 들죠? 예산은 어떻게 잡나요?" | [decisions](decisions.md) | [AWS Embodied AI 블로그](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "기존 ROS 2 스택·rosbag 데이터를 AWS와 어떻게 연결하죠?" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac 블로그](https://aws.amazon.com/blogs/robotics/) |
| 13 | "여러 노드로 학습을 확장하려면? AWS Batch vs SageMaker HyperPod?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "실배포 전에 정책이 실제로 되는지 어떻게 검증·벤치마크하죠?" | [pillar-4](pillar-4.md) | [NVIDIA 정책 평가](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "로봇/공장 데이터가 민감한데 클라우드 학습이 규제상 괜찮나요? 온프렘·하이브리드는?" | [decisions](decisions.md) | [AWS AI 주권](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "학습한 정책을 어떻게 버전 관리·재현하고 체크포인트를 복구하죠?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Isaac Sim·오픈 모델을 상용 제품에 써도 되나요? NVIDIA AI Enterprise는 언제 필요?" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "정책 추론을 실시간(저지연)으로 최적화하려면? TensorRT·양자화·action chunking?" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "설비/공장 디지털 트윈을 만들어 로봇 시뮬레이션과 연결하려면? TwinMaker·Omniverse?" | [pillar-3](pillar-3.md) | [AWS Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "ML 전문가가 없는데 어디서부터 시작하죠? 최소 PoC 설계는?" | [decisions](decisions.md) | [AWS Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/) |

---

## 페이지 목록

- [pillar-1 — 데이터 수집 & 처리](pillar-1.md)
- [pillar-2 — 모델 학습 (VLA)](pillar-2.md)
- [pillar-3 — 시뮬레이션](pillar-3.md)
- [pillar-4 — Sim-to-Real](pillar-4.md)
- [pillar-5 — 에이전트 오케스트레이션](pillar-5.md)
- [decisions — 교차 의사결정 트리](decisions.md)
- [radar — 대기열/관찰 목록](radar.md)
- [maintenance — 소유권 · 갱신 규칙 · 승격 파이프라인](maintenance.md)

---

## 이 playbook이 담지 않는 것

- **포함 기준 미달 항목**: ⓐ production 검증 ⓑ AWS 매핑 가능 ⓒ 실제 문의 이력 ⓓ GA(로드맵) — 이 중 **2개 미만**이면 본문에 없다. [Radar](radar.md)에 한 줄로만 존재한다.
- **뉴스 속보**: "새로 나왔다"는 포함 사유가 아니다.
- **개념 설명으로 끝나는 항목**: 모든 항목은 "➡️ SA 다음 액션"으로 끝난다. 액션이 없으면 미완성이다.

---

_owner: comeddy · updated: 2026-07 · volatility: 낮음 (구조 페이지 — FAQ Top 20 순위만 분기별 재검토)_
