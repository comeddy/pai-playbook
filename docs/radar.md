# Radar — 대기열 / 관찰 목록

_최종 갱신: 2026-07 · owner: comeddy · volatility: 높음_
[← index로](index.md)

> **L0 TL;DR**: 포함 기준([2.5 THE FILTER](maintenance.md#포함-기준-the-filter))을 아직 통과 못했지만 **지켜볼 것들**. 각 항목은 한 줄 — 성숙도 라벨 + **왜 대기 중인지**. 게이트(4개 중 2개)를 통과하면 담당 필러 owner가 표준 템플릿으로 승격한다.
>
> ⚠️ **여기 있는 항목을 고객 제안에 "성숙한 역량"처럼 쓰지 말 것.** 화려한 데모가 배포 가능성을 가리는 경우가 많다.

---

## 🔬 모델 / 알고리즘 (검증 대기)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| Physical Intelligence **π0.7** | 🔵 Research | 2차 출처만 `[4]`, PI 1차 확인 없음 | PI 공식 릴리스 + 성능 검증 |
| **GR00T N1.6 / N1.7 상업 라이선스** | 🟡→ | 상업 허용 주장이 2차 출처뿐 `[4]` (N1.5는 모델카드상 명백 비상업 `[1]`) | 라이브 모델 카드에서 라이선스 확정 |
| **World-action models** (DreamZero → GR00T N2) | 🟡 Preview | GR00T N2 "연말 예정", DreamZero는 연구 | GA + 실배포 사례 |
| Google DeepMind **Genie 3** (로봇 학습용 월드모델) | 🟡 Preview | 월드모델 자체는 프리뷰, 로봇 학습 적용은 연구 | 로봇 정책 학습 검증 사례 |
| **VLM 기반 SysID** (Vid2Sid, Swim2Real) | 🔵 Research | 2026 프리프린트, 단일 랩 | peer-review + 재현 |
| **VIRAL / VideoMimic / Real2Render2Real** (visual sim-to-real at scale) | 🔵 Research | CVPR/CoRL 연구, 프로덕션 아님 | 프로덕션 배포 증거 |
| **Robbyant LingBot-VLA / UnifoLM-VLA-0** | 🔵 Research | 2차 출처, 검증 없음 | 1차 확인 + AWS 매핑 |

## 🖥️ 시뮬레이션 / 도구 (성숙도 대기)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| **Genesis** 물리엔진 | ⚪ Hype | "430,000배" 반박됨 `[1]`, 접촉 조작서 느림 | 독립 벤치 + 프로덕션 채택 |
| **MuJoCo Warp** | 🟡 Alpha | PyPI classifier "3-Alpha" `[1]`, 프로덕션 아님 | Beta/GA 전환 |
| **NVIDIA Newton** 물리엔진 | 🟡 Preview | Isaac Sim 6.0서 experimental 백엔드 | GA + Isaac Lab 3.0 정식 |
| **Isaac Sim 6.0** | 🟡 Preview | "Early Developer Release", API 변동 (최신 GA는 5.1) | 6.x GA 선언 |
| **Cosmos 3 as sim-to-real 학습원** | 🟢 GA(모델)/🔵(실전) | 모델 GA지만 "월드모델 데이터로 실배포 정책 학습"은 얼리어답터만. ⚠️ **AWS 미호스팅** | AWS 매핑 강화 + 학습 검증 |

## 🤖 하드웨어 / 배포 (로드맵·데모)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | Musk 주장뿐, 생산 미시작 | 검증된 배포 |
| **Hyundai·BD 전기식 Atlas** | ⚪ 로드맵 | 전기식 Atlas 제품 버전 공개(2026-07, BD 공식 `[3]`). 배포 2.5만+대·양산능력 3만/년 모두 **2028 시작**, 현재 실가동 ~0. 2026은 소규모 파일럿만(현대 RMAC + Google DeepMind). ⚠️ "5세대"는 오칭 | 실가동 출하 시작 |
| **Apptronik Apollo 2 + Robot Park** | 🟡 파일럿 | Mercedes-Benz·GXO 운영 파일럿 `[3]` + Google DeepMind Gemini Robotics 데이터 파트너십(9만 sqft). 자율·상용 확산 미검증. AWS 매핑은 일반적(데이터→S3/SageMaker), 파트너십 자체는 Google `[4]` | 상용 배포 규모 + 자율 성과 검증 |
| **1X Neo** 자율성 | 🟡 Preview | 제품 출시했으나 자율 ~60~70%, 나머지 VR 원격조작 | 진짜 자율 검증 |
| **Figure 03 "8시간 자율 시프트"** | ⚪ Hype | CEO 트윗, 독립 검증 없음 (Figure 02@BMW는 검증 파일럿) | 3자 자율성 감사 |
| **Cosmos 3 채택** (Doosan/LG/Samsung) | 🟢 GA(발표) | 채택 "발표"지 프로덕션 검증 아님 | 프로덕션 사례 공개 |

## 🔗 에이전트 / 연결 (초기)

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| **MCP for robotics** (ros-mcp-server 등) | 🔵 Research | 50+ 서버 있으나 오픈소스/데모, 프로덕션 없음 (안전·지연·결정성 미검증) | 프로덕션 하드닝 사례 |
| **ROS 2 + LLM 에이전트** (NASA JPL ROSA, RAI) | 🔵 Research | ROSA(JPL)가 최강 실사례지만 mock-ops. 현장 배포 제한적 | 현장 프로덕션 배포 |
| **에이전트 물리안전 표준** (RoboGuard 등) | 🔵 Research | ISO는 물리만, LLM 의미 위험 표준 부재 | 표준화 진전 |
| **AgentCore Payments / Agent Registry (서울)** | 🟡 Preview/미제공 | 서울 리전 미제공 (도쿄 Agent Registry ✅) | 서울 리전 확장 |

## 🆕 최신 스캔 유입 (2026-07-26 · 1차 검증 완료 2026-07-21)

<!-- 자동 스캔(arXiv/웹) 유입분. 2026-07-21 1차 출처 검증 완료(검증 에이전트 4식, 공식 발표·arXiv 원문 대조) — 승격 0건, 정정 6건. THE FILTER 통과 전까지 고객 제안 사용 금지. 정기 갱신은 scripts/radar_scan.md 참고. -->

| 항목 | 라벨 | 왜 대기인가 | 승격 조건 |
|---|---|---|---|
| **RLWRLD RLDX-1** (손 dexterity 파운데이션 모델) | 🟡 Preview | 가중치 공개는 사실이나 ⚠️ "오픈소스" 아님 — RLWRLD Model License v1.0(비상업·상업 배포 금지) `[3]`, 7~9B 변형군(주력 8.1B). RoboCasa/LIBERO/SIMPLER SOTA는 자체 발표, 독립 재현 없음([aws-samples VLA Simulator](https://github.com/aws-samples/sample-vla-simulator-on-aws)가 EC2에서 n=5 스모크 실측 제공 — 완전한 벤치 재현은 아님). AWS 연계는 시뮬 벤치마킹 한정(비상업 라이선스가 명시 허용하는 용도, 상업 포지셔닝 불가) — "연계 근거 없음" 표기 갱신(2026-07). 실고객 배포 0 | 독립 벤치마크 재현 + 실배포 사례 |
| **NEURA Robotics × AWS 전략적 협력** | ⚪ Hype·로드맵 | 2026-04-21 AWS 공식 프레스 확인 `[1]` — AWS가 primary cloud, Neuraverse 호스팅 + NEURA Gym·SageMaker 연동 명시. 단 풀필먼트센터는 원문상 "배포 기회 탐색(explore)" 단계 — 실배포 0 | 실제 AWS 인프라 사용 사례 공개 + 풀필먼트 배포 검증 |
| **TACO** (Tactile World Model as Self-Corrector, VLA 후처리) | 🔵 Research | 실존 확인(arXiv 2607.02840, 2026-07-03) `[1]` — 4개 기관 공동("단일 랩" 표기 정정), Franka 실기 6개 태스크 절대 +44%p. peer-review 미채택 | peer-review + 독립 재현 |
| **MotionWAM** (실시간 휴머노이드 loco-manipulation용 Foundation World Action Model) | 🔵 Research | 실존 확인(arXiv 2606.09215, 2026-06-08) `[1]` — 3개 기관 공동("단일 랩" 표기 정정), Unitree G1 실기 9개 태스크 76.1%(GR00T-N1.7 대비 절대 +32%p). peer-review 미채택 | peer-review + 독립 재현 |
| **Kairos** (Regret-aware Native World-Action Model 스택) | 🔵 Research | 실존 확인(arXiv 2606.16533, 2026-06-15) `[1]`, 코드 공개. ⚠️ "풀스택"은 과장 — 실기 폐루프 검증 없음(저자 스스로 향후 과제로 인정), 시뮬·벤치마크 한정 | 실기 폐루프 검증 + 독립 재현 |
| **Actuator Reality Shaping** (zero-shot sim-to-real) | 🔵 Research | 실존 확인(arXiv 2607.02205, 2026-07-02) `[1]` — 실물 하드웨어 4종(휴머노이드 보행 포함) 검증, 요약·초록 일치(정정 없음). peer-review 미채택 | peer-review + 독립 재현 |
| **AgiBot 통산 1.5만 호기 + Longcheer 라인 배치** | 🟡 파일럿 | 누계 **양산 하선 1.5만 대**이며 15,000호기는 **고객 Longcheer 공장에 납품**("자사 공장" 표기 정정) + 품질검사 라인 1개에 G2 8대 `[3]`. 6일 데모 99.99%(작업 64,828회·생산 17,625개)는 사실이나 벤더 통제 환경, 독립 검증 없음; 데이터셋 라이선스는 [pillar-1](pillar-1.md) | 독립 생산성 검증 + 라인 확산 |
| **1X NEO 25-DoF 텐던 구동 핸드** | 🟡 예약 판매 | 핸드 사양(25-DoF·텐던·촉각 스킨) 공식 확인 `[3]`, "5일 1만 대 완판"은 1X 자체 주장·독립 검증 없음. **검증된 소비자 인도 0**($20k 또는 $499/월, 출하 2026 후반 계획) — 초기 가정 배치는 텔레옵 파일럿, 자율률은 1X 추정 60~70% | 실인도 검증 + 자율 매니퓰레이션 사례 |
| **Anthropic × Physical Intelligence 인수설** | ⚪ Hype·로드맵 | 2026-07-19 소셜 루머(Scoble 트윗) 확산 → The Information 보도로는 "2026년 봄 인수 논의는 있었다"는 정황이나 실제 인수는 아님, PI CEO Karol Hausman이 사내 Slack에서 부인 `[4]` — 2차 보도뿐, 당사자 1차 확인 없음. PI는 GCP 기반(pillar-2 참고)·OpenAI 투자사라 성사 시 클라우드·경쟁 지형에 영향 큼 | 당사자 공식 발표(거래 성사 또는 명시적 종결) 확인 |
| **AXIS** (커뮤니티 기반 성장형 로봇 매니퓰레이션 데이터 엔진) | 🔵 Research | 실존 확인(arXiv 2607.21588, 2026-07-23) `[4]` — 8개 대학 + Axis Robotics 공동, 브라우저 MuJoCo-WASM 텔레옵으로 크라우드소싱 후 IsaacSim 증강. Franka 시뮬레이션 전용(207 태스크·5만+ 궤적), π0.5 continual pretraining으로 LIBERO-Plus +4.9%p 보고(자체 벤치, 독립 재현 없음). sim-to-real은 저자 스스로 "향후 과제"로 명시 — 실기 미검증 | peer-review + 실기 sim-to-real 검증 |
| **AMD Ryzen AI Embedded X100 + Kria AI SoM** (로봇 엣지 컴퓨트, NVIDIA Jetson Thor 대항) | ⚪ Hype·로드맵 | AMD 공식 발표 `[4]`(2026-07-24) — Zen 5 CPU·RDNA 3.5 iGPU·XDNA 2 NPU 통합 메모리(최대 128GB), Jetson Thor 대비 FP32 3배·Intel 대비 멀티스레드 2.1배 주장(자체 벤치, 독립 검증 없음). SOM 양산은 2026 Q4 예정(Arbor/Congatec 등), 현재 로봇 엣지 배포 사례 0 | 독립 벤치마크 + 실제 로봇 엣지 배포 사례 |

## ⚰️ 폐기됨 — 제안 금지 (기록 보존용)

| 항목 | 상태 | 대체 |
|---|---|---|
| **AWS RoboMaker** | 🔴 종료 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **SageMaker Edge Manager** | 🔴 종료 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **IoT Greengrass V1** | 🔴 종료 (2026-06-01) `[1]` | Greengrass V2 |
| **Gazebo Classic 11** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
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
_owner: comeddy · updated: 2026-07 · volatility: 높음 (Radar는 본질적으로 빠르게 변함 — 월 단위 검토 권장)_
