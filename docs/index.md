# Physical AI Playbook 안내

_최종 갱신: 2026-07 · owner: Youngjin · 상태: 초기 구축 중_

> **L0 TL;DR**: 고객이 Physical AI 질문을 던졌을 때, 슬랙을 뒤지지 않고 **이 playbook 하나로 아키텍처 방향 · AWS 매핑 · 다음 액션을 5분 안에** 제시하기 위한 참조 자산이다. 논문 요약집도, 뉴스 아카이브도 아니다.

!!! info "비공식 자료 (Unofficial)"
    이 사이트는 개인이 운영하는 참조 자산으로, **AWS(Amazon Web Services)의 공식 문서·공식 입장이 아니다.** 서비스 사양·가격·리전 지원은 반드시 [AWS 공식 문서](https://docs.aws.amazon.com/)에서 재확인할 것. 타사 제품·기술에 대한 성숙도 판정은 각 항목의 출처 등급에 근거한 운영자 개인의 평가다.

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
| 1 | **데이터 수집 & 처리** | 로봇 학습의 병목은 모델이 아니라 데이터다 — 텔레옵[^teleop]·오픈 데이터셋·합성 데이터를 AWS 파이프라인으로 처리하는 법 | [pillar-1](pillar-1.md) |
| 2 | **모델 학습 (VLA)** | VLA[^vla]/로봇 파운데이션 모델을 어느 규모의 GPU로, 파인튜닝[^ft]인지 사전학습[^pretrain]인지부터 갈라서 설계하는 법 | [pillar-2](pillar-2.md) |
| 3 | **시뮬레이션** | Isaac Sim/Lab vs 오픈소스 선택과 AWS 위에서의 대규모 병렬 시뮬레이션 실행 패턴 | [pillar-3](pillar-3.md) |
| 4 | **Sim-to-Real** | 시뮬레이션에서 학습한 정책을 실기체로 옮기는 검증된 방법론과 엣지 추론 배포 경로 | [pillar-4](pillar-4.md) |
| 5 | **에이전트 오케스트레이션** | LLM 플래너(System 2[^sys])가 로봇 컨트롤러(System 1)와 플릿[^fleet]을 지휘하는 계층 — Bedrock AgentCore 중심 | [pillar-5](pillar-5.md) |

> 필러 간 비중은 균등. 각 필러 내부는 **고객 실제 수요 × production-readiness** 순으로 정렬되어 있고, 상단에 "이 필러에서 고객이 가장 자주 묻는 질문 Top 3"가 있다.

---

## 자주 묻는 질문 Top 20

<!-- 1~10: 초기 시드(마스터 프롬프트 예시 + IA 구조). 11~20: 공개 커뮤니티/블로그 심화 조사(2026-07). ⚠️ 둘 다 SA 실제 문의 로그가 아니므로, Slack 문의 이력 확보 시 빈도순 재정렬할 것. -->

| # | 질문 | 어디로 | 출처 |
|---|---|---|---|
| 1 | "Isaac Sim / Isaac Lab을 AWS에서 어떻게 돌리나요?" | [pillar-3](pillar-3.md) | 시드 ⚠️ |
| 2 | "VLA 모델 학습(파인튜닝) 인프라는 어떻게 잡아야 하나요?" | [pillar-2](pillar-2.md) | 시드 ⚠️ |
| 3 | "GPU를 못 구합니다 — On-Demand, Capacity Blocks, 대안 중 뭘 써야 하나요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 4 | "sim-to-real[^s2r] gap은 실제로 어떻게 극복하나요? 검증된 방법이 있나요?" | [pillar-4](pillar-4.md) | 시드 ⚠️ |
| 5 | "로봇 실시간 제어(30–100Hz)인데 추론을 클라우드에 둘 수 있나요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 6 | "파운데이션 모델(GR00T/π0 등)을 파인튜닝할까요, 자체 학습할까요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 7 | "로봇 학습 데이터를 어떻게 모으고 어디에 쌓아야 하나요? (텔레옵/합성 데이터)" | [pillar-1](pillar-1.md) | 시드 ⚠️ |
| 8 | "NVIDIA 풀스택에 얼마나 종속되나요? 오픈소스 대안은요?" | [decisions](decisions.md) | 시드 ⚠️ |
| 9 | "엣지 배포(Jetson 등)와 AWS를 어떻게 연결하나요?" | [pillar-4](pillar-4.md) | 시드 ⚠️ |
| 10 | "LLM 에이전트[^agent]로 로봇/설비를 지휘하는 아키텍처가 실제로 되나요?" | [pillar-5](pillar-5.md) | 시드 ⚠️ |
| 11 | "이거 다 돌리면 GPU 비용이 얼마나 들죠? 예산은 어떻게 잡나요?" | [decisions](decisions.md) | [AWS Embodied AI 블로그](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "기존 ROS 2[^ros] 스택·rosbag[^rosbag] 데이터를 AWS와 어떻게 연결하죠?" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac 블로그](https://aws.amazon.com/blogs/robotics/) |
| 13 | "여러 노드로 학습을 확장하려면? AWS Batch vs SageMaker HyperPod?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "실배포 전에 정책이 실제로 되는지 어떻게 검증·벤치마크하죠?" | [pillar-4](pillar-4.md) | [NVIDIA 정책 평가](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "로봇/공장 데이터가 민감한데 클라우드 학습이 규제상 괜찮나요? 온프렘·하이브리드는?" | [decisions](decisions.md) | [AWS AI 주권](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "학습한 정책을 어떻게 버전 관리·재현하고 체크포인트를 복구하죠?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Isaac Sim·오픈 모델을 상용 제품에 써도 되나요? NVIDIA AI Enterprise는 언제 필요?" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "정책 추론을 실시간(저지연)으로 최적화하려면? TensorRT·양자화[^quant]·action chunking[^chunk]?" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "설비/공장 디지털 트윈[^dtwin]을 만들어 로봇 시뮬레이션과 연결하려면? TwinMaker·Omniverse?" | [pillar-3](pillar-3.md) | [AWS Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "ML 전문가가 없는데 어디서부터 시작하죠? 최소 PoC 설계는?" | [decisions](decisions.md) | [AWS Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/) |

---

## 페이지 목록

- [guide — 이 플레이북이 만들어지고 관리되는 방식 (검증 파이프라인 전과정)](guide.md)
- [경영진 브리핑 — 임원용 5분 판단 프레임 (지금/곧/아직 매트릭스)](exec.md)
- [임원 대화 가이드 — SA용 임원 미팅 준비 (피치·Top 10 Q&A·금지 표현)](exec-guide.md)
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
- **개념 설명으로 끝나는 항목**: 모든 항목은 "➡️ 다음 액션"으로 끝난다. 액션이 없으면 미완성이다.

---

_owner: Youngjin · updated: 2026-07 · volatility: 낮음 (구조 페이지 — FAQ Top 20 순위만 분기별 재검토)_

<!-- 용어 각주 -->

[^teleop]: **텔레오퍼레이션(텔레옵)** — 사람이 VR 컨트롤러·리더암 등으로 로봇을 원격 조종하며 시범 동작을 기록하는 데이터 수집 방식. 품질이 가장 높지만 사람의 시간이 그대로 비용이 된다. 🎥 [Stanford Mobile ALOHA 텔레옵 시연](https://www.youtube.com/watch?v=mnLVbwxSdNM)
[^vla]: **VLA (Vision-Language-Action)** — 카메라 영상(Vision)과 자연어 지시(Language)를 입력받아 로봇의 동작(Action)을 직접 출력하는 파운데이션 모델. "컵을 집어"라고 말하면 관절 움직임을 생성하는 식. 🎥 [NVIDIA Isaac GR00T N1 소개](https://www.youtube.com/watch?v=m1CH-mgpdYg)
[^ft]: **파인튜닝(fine-tuning)** — 대규모 데이터로 사전학습된 모델을 자기 태스크·로봇의 소량 데이터로 추가 학습시키는 것. 밑바닥부터 학습하는 것보다 데이터·GPU가 수십~수백 배 절약된다.
[^pretrain]: **사전학습(pre-training)** — 대규모 범용 데이터로 모델을 밑바닥부터 학습시켜 기초 능력을 만드는 단계. 이후 소량 데이터 파인튜닝으로 특정 태스크에 맞춘다. 프런티어 VLA 사전학습은 극소수 조직의 영역이다.
[^sys]: **System 2 / System 1** — 인지과학의 "느린 사고 / 빠른 반응" 구분을 로봇 아키텍처에 적용한 구조. System 2는 느린 대형 모델이 계획을(5~10Hz), System 1은 작은 정책이 실시간 제어를(50~200Hz) 맡는다. 추론을 클라우드에 둘지 엣지에 둘지를 가르는 기준이 된다.
[^fleet]: **플릿(fleet) 조율** — 다수의 로봇 무리를 하나의 시스템으로 스케줄링·경로 배분하는 것. 창고 로봇처럼 수백~수천 대 규모에서 이미 프로덕션 검증된 영역이다.
[^s2r]: **sim-to-real** — 시뮬레이션에서 학습한 정책을 실제 로봇으로 옮기는 것, 또는 그 방법론. 시뮬레이션과 현실의 물리·시각 차이(도메인 갭) 때문에 그냥 옮기면 성능이 무너진다. 🎥 [NVIDIA sim-to-real 로보틱스 쇼케이스](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM 에이전트** — 대형 언어 모델이 스스로 계획을 세우고 툴(API·로봇 스킬)을 골라 호출하며 다단계 작업을 수행하는 소프트웨어. 단순 질의응답과 달리 "행동"이 있다는 점이 핵심이다.
[^ros]: **ROS 2 (Robot Operating System 2)** — 로봇 소프트웨어의 사실상 표준 오픈소스 미들웨어. 센서·제어 노드들이 토픽(topic)으로 통신하는 분산 구조로, 산업·연구 로봇 스택의 공용 기반이다.
[^rosbag]: **ROS bag(rosbag2)** — 로봇 운영체제 ROS 2가 토픽(센서·명령 스트림)을 통째로 녹화하는 표준 로그 포맷. 로봇 회사 원천 데이터의 사실상 기본 형태지만, 그대로는 학습에 쓸 수 없어 변환이 필요하다.
[^quant]: **양자화(quantization)** — 모델 가중치·연산을 FP16→INT8/FP4처럼 낮은 정밀도로 변환해 메모리와 연산량을 줄이는 경량화 기법. 엣지 디바이스에서 지연 예산을 맞추는 핵심 수단이며, 정확도 손실과의 트레이드오프를 관리한다.
[^chunk]: **action chunking** — 매 스텝 동작 1개가 아니라 앞으로의 동작 여러 스텝(청크)을 한 번에 예측하는 기법. 추론 횟수를 줄여 실시간 제어 주파수를 맞추기 쉽게 한다.
[^dtwin]: **디지털 트윈(digital twin)** — 실제 공장·창고·로봇을 물리적으로 충실하게 본뜬 가상 복제본. 실환경을 건드리지 않고 정책 학습·검증·시나리오 실험을 할 수 있게 한다.
