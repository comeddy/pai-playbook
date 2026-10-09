# Radar — 대기열 / 관찰 목록

_최종 갱신: 2026-09 · owner: Youngjin · volatility: 높음_
[← index로](index.md)

> **L0 TL;DR**: 원문·재현·현장 검증이 더 필요한 후보 목록이다. [수록 기준](maintenance.md#포함-기준-the-filter)을 모두 확인하고 owner가 사용 범위를 검토해야 본문으로 승격한다. 자동 스캔은 승격을 승인하지 않는다.
>
> ⚠️ **여기 있는 항목을 고객 제안에 "성숙한 역량"처럼 쓰지 말 것.** 화려한 데모가 배포 가능성을 가리는 경우가 많다.

---

> **검토 범위**: 페이지 수정일은 모든 기술 항목의 재검증일이 아니다. 핵심 정정의 확인일·재현/사람 검토 상태는 [근거 기록](evidence.md)에 있으며, 기존 항목의 개별 확인일은 그대로 적용한다.

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

## 🆕 최신 스캔 유입 (2026-10-09 · 링크·1차 출처 대조 2026-09-27)

<!-- 자동 스캔(arXiv/웹) 유입분. 2026-09-27 링크 생존 전수 확인(20/20 200) + 1차 출처 원문 대조 10건 — 승격 0건, 정정 6건(RLDX 벤치 마진 +11.1p, KIMM 링크 교체, OpenAI 링크 교체·인용 2차 표기, Skild 자체 벤치 공개 반영, Figure Index 수치 출처 분리, NEURA IFA 실기 전시 삭제). 등급은 유입 정책상 [4](자체 공표·독립 검증 없음) 유지. THE FILTER 통과 전까지 고객 제안 사용 금지. 정기 갱신은 scripts/radar_scan.md 참고. -->

| 항목 | 라벨 | 요점 | 승격 조건 |
|---|---|---|---|
| **[NEURA Robotics 4NE1 / Neuraverse × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale)** (독일 풀스택 로보틱스, AWS 전략적 협업) | ⚪ 로드맵 | ✨ **주목**: AWS가 Neuraverse의 주 클라우드 공급자로 플랫폼을 호스팅하고 NEURA Gym 훈련 파이프라인을 SageMaker와 통합, NEURA가 AWS 파트너 네트워크(APN)로 GTM을 확장 — 서비스명이 명시된 AWS 파트너십으로 Radar 내 유럽 휴머노이드 트랙<br>⏳ **대기**: AWS·NEURA 공식 발표(2026-04-21, press.aboutamazon.com) `[4]` — Amazon 풀필먼트센터 배치는 원문 표현이 "explore opportunities"(검토)일 뿐 실배포 아님. [시리즈C 최대 14억 달러](https://neura-robotics.com/record-series-c/)(2026-06-10, Amazon·NVIDIA·Tether 등 참여, 자사 표현 "풀스택 로보틱스 사상 최대") + [IFA 2026 베를린 키노트](https://www.ifa-berlin.com/press-releases/ifa-2026-neura)(2026-09-05)로 화제 갱신, 3자 검증 없음. 🔗 링크 200 · 원문 대조 2026-09-27. **AWS 각도: 공식 협업(SageMaker·APN 명시)** | Amazon 풀필먼트센터 등 실배포 사례 공개 + 독립 성능 검증 |
| **[RLWRLD RLDX-1](https://arxiv.org/abs/2605.03269)** (81억 파라미터 덱스터리티[^dext] 파운데이션 모델, AWS에서 학습) | 🔵 Research | ✨ **주목**: KAIST 출신 서울 스타트업의 오픈 로보틱스 파운데이션 모델을 [AWS Physical AI 블로그](https://aws.amazon.com/blogs/physical-ai/putting-dexterous-robots-to-work-how-rlwrld-builds-physical-ai-with-aws/)(2026-06-22)가 직접 소개 — EC2 p5e/p5en(H200)·ParallelCluster·FSx for Lustre로 학습, 5지 핸드 정밀 조작 특화, 코드·가중치 [GitHub 공개](https://github.com/RLWRLD/RLDX-1)(CC BY 4.0) — NEURA와 함께 Radar 내 AWS 공식 협업 사례이자 한국발 트랙<br>⏳ **대기**: arXiv 기술 리포트(2026-05-05) + AWS 블로그 `[4]` — 시뮬 벤치 6종·실기 3플랫폼 자체 측정치(GR-1 Tabletop 58.7 vs GR00T N1.6 47.6 = +11.1p, 표 1(b); ALLEX 실기 86.8% vs π0.5·GR00T N1.6 약 40%; SIMPLER 81.5%는 AWS 블로그 인용), 독립 재현·peer-review 없음 — **자체 공표치, 고객 인용 금지**. AWS 관계는 학습 인프라 + Generative AI Accelerator 참여(2025-10) 단계, 실배포는 롯데호텔앤리조트 2030 목표(안전 검증 조건부). 🔗 링크 200 · 원문 대조 2026-09-27. **AWS 각도: AWS 블로그 사례(EC2·ParallelCluster·FSx) · 🇰🇷 한국 접점** | 독립 벤치마크 재현 + 실배포 사례 공개 |
| **[Figure Index → Helix 2.5](https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization)** (크라우드소싱 인간 영상 데이터로 사전학습한 휴머노이드 신경망, 미학습 가정 30곳에서 zero-shot 검증) | 🟡 Preview | ✨ **주목**: Figure가 크라우드소싱 데이터(Index)로 사전학습한 단일 정책을 데이터 수집·파인튜닝 없이 베이 지역 실제 가정 30곳(전부 미학습)에 배포해 거실 정리·수건 접기·이불 정리 3개 과제를 수행 — Index 사전학습만으로 zero-shot 전체 과제 성공률이 9%→56%로 상승했다고 발표, 크라우드소싱 데이터 파이프라인이 실제 정책 성능으로 이어진다는 최초의 정량적 주장<br>⏳ **대기**: Figure 공식 발표(2026-09-17, figure.ai) `[4]` — 9%→56%는 Figure 내부 블라인드 평가 **자체 측정치, 고객 인용 금지**(시행 420회 중 237회는 2차 매체 기재로 원문 페이지 텍스트에서 미확인; Index 보상 지급 1,500만 달러는 [Index 발표](https://www.figure.ai/news/introducing-index)(2026-08-25) 출처), 독립 재현·3자 검증 없음. 🔗 링크 200 · 원문 대조 2026-09-27. **AWS 각도: 없음** | 독립 재현·3자 벤치마크 검증 + 추가 가정·과제 확대 실증 |
| **[KIMM 카이로스(KAIROS) V0.7](https://www.kimm.re.kr/sub0504/view/id/21372)** (K-Moonshot 국가전략기술 과제 국산 AI 휴머노이드) | ⚪ 로드맵 | ✨ **주목**: 한국기계연구원(KIMM)이 과기정통부 지원 'AI 휴머노이드 글로벌 톱 연구단'으로 개발 중인 국책 휴머노이드 — 2026-09-07 '2026 글로벌 기계기술 포럼'에서 V0.7 공개, 탈춤·국민체조 등 전신 동작 시연(4월 창립 50주년 첫 공개 V0.5는 악수·손흔들기 수준) — 한국 고객 대화에서 나올 수 있는 '국책 연구기관발' 휴머노이드 트랙<br>⏳ **대기**: KIMM 공식 뉴스(2026-09-07) `[4]` — 시연은 자체 데모, 자율 성능 수치 없음. V1.0 공개 2027-04 목표·추가 개발비 약 30억 원은 KIMM 원문에 없고 [이데일리](https://www.edaily.co.kr/News/Read?newsId=03883526645577824)·[뉴스핌](https://www.newspim.com/news/view/20260907001070) 보도(2차). 상용화·자율 성능 전무, 데모 단계. 🔗 링크 200(기존 4월 보도자료 링크를 9-07 공식 뉴스로 교체) · 원문 대조 2026-09-27. **AWS 각도: 없음 · 🇰🇷 한국 접점** | V1.0 공개 + 자동차 조립·가정용 실증 사례 공개 |
| **[XPENG IRON](https://www.xpeng.com/news/01a080371029a057bc8e8a02a2c6012b)** (중국 EV업체 XPENG의 휴머노이드, 자동차급 양산 라인에서 첫 완성 로봇이 자력 보행) | ⚪ 로드맵 | ✨ **주목**: 완성차 업체가 자사 EV 생산 노하우(핵심 공정 자동화 80%+)를 그대로 휴머노이드 양산 라인에 이식 — 실제 완성 로봇이 라인에서 자력으로 걸어나오는 모습을 공개(전신 76자유도, 손 각 21자유도) — 한국 고객 대화의 "중국 EV발 휴머노이드" 경쟁 트랙<br>⏳ **대기**: XPENG 공식 발표(2026-09-08, xpeng.com) `[4]` — 원문 기준 "양산 진입"은 2026년 말 목표, 초기 상업 투입은 자사 매장·캠퍼스, 중국·해외 정식 출시·인도는 2027년. 자유도·자동화율은 자체 공표, 독립 성능·안전 검증 없음. 🔗 링크 200 · 원문 대조 2026-09-27. **AWS 각도: 없음** | 실제 양산 출하 시작 + 3자 안전·성능 검증 |
| **[Skild AI S1](https://skild.ai/blogs/s1)** (단일 인간 시연 영상만으로 파인튜닝 없이 최대 10분 장기 태스크를 수행하는 인컨텍스트 러닝 로봇 파운데이션 모델) | 🟡 Preview | ✨ **주목**: 인간 시연 영상 1개를 "비주얼 프롬프트"로 받아 파인튜닝·가중치 변경 없이 최대 10분·수십 스텝의 미학습 장기 태스크를 수행 — [NVIDIA 공식 블로그](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/)(2026-09-10)가 Skild·NVIDIA·Foxconn의 NVIDIA Blackwell 시스템 조립 라인(부스바·리밋블록 장착, 나사 16개 체결) 배포와 "배포 파트너십 60개+"를 소개 — "소수 파트너 배포" 선언 단계에서 산업 매출 단계로 진입했다는 초기 사례<br>⏳ **대기**: NVIDIA·Skild AI 공식 발표(2026-09-10) `[4]` — [Skild 자사 포스트](https://www.skild.ai/blogs/skild-crosses-100m-arr)의 ARR 1억 달러(첫 상용 배포 10개월 만)·인식 매출 5천만 달러·유상 고객 60개+, S1 블로그(2026-08)의 학습 태스크 96%·미학습 66% 성공률은 모두 **자체 공표치, 고객 인용 금지**(3자 감사·독립 검증 없음). AWS 매핑·서울 리전 연계 사례 없음. 🔗 링크 200 · 원문 대조 2026-09-27. **AWS 각도: 없음(NVIDIA 스택)** | 독립 성능·매출 검증(3자 감사) + AWS 매핑 사례 공개 |
| **[Intrinsic Core](https://www.intrinsic.ai/blog/posts/introducing-intrinsic-core)** (Alphabet 로보틱스 자회사 Intrinsic의 산업용 로보틱스 스택 오픈소스화 — 실시간 제어·NVIDIA FoundationPose 기반 포즈추정·모션/그립 플래닝·Gazebo 기반 시뮬레이션·카메라 캘리브레이션·ROS 호환 드라이버) | 🟢 GA(오픈소스) | ✨ **주목**: Intrinsic이 실제 자사 제조 배포에 쓰는 것과 같은 스택을 ROSCon 2026(토론토)에서 Apache 2.0으로 통째 공개([GitHub](https://github.com/intrinsic-ai/intrinsic-core)) — Isaac 생태계 일강 구도에 Alphabet발 대안 스택이 처음 등장, Radar 🖥️ 시뮬레이션/도구 축(Isaac/MuJoCo/Newton)에 경쟁 관찰 대상 추가<br>⏳ **대기**: Intrinsic 공식 블로그(2026-09-22) `[4]` — 코드는 공개됐지만 Intrinsic 외부의 독립 채택 사례(원문은 FANUC·UR 호환과 챌린지 참가자 수만 언급)·AWS 매핑 사례 없음. 🔗 링크 200 · 원문 대조 2026-09-27. **AWS 각도: 없음(경쟁 스택)** | 외부 독립 채택 사례 공개 + AWS 인프라 매핑 검증 |
| **[Agility Robotics Digit 5](https://www.agilityrobotics.com/content/agility-unveils-digit-5-humanoid-robot-built-for-cooperatively-safe-work-at-scale)** (기존 Digit@GXO 대비 근접 협업 안전 아키텍처·90분 러닝타임 배터리를 갖춘 5세대 범용 휴머노이드) | 🟡 Preview | ✨ **주목**: pillar-4에 "가장 잘 검증된 유료 휴머노이드"로 이미 오른 Agility Digit(@GXO)의 차세대 모델 — 충돌 위험 감지 시 회피·정지·착석 + 시청각 신호로 사람과 근접 작업이 가능한 안전 설계, 90분 구동·9분 충전, CE 마킹으로 EU·영국 진입 계획 발표<br>⏳ **대기**: Agility 공식 발표(2026-09-15, agilityrobotics.com) `[4]` — 다년 주문 3억 달러+는 "2026-05 기준, 계약 마일스톤 충족 조건부"이며 Digit 5 실가동은 0(기존 65,000시간+ 실적은 Digit 4). Early access 2027 상반기, 제조·창고 고객 GA는 2027년 말 예정. 🔗 링크 200 · 원문 대조 2026-09-27. **AWS 각도: 없음** | Digit 5 실가동 고객 사례 공개(EU/북미) + 안전 아키텍처 3자 검증 |
| **[Dyna Robotics DYNA-2 / DYNA 2.1](https://www.prnewswire.com/news-releases/dyna-robotics-launches-dyna-2-1-physical-agent-a-semi-humanoid-robot-that-completes-full-workflows-such-as-a-commercial-laundry-shift-302892411.html)** (로봇 실기 데이터 없이 에고센트릭 인간 영상 100만+시간만으로 사전학습한 월드-액션 모델 + 세탁·호텔 하우스키핑·식음료 서빙 등 풀 워크플로우를 수행하는 세미휴머노이드 physical agent 실배포) | 🟡 Preview | ✨ **주목**: 로봇 실기 데이터 없이 사람 1인칭 영상만으로 사전학습한 월드-액션 모델(DYNA-2)을 소량 로봇 데이터 파인튜닝만으로 호텔·레스토랑·세탁소에 실배포된 세미휴머노이드(DYNA 2.1)로 연결 — "인간 데이터 → 로봇 스케일 법칙" 주장, Radar 🔬 World-action models 축에 데이터 파이프라인 관점(로봇-프리 사전학습)을 더하는 사례<br>⏳ **대기**: Dyna Robotics 공식 발표(PR Newswire, DYNA-2 2026-08-10 정정판·DYNA 2.1 2026-09-29) `[4]` — 성공률 20%→80~90%, DYNA-1 대비 1.55배, 고객 현장 87% vs 46% 전부 **자체 공표치, 고객 인용 금지**, 독립 검증·peer-review 없음. 모델 가중치·API 비공개(자사 운영 하드웨어로만 접근). ⚠️ 이번 실행 환경 egress 제한으로 prnewswire.com curl 200 수동 검증 미수행(커밋 메시지·이슈 참조). **AWS 각도: 없음(2025-09 Series A에 Amazon Industrial Innovation Fund가 투자자로만 참여, 인프라 파트너십 아님)** | 독립 성능 검증(3자 감사) + 실배포 고객사례 공개 확대 |
| **[Magic-W0](https://arxiv.org/abs/2609.39870)** (Magiclab Robotics, 3D 기하·모션·미래 시맨틱으로 구조화한 월드 표현과 행동 생성을 양방향 결합한 월드-액션 파운데이션 모델) | 🔵 Research | ✨ **주목**: 에고센트릭 인간 조작 영상·실로봇 궤적·시뮬 데이터로 대규모 사전학습해 RoboDojo-Sim 벤치마크 1위를 자체 주장 — Radar 🔬 World-action models 축(DreamZero→GR00T N2)에 코드 공개(GitHub)를 동반한 중국 로보틱스 스타트업 구현 사례 추가<br>⏳ **대기**: arXiv 프리프린트(2026-09-30 제출·v2 2026-10-03) `[4]` — RoboDojo-Sim·LIBERO 자체 벤치마크와 자체 실기 테스트 위주, peer-review·독립 재현 없음. 코드는 공개(MagiclabRobotics/Magic-W0)이나 학습 가중치 공개 여부 불명. ⚠️ 이번 실행 환경 egress 제한으로 arxiv.org·github.com curl 200 수동 검증 미수행(커밋 메시지·이슈 참조). **AWS 각도: 없음** | peer-review + 독립 재현 + 실기 배포 사례 |

## 종료·가입 제한 — 상태별 확인 { #-폐기됨--제안-금지-기록-보존용 }

| 항목 | 상태 | 대체 |
|---|---|---|
| **[AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)** | 신규 고객 가입 제한, 기존 고객 이용 가능 `[1]` | 신규 로봇 기본 옵션에서 제외 — [근거](evidence.md#fleetwise-new-customers) |
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 종료 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 종료 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 종료 (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 공개 사례 없음 `[4]` | 현재 CUDA/NVIDIA (제안 시 리스크 명시) |

> ⚠️ **루머 주의(사실 아님)**: "AWS IoT TwinMaker 폐기" 는 **오정보** — TwinMaker는 GA·신규 오픈(저속도). SiteWise 유지보수와 혼동한 3rd-party 블로그 주장. 반복 금지. → [pillar-3](pillar-3.md).

---

## 승격 절차 (요약)

1. **캡처**: 지정 채널/이모지로 후보 수집
2. **필터**: [수록 조건](maintenance.md#포함-기준-the-filter)을 모두 확인하고 출시·근거·용도·지원 범위를 분리한다.
3. **통과 시**: 담당 필러 owner가 [표준 템플릿](maintenance.md#표준-템플릿)으로 편입, Radar에서 제거
4. **미달 시**: 여기 한 줄로 유지, 승격 조건 명시

전체 파이프라인 → [maintenance](maintenance.md#playbook-승격-파이프라인).

---
_owner: Youngjin · updated: 2026-09 · volatility: 높음 (Radar는 본질적으로 빠르게 변함 — 월 단위 검토 권장)_

<!-- 용어 각주 -->

[^wfm]: **월드 파운데이션 모델(WFM, World Foundation Model)** — 물리 세계의 다음 장면을 예측·생성하도록 학습된 대형 모델. 텍스트·영상 프롬프트로 물리적으로 그럴듯한 영상·시나리오를 만들어 로봇 학습 데이터를 증강한다. 🎥 [NVIDIA Cosmos 소개](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **시스템 식별(SysID, System Identification)** — 실물 로봇의 물리 파라미터(마찰·질량·모터 응답)를 측정해 시뮬레이터를 실물에 맞게 보정하는 작업.
[^s2r]: **sim-to-real** — 시뮬레이션에서 학습한 정책을 실제 로봇으로 옮기는 것, 또는 그 방법론. 시뮬레이션과 현실의 물리·시각 차이(도메인 갭) 때문에 그냥 옮기면 성능이 무너진다. 🎥 [NVIDIA sim-to-real 로보틱스 쇼케이스](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **물리 엔진(physics engine)** — 강체 동역학·접촉·마찰·충돌을 수치적으로 계산하는 시뮬레이터의 핵심 소프트웨어. 엔진의 정확도·속도 트레이드오프가 시뮬레이터 선택(Isaac/MuJoCo/Genesis)을 좌우한다.
[^mcp]: **MCP (Model Context Protocol)** — 에이전트와 툴·데이터 소스를 잇는 개방형 표준 프로토콜. "에이전트용 USB-C"에 비유되며, 로봇 스킬을 MCP 서버로 노출하는 실험이 늘고 있다.
[^ros]: **ROS 2 (Robot Operating System 2)** — 로봇 소프트웨어의 사실상 표준 오픈소스 미들웨어. 센서·제어 노드들이 토픽(topic)으로 통신하는 분산 구조로, 산업·연구 로봇 스택의 공용 기반이다.
[^agent]: **LLM 에이전트** — 대형 언어 모델이 스스로 계획을 세우고 툴(API·로봇 스킬)을 골라 호출하며 다단계 작업을 수행하는 소프트웨어. 단순 질의응답과 달리 "행동"이 있다는 점이 핵심이다.
[^dext]: **덱스터리티(dexterity)** — 로봇 손·팔이 사람 손처럼 정교하고 섬세하게 물체를 다루는 능력. 단순 그리퍼의 집기·놓기와 달리, 5지 핸드로 물체를 돌리거나 도구를 조작하는 등 접촉이 많고 복잡한 조작을 뜻한다.
