# Radar — 대기열 / 관찰 목록

_최종 갱신: 2026-07 · owner: 미정 ⚠️ · volatility: 높음_
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
| **Hyundai 25,000 Atlas** | ⚪ 로드맵 | 2028 시작 목표, 0대 가동, 노조 반대 | 실가동 시작 |
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

전체 파이프라인 → [maintenance](maintenance.md#슬랙--playbook-승격-파이프라인).

---
_owner: 미정 ⚠️ · updated: 2026-07 · volatility: 높음 (Radar는 본질적으로 빠르게 변함 — 월 단위 검토 권장)_
