# Radar — 대기열 / 관찰 목록

_최종 갱신: 2026-07 · owner: Youngjin · volatility: 높음_
[← index로](index.md)

> **L0 TL;DR**: 포함 기준([2.5 THE FILTER](maintenance.md#포함-기준-the-filter))을 아직 통과 못했지만 **지켜볼 것들**. 각 항목은 한 줄 — 성숙도 라벨 + **왜 대기 중인지**. 게이트(4개 중 2개)를 통과하면 담당 필러 owner가 표준 템플릿으로 승격한다.
>
> ⚠️ **여기 있는 항목을 고객 제안에 "성숙한 역량"처럼 쓰지 말 것.** 화려한 데모가 배포 가능성을 가리는 경우가 많다.

---

## 🔬 모델 / 알고리즘 (검증 대기)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| Physical Intelligence **[π0.7](https://www.physicalintelligence.company/)** | 🔵 Research | 2차 출처만 `[4]`, PI 1차 확인 없음 | PI 공식 릴리스 + 성능 검증 |
| **[GR00T N1.6 / N1.7](https://github.com/NVIDIA/Isaac-GR00T) 상업 라이선스** | 🟡→ | 상업 허용 주장이 2차 출처뿐 `[4]` (N1.5는 모델카드상 명백 비상업 `[1]`) | 라이브 모델 카드에서 라이선스 확정 |
| **[World-action models](https://developer.nvidia.com/isaac/gr00t)** (DreamZero → GR00T N2) | 🟡 Preview | GR00T N2 "연말 예정", DreamZero는 연구 | GA + 실배포 사례 |
| Google DeepMind **[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)** (로봇 학습용 월드모델[^wfm]) | 🟡 Preview | 월드모델 자체는 프리뷰, 로봇 학습 적용은 연구 | 로봇 정책 학습 검증 사례 |
| **VLM 기반 SysID[^sysid]** ([Vid2Sid](https://arxiv.org/abs/2602.19359), [Swim2Real](https://arxiv.org/abs/2603.20827)) | 🔵 Research | 2026 프리프린트, 단일 랩 | peer-review + 재현 |
| **VIRAL / [VideoMimic](https://www.videomimic.net/) / [Real2Render2Real](https://real2render2real.com/)** (visual sim-to-real[^s2r] at scale) | 🔵 Research | CVPR/CoRL 연구, 프로덕션 아님 | 프로덕션 배포 증거 |
| **Robbyant [LingBot-VLA](https://huggingface.co/robbyant) / [UnifoLM-VLA-0](https://huggingface.co/unitreerobotics)** | 🔵 Research | 2차 출처, 검증 없음 | 1차 확인 + AWS 매핑 |

## 🖥️ 시뮬레이션 / 도구 (성숙도 대기)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** 물리엔진[^physeng] | ⚪ Hype | "430,000배" 반박됨 `[1]`, 접촉 조작서 느림 | 독립 벤치 + 프로덕션 채택 |
| **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** | 🟡 Alpha | PyPI classifier "3-Alpha" `[1]`, 프로덕션 아님 | Beta/GA 전환 |
| **[NVIDIA Newton](https://github.com/newton-physics/newton)** 물리엔진 | 🟡 Preview | Isaac Sim 6.0서 experimental 백엔드 | GA + Isaac Lab 3.0 정식 |
| **[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)** | 🟡 Preview | "Early Developer Release", API 변동 (최신 GA는 5.1) | 6.x GA 선언 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) as sim-to-real 학습원** | 🟢 GA(모델)/🔵(실전) | 모델 GA지만 "월드모델 데이터로 실배포 정책 학습"은 얼리어답터만. ⚠️ **AWS 미호스팅** | AWS 매핑 강화 + 학습 검증 |

## 🤖 하드웨어 / 배포 (로드맵·데모)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | Musk 주장뿐, 생산 미시작 | 검증된 배포 |
| **Hyundai·BD 전기식 [Atlas](https://bostondynamics.com/atlas/)** | ⚪ 로드맵 | 전기식 Atlas 제품 버전 공개(2026-07, BD 공식 `[3]`). 배포 2.5만+대·양산능력 3만/년 모두 **2028 시작**, 현재 실가동 ~0. 2026은 소규모 파일럿만(현대 RMAC + Google DeepMind). ⚠️ "5세대"는 오칭 | 실가동 출하 시작 |
| **[Apptronik Apollo 2 + Robot Park](https://apptronik.com/)** | 🟡 파일럿 | Mercedes-Benz·GXO 운영 파일럿 `[3]` + Google DeepMind Gemini Robotics 데이터 파트너십(9만 sqft). 자율·상용 확산 미검증. AWS 매핑은 일반적(데이터→S3/SageMaker), 파트너십 자체는 Google `[4]` | 상용 배포 규모 + 자율 성과 검증 |
| **[1X Neo](https://www.1x.tech/neo)** 자율성 | 🟡 Preview | 자율+VR 원격조작(Expert Mode) 혼합 운용 — CEO 직접 인정 ([Engadget](https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html) `[3]`). "자율 60~70%" 수치는 1차 출처 없음 `[4]` | 진짜 자율 검증 |
| **[Figure 03](https://www.figure.ai/) "8시간 자율 시프트"** | ⚪ Hype | CEO 트윗, 독립 검증 없음 (Figure 02@BMW는 검증 파일럿) | 3자 자율성 감사 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 채택** (Doosan/LG/Samsung) | 🟢 GA(발표) | 채택 "발표"지 프로덕션 검증 아님 | 프로덕션 사례 공개 |

## 🔗 에이전트 / 연결 (초기)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| **MCP[^mcp] for robotics** ([ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 등) | 🔵 Research | 50+ 서버 있으나 오픈소스/데모, 프로덕션 없음 (안전·지연·결정성 미검증) | 프로덕션 하드닝 사례 |
| **ROS 2[^ros] + LLM 에이전트[^agent]** (NASA JPL [ROSA](https://github.com/nasa-jpl/rosa), [RAI](https://github.com/RobotecAI/rai)) | 🔵 Research | ROSA(JPL)가 최강 실사례지만 mock-ops. 현장 배포 제한적 | 현장 프로덕션 배포 |
| **에이전트 물리안전 표준** ([RoboGuard](https://arxiv.org/abs/2503.07885) 등) | 🔵 Research | ISO는 물리만, LLM 의미 위험 표준 부재 | 표준화 진전 |
| **[AgentCore Payments / Agent Registry](https://aws.amazon.com/bedrock/agentcore/) (서울)** | 🟡 Preview/미제공 | 서울 리전 미제공 (도쿄 Agent Registry ✅) | 서울 리전 확장 |

## 🆕 최신 스캔 유입 (2026-08-08 · 1차 검증 완료 2026-07-21)

<!-- 자동 스캔(arXiv/웹) 유입분. 2026-07-21 1차 출처 검증 완료(검증 에이전트 4식, 공식 발표·arXiv 원문 대조) — 승격 0건, 정정 6건. THE FILTER 통과 전까지 고객 제안 사용 금지. 정기 갱신은 scripts/radar_scan.md 참고. -->

| 항목 | 라벨 | 왜 주목받는가 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|---|
| **[RLWRLD RLDX-1](https://huggingface.co/RLWRLD)** (손 dexterity[^dex] 파운데이션 모델) | 🟡 Preview | 한국 스타트업의 손 조작 특화 파운데이션 모델 — 3대 시뮬 벤치 SOTA 주장에 가중치 실공개까지 겹쳐 직접 실측이 가능 | 가중치 공개는 사실이나 ⚠️ "오픈소스" 아님 — RLWRLD Model License v1.0(비상업·상업 배포 금지) `[3]`, 7~9B 변형군(주력 8.1B). RoboCasa/LIBERO/SIMPLER[^simbench] SOTA는 자체 발표, 독립 재현 없음([aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws)가 EC2에서 n=5 스모크[^smoke] 실측 제공 — 완전한 벤치 재현은 아님). AWS 연계는 시뮬 벤치마킹 한정(비상업 라이선스가 명시 허용하는 용도, 상업 포지셔닝 불가) — "연계 근거 없음" 표기 갱신(2026-07). 실고객 배포 0 | 독립 벤치마크 재현 + 실배포 사례 |
| **[NEURA Robotics × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale) 전략적 협력** | ⚪ Hype·로드맵 | 휴머노이드 제조사가 AWS를 primary cloud로 명시한 드문 공식 협력 — "Physical AI on AWS" 고객 대화의 직접 레퍼런스 후보 | 2026-04-21 AWS 공식 프레스 확인 `[1]` — AWS가 primary cloud, Neuraverse 호스팅 + NEURA Gym·SageMaker 연동 명시. 단 풀필먼트센터는 원문상 "배포 기회 탐색(explore)" 단계 — 실배포 0. NEURA Gym RWTH Aachen 등 훈련망 확장(2026-07-22) 발표에는 AWS 언급 없음 — 별개 트랙으로 관찰 | 실제 AWS 인프라 사용 사례 공개 + 풀필먼트 배포 검증 |
| **[Actuator Reality Shaping](https://arxiv.org/abs/2607.02205)** (zero-shot sim-to-real) | 🔵 Research | 액추에이터 갭 보정만으로 zero-shot sim-to-real을 실물 4종에서 입증 — 실기 파인튜닝 비용을 건너뛸 수 있는 접근 | 실존 확인(arXiv 2607.02205, 2026-07-02) `[1]` — 실물 하드웨어 4종(휴머노이드 보행 포함) 검증, 요약·초록 일치(정정 없음). peer-review 미채택 | peer-review + 독립 재현 |
| **[AgiBot World 2026](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)** (오픈소스 실세계 로봇 매니퓰레이션 데이터셋, 5단계 순차 공개) | 🔵 Research | 상업·서비스 환경에서 수집한 100% 실세계 매니퓰레이션 데이터를 무상 공개 — 업계 최대 병목인 실데이터 부족을 정면 겨냥 | AgiBot 공식 공개(HuggingFace `agibot-world/AgiBotWorld2026`, 2026-07) `[4]` — AgiBot G2 실기로 수집한 100% 실세계 데이터, 5개 연구축(모방학습 등) 순차 공개 예정, 1차분은 상업·서비스 환경 수백 시간. 라이선스·상업적 이용 조건 미확인, 독립 벤치마크·학습 검증 사례 없음 | 라이선스 확정 + 독립 학습 검증(SOTA 재현) 사례 |
| **[AXIS](https://arxiv.org/abs/2607.21588)** (커뮤니티 기반 성장형 로봇 매니퓰레이션 데이터 엔진) | 🔵 Research | 브라우저 텔레옵 크라우드소싱으로 시연 데이터 수집의 비용 구조를 바꾸는 시도 — π0.5 성능 향상(+4.9%p)으로 효용을 실증 | 실존 확인(arXiv 2607.21588, 2026-07-23) `[4]` — 8개 대학 + Axis Robotics 공동, 브라우저 MuJoCo-WASM[^wasm] 텔레옵[^teleop]으로 크라우드소싱 후 IsaacSim 증강. Franka 시뮬레이션 전용(207 태스크·5만+ 궤적), π0.5 continual pretraining[^ctp]으로 LIBERO-Plus +4.9%p 보고(자체 벤치, 독립 재현 없음). sim-to-real은 저자 스스로 "향후 과제"로 명시 — 실기 미검증 | peer-review + 실기 sim-to-real 검증 |
| **[NVIDIA Cosmos 3 Edge](https://www.nvidia.com/en-us/ai/cosmos/)** (Cosmos 3 계열 온디바이스 4B 월드모델+정책) | 🟡 Preview | 월드모델+정책을 Jetson Thor 온디바이스 15Hz로 구동 — 클라우드 왕복 없는 엣지 추론 축의 선두 사례 | NVIDIA 공식 발표 `[4]`(2026-07-21, HuggingFace/developer 블로그) — Jetson Thor 온디바이스 추론으로 15Hz 실시간 로봇 정책 제어(자체 벤치, 독립 검증 없음), Cosmos 3 Edge Policy(DROID[^droid])로 pick-and-place 파인튜닝 지원. 기존 "Cosmos 3 as sim-to-real 학습원"(🖥️ 섹션)과 별개로 엣지 배포 축만 다룸, AMD Ryzen AI Embedded X100(본 표)과 경쟁 구도 병행 관찰. 실제 프로덕션 로봇 배포 사례 0 | 독립 벤치마크 + 실제 로봇 프로덕션 배포 사례 |
| **[Walden Robotics](https://www.waldenrobotics.com/news/walden-robotics-launches-from-stealth)** (Toyota Research Institute 스핀아웃, Large Behavior Models[^lbm] 휴머노이드) | 🟡 파일럿 | TRI 로보틱스를 이끈 Russ Tedrake의 스핀아웃 + 시드 3억 달러 — LBM 상용화 최전선, Toyota 공장 실파일럿 보유 | 회사 공식 발표(2026-07-15) `[4]` — 2026-01 TRI에서 스핀아웃(창업자 Russ Tedrake, 전 TRI SVP), Toyota·Deviation Capital 공동 리드 + NVIDIA·Boeing·Samsung Ventures 등 참여 시드 3억 달러(밸류 11억 달러). 휴머노이드 상반신+이동형 베이스, Diffusion Policy[^diffpol]·Large Behavior Models 기반 정책으로 노스아메리카 Toyota 공장에서 2026-02부터 파일럿→"프로덕션 전환" 자체 주장, 3자 검증 없음 | 3자 감사·독립 검증 + 배포 규모 확대 사례 |
| **[Generalist AI GEN-1](https://generalistai.com/blog/gen-1)** (범용 end-effector[^eef] 대응 embodied foundation model) | 🟡 Preview | 약 9,000종 end-effector를 단일 모델로 커버 + 실측 50만 시간 사전학습 — embodiment 범용성에서 전례 없는 스케일 주장 | Generalist AI 공식 블로그 발표(2026-07) `[4]` — 5-finger 핸드~특수 툴 약 9,000종 end-effector, 실측 데이터 50만+시간 사전학습, 자체 벤치 성공률 99%·속도 3배 주장(독립 재현 없음). Generalist AI는 [pillar-1](pillar-1.md)에 Cosmos WFM 데이터 생성 활용사로 이미 언급되어 있으나 GEN-1 모델 자체는 별개 신규 사안 | 독립 벤치마크 재현 + 실배포 사례 |
| **[Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)** (VLA[^vla] 파운데이션 모델, UMI[^umi] 10만+시간 실세계 궤적) | 🔵 Research | UMI 10만+시간 실세계 궤적이라는 데이터 스케일로 4개 벤치 SOTA 주장 — 중국 빅테크의 VLA 경쟁 본격 진입 신호 | Xiaomi 공식 arXiv 발표(2607.15330, 2026-07-16) `[4]` — Qwen3-VL 기반 MoT(VLM+DiT), RoboCasa365(57.4%, 기존 SOTA 46.6%↑)·RoboDojo(20.07, 기존 13.07↑)·VLABench·RoboCasa 4개 벤치마크 SOTA 자체 주장(RLDX-1·GR00T N1.6 포함 비교, 독립 재현 없음). "코드·가중치 공개 예정"이나 GitHub 리포지토리는 README뿐, 실공개 미확인(2026-08-01 기준) | 코드·가중치 실공개 확인 + 독립 벤치마크 재현 |
| **[Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)** (Google DeepMind, 전신 제어 VLA) | 🟡 Preview | 프론티어 랩 VLA가 상체 조작을 넘어 전신(보행·양손 협응) 제어로 확장 — 경쟁 스택 지형을 바꾸는 세대 전환 신호 | 공식 발표(2026-07-30) `[4]` — 기존 상체 전용 제어에서 전신(보행·굽힘·양손 협응) 제어로 확장, 추론 모델 Gemini Robotics ER 2·엣지 모델 On-Device 2 동반 출시. Apptronik Apollo 2 실기 데모(전구 분리 92% 성공)로 시연, 자체 벤치·독립 검증 없음. ER 2만 AI Studio/Enterprise Agent Platform 프리뷰 공개, VLA·On-Device 2는 얼리액세스 파트너 한정. ⚠️ [pillar-2](pillar-2.md) "Gemini Robotics" 경쟁 스택 절은 이 발표 이전(2026-07 확인, ER 1.6/On-Device/1.5 기준) 스냅샷 — pillar owner 갱신 필요 | 얼리액세스 종료·GA 공개 + 독립 벤치마크 검증 |

## ⚰️ 폐기됨 — 제안 금지 (기록 보존용)

| 항목 | 상태 | 대체 |
|---|---|---|
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 종료 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 종료 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 종료 (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 공개 사례 없음 `[4]` | 현재 CUDA/NVIDIA (제안 시 리스크 명시) |

> ⚠️ **루머 주의(사실 아님)**: "AWS IoT TwinMaker 폐기" 는 **오정보** — TwinMaker는 GA·신규 오픈(저속도). SiteWise 유지보수와 혼동한 3rd-party 블로그 주장. 반복 금지. → [pillar-3](pillar-3.md).

---

## 승격 절차 (요약)

1. **캡처**: 지정 채널/이모지로 후보 수집
2. **필터**: [2.5 게이트](maintenance.md#포함-기준-the-filter) 적용 (4개 중 2개 이상)
3. **통과 시**: 담당 필러 owner가 [표준 템플릿](maintenance.md#표준-템플릿)으로 편입, Radar에서 제거
4. **미달 시**: 여기 한 줄로 유지, 승격 조건 명시

전체 파이프라인 → [maintenance](maintenance.md#playbook-승격-파이프라인).

---
_owner: Youngjin · updated: 2026-07 · volatility: 높음 (Radar는 본질적으로 빠르게 변함 — 월 단위 검토 권장)_

<!-- 용어 각주 -->

[^wfm]: **월드 파운데이션 모델(WFM, World Foundation Model)** — 물리 세계의 다음 장면을 예측·생성하도록 학습된 대형 모델. 텍스트·영상 프롬프트로 물리적으로 그럴듯한 영상·시나리오를 만들어 로봇 학습 데이터를 증강한다. 🎥 [NVIDIA Cosmos 소개](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **시스템 식별(SysID, System Identification)** — 실물 로봇의 물리 파라미터(마찰·질량·모터 응답)를 측정해 시뮬레이터를 실물에 맞게 보정하는 작업.
[^s2r]: **sim-to-real** — 시뮬레이션에서 학습한 정책을 실제 로봇으로 옮기는 것, 또는 그 방법론. 시뮬레이션과 현실의 물리·시각 차이(도메인 갭) 때문에 그냥 옮기면 성능이 무너진다. 🎥 [NVIDIA sim-to-real 로보틱스 쇼케이스](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **물리 엔진(physics engine)** — 강체 동역학·접촉·마찰·충돌을 수치적으로 계산하는 시뮬레이터의 핵심 소프트웨어. 엔진의 정확도·속도 트레이드오프가 시뮬레이터 선택(Isaac/MuJoCo/Genesis)을 좌우한다.
[^mcp]: **MCP (Model Context Protocol)** — 에이전트와 툴·데이터 소스를 잇는 개방형 표준 프로토콜. "에이전트용 USB-C"에 비유되며, 로봇 스킬을 MCP 서버로 노출하는 실험이 늘고 있다.
[^ros]: **ROS 2 (Robot Operating System 2)** — 로봇 소프트웨어의 사실상 표준 오픈소스 미들웨어. 센서·제어 노드들이 토픽(topic)으로 통신하는 분산 구조로, 산업·연구 로봇 스택의 공용 기반이다.
[^agent]: **LLM 에이전트** — 대형 언어 모델이 스스로 계획을 세우고 툴(API·로봇 스킬)을 골라 호출하며 다단계 작업을 수행하는 소프트웨어. 단순 질의응답과 달리 "행동"이 있다는 점이 핵심이다.
[^vla]: **VLA (Vision-Language-Action)** — 카메라 영상(Vision)과 자연어 지시(Language)를 입력받아 로봇의 동작(Action)을 직접 출력하는 파운데이션 모델. "컵을 집어"라고 말하면 관절 움직임을 생성하는 식. 🎥 [NVIDIA Isaac GR00T N1 소개](https://www.youtube.com/watch?v=m1CH-mgpdYg)
[^dex]: **덱스터리티(dexterity)** — 손가락 수준의 정밀하고 기민한 매니퓰레이션 능력. 접촉 물리가 보행보다 훨씬 복잡해 로봇 학습에서 가장 어려운 축으로 꼽힌다.
[^simbench]: **LIBERO · RoboCasa · SIMPLER** — 실기 없이 VLA·매니퓰레이션 정책의 성능을 비교하는 표준 시뮬레이션 벤치마크 스위트. 시뮬 점수가 실기 성능을 보장하지는 않는다.
[^smoke]: **스모크 테스트(smoke test)** — 완전한 검증이 아니라 "일단 돌아가는지"만 확인하는 소규모 실행. n=5 같은 표본으로는 통계적 성능 주장을 할 수 없다.
[^wasm]: **MuJoCo-WASM** — 물리 엔진 MuJoCo를 WebAssembly로 포팅해 설치 없이 웹 브라우저 안에서 시뮬레이션을 돌리는 기술. 불특정 다수의 원격 시연 수집(크라우드소싱)을 가능하게 한다.
[^teleop]: **텔레오퍼레이션(텔레옵)** — 사람이 VR 컨트롤러·리더암 등으로 로봇을 원격 조종하며 시범 동작을 기록하는 데이터 수집 방식. 품질이 가장 높지만 사람의 시간이 그대로 비용이 된다. 🎥 [Stanford Mobile ALOHA 텔레옵 시연](https://www.youtube.com/watch?v=mnLVbwxSdNM)
[^ctp]: **continual pretraining(계속 사전학습)** — 이미 사전학습된 모델에 새 대규모 데이터로 사전학습을 이어가는 것. 처음부터 다시 학습하지 않고 기존 능력 위에 데이터를 흡수시킨다.
[^droid]: **DROID** — 13개 기관이 Franka 로봇 팔로 수집한 대규모 공개 실세계 매니퓰레이션 데이터셋. 매니퓰레이션 정책의 사전학습·파인튜닝 재료로 널리 쓰인다.
[^lbm]: **Large Behavior Models (LBM)** — LLM의 "로봇 행동" 판. 대규모 시연 데이터로 학습해 여러 매니퓰레이션 태스크를 한 모델로 수행하는 로봇 파운데이션 모델을 가리키는 Toyota Research Institute의 용어.
[^diffpol]: **Diffusion Policy** — 이미지 생성에 쓰이는 확산(diffusion) 모델로 로봇 동작 시퀀스를 생성하는 정책 아키텍처. 여러 갈래의 시연 데이터를 안정적으로 학습해 모방학습의 사실상 표준이 됐다.
[^eef]: **end-effector(엔드이펙터)** — 로봇 팔 끝단에 장착되는 작업 도구(그리퍼·다지 핸드·특수 툴). 어떤 end-effector를 쓰느냐가 데이터·정책의 호환성을 좌우한다.
[^umi]: **UMI (Universal Manipulation Interface)** — 로봇 없이, 사람이 카메라 달린 휴대형 그리퍼를 손에 쥐고 시연 데이터를 모으는 수집 방식. 로봇 투입 없이 실세계 데이터를 대량 확보할 수 있다.
