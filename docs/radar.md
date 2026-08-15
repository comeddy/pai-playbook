# Radar — 대기열 / 관찰 목록

_최종 갱신: 2026-07 · owner: Youngjin · volatility: 높음_
[← index로](index.md)

> **L0 TL;DR**: 포함 기준([2.5 THE FILTER](maintenance.md#포함-기준-the-filter))을 아직 통과 못했지만 **지켜볼 것들**. 각 항목은 한 줄 — 성숙도 라벨 + **왜 주목받는지 + 왜 대기 중인지**. 게이트(4개 중 2개)를 통과하면 담당 필러 owner가 표준 템플릿으로 승격한다.
>
> ⚠️ **여기 있는 항목을 고객 제안에 "성숙한 역량"처럼 쓰지 말 것.** 화려한 데모가 배포 가능성을 가리는 경우가 많다.

---

## 🔬 모델 / 알고리즘 (검증 대기)

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| Physical Intelligence **[π0.7](https://www.physicalintelligence.company/)** | 🔵 Research | ✨ **주목**: π0/π0.5로 VLA 선두권인 PI의 차기 플래그십 루머 — 나오면 업계 기준점을 다시 옮길 수 있음<br>⏳ **대기**: 2차 출처만 `[4]`, PI 1차 확인 없음 | PI 공식 릴리스 + 성능 검증 |
| **[GR00T N1.6 / N1.7](https://github.com/NVIDIA/Isaac-GR00T) 상업 라이선스** | 🟡→ | ✨ **주목**: 상업 허용이 사실이면 고객 제안에 쓸 수 있는 희귀한 오픈 VLA가 됨(N1.5는 비상업이라 제안 불가)<br>⏳ **대기**: 상업 허용 주장이 2차 출처뿐 `[4]` (N1.5는 모델카드상 명백 비상업 `[1]`) | 라이브 모델 카드에서 라이선스 확정 |
| **[World-action models](https://developer.nvidia.com/isaac/gr00t)** (DreamZero → GR00T N2) | 🟡 Preview | ✨ **주목**: VLA 다음 세대로 거론되는 "행동까지 생성하는 월드모델" 축 — NVIDIA 로드맵의 방향 지표<br>⏳ **대기**: GR00T N2 "연말 예정", DreamZero는 연구 | GA + 실배포 사례 |
| Google DeepMind **[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)** (로봇 학습용 월드모델[^wfm]) | 🟡 Preview | ✨ **주목**: 프론티어급 월드모델을 로봇 정책 학습 데이터원으로 쓰려는 시도 — 성사 시 실데이터 병목 우회<br>⏳ **대기**: 월드모델 자체는 프리뷰, 로봇 학습 적용은 연구 | 로봇 정책 학습 검증 사례 |
| **VLM 기반 SysID[^sysid]** ([Vid2Sid](https://arxiv.org/abs/2602.19359), [Swim2Real](https://arxiv.org/abs/2603.20827)) | 🔵 Research | ✨ **주목**: 영상만으로 물리 파라미터를 추정해 시뮬 보정을 자동화 — sim-to-real 수작업 캘리브레이션을 없앨 가능성<br>⏳ **대기**: 2026 프리프린트, 단일 랩 | peer-review + 재현 |
| **VIRAL / [VideoMimic](https://www.videomimic.net/) / [Real2Render2Real](https://real2render2real.com/)** (visual sim-to-real[^s2r] at scale) | 🔵 Research | ✨ **주목**: 일반 영상에서 시뮬 환경·시연을 재구성하는 visual sim-to-real — 데이터 수집 비용 구조를 바꿀 후보<br>⏳ **대기**: CVPR/CoRL 연구, 프로덕션 아님 | 프로덕션 배포 증거 |
| **Robbyant [LingBot-VLA](https://huggingface.co/robbyant) / [UnifoLM-VLA-0](https://huggingface.co/unitreerobotics)** | 🔵 Research | ✨ **주목**: 중국발 신규 오픈 VLA 계열 — 오픈 가중치 경쟁 구도 관찰용<br>⏳ **대기**: 2차 출처, 검증 없음 | 1차 확인 + AWS 매핑 |

## 🖥️ 시뮬레이션 / 도구 (성숙도 대기)

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** 물리엔진[^physeng] | ⚪ Hype | ✨ **주목**: "초고속 범용 물리엔진" 주장으로 화제 — 사실이면 GPU 시뮬 비용 구조가 바뀜<br>⏳ **대기**: "430,000배" 반박됨 `[1]`, 접촉 조작서 느림 | 독립 벤치 + 프로덕션 채택 |
| **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** | 🟡 Alpha | ✨ **주목**: MuJoCo 정확도 + GPU 병렬화 결합 — Isaac 일강 구도의 대안 후보<br>⏳ **대기**: PyPI classifier "3-Alpha" `[1]`, 프로덕션 아님 | Beta/GA 전환 |
| **[NVIDIA Newton](https://github.com/newton-physics/newton)** 물리엔진 | 🟡 Preview | ✨ **주목**: Google DeepMind·Disney Research와 공동 개발하는 차세대 오픈소스 물리엔진 — Isaac 생태계의 차기 표준 유력<br>⏳ **대기**: Isaac Sim 6.0서 experimental 백엔드 | GA + Isaac Lab 3.0 정식 |
| **[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)** | 🟡 Preview | ✨ **주목**: Newton 통합 등 차세대 구조 개편 — 현행 5.x 스택의 마이그레이션 방향 지표<br>⏳ **대기**: "Early Developer Release", API 변동 (최신 GA는 5.1) | 6.x GA 선언 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) as sim-to-real 학습원** | 🟢 GA(모델)/🔵(실전) | ✨ **주목**: 월드모델 생성 데이터로 실배포 정책을 학습하는 축 — 성사 시 SDG 파이프라인 판도 변화<br>⏳ **대기**: 모델 GA지만 "월드모델 데이터로 실배포 정책 학습"은 얼리어답터만. ⚠️ **AWS 미호스팅** | AWS 매핑 강화 + 학습 검증 |

## 🤖 하드웨어 / 배포 (로드맵·데모)

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | ✨ **주목**: 화제성 최대의 휴머노이드 양산 계획 — 고객 질문 빈도가 가장 높은 항목<br>⏳ **대기**: Musk 주장뿐, 생산 미시작 | 검증된 배포 |
| **Hyundai·BD 전기식 [Atlas](https://bostondynamics.com/atlas/)** | ⚪ 로드맵 | ✨ **주목**: 현대차그룹의 양산 로드맵(2028부터 3만 대/년) — 한국 고객 접점에서 가장 직접적인 휴머노이드 트랙<br>⏳ **대기**: 전기식 Atlas 제품 버전 공개(2026-07, BD 공식 `[3]`). 배포 2.5만+대·양산능력 3만/년 모두 **2028 시작**, 현재 실가동 ~0. 2026은 소규모 파일럿만(현대 RMAC + Google DeepMind). ⚠️ "5세대"는 오칭 | 실가동 출하 시작 |
| **[Apptronik Apollo 2 + Robot Park](https://apptronik.com/)** | 🟡 파일럿 | ✨ **주목**: Mercedes·GXO 실운영 파일럿 + Google DeepMind 데이터 파트너십 — 휴머노이드 상용화 최전선 지표<br>⏳ **대기**: Mercedes-Benz·GXO 운영 파일럿 `[3]` + Google DeepMind Gemini Robotics 데이터 파트너십(9만 sqft). 자율·상용 확산 미검증. AWS 매핑은 일반적(데이터→S3/SageMaker), 파트너십 자체는 Google `[4]` | 상용 배포 규모 + 자율 성과 검증 |
| **[1X Neo](https://www.1x.tech/neo)** 자율성 | 🟡 Preview | ✨ **주목**: 가정용 휴머노이드를 실제 판매($20k)하는 첫 사례군 — 원격조작 혼합 운용 모델의 시험대<br>⏳ **대기**: 자율+VR 원격조작(Expert Mode) 혼합 운용 — CEO 직접 인정 ([Engadget](https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html) `[3]`). "자율 60~70%" 수치는 1차 출처 없음 `[4]` | 진짜 자율 검증 |
| **[Figure 03](https://www.figure.ai/) "8시간 자율 시프트"** | ⚪ Hype | ✨ **주목**: 검증된 BMW 파일럿 실적 위의 자율성 주장 — 사실이면 산업 휴머노이드 자율성 기준 갱신<br>⏳ **대기**: CEO 트윗, 독립 검증 없음 (Figure 02@BMW는 검증 파일럿) | 3자 자율성 감사 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 채택** (Doosan/LG/Samsung) | 🟢 GA(발표) | ✨ **주목**: 한국 대기업 3사의 채택 발표 — 한국 고객 대화에서 바로 나오는 레퍼런스<br>⏳ **대기**: 채택 "발표"지 프로덕션 검증 아님 | 프로덕션 사례 공개 |

## 🔗 에이전트 / 연결 (초기)

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| **MCP[^mcp] for robotics** ([ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 등) | 🔵 Research | ✨ **주목**: 에이전트 표준 프로토콜을 로봇 스킬에 잇는 실험 급증(50+ 서버) — AgentCore 연계 각도<br>⏳ **대기**: 50+ 서버 있으나 오픈소스/데모, 프로덕션 없음 (안전·지연·결정성 미검증) | 프로덕션 하드닝 사례 |
| **ROS 2[^ros] + LLM 에이전트[^agent]** (NASA JPL [ROSA](https://github.com/nasa-jpl/rosa), [RAI](https://github.com/RobotecAI/rai)) | 🔵 Research | ✨ **주목**: NASA JPL ROSA 등 실조직 검증 사례 보유 — 자연어→로봇 운영의 가장 현실적인 진입로<br>⏳ **대기**: ROSA(JPL)가 최강 실사례지만 mock-ops. 현장 배포 제한적 | 현장 프로덕션 배포 |
| **에이전트 물리안전 표준** ([RoboGuard](https://arxiv.org/abs/2503.07885) 등) | 🔵 Research | ✨ **주목**: LLM 의미 수준 위험을 다루는 표준 공백 지대 — 규제·조달 요구사항으로 부상 가능<br>⏳ **대기**: ISO는 물리만, LLM 의미 위험 표준 부재 | 표준화 진전 |
| **[AgentCore Payments / Agent Registry](https://aws.amazon.com/bedrock/agentcore/) (서울)** | 🟡 Preview/미제공 | ✨ **주목**: 로봇 에이전트 상거래·등록 인프라의 AWS 네이티브 축 — 서울 리전 오픈 시 즉시 제안 가능<br>⏳ **대기**: 서울 리전 미제공 — Agent Registry는 도쿄 ✅, Payments는 도쿄에도 미제공(APAC은 시드니만) `[1]` | 서울 리전 확장 |

## 🆕 최신 스캔 유입 (2026-08-15 · 1차 검증 완료 2026-07-21)

<!-- 자동 스캔(arXiv/웹) 유입분. 2026-07-21 1차 출처 검증 완료(검증 에이전트 4식, 공식 발표·arXiv 원문 대조) — 승격 0건, 정정 6건. THE FILTER 통과 전까지 고객 제안 사용 금지. 정기 갱신은 scripts/radar_scan.md 참고. -->

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| **[RLWRLD RLDX-1](https://huggingface.co/RLWRLD)** (손 dexterity[^dex] 파운데이션 모델) | 🟡 Preview | ✨ **주목**: 한국 스타트업의 손 조작 특화 파운데이션 모델 — 3대 시뮬 벤치 SOTA 주장에 가중치 실공개까지 겹쳐 직접 실측이 가능<br>⏳ **대기**: 가중치 공개는 사실이나 ⚠️ "오픈소스" 아님 — RLWRLD Model License v1.0(비상업·상업 배포 금지) `[3]`, 7~9B 변형군(주력 8.1B). RoboCasa/LIBERO/SIMPLER[^simbench] SOTA는 자체 발표, 독립 재현 없음([aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws)가 EC2에서 n=5 스모크[^smoke] 실측 제공 — 완전한 벤치 재현은 아님). AWS 연계는 시뮬 벤치마킹 한정(비상업 라이선스가 명시 허용하는 용도, 상업 포지셔닝 불가) — "연계 근거 없음" 표기 갱신(2026-07). 실고객 배포 0 | 독립 벤치마크 재현 + 실배포 사례 |
| **[NEURA Robotics × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale) 전략적 협력** | ⚪ Hype·로드맵 | ✨ **주목**: 휴머노이드 제조사가 AWS를 primary cloud로 명시한 드문 공식 협력 — "Physical AI on AWS" 고객 대화의 직접 레퍼런스 후보<br>⏳ **대기**: 2026-04-21 AWS 공식 프레스 확인 `[1]` — AWS가 primary cloud, Neuraverse 호스팅 + NEURA Gym·SageMaker 연동 명시. 단 풀필먼트센터는 원문상 "배포 기회 탐색(explore)" 단계 — 실배포 0. NEURA Gym RWTH Aachen 등 훈련망 확장(2026-07-22) 발표에는 AWS 언급 없음 — 별개 트랙으로 관찰 | 실제 AWS 인프라 사용 사례 공개 + 풀필먼트 배포 검증 |
| **[NVIDIA Cosmos 3 Edge](https://www.nvidia.com/en-us/ai/cosmos/)** (Cosmos 3 계열 온디바이스 4B 월드모델+정책) | 🟡 Preview | ✨ **주목**: 월드모델+정책을 Jetson Thor 온디바이스 15Hz로 구동 — 클라우드 왕복 없는 엣지 추론 축의 선두 사례<br>⏳ **대기**: NVIDIA 공식 발표 `[4]`(2026-07-21, HuggingFace/developer 블로그) — Jetson Thor 온디바이스 추론으로 15Hz 실시간 로봇 정책 제어(자체 벤치, 독립 검증 없음), Cosmos 3 Edge Policy(DROID[^droid])로 pick-and-place 파인튜닝 지원. 기존 "Cosmos 3 as sim-to-real 학습원"(🖥️ 섹션)과 별개로 엣지 배포 축만 다룸, AMD Ryzen AI Embedded X100(본 표)과 경쟁 구도 병행 관찰. 실제 프로덕션 로봇 배포 사례 0 | 독립 벤치마크 + 실제 로봇 프로덕션 배포 사례 |
| **[Walden Robotics](https://www.waldenrobotics.com/news/walden-robotics-launches-from-stealth)** (Toyota Research Institute 스핀아웃, Large Behavior Models[^lbm] 휴머노이드) | 🟡 파일럿 | ✨ **주목**: TRI 로보틱스를 이끈 Russ Tedrake의 스핀아웃 + 시드 3억 달러 — LBM 상용화 최전선, Toyota 공장 실파일럿 보유<br>⏳ **대기**: 회사 공식 발표(2026-07-15) `[4]` — 2026-01 TRI에서 스핀아웃(창업자 Russ Tedrake, 전 TRI SVP), Toyota·Deviation Capital 공동 리드 + NVIDIA·Boeing·Samsung Ventures 등 참여 시드 3억 달러(밸류 11억 달러). 휴머노이드 상반신+이동형 베이스, Diffusion Policy[^diffpol]·Large Behavior Models 기반 정책으로 노스아메리카 Toyota 공장에서 2026-02부터 파일럿→"프로덕션 전환" 자체 주장, 3자 검증 없음 | 3자 감사·독립 검증 + 배포 규모 확대 사례 |
| **[Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)** (VLA[^vla] 파운데이션 모델, UMI[^umi] 10만+시간 실세계 궤적) | 🔵 Research | ✨ **주목**: UMI 10만+시간 실세계 궤적이라는 데이터 스케일로 4개 벤치 SOTA 주장 — 중국 빅테크의 VLA 경쟁 본격 진입 신호<br>⏳ **대기**: Xiaomi 공식 arXiv 발표(2607.15330, 2026-07-16) `[4]` — Qwen3-VL 기반 MoT(VLM+DiT), RoboCasa365(57.4%, 기존 SOTA 46.6%↑) 등 4개 벤치마크 SOTA 자체 주장(RLDX-1·GR00T N1.6 포함 비교, 독립 재현 없음). ⚠️ **정정(2026-08-10)**: 2026-08-03 GitHub에 코드·체크포인트(base 5B + RoboCasa/RoboCasa365/VLABench 태스크별 3종) 실공개 확인 — **Apache-2.0**(RLDX-1과 달리 상업 이용 명시 허용, AWS 매핑 가능성). 리포 자체 리더보드 수치는 arXiv 발표치와 표기 방식이 달라 직접 대조 필요, 독립 재현·실배포는 여전히 0 | 독립 벤치마크 재현 + 실배포 사례 |
| **[Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)** (Google DeepMind, 전신 제어 VLA) | 🟡 Preview | ✨ **주목**: 프론티어 랩 VLA가 상체 조작을 넘어 전신(보행·양손 협응) 제어로 확장 — 경쟁 스택 지형을 바꾸는 세대 전환 신호<br>⏳ **대기**: 공식 발표(2026-07-30) `[4]` — 기존 상체 전용 제어에서 전신(보행·굽힘·양손 협응) 제어로 확장, 추론 모델 Gemini Robotics ER 2·엣지 모델 On-Device 2 동반 출시. Apptronik Apollo 2 실기 데모(전구 분리 92% 성공)로 시연, 자체 벤치·독립 검증 없음. ER 2만 AI Studio/Enterprise Agent Platform 프리뷰 공개, VLA·On-Device 2는 얼리액세스 파트너 한정. ⚠️ [pillar-2](pillar-2.md) "Gemini Robotics" 경쟁 스택 절은 이 발표 이전(2026-07 확인, ER 1.6/On-Device/1.5 기준) 스냅샷 — pillar owner 갱신 필요 | 얼리액세스 종료·GA 공개 + 독립 벤치마크 검증 |
| **[SiMDex](https://arxiv.org/abs/2608.04196)** (사람 1인칭 시점 영상 마이닝으로 로봇 손 조작 데이터 확보) | 🔵 Research | ✨ **주목**: 기존에 쌓인 사람 1인칭 시점 영상 약 3,200만 건 중 태스크에 맞는 것만 추천 시스템 방식(recall→rank→re-rank)으로 골라 VLA 후속학습에 재활용 — 신규 시연 수집 없이 실데이터 병목을 우회하는 접근<br>⏳ **대기**: arXiv 2608.04196(2026-08-04, 도쿄대·ByteDance Seed 등) `[4]` — 로봇 형태(임바디먼트)에 무관하게 재사용 가능한 행동 표현으로 VLA 구조 변경 없이 적용, 실물 손 조작 태스크에서 가용 샘플 5% 미만 사용으로 성공률 47.7%→61.1% 자체 벤치 주장. peer-review 미채택, 독립 재현 없음 | peer-review + 독립 재현 |
| **[ω-0](https://arxiv.org/abs/2608.06375)** (로코모션+매니퓰레이션 동시 제어 월드-액션 모델) | 🔵 Research | ✨ **주목**: 이동·자세 조정·균형·조작을 분리하지 않고 단일 모델이 동시 수행(concurrent loco-manipulation)하도록 diffusion[^diffpol] 기반 whole-body 액션을 생성 — 실기(Unitree G1) 11개 가정 태스크에서 자율 수행 시연, 사람 동작 데이터 전이(human-to-humanoid)까지 포함<br>⏳ **대기**: arXiv 2608.06375(2026-08-06, NTU·PKU·BAAI 등) `[4]` — 자체 벤치에서 기존 모방학습·VLA·휴머노이드·WAM 베이스라인 대비 우위 주장, 독립 재현·peer-review 없음. 40시간 규모 ω-HOME 데이터셋 공개 여부 불명 | peer-review + 독립 재현 + 데이터셋·코드 공개 확인 |
| **[Xiaomi-Robotics-U0](https://arxiv.org/abs/2607.11643)** (통합 임바디드 데이터 합성 월드 파운데이션 모델, 38B) | 🔵 Research | ✨ **주목**: text-to-image·장면합성·비디오생성·"embodied transfer"를 하나의 오토레그레시브 프레임워크로 통합해 로봇 학습용 합성 데이터를 직접 생성 — WorldArena 벤치 100+ 모델 중 종합 1위 자체 주장, π0.5 실기 정책에 증강 데이터를 적용해 held-out(배경·조명 변경) 조건 완료율 36.9%→63.2% 개선까지 실측<br>⏳ **대기**: Xiaomi 공식 arXiv 발표(2607.11643, 2026-07-13) `[4]` — 벤치·실기 결과 모두 자체 측정, 독립 재현·peer-review 없음, 오픈소스 가중치·코드 공개 여부 불명. 같은 표의 Xiaomi-Robotics-1(VLA 정책 모델)과는 별개 모델·별개 사안(이쪽은 데이터 합성용 WFM) | peer-review + 독립 재현 + 가중치·코드 공개 확인 |
| **[In-Context VLA / VLA-Talker](https://arxiv.org/abs/2608.05738)** (에이전틱 툴 사용[^agent]으로 추론-제어 충돌을 회피하는 VLA[^vla] 구조) | 🔵 Research | ✨ **주목**: VLA에 자유형 텍스트 추론(CoT)을 넣으면 지연·최적화 목표 충돌로 저수준 제어 성능이 떨어짐을 실증하고, 대신 정책이 오픈보캐뷸러리 탐지기·깊이 추정·VLM을 능동적으로 호출해 필요한 정보만 얻는 구조(VLA-Talker)로 전환 — 추론과 행동을 텍스트로 섞지 않고 아키텍처로 분리하는 접근<br>⏳ **대기**: arXiv 2608.05738(2026-08-06, 단일 연구팀) `[4]` — 자체 벤치 결과, 독립 재현·peer-review 없음, 코드·가중치 공개 여부 불명 | peer-review + 독립 재현 + 공개 확인 |

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
[^droid]: **DROID** — 13개 기관이 Franka 로봇 팔로 수집한 대규모 공개 실세계 매니퓰레이션 데이터셋. 매니퓰레이션 정책의 사전학습·파인튜닝 재료로 널리 쓰인다.
[^lbm]: **Large Behavior Models (LBM)** — LLM의 "로봇 행동" 판. 대규모 시연 데이터로 학습해 여러 매니퓰레이션 태스크를 한 모델로 수행하는 로봇 파운데이션 모델을 가리키는 Toyota Research Institute의 용어.
[^diffpol]: **Diffusion Policy** — 이미지 생성에 쓰이는 확산(diffusion) 모델로 로봇 동작 시퀀스를 생성하는 정책 아키텍처. 여러 갈래의 시연 데이터를 안정적으로 학습해 모방학습의 사실상 표준이 됐다.
[^umi]: **UMI (Universal Manipulation Interface)** — 로봇 없이, 사람이 카메라 달린 휴대형 그리퍼를 손에 쥐고 시연 데이터를 모으는 수집 방식. 로봇 투입 없이 실세계 데이터를 대량 확보할 수 있다.
