# Physical AI Playbook

_최종 갱신: 2026-09 · owner: Youngjin · volatility: 중간_

**L0 TL;DR**: 고객의 로봇 업무에 필요한 기술을 판단하고, AWS에서 실험·평가·운영으로 이어가기 위한 안내서다. 업무 적합성·총비용·실행 조건을 먼저 확인한다.

!!! info "비공식 자료"
    개인이 운영하는 참조 자산으로 AWS 공식 문서·공식 입장이 아니다. 기술·라이선스·가격·리전은 연결된 1차 출처와 확인일을 검토한다. 샘플 코드와 서비스 GA가 고객 현장 성과를 보증하지 않는다.

## 역할별로 시작

| 나는… | 읽을 경로 | 남길 결과 |
|---|---|---|
| 고객 의사결정자 | [시작·ROI](start.md) → [경영진 브리핑](exec.md) | 업무·대안·예산·파일럿 승인 조건 |
| 고객 기술팀 | [실행 경로](execution.md) → 해당 필러 → [운영·복구](operations.md) | 실험 결과·비용·배포 및 복구 증거 |
| AWS 직원 | [대화 가이드](exec-guide.md) → [의사결정](decisions.md) | 발견 질문·적합성 판단·파트너 인계 |

## 기술 참조 — 5개 필러

| 필러 | 확인할 내용 |
|---|---|
| [P1 데이터](pillar-1.md) | 수집·권리·포맷·품질·학습 파이프라인 |
| [P2 모델 학습](pillar-2.md) | 모델 선택·라이선스·자원 산정·평가 |
| [P3 시뮬레이션](pillar-3.md) | 환경·도구·병렬 실행·비용 |
| [P4 Sim-to-Real](pillar-4.md) | 실기 적용·엣지 배포·검증·안전 |
| [P5 오케스트레이션](pillar-5.md) | 업무 계획·로봇 스킬·권한·플릿 연결 |

## 라벨과 확인 범위

GA/Preview/Research는 **출시 상태**다. 원문 대조·실험 재현·현장 검증, 권장 용도, 지원 주체는 별도로 확인한다. `[1]` 공식 문서·논문 / `[2]` 기록된 재현 / `[3]` 벤더 발표 / `[4]` 미검증은 출처 유형이며 AWS 공식 승인을 뜻하지 않는다. [근거 기록](evidence.md)과 [유지보수 규칙](maintenance.md)을 참조한다.

아래 질문은 탐색용 예시이며 실제 문의 빈도 순위가 아니다. 급하면 질문에서 시작하되, 제안 전 [파일럿 카드](start.md#pilot)의 조건을 확인한다.

## 자주 묻는 질문 Top 20

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
| 11 | "이거 다 돌리면 GPU 비용이 얼마나 들죠? 예산은 어떻게 잡나요?" | [start](start.md) | [AWS Embodied AI 블로그](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/) |
| 12 | "기존 ROS 2[^ros] 스택·rosbag[^rosbag] 데이터를 AWS와 어떻게 연결하죠?" | [pillar-1](pillar-1.md) | [AWS ROS 2 on Isaac 블로그](https://aws.amazon.com/blogs/robotics/) |
| 13 | "여러 노드로 학습을 확장하려면? AWS Batch vs SageMaker HyperPod?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 14 | "실배포 전에 정책이 실제로 되는지 어떻게 검증·벤치마크하죠?" | [pillar-4](pillar-4.md) | [NVIDIA 정책 평가](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/) |
| 15 | "로봇/공장 데이터가 민감한데 클라우드 학습이 규제상 괜찮나요? 온프렘·하이브리드는?" | [decisions](decisions.md) | [AWS AI 주권](https://aws.amazon.com/blogs/security/enabling-ai-sovereignty-on-aws/) |
| 16 | "학습한 정책을 어떻게 버전 관리·재현하고 체크포인트를 복구하죠?" | [pillar-2](pillar-2.md) | [Isaac Lab on SageMaker](https://aws.amazon.com/blogs/machine-learning/scale-robot-reinforcement-learning-with-nvidia-isaac-lab-on-amazon-sagemaker-ai/) |
| 17 | "Isaac Sim·오픈 모델을 상용 제품에 써도 되나요? NVIDIA AI Enterprise는 언제 필요?" | [pillar-3](pillar-3.md) | [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) |
| 18 | "정책 추론을 실시간(저지연)으로 최적화하려면? TensorRT·양자화[^quant]·action chunking[^chunk]?" | [pillar-4](pillar-4.md) | [NVIDIA Jetson Edge AI](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/) |
| 19 | "설비/공장 디지털 트윈[^dtwin]을 만들어 로봇 시뮬레이션과 연결하려면? TwinMaker·Omniverse?" | [pillar-3](pillar-3.md) | [AWS Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/) |
| 20 | "ML 전문가가 없는데 어디서부터 시작하죠? 최소 PoC 설계는?" | [start](start.md) | [AWS Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/) |

---

## 페이지 목록

- [시작·ROI](start.md)
- [실행 경로](execution.md)
- [운영·복구](operations.md)
- [사용 가이드](guide.md)
- [새 소식 — 최근 공식 글과 기존 필러 연결](news.md)
- [워크숍·자료 — 공개 워크숍·구현 가이드·샘플 모음](workshops.md)
- [경영진 브리핑](exec.md)
- [AWS 직원 대화 가이드](exec-guide.md)
- [P1 데이터](pillar-1.md)
- [P2 모델 학습](pillar-2.md)
- [P3 시뮬레이션](pillar-3.md)
- [P4 Sim-to-Real](pillar-4.md)
- [P5 오케스트레이션](pillar-5.md)
- [의사결정](decisions.md)
- [Radar](radar.md)
- [근거 기록](evidence.md)
- [유지보수](maintenance.md)
- [설정 · MCP 연결](mcp.md)

_owner: Youngjin · updated: 2026-09 · volatility: 중간_

<!-- 용어 각주 -->

[^s2r]: **sim-to-real** — 시뮬레이션에서 학습한 정책을 실제 로봇으로 옮기는 것, 또는 그 방법론. 시뮬레이션과 현실의 물리·시각 차이(도메인 갭) 때문에 그냥 옮기면 성능이 무너진다. 🎥 [NVIDIA sim-to-real 로보틱스 쇼케이스](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^agent]: **LLM 에이전트** — 대형 언어 모델이 스스로 계획을 세우고 툴(API·로봇 스킬)을 골라 호출하며 다단계 작업을 수행하는 소프트웨어. 단순 질의응답과 달리 "행동"이 있다는 점이 핵심이다.
[^ros]: **ROS 2 (Robot Operating System 2)** — 로봇 소프트웨어의 사실상 표준 오픈소스 미들웨어. 센서·제어 노드들이 토픽(topic)으로 통신하는 분산 구조로, 산업·연구 로봇 스택의 공용 기반이다.
[^rosbag]: **ROS bag(rosbag2)** — 로봇 운영체제 ROS 2가 토픽(센서·명령 스트림)을 통째로 녹화하는 표준 로그 포맷. 로봇 회사 원천 데이터의 사실상 기본 형태지만, 그대로는 학습에 쓸 수 없어 변환이 필요하다.
[^quant]: **양자화(quantization)** — 모델 가중치·연산을 FP16→INT8/FP4처럼 낮은 정밀도로 변환해 메모리와 연산량을 줄이는 경량화 기법. 엣지 디바이스에서 지연 예산을 맞추는 핵심 수단이며, 정확도 손실과의 트레이드오프를 관리한다.
[^chunk]: **action chunking** — 한 추론에서 미래 동작 여러 개를 생성하는 기법. 동작 실행 빈도와 새 관측에 반응하는 빈도는 다르며, 모델별 실행 구간·전환·지연을 검증해야 한다.
[^dtwin]: **디지털 트윈(digital twin)** — 실제 공장·창고·로봇을 물리적으로 충실하게 본뜬 가상 복제본. 실환경을 건드리지 않고 정책 학습·검증·시나리오 실험을 할 수 있게 한다.
