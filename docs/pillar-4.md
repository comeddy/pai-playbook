# Pillar 4 — Sim-to-Real

_최종 갱신: 2026-07 · owner: Youngjin · volatility: 중간(엣지 HW·모델은 높음)_
_개별 항목은 별도 표기가 없는 한 페이지 메타데이터(owner/updated/volatility)를 상속. 항목별 owner 지정 시 항목 푸터 추가._
[← index로](index.md)

> **L0 TL;DR**: 정직한 한 줄 — **로코모션(보행)[^loco] sim-to-real[^s2r]은 사실상 풀렸고 배포됐다**(ANYmal, Agility Digit). **조작(manipulation)[^manip] sim-to-real은 아직 아니다** — 프런티어 VLA조차 시뮬레이션이 아니라 **실기체 데이터로 학습**하고, 시뮬레이션은 주로 평가/적응에 쓴다. 그리고 아키텍처 불변 법칙: **30~100Hz 실시간 제어는 반드시 엣지(온보드)**, 고수준 계획만 클라우드로.

---

## 이 필러에서 고객이 가장 자주 묻는 질문 Top 3

1. **"sim-to-real이 실제로 되나요? 검증된 사례가 있나요?"** → [로코모션(된다)](#2-로코모션-sim-to-real--검증됨-프로덕션), [조작(아직)](#4-조작-manipulation-sim-to-real--research---좁은-프로덕션)
2. **"실시간 제어인데 추론을 엣지에 둬야 하나요, 클라우드에 둬야 하나요?"** → [엣지 추론 배포](#1-엣지-추론-배포--ga), [decisions](decisions.md)
3. **"실기체 배포 전에 정책이 잘 되는지 어떻게 검증하죠?"** → [정책 평가](#5-정책-평가--배포-전-검증--research-미해결-문제)

> **안정 원리 (잘 안 바뀜)**: sim-to-real gap의 정체는 (1) **동역학[^dyn] 불일치**(시뮬 물리 ≠ 실물, 특히 접촉), (2) **시각 불일치**(렌더 ≠ 실카메라). 로코모션이 잘 되는 이유는 로봇+지면이라는 단순·관대한 동역학이고, 조작이 안 되는 이유는 접촉 동역학이 까다롭기 때문. 검증된 처방은 **선택적 도메인 랜덤화(DR)[^dr] + 시스템 식별(SysID)[^sysid] + RL을 MPC[^mpc] 위에 얹는 하이브리드**.

---

## 1. 엣지 추론 배포  🟢 GA

**L0 TL;DR**: 실시간 제어 추론은 로봇 온보드에서 돌려야 한다. 2026년 표준 경로 = **NVIDIA Jetson Thor(GA) + AWS IoT Greengrass V2 + ONNX[^onnx]/TensorRT**. ⚠️ **SageMaker Edge Manager는 2024-04 종료** — 대체 없다, ONNX+Greengrass로 간다.

**고객 니즈/문제**: "학습은 클라우드에서 했는데, 로봇에 어떻게 배포하고 OTA[^ota]로 관리하나? 실시간인데 클라우드 왕복은 안 되지 않나?"

**솔루션 개요** `[1]/[3]`:

- **엣지 HW**: **[Jetson](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/) Thor(Blackwell) GA**, T5000 프로덕션 모듈 유통. Jetson Orin 계열도 여전히 생산(저전력). 스펙·가격은 아래 접힌 블록.
- **배포/관리**: **[AWS IoT Greengrass V2](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)**(GA) — Lambda/Docker/커스텀 컴포넌트, ML 추론 컴포넌트, MQTT 텔레메트리. ⚠️ **Greengrass V1은 2026-06-01 지원 종료** — V2만 현행.
- **모델 경로**: PyTorch 정책 → **[ONNX](https://onnx.ai/)** → **[TensorRT](https://developer.nvidia.com/tensorrt)** 엔진 컴파일(온디바이스 가속)로 실시간 제어 지연 예산(sub-20~30ms급)[^latency]을 맞추는 것이 표준 경로. [SageMaker Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)(엣지 컴파일)는 존속하며 Greengrass와 조합.
- ⚠️ **SageMaker Edge Manager EOL(2024-04-26)** — 콘솔·API 전부 불가. **드롭인 매니지드 후속 서비스 없음**. AWS 권고 = ONNX + Greengrass V2 (+ 선택적 SageMaker Neo).

```mermaid
graph LR
    PT["PyTorch 정책<br>(클라우드 학습)"] --> ONNX[ONNX 변환]
    ONNX --> TRT["TensorRT 엔진<br>온디바이스 가속"]
    TRT --> JET["Jetson Thor<br>온보드 실시간 제어"]
    GG["AWS IoT Greengrass V2<br>OTA · 컴포넌트 · MQTT"] -. 배포 · 관리 .-> JET
    EM["SageMaker Edge Manager<br>2024-04 EOL"] -. x 후속 없음 .-> GG
```

<details markdown="1"><summary>🔄 휘발성 데이터 (엣지 HW 스펙·가격 — 2026-07 확인)</summary>

| 항목 | 값 | 출처 |
|---|---|---|
| Jetson Thor GA | 2025-08-25 발표, dev kit $3,499, 2025-11 출하 시작 | NVIDIA `[3]` |
| AGX Thor 스펙 | Blackwell GPU, 128GB 통합 LPDDR5X, 130W, FP4 지원 | NVIDIA `[3]` |
| Thor vs Orin | NVIDIA 공식: 정규화 AI 컴퓨트 ~7.5배, 에너지효율 ~3.5배. ⚠️ Thor=FP4/FP8 TFLOPS, Orin=INT8 TOPS — 원시 수치 직접 비교 금지 | NVIDIA `[3]` |
| ONNX→TensorRT 가속 | ~7배(벤더 수치, NVIDIA Jetson 블로그 2025, 모델·HW 의존 — 인용 시 조건 병기) | NVIDIA `[3]` |
</details>

**AWS 매핑**: IoT Greengrass V2 + IoT Core(MQTT) + SageMaker Neo(컴파일) + S3(모델 아티팩트) + IoT Jobs(OTA). Model Monitor로 엣지 텔레메트리 수집.

**의사결정 기준** (상세 → [decisions Cloud vs Edge](decisions.md)):

- **30~100Hz+ 반응형 제어**(균형·힘·파지·보행) → **반드시 온보드 Jetson**. 클라우드 왕복 불가.
- **sub-1Hz~few-Hz 고수준 계획·VLA 추론** → 클라우드/비동기 가능. **action chunking**이 두 rate를 잇는 다리.
- 매니지드 엣지 서비스 원함 → 없다고 정직히 말하고 ONNX+Greengrass V2 설계 제공.

**고객 사례**: (엣지 배포 자체의 공개 AWS 로봇 사례 제한적 — 참조 아키텍처 중심)

**➡️ 다음 액션**: **"Jetson Thor(온보드 제어) + Greengrass V2(OTA/관리) + ONNX→TensorRT" 엣지 참조 아키텍처를 그려주고**, "Edge Manager 없어졌다"는 점을 선제적으로 알려 고객의 잘못된 기대를 정정. 실시간 요구 Hz를 물어 엣지/클라우드 경계 확정.

**🔗 관련 자산**: [pillar-2 System1/System2](pillar-2.md) · [pillar-5 오케스트레이션](pillar-5.md) · [decisions](decisions.md)

---

## 2. 로코모션 Sim-to-Real  🟢 검증됨 (프로덕션)

**L0 TL;DR**: sim-to-real이 "된다"는 증거가 여기 있다. 사족보행(ANYmal)과 이족 물류로봇(Agility Digit)은 시뮬레이션에서 RL로 학습해 **실제 유료 산업 현장에 배포**됐다.

**고객 니즈/문제**: "sim-to-real이 마케팅 아니냐? 실제로 돈 받고 일하는 로봇이 있나?"

**솔루션 개요** `[1]/[3]`:

- **ANYmal ([ANYbotics](https://www.anybotics.com/anymal/))** 🟢 — 대규모 병렬 시뮬레이션 RL로 학습한 보행, **수백 대가 전 세계 산업 점검(석유·가스·광산·화학)에 배포**. ETH RL-walking 계보(peer-reviewed). **프로덕션 + 증거**.
- **[Agility Digit](https://agilityrobotics.com/robots) @ GXO** 🟢 — **다년 RaaS 계약 하에 유료 상업 작업**, 2025-11 기준 **10만+ 토트 이동**, ~1년 연속 풀타임, 6.5만+ 가동시간. **가장 잘 검증된 유료 휴머노이드 작업**(고객 GXO가 교차 확인). 단 좁은 구조화 토트 이동 태스크.
- ⚠️ **Boston Dynamics Spot은 제품에 MPC(고전 제어) 탑재 — RL 아님**. Spot의 RL 보행(5.2m/s)은 연구킷(BD+NVIDIA+RAI)에만 존재. **이 업계에서 가장 자주 틀리는 사실** — 반대로 말하지 말 것.

**AWS 매핑**: 학습(→[pillar-2](pillar-2.md), [pillar-3](pillar-3.md)) + 엣지 배포(→1번). 벤더별 인프라는 비공개.

**의사결정 기준**: 고객 유스케이스가 보행·이동(로코모션) → sim-to-real 성숙, 적극 제안 가능. 정밀 조작 → 신중(4번).

**고객 사례**: ANYmal(산업 점검, 프로덕션), Agility Digit@GXO(물류, 유료). ⚠️ **독립 3자 자율성 감사는 어떤 휴머노이드에도 없음** — 벤더/고객 PR 기준([3]).

**➡️ 다음 액션**: 고객이 sim-to-real 회의적이면 **ANYmal/Digit@GXO를 "된다"의 근거로, 단 "로코모션이라 된다"를 명확히**. Spot=MPC 사실을 정확히 알아 신뢰 확보.

**🔗 관련 자산**: [pillar-3 병렬 RL](pillar-3.md) · [pillar-2 학습](pillar-2.md)

<details markdown="1"><summary>🔄 휘발성 데이터 (휴머노이드 데모↔프로덕션 사다리 — 2026-07)</summary>

| 단계 | 사례 |
|---|---|
| 유료·검증 | ANYmal(사족, 수백 대), Agility Digit@GXO(10만+ 토트) |
| 프로덕션 파일럿(메트릭·자율, 벤더보고) | Figure 02@BMW(~1,250h, 9만+ 부품→Figure 03), Apptronik Apollo@Mercedes |
| 제품 출시했으나 자율 아님 | 1X Neo(자율 ~60~70%, 나머지 VR 원격조작 "Expert Mode") |
| 인상적 데모/연구 | Atlas 애자일 동작, Spot RL 연구킷(제품은 MPC), Unitree 애자일 스킬, Figure 03 "8시간 자율" 주장(CEO 트윗) |
| 발표·로드맵(0대 가동) | Hyundai Atlas 2.5만 대(2028, 노조 반대), Tesla Optimus V3 |
</details>

---

## 3. Sim-to-Real 방법론  🟢 GA (안정 원리)

**L0 TL;DR**: 검증된 처방은 화려한 신기법이 아니라 **선택적 DR + SysID + RL을 MPC 위에 얹는 하이브리드**다. 무작정 다 랜덤화하면 RL이 불안정해진다.

**고객 니즈/문제**: "sim-to-real gap을 실제로 어떻게 좁히나? 어떤 기법이 프로덕션에서 통하나?"

**솔루션 개요** `[1]/[3]`:

- **선택적 도메인 랜덤화(DR)** 🟢 — 로코모션 표준. 단 **과도한 랜덤화는 학습 불안정** → 선택적으로.
- **시스템 식별(SysID) + 선택적 DR** 🟢 — 핵심 동역학 파라미터를 실측 보정 후 선택적 DR. 현 베스트 프랙티스.
- **RL over MPC 하이브리드** 🟢 — 순수 end-to-end RL이 아니라 고전 MPC 베이스 + 학습 정책으로 강건화. **Boston Dynamics도 이 하이브리드 = 실제 배포에 가장 근접**.
- **연구 단계**(프로덕션 아님): 잔차 real2sim2real(ASAP), 분포적 SysID(Spot 연구), VLM 기반 SysID(Vid2Sid) — 🔵 인상적이나 단일 랩 데모.

```mermaid
graph LR
    SIM["시뮬레이션 RL 학습"] --> SID["SysID<br>핵심 동역학 실측 보정"]
    SID --> DR["선택적 도메인 랜덤화"]
    DR --> MPC["RL over MPC 하이브리드<br>고전 제어 + 학습 정책"]
    MPC --> VAL["실기체 소량 검증"]
    VAL --> DEP["프로덕션 배포<br>(로코모션 검증됨)"]
```

**AWS 매핑**: 방법론 자체는 클라우드 중립. 대규모 DR/SysID 스윕은 AWS Batch 병렬화(→[pillar-3](pillar-3.md)).

**의사결정 기준**: 로코모션 → DR+SysID+하이브리드 신뢰. 조작 → 이 처방만으론 부족, 실데이터 병행 필수(4번).

**고객 사례**: ANYmal·Digit(위 2번)이 이 방법론의 산물.

**➡️ 다음 액션**: 고객 팀이 "무작정 DR"로 헤매면 **"선택적 DR + SysID + MPC 하이브리드"** 로 방향 교정. 연구 신기법(ASAP 등)은 "연구단계"로 정직히 라벨.

**🔗 관련 자산**: [pillar-3 시뮬레이션](pillar-3.md)

---

## 4. 조작 (Manipulation) Sim-to-Real  🔵 Research / 🟡 좁은 프로덕션

**L0 TL;DR**: 정직한 나쁜 소식 — **일반 접촉 풍부 조작의 sim-to-real은 안 풀렸다**. 그래서 프런티어 VLA(OpenVLA, π0.5, Gemini Robotics)는 시뮬레이션이 아니라 **실기체 데이터**로 학습한다. 프로덕션은 좁은 저난도 로코-매니퓰레이션(토트/부품 이동)만.

**고객 니즈/문제**: "우리는 조립/파지 같은 조작이 필요하다. 시뮬레이션으로 학습해서 되나?"

**솔루션 개요** `[1]`:

- **왜 뒤처지나**: 조작은 **접촉 동역학 불일치**가 커서, 보고된 sim-to-real 성능 저하 ~24~30%, 조명/카메라 포즈 변화만으로 성공률 30~50% 하락.
- **핵심 통찰 — VLA는 실데이터에 의존**: **[OpenVLA](https://github.com/openvla/openvla)**(7B)는 ~97만 개 **실기체** 데모(Open X-Embodiment)로 학습. **π0/π0.5**, **RT-2**, **Gemini Robotics** 전부 대규모 **실로봇 데이터** 중심, 시뮬레이션은 평가/적응 보조. Gemini Robotics는 SDK에 MuJoCo를 평가용으로 번들.
- **성숙도**: 정밀·다지 접촉 조작, 오픈월드 VLA 가사(π0.5) → **인상적 데모/trusted-tester Preview**. **2026-07 기준 접촉 풍부 조작을 GA 프로덕션으로 검증한 범용 VLA는 없음**.

**AWS 매핑**: 실데이터 파이프라인이 관건 → [pillar-1](pillar-1.md). 시뮬레이션은 평가 보조(5번).

**의사결정 기준**:

- 좁은 구조화 파지·이동 → 가능(Digit급).
- 범용·정밀·접촉 풍부 조작 → **현재 미해결**, 실데이터 대량 수집 전제 + 기대치 관리.
- "시뮬레이션만으로 조작 정책" → 위험, 실데모 파인튜닝 필수.

**고객 사례**: 좁은 로코-매니퓰레이션(Digit, Figure 02)만 프로덕션. 정밀 조작은 연구/Preview.

**➡️ 다음 액션**: 조작 고객에겐 **기대치를 정직하게 관리** — "로코모션만큼 안 풀렸다, 실데이터가 핵심"을 먼저 말하고, [pillar-1 실데이터 파이프라인](pillar-1.md)으로 연결. 과약속 금지.

**🔗 관련 자산**: [pillar-1 텔레옵/실데이터](pillar-1.md) · [pillar-2 VLA 파인튜닝](pillar-2.md)

---

## 5. 정책 평가 — 배포 전 검증  🔵 Research (미해결 문제)

**L0 TL;DR**: 불편한 진실 — **어떤 시뮬레이션 평가 스위트도 실배포 게이트로 신뢰받지 못한다**. 인기 벤치마크(LIBERO/SimplerEnv/CALVIN)가 shortcut·과적합·통계적 무의미 문제를 드러냈다. 현재 방향은 real-to-sim 재구성 + 분산 실세계 A/B.

**고객 니즈/문제**: "실기체에 올리기 전에 정책이 진짜 잘 되는지 어떻게 확신하나?"

**솔루션 개요** `[1]`:

- **sim 평가 스위트**: SimplerEnv, LIBERO, Meta-World 등 존재하나 한계 노출. 2026-06 감사: 언어 인코더 없는 90M 프로브가 LIBERO 3/4에서 SOTA 매칭(shortcut), 보고된 "진보"의 ~20%만 통계적 입증, CALVIN은 배치 포즈 리샘플만으로 25% 하락. **sim↔real 상관 낮음**.
- **실세계 평가**: **[RoboArena](https://robo-arena.github.io/)** — 분산 이중맹검 A/B(정책 IP만 주고 정체 숨김), 7기관 4,284 에피소드, Bradley-Terry/Elo. 연구 프레임워크지만 방향 제시.
- **신방향**: real-to-sim(Gaussian Splatting/월드모델 씬 재구성) + 분산 실 A/B. 단일 sim 스위트 = 신뢰 게이트 아님.

**AWS 매핑**: 대규모 평가 스윕 병렬화 → AWS Batch. 실세계 A/B 데이터 수집 → IoT/S3. (매니지드 로봇 평가 서비스는 없음)

**의사결정 기준**: sim 벤치 점수만으로 배포 결정 금지. **sim 스크리닝 + 실세계 단계적 검증** 병행. 벤치 점수 인용 시 통계적 유의성·측정조건 확인.

**고객 사례**: (평가 자체는 연구 영역)

**➡️ 다음 액션**: 고객이 "sim에서 95% 나왔으니 배포" 하려 하면 **"sim↔real 상관이 낮다는 최신 연구"를 근거로 단계적 실세계 검증을 설계**하도록 조언. 이 정직함이 사고를 막는다.

**🔗 관련 자산**: [pillar-3 시뮬레이션](pillar-3.md) · [pillar-1 실데이터](pillar-1.md)

---

## 이 필러의 정직한 현실 (SA 필독)

- **로코모션은 된다, 조작은 아직이다.** 이 한 문장이 sim-to-real 대화의 뼈대. 과약속은 신뢰를 잃는다.
- **Spot = MPC, RL 아님.** 이 업계 최다 오류. 반대로 말하면 전문성 의심받는다.
- **프런티어 VLA는 실데이터로 학습**, 시뮬레이션은 평가/적응 보조 — "시뮬레이션만으로 조작 정책"은 함정.
- **SageMaker Edge Manager 죽음(2024-04)**, 후속 없음 → ONNX + Greengrass V2. **Greengrass V1도 2026-06 종료**, V2만 현행.
- **30~100Hz 제어는 반드시 엣지.** action chunking이 클라우드 계획과 엣지 제어를 잇는 다리.
- **휴머노이드 "프로덕션" 지표는 대부분 벤더 PR** — 독립 자율성 감사 없음. Digit@GXO·Figure@BMW만 고객 교차확인. 1X Neo는 "제품이지만 실제론 원격조작".

---
_owner: Youngjin · updated: 2026-07 · volatility: 중간 (엣지 HW·벤더 지표는 높음) · sources: [1] 공식/논문, [2] AWS 내부 검증, [3] 벤더/PR, [4] 미검증. 2026 arXiv 프리프린트는 비심사(illustrative)._

<!-- 용어 각주 -->

[^s2r]: **sim-to-real** — 시뮬레이션에서 학습한 정책을 실제 로봇으로 옮기는 것, 또는 그 방법론. 시뮬레이션과 현실의 물리·시각 차이(도메인 갭) 때문에 그냥 옮기면 성능이 무너진다. 🎥 [NVIDIA sim-to-real 로보틱스 쇼케이스](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^loco]: **로코모션(locomotion)** — 보행·주행 등 로봇이 이동하는 능력. 로봇과 지면의 접촉이라는 상대적으로 단순한 물리 덕분에 sim-to-real이 가장 먼저 풀린 영역이다.
[^manip]: **매니퓰레이션(manipulation, 조작)** — 물체를 집고 옮기고 조립하는 능력. 손끝 접촉의 물리가 복잡해 sim-to-real이 아직 풀리지 않은 영역이다.
[^dyn]: **동역학(dynamics)** — 힘·마찰·충돌이 만드는 운동의 물리. 특히 물체를 쥘 때의 접촉 동역학은 시뮬레이터가 정확히 재현하기 가장 어려운 부분이다.
[^dr]: **도메인 랜덤화(Domain Randomization)** — 시뮬레이션의 조명·질감·물체 위치·카메라 각도·물리 파라미터를 무작위로 바꿔가며 데이터를 생성·학습시키는 기법. 정책이 어떤 환경 변화에도 견디게 만든다 — sim-to-real의 대표 처방.
[^sysid]: **시스템 식별(SysID, System Identification)** — 실물 로봇의 물리 파라미터(마찰·질량·모터 응답)를 측정해 시뮬레이터를 실물에 맞게 보정하는 작업.
[^mpc]: **MPC (Model Predictive Control)** — 짧은 미래를 반복 예측·최적화하며 제어하는 고전 제어 기법. 학습된 RL 정책을 MPC 위에 얹는 하이브리드가 검증된 처방으로 자리 잡았다.
[^onnx]: **ONNX / TensorRT** — ONNX는 프레임워크 간 모델 교환 표준 포맷, TensorRT는 NVIDIA GPU용 추론 최적화 컴파일러. "PyTorch → ONNX → TensorRT" 변환이 엣지 실시간 추론의 표준 경로다.
[^ota]: **OTA (Over-The-Air)** — 네트워크로 원격에서 로봇의 모델·소프트웨어를 갱신·배포하는 방식.
[^latency]: **지연 예산(latency budget)** — 실시간 제어 루프가 허용하는 최대 추론 시간. 30~100Hz 제어면 한 사이클이 10~33ms이므로, 추론이 이 안에 끝나야 한다 — 클라우드 왕복이 불가능한 이유다.
