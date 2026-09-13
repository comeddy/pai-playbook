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

## 🆕 최신 스캔 유입 (2026-09-13 · 1차 검증 완료 2026-07-21)

<!-- 자동 스캔(arXiv/웹) 유입분. 2026-07-21 1차 출처 검증 완료(검증 에이전트 4식, 공식 발표·arXiv 원문 대조) — 승격 0건, 정정 6건. THE FILTER 통과 전까지 고객 제안 사용 금지. 정기 갱신은 scripts/radar_scan.md 참고. -->

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| **[GHOST](https://arxiv.org/abs/2608.29080)** (온보드 카메라만으로 1인이 로봇 2대를 동시 원격조작하는 VR 텔레옵) | 🔵 Research | ✨ **주목**: Brown University(Tellex lab)가 Amazon 자금 지원으로 개발 — 외부 모션캡처 없이 온보드 RGB-D만으로 1인 오퍼레이터가 Boston Dynamics Spot 2대를 동시에 VR로 원격조작, IEEE RA-L 게재(peer-review 통과). 초보자 성공률 1.6~4배, 전문가 작업 속도 1.47배 개선 실측 — 텔레옵 기반 로봇 데이터 수집 파이프라인 비용을 낮출 수 있는 오픈소스 사례<br>⏳ **대기**: arXiv 2608.29080(2026-08-29, IEEE RA-L 2026-08 accept) `[4]` — 전문가 평가자가 논문 저자 3인 자신(편향 가능), 초보자 평가 n=15(9개 태스크 중 2개만 수행), Boston Dynamics Spot 하드웨어 전용·전용 Wi-Fi 환경(프로덕션 신뢰성 미검증) | 독립 사용자 평가 확대 + 다양한 하드웨어·네트워크 환경 검증 |
| **[Perceptron Isaac 0.5](https://github.com/perceptron-ai-inc/isaac)** (오픈 웨이트 임바디드 파운데이션 모델, 360억 파라미터) | 🔵 Research | ✨ **주목**: 영상 이해·임바디드 추론·로봇 제어를 단일 스파스 백본에 통합한 오픈 웨이트 모델 — 35개+ 로봇 시스템·10만+시간 로봇 경험·100만 시간 영상·3T 멀티모달 토큰으로 학습, π0.5·GR00T N1.7 대비 우위를 자체 주장하며 코드·가중치를 함께 공개(코드 Apache-2.0)<br>⏳ **대기**: 회사 공식 발표 + GitHub 공식 저장소(2026-08-27/28, ex-Meta 연구진 스타트업 Perceptron AI) `[4]` — 자체 벤치, 독립 재현·peer-review 없음. 가중치 자체의 라이선스 조건은 Hugging Face 저장소 별도 표기(접속 미확인) | 독립 벤치마크 재현 + 실배포 사례 |
| **[ABEJA×무라타제작소 GR00T N1.7 양팔 로봇 PoC](https://prtimes.jp/main/html/rd/p/000000229.000010628.html)** (VLA 기반 물리AI 기술검증) | 🟡 Preview | ✨ **주목**: 일본 제조 대기업 무라타제작소가 NVIDIA GR00T N1.7(상업 라이선스 오픈 VLA)로 양팔 로봇의 부품 주고받기·자세 전환·삽입 연속 동작을 실기로 검증 — 상업 라이선스 오픈 VLA를 실제 제조 대기업이 검증한 초기 사례, 실험실 자동화 각도<br>⏳ **대기**: ABEJA·무라타제작소 공식 발표(2026-08-31, PR TIMES) `[4]` — 텔레옵 시연 수백 건으로 모방학습, 검증(테스트) 환경 실기 성공. 생산 규모 배포·자율 성능 독립 검증 없음. ⚠️ 링크는 공식 PR TIMES 배포분이나 이번 실행 환경의 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 실 생산 라인 배포 + 독립 검증 |
| **[NEURA Robotics 4NE1 / Neuraverse × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale)** (독일 풀스택 로보틱스, AWS 전략적 협업) | ⚪ 로드맵 | ✨ **주목**: AWS가 Neuraverse의 주 클라우드 공급자로 참여해 Gym 훈련 환경을 SageMaker와 통합하고 NEURA가 APN에 합류하는 등 서비스명이 구체적으로 명시된 AWS 파트너십 — Radar 내 "AWS 자사" 물리 AI 사례 중 구체적인 유럽 휴머노이드 트랙<br>⏳ **대기**: AWS·NEURA 공식 발표(2026-04-21, press.aboutamazon.com) `[4]` — Amazon 풀필먼트센터 배치는 "검토 중" 단계일 뿐 실배포 아님. 시리즈C 최대 14억 달러(2026-06-10, Amazon·NVIDIA·Tether 등 참여, 풀스택 로보틱스 사상 최대) + IFA 2026 베를린 키노트(2026-09-05, 4NE1 실기 전시)로 화제 갱신, 3자 검증 없음. ⚠️ 링크는 공식 press.aboutamazon.com 배포분이나 이번 실행 환경의 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | Amazon 풀필먼트센터 등 실배포 사례 공개 + 독립 성능 검증 |
| **[RLWRLD RLDX-1](https://arxiv.org/abs/2605.03269)** (81억 파라미터 덱스터리티[^dext] 파운데이션 모델, AWS Generative AI Accelerator 참여) | 🔵 Research | ✨ **주목**: KAIST 출신 서울 스타트업이 AWS Generative AI Accelerator 컴퓨트로 학습한 오픈 로보틱스 파운데이션 모델을 AWS 공식 블로그가 직접 소개 — 5지 핸드 정밀 조작 특화, GR00T N1.6·π0.5 대비 우위를 자체 벤치마크로 주장하는 한국발 "AWS 자사" 파트너십 사례(NEURA와 함께 Radar 내 AWS 공식 협업 사례)<br>⏳ **대기**: RLWRLD 공식 발표 + arXiv 기술 리포트(2026-05, arXiv 2605.03269) `[4]` — 8개 공개 벤치마크 자체 측정치(예: GR-1 Tabletop 58.7점, GR00T N1.6 대비 +10.7%p), 독립 재현·peer-review 없음. AWS 관계는 accelerator 참여 단계, 실배포는 롯데호텔앤리조트 목표 2030년(초기 단계). ⚠️ 링크는 arXiv 원문이나 이번 실행 환경의 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 독립 벤치마크 재현 + 실배포 사례 공개 |
| **[Figure Index](https://www.figure.ai/index-app)** (크라우드소싱 인간 영상 기반 로봇 데이터 수집 앱) | 🟡 Preview | ✨ **주목**: Figure AI가 자체 VLA Helix 학습 데이터를 벤더 구매가 아니라 일반인 대상 유료 크라우드소싱 앱으로 직접 수집 — 2026-08-25 공개 후 108개국 4.4만+ 주간 활성 사용자, 영상 1,600만+ 건 업로드(초당 약 30분 분량), 향후 12개월 데이터·컴퓨트에 10억 달러+ 투자 공표 — 기업이 실사용 영상 데이터 파이프라인을 자체 운영하는 드문 사례<br>⏳ **대기**: Figure 공식(figure.ai) `[4]` — 참가자 누적 보상 1,500만 달러 지급 발표뿐, 수집 영상이 Helix 정책 성능에 실제로 반영된 정량 성과·품질 관리 방식 독립 검증 없음. ⚠️ 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | Helix 정책 성능 개선 실측 공개 + 독립 검증 |
| **[KIMM 카이로스(KAIROS) V0.7](https://www.kimm.re.kr/eng/sub011001/view/id/1565)** (K-Moonshot 국가전략기술 과제 국산 AI 휴머노이드) | ⚪ 로드맵 | ✨ **주목**: 한국기계연구원(KIMM)이 과기정통부 지원 'AI 휴머노이드 글로벌 톱 연구단'으로 개발 중인 국책 휴머노이드 — 2026-09-07 '2026 글로벌 기계기술 포럼'에서 V0.7 공개, 국민체조·탈춤 동작까지 구현(4월 V0.5는 악수·손흔들기 수준) — 한국 고객 대화에서 나올 수 있는 '국책 연구기관발' 휴머노이드 트랙(현대·BD Atlas와 다른 각도)<br>⏳ **대기**: KIMM 공식 발표 `[4]`(2차: 다수 국내 매체 교차 확인 — 국민체조·탈춤 시연은 자체 데모. ⚠️ 이번 실행 환경 egress 제한으로 kimm.re.kr curl 200 수동 검증 미수행, 커밋 메시지·이슈 참조) — V1.0 공개는 2027-04 목표, 추가 개발비(약 30억 원) 필요 상태로 보도됨. 상용화·자율 성능 전무, 데모 단계 | V1.0 공개 + 자동차 조립·가정용 실증 사례 공개 |
| **[Generalist AI GEN-1.5](https://generalistai.com/blog/gen-1.5)** (물리 상호작용 데이터로 8개월+ 사전학습한 임바디드 파운데이션 모델, 단일 시연 3~12초만으로 새 작업을 그래디언트 업데이트·파인튜닝 없이 즉시 수행하는 원샷 학습) | 🔵 Research | ✨ **주목**: 시연 영상 3~12초를 "물리적 프롬프트"로 컨텍스트에 넣어 파인튜닝 없이 새 작업을 바로 시도 — VLA의 태스크별 파인튜닝 의존도를 낮출 수 있는 축, 다수 매체가 "로보틱스의 GPT-3 모먼트"로 평가<br>⏳ **대기**: 회사 공식 발표(2026-08-19, generalistai.com) `[4]` — 10개 태스크 자체 벤치마크(원샷 평균 성공률 59%, 5분 데이터+10 gradient step 후 83%)뿐, 독립 재현·peer-review 없음. ⚠️ 이번 실행 환경의 egress 제한으로 generalistai.com curl 200 수동 검증 미수행(커밋 메시지·이슈 참조) | 독립 벤치마크 재현 + 다양한 태스크·하드웨어 검증 |
| **[NVIDIA Isaac GR00T Reference Humanoid Robot](https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design)** (오픈 레퍼런스 휴머노이드 하드웨어, GTC Taipei 발표) | 🟡 Preview | ✨ **주목**: NVIDIA가 처음으로 완전한 레퍼런스 휴머노이드 하드웨어(Unitree H2 Plus 섀시 31DOF + Sharpa Wave 5지 촉각 핸드 22DOF + Jetson AGX Thor T5000 온보드 컴퓨트 + Isaac GR00T 소프트웨어 스택)를 발표 — Radar에 이미 있는 NEURA Robotics·1X 등이 GR00T 생태계 파트너로 합류, GR00T가 소프트웨어에서 하드웨어까지 수직 통합되는 신호<br>⏳ **대기**: NVIDIA 공식 발표(2026-06-01, GTC Taipei) `[4]`(1차 출처 nvidianews.nvidia.com — 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행, 커밋 메시지·이슈 참조) — Unitree를 통한 출하는 "2026년 말" 예정이며 대상은 학술연구용(Stanford·ETH Zurich·Ai2·UCSD 런칭 파트너), 실제 배송·연구 성과 0건 | 실제 출하 + 연구기관 활용 성과 공개 |
| **[UBTech UWORLD U1](https://www.prnewswire.com/news-releases/ubtech-launches-uworld-u1-the-worlds-first-full-size-mass-produced-ultra-bionic-humanoid-robot-302815272.html)** (중국 가정용 컴패니언 휴머노이드, 88DOF) | 🟡 Preview | ✨ **주목**: UBTECH가 "세계 최초 완전 사이즈 양산형" 가정용 컴패니언 휴머노이드로 공개 — 3개 모델 라인($17,600~$145,000), 사전주문 1.3만+대 확보 후 2026-09-16 첫 배송 예정 — 소비자 휴머노이드 양산 트랙에서 1X Neo와 다른 각도(중국발 대량생산·양산가 공개)<br>⏳ **대기**: UBTECH 공식 발표(2026-06-30) `[4]`(1차 출처는 PRNewswire 공식 배포분 — 이번 실행 환경 egress 제한으로 curl 200 수동 검증 미수행, 커밋 메시지·이슈 참조) — "양산" 주장은 발표·사전주문 단계, 실제 배송·자율성능(원격조작 비율 등) 독립 검증 없음 | 실배송 완료 + 독립 사용후기·자율성능 검증 |

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
