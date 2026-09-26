# Radar — 대기열 / 관찰 목록

_최종 갱신: 2026-08 · owner: Youngjin · volatility: 높음_
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

## 🆕 최신 스캔 유입 (2026-09-26 · 1차 검증 완료 2026-07-21)

<!-- 자동 스캔(arXiv/웹) 유입분. 2026-07-21 1차 출처 검증 완료(검증 에이전트 4식, 공식 발표·arXiv 원문 대조) — 승격 0건, 정정 6건. THE FILTER 통과 전까지 고객 제안 사용 금지. 정기 갱신은 scripts/radar_scan.md 참고. -->

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| **[NEURA Robotics 4NE1 / Neuraverse × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale)** (독일 풀스택 로보틱스, AWS 전략적 협업) | ⚪ 로드맵 | ✨ **주목**: AWS가 Neuraverse의 주 클라우드 공급자로 참여해 Gym 훈련 환경을 SageMaker와 통합하고 NEURA가 APN에 합류하는 등 서비스명이 구체적으로 명시된 AWS 파트너십 — Radar 내 "AWS 자사" 물리 AI 사례 중 구체적인 유럽 휴머노이드 트랙<br>⏳ **대기**: AWS·NEURA 공식 발표(2026-04-21, press.aboutamazon.com) `[4]` — Amazon 풀필먼트센터 배치는 "검토 중" 단계일 뿐 실배포 아님. 시리즈C 최대 14억 달러(2026-06-10, Amazon·NVIDIA·Tether 등 참여, 풀스택 로보틱스 사상 최대) + IFA 2026 베를린 키노트(2026-09-05, 4NE1 실기 전시)로 화제 갱신, 3자 검증 없음. ⚠️ 링크는 공식 press.aboutamazon.com 배포분이나 이번 실행 환경의 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | Amazon 풀필먼트센터 등 실배포 사례 공개 + 독립 성능 검증 |
| **[RLWRLD RLDX-1](https://arxiv.org/abs/2605.03269)** (81억 파라미터 덱스터리티[^dext] 파운데이션 모델, AWS Generative AI Accelerator 참여) | 🔵 Research | ✨ **주목**: KAIST 출신 서울 스타트업이 AWS Generative AI Accelerator 컴퓨트로 학습한 오픈 로보틱스 파운데이션 모델을 AWS 공식 블로그가 직접 소개 — 5지 핸드 정밀 조작 특화, GR00T N1.6·π0.5 대비 우위를 자체 벤치마크로 주장하는 한국발 "AWS 자사" 파트너십 사례(NEURA와 함께 Radar 내 AWS 공식 협업 사례)<br>⏳ **대기**: RLWRLD 공식 발표 + arXiv 기술 리포트(2026-05, arXiv 2605.03269) `[4]` — 8개 공개 벤치마크 자체 측정치(예: GR-1 Tabletop 58.7점, GR00T N1.6 대비 +10.7%p), 독립 재현·peer-review 없음. AWS 관계는 accelerator 참여 단계, 실배포는 롯데호텔앤리조트 목표 2030년(초기 단계). ⚠️ 링크는 arXiv 원문이나 이번 실행 환경의 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 독립 벤치마크 재현 + 실배포 사례 공개 |
| **[Figure Index → Helix 2.5](https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization)** (크라우드소싱 인간 영상 데이터로 사전학습한 휴머노이드 신경망, 미학습 가정 30곳에서 zero-shot 검증) | 🟡 Preview | ✨ **주목**: Figure가 크라우드소싱 데이터(Index)로 사전학습한 단일 정책을 데이터 수집·파인튜닝 없이 베이 지역 실제 가정 30곳(전부 미학습)에 배포해 거실 정리·수건 접기·이불 정리 3개 과제를 수행 — Index 사전학습만으로 zero-shot 전체 과제 성공률이 9%→56%(420회 중 237회)로 상승했다고 발표, 크라우드소싱 데이터 파이프라인이 실제 정책 성능으로 이어진다는 최초의 정량적 증거로 기존 유입 항목의 승격 조건 중 "실측 공개"를 충족<br>⏳ **대기**: Figure 공식 발표(2026-09-17, figure.ai) `[4]` — 자체 측정치(9%→56%, 30개 가정, 420회 시행)뿐, 독립 재현·3자 검증 없음. Index 앱 자체의 보상 지급(1,500만 달러)·품질관리 방식도 여전히 자체 공표 수준. ⚠️ 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 독립 재현·3자 벤치마크 검증 + 추가 가정·과제 확대 실증 |
| **[KIMM 카이로스(KAIROS) V0.7](https://www.kimm.re.kr/eng/sub011001/view/id/1565)** (K-Moonshot 국가전략기술 과제 국산 AI 휴머노이드) | ⚪ 로드맵 | ✨ **주목**: 한국기계연구원(KIMM)이 과기정통부 지원 'AI 휴머노이드 글로벌 톱 연구단'으로 개발 중인 국책 휴머노이드 — 2026-09-07 '2026 글로벌 기계기술 포럼'에서 V0.7 공개, 국민체조·탈춤 동작까지 구현(4월 V0.5는 악수·손흔들기 수준) — 한국 고객 대화에서 나올 수 있는 '국책 연구기관발' 휴머노이드 트랙(현대·BD Atlas와 다른 각도)<br>⏳ **대기**: KIMM 공식 발표 `[4]`(2차: 다수 국내 매체 교차 확인 — 국민체조·탈춤 시연은 자체 데모. ⚠️ 이번 실행 환경 egress 제한으로 kimm.re.kr curl 200 수동 검증 미수행, 커밋 메시지·이슈 참조) — V1.0 공개는 2027-04 목표, 추가 개발비(약 30억 원) 필요 상태로 보도됨. 상용화·자율 성능 전무, 데모 단계 | V1.0 공개 + 자동차 조립·가정용 실증 사례 공개 |
| **[XPENG IRON](https://www.xpeng.com/news/01a080371029a057bc8e8a02a2c6012b)** (중국 EV업체 XPENG의 휴머노이드, 자동차급 양산 라인에서 첫 완성 로봇이 자력 보행) | ⚪ 로드맵 | ✨ **주목**: 완성차 업체가 자사 EV 생산 노하우(공정 자동화 80%+)를 그대로 휴머노이드 양산 라인에 이식 — Tesla Optimus가 여전히 "학습·데이터 수집" 단계에 머무는 것과 대조적으로 실제 완성 로봇이 라인에서 자력으로 걸어나오는 모습을 공개(76자유도, 손 각 21자유도) — 한국 고객 대화의 "중국 EV발 휴머노이드" 경쟁 트랙을 새로 추가<br>⏳ **대기**: XPENG 공식 발표(2026-09-07/08, xpeng.com) + CnEVPost·Electrek 교차 확인 `[4]` — "양산 시작"은 2026년 말 목표치이며 초기 배치는 매장·캠퍼스 내부용, 해외·일반 상업 인도는 2027년부터. 독립 성능·안전 검증 없음. ⚠️ 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 실제 양산 출하 시작 + 3자 안전·성능 검증 |
| **[Skild AI S1](https://skild.ai/blogs/s1)** (단일 인간 시연 영상만으로 파인튜닝 없이 최대 10분 장기 태스크를 수행하는 인컨텍스트 러닝 로봇 파운데이션 모델) | 🟡 Preview | ✨ **주목**: Skild AI가 인간 시연 영상 1개를 "비주얼 프롬프트"로 받아 파인튜닝·가중치 변경 없이 최대 10분·수십 스텝의 미학습 장기 태스크를 수행 — [NVIDIA 공식 블로그](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/)(2026-09-10)가 Skild·NVIDIA·Foxconn의 NVIDIA Blackwell 시스템 조립 라인(부스바·리밋블록 장착, 나사 16개 체결 등) 실배포와 유상 고객 60개+ 확보, 첫 상용 배포 10개월 만에 연환산매출(ARR) 1억 달러 달성을 공식 확인 — "소수 파트너 배포 시작" 선언 단계에서 실제 산업 매출 단계로 진입한 초기 사례로 갱신<br>⏳ **대기**: NVIDIA·Skild AI 공식 발표(2026-09-10) `[4]` — 매출·고객 수는 회사 자체 공표치이며 3자 감사·독립 성능 검증 없음(범용 태스크 성공률 등 세부 미공개). AWS 매핑·서울 리전 연계 사례 없음. ⚠️ 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 독립 성능·매출 검증(3자 감사) + AWS 매핑 사례 공개 |
| **[Opt2VLA](https://opt2vla.github.io/)** (접촉이 많은 휴머노이드 전신 조작을 위한 힘(force)-인지 VLA — 기하학적 동작 목표뿐 아니라 접촉력 기준값까지 함께 예측) | 🔵 Research | ✨ **주목**: 기존 VLA는 동작(모션) 목표만 예측하고 접촉 후 시각 정보가 불안정해지는 순간의 힘 제어는 전신 컨트롤러에 맡겨왔는데, Opt2VLA는 단일 멀티태스크 VLA가 동작 목표와 접촉력 기준값을 함께 예측해 태스크별 RL 전신 컨트롤러가 그 힘을 추적하도록 함 — 궤적 최적화(TO)로 접촉과 일관된 학습 데이터를 직접 생성. TANGO(전신 내비게이션)와 다른 각도로 "전신 제어형 VLA"의 조작(매니퓰레이션) 축을 보완하는 연구<br>⏳ **대기**: arXiv 프리프린트(2026-09-21, Georgia Tech·Ye Zhao/Zsolt Kira 랩 등) `[4]` — 접촉이 많은 태스크 3종 자체 벤치마크뿐, peer-review·독립 재현·오픈소스 공개 없음. ⚠️ 이번 실행 환경의 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | peer-review + 코드/체크포인트 오픈소스 공개 후 독립 재현 |
| **[OpenAI 휴머노이드 로봇 개발 확인](https://sources.news/p/introducing-the-sources-podcast-with)** (Sam Altman, Sources 팟캐스트에서 자사 휴머노이드 로봇 개발을 직접 확인) | ⚪ Hype·로드맵 | ✨ **주목**: OpenAI CEO가 "우리는 분명히 휴머노이드를 만들 것"이라고 처음으로 직접 확인 — 로봇 하드웨어 폼팩터로 공식 확장을 시사해 Radar 경쟁 휴머노이드 관찰 목록(Tesla/Figure/1X/Google)에 OpenAI가 새로 추가되는 계기, 고객 대화 화제성이 가장 높을 항목 중 하나<br>⏳ **대기**: 2026-09-01 Sources 팟캐스트 발언뿐 `[4]` — 프로토타입·출시 일정·제조 파트너 전무(Forbes 등 확인), 데이터센터용 등 "다른 폼팩터"도 동시 언급되어 휴머노이드 전용 전략인지도 불확실. ⚠️ 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 프로토타입·제조 파트너·출시 일정 공식 발표 |
| **[Intrinsic Core](https://www.intrinsic.ai/blog/posts/introducing-intrinsic-core)** (Alphabet 로보틱스 자회사 Intrinsic의 산업용 로보틱스 스택 오픈소스화 — 실시간 제어·NVIDIA FoundationPose 기반 포즈추정·모션/그립 플래닝·시뮬레이션·카메라 캘리브레이션·ROS 호환 드라이버) | 🟢 GA(오픈소스) | ✨ **주목**: Intrinsic이 실제 자사 프로덕션 배포에 쓰는 스택을 ROSCon 2026(토론토)에서 Apache 2.0으로 통째 공개 — Isaac 생태계 일강 구도에 Alphabet발 대안 스택이 처음 등장, Radar 🖥️ 시뮬레이션/도구 축(Isaac/MuJoCo/Newton)에 경쟁사 관찰 대상 추가<br>⏳ **대기**: Intrinsic 공식 블로그 + The Robot Report(2026-09-22/23) `[4]` — 코드 자체는 GitHub 공개(Apache 2.0)지만 Intrinsic 외부의 독립 채택 사례·AWS 매핑 사례 없음. ⚠️ 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 외부 독립 채택 사례 공개 + AWS 인프라 매핑 검증 |
| **[Agility Robotics Digit 5](https://www.agilityrobotics.com/content/agility-unveils-digit-5-humanoid-robot-built-for-cooperatively-safe-work-at-scale)** (기존 Digit@GXO 대비 근접 협업 안전 아키텍처·90분 러닝타임 배터리를 갖춘 5세대 범용 휴머노이드) | 🟡 Preview | ✨ **주목**: pillar-4에 "가장 잘 검증된 유료 휴머노이드"로 이미 오른 Agility Digit(@GXO)의 차세대 모델 — 충돌 위험 감지 시 정지/착석 + 시청각 경고로 사람과 근접 작업이 가능한 안전 설계, 3억 달러+ 다년 주문 확보 후 최초로 EU·영국까지 상업 배포 확장 발표(CE 마킹 계획)<br>⏳ **대기**: Agility 공식 발표(2026-09-15, agilityrobotics.com) `[4]` — 주문 잔고·CE 마킹 계획일 뿐, Digit 5 자체의 실가동 사례는 아직 없음(기존 GXO 사례는 이전 세대 Digit). ⚠️ 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | Digit 5 실가동 고객 사례 공개(EU/북미) + 안전 아키텍처 3자 검증 |

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
_owner: Youngjin · updated: 2026-08 · volatility: 높음 (Radar는 본질적으로 빠르게 변함 — 월 단위 검토 권장)_

<!-- 용어 각주 -->

[^wfm]: **월드 파운데이션 모델(WFM, World Foundation Model)** — 물리 세계의 다음 장면을 예측·생성하도록 학습된 대형 모델. 텍스트·영상 프롬프트로 물리적으로 그럴듯한 영상·시나리오를 만들어 로봇 학습 데이터를 증강한다. 🎥 [NVIDIA Cosmos 소개](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **시스템 식별(SysID, System Identification)** — 실물 로봇의 물리 파라미터(마찰·질량·모터 응답)를 측정해 시뮬레이터를 실물에 맞게 보정하는 작업.
[^s2r]: **sim-to-real** — 시뮬레이션에서 학습한 정책을 실제 로봇으로 옮기는 것, 또는 그 방법론. 시뮬레이션과 현실의 물리·시각 차이(도메인 갭) 때문에 그냥 옮기면 성능이 무너진다. 🎥 [NVIDIA sim-to-real 로보틱스 쇼케이스](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **물리 엔진(physics engine)** — 강체 동역학·접촉·마찰·충돌을 수치적으로 계산하는 시뮬레이터의 핵심 소프트웨어. 엔진의 정확도·속도 트레이드오프가 시뮬레이터 선택(Isaac/MuJoCo/Genesis)을 좌우한다.
[^mcp]: **MCP (Model Context Protocol)** — 에이전트와 툴·데이터 소스를 잇는 개방형 표준 프로토콜. "에이전트용 USB-C"에 비유되며, 로봇 스킬을 MCP 서버로 노출하는 실험이 늘고 있다.
[^ros]: **ROS 2 (Robot Operating System 2)** — 로봇 소프트웨어의 사실상 표준 오픈소스 미들웨어. 센서·제어 노드들이 토픽(topic)으로 통신하는 분산 구조로, 산업·연구 로봇 스택의 공용 기반이다.
[^agent]: **LLM 에이전트** — 대형 언어 모델이 스스로 계획을 세우고 툴(API·로봇 스킬)을 골라 호출하며 다단계 작업을 수행하는 소프트웨어. 단순 질의응답과 달리 "행동"이 있다는 점이 핵심이다.
[^dext]: **덱스터리티(dexterity)** — 로봇 손·팔이 사람 손처럼 정교하고 섬세하게 물체를 다루는 능력. 단순 그리퍼의 집기·놓기와 달리, 5지 핸드로 물체를 돌리거나 도구를 조작하는 등 접촉이 많고 복잡한 조작을 뜻한다.
