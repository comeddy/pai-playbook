# Pillar 5 — 에이전트 오케스트레이션 (Agentic Orchestration)

_최종 갱신: 2026-09 · owner: Youngjin · volatility: 높음(AgentCore 기능·리전 자주 확장)_
_개별 항목은 별도 표기가 없는 한 페이지 메타데이터(owner/updated/volatility)를 상속. 항목별 owner 지정 시 항목 푸터 추가._
[← index로](index.md)

> **L0 TL;DR**: 업무 계획·로봇 스킬 호출·플릿 연결의 요구를 구분한다. AgentCore는 필요한 에이전트 기능에 선택적으로 사용하며, 로봇 제어·안전과 데이터 처리 위치는 [별도 검증](operations.md)이 필요하다.

---

> **검토 범위**: 페이지 수정일은 모든 기술 항목의 재검증일이 아니다. 핵심 정정의 확인일·재현/사람 검토 상태는 [근거 기록](evidence.md)에 있으며, 기존 항목의 개별 확인일은 그대로 적용한다.

## 이 필러에서 고객이 가장 자주 묻는 질문 Top 3

> 질문은 탐색용 예시다. 실제 문의 빈도 순위로 검증되지 않았다.

1. **"LLM 에이전트로 로봇/설비를 지휘하는 게 실제로 되나요? AWS엔 뭐가 있죠?"** → [Bedrock AgentCore](#1-amazon-bedrock-agentcore--ga)
2. **"실시간 로봇에 에이전트를 어떻게? 엣지에서 오프라인으로도?"** → [엣지 에이전트 오케스트레이션](#3-엣지-에이전트-오케스트레이션--preview-참조-아키텍처)
3. **"에이전트가 물리 시스템을 제어할 때 안전은 어떻게 보장하죠?"** → [안전 & 가드레일](#5-안전--가드레일--ga-에이전트층---미해결-물리-의미-갭)

> **L0/L1**: 업무 계획, 관측 기반 정책, 저수준 제어, 독립 안전은 서로 다른 책임이다. 서비스 출시 상태와 고객 현장의 검증 수준을 구분한다.

---

## 1. Amazon Bedrock AgentCore  🟢 GA

**L0 TL;DR**: AgentCore는 에이전트 실행·툴 접근·권한·관측을 위한 서비스다. **서비스 GA와 로봇 현장의 검증, 서울 제공과 국내 데이터 처리를 구분**한다.

| 구성 | 로봇 워크로드에서 검토할 역할 | 한계 |
|---|---|---|
| Runtime | 업무 계획 에이전트 실행 | 로봇 제어 기한을 보장하는 실시간 제어기 아님 |
| Gateway·Identity | 허용된 로봇 스킬 API 연결·인증 | 장치 동작 완료·취소·중복 처리는 별도 구현 |
| Policy | Gateway를 통한 툴 호출의 정책 검사 | 물리 상태 확인·독립 안전 기능 대체 불가 |
| Memory·Evaluations | 맥락 저장·평가 | 저장 위치와 추론 처리 위치를 각각 확인 |
| Observability | 업무 실행·툴 호출 추적 | 장치·제어·안전 로그와 연결 필요 |

**리전·데이터 처리 정정** `[1]`: 서울에서 서비스를 사용할 수 있다는 사실만으로 데이터 레지던시 문제가 해소되지 않는다. [AWS 교차 리전 추론 문서](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html)는 Memory 등의 입력·출력이 기본 리전 밖에서 처리될 수 있음을 명시한다. 서울발 Evaluations는 글로벌 교차 리전 추론 대상이다. 기능·모델·외부 툴별 처리 국가를 기록한다([근거](evidence.md#agentcore-residency)).

**의사결정 기준**: 단발 추론은 직접 모델 호출부터 검토한다. 지속 세션·툴 권한·관측이 필요할 때 AgentCore 구성요소를 선택한다. 사용 기능의 [리전 표](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)와 [가격](https://aws.amazon.com/bedrock/agentcore/pricing/)을 확인하고 모델/API·네트워크·로그 요금까지 견적한다. ‘하네스 무료’로 전체 비용을 설명하지 않는다.

**고객 사례**: 기존 AWS×SoftServe 소개는 데모/쇼케이스이며 고객 생산라인 운영을 입증하지 않는다.

**➡️ 다음 액션**: 로봇 스킬의 입력·권한·완료·취소 계약과 데이터 처리 경로를 정의하고 [운영·복구 시험](operations.md)을 연결한다.

**🔗 관련 자산**:

- 플레이북: [pillar-4 엣지](pillar-4.md)
- [AgentCore 시작 워크숍](https://catalog.workshops.aws/agentcore-getting-started/en-US) · [AgentCore Deep Dive 워크숍](https://catalog.workshops.aws/agentcore-deep-dive/en-US)
- [AgentCore 리테일 에이전트 워크숍 "Build! Deploy! Observe!"](https://catalog.us-east-1.prod.workshops.aws/workshops/3cab1e1f-1dfa-42e0-959c-6e2e0a072ea3/ko-KR) — 한국어. 리테일 도메인 예제지만 AgentCore 7개 서비스(Gateway·Runtime·Observability·Code Interpreter·Memory·Policy·Browser) 전부를 3단계 핸즈온으로 커버 — Policy 가드레일·에스컬레이션 실습은 5번(안전 & 가드레일)의 접점. 가이드: [워크숍 사이트](https://dxdbmmdwak6t8.cloudfront.net/) (이벤트용 CloudFront 배포 — 링크 지속성 확인 필요 ⚠️)
- (사내 AgentCore 워크숍 — 확인 필요 ⚠️)
- [AWS Physical AI Toolchain](https://github.com/aws-samples/sample-aws-physical-ai-toolchain) — aws-samples. 4-필러 플라이휠 참조 아키텍처. ⚠️ 현재 NVIDIA OSMO 6.3 on EKS 오케스트레이션만 Available, Cosmos·Isaac Lab·GR00T·Strands+AgentCore 에이전틱 레이어는 Planned
- [Self-improving Physical AI](https://github.com/aws-samples/sample-self-improving-physical-AI) — aws-samples. Bedrock 에이전트가 Isaac Sim·실기 SO-ARM101/XGO2/Zumi를 IoT로 제어, 에이전트 메모리로 sim-to-real 반복 학습
- [Agentic AI Robot — 산업 안전 모니터링](https://github.com/aws-samples/sample-agentic-ai-robot) — aws-samples. AgentCore+IoT+로봇 자율 순찰·엣지 추론 데모, AWS AI x Industry Week 2025 시연, 한국어 README. ⚠️ 실험·교육용 명시 — 프로덕션 아님
- [Smart Machines — 산업 장비 하이브리드 Physical AI](https://github.com/aws-samples/sample-smart-machines-physical-hybrid-ai) — aws-samples. 에이전트가 플릿 텔레메트리 이상 감지→원인 진단→티켓 생성·파라미터 조정까지 수행하는 풀스택 데모(멀티에이전트 챗·자연어 시나리오 빌더·KVS 영상→Bedrock 분석·Jetson YOLOWorld+VLM 엣지 모니터링). ⚠️ README 명시 데모 — 현재 굴착기(시뮬 텔레메트리)만 완동, 로봇 암은 WIP

---

## 2. 업무 계획과 로봇 제어의 분리 { #2-system-2--system-1-오케스트레이션-패턴--ga-안정-원리 }

**L0 TL;DR**: 업무 계획 에이전트와 로봇 실행·제어·안전을 나누되, 모델 내부 System 1/2와 같은 구분으로 취급하지 않는다.

**배치 기준**: 클라우드에서 허용할 지연·단절 시간·처리 국가를 먼저 정한다. 로봇의 관측 기반 정책, 로컬 제어, 독립 안전 기능은 해당 기한과 위험 평가에 따라 배치한다. Helix의 두 모델이 모두 온보드라는 점은 [P2](pillar-2.md)와 [근거 기록](evidence.md#action-chunking)을 참조한다.

**AWS 매핑**: AgentCore는 조건을 충족하는 업무 계획의 선택지다. 로봇 스킬 호출에는 ID·만료·사전 조건·완료 확인이 필요하며 action chunking만으로 네트워크 지연과 안전 문제가 해결되지는 않는다.

**➡️ 다음 액션**: [운영·복구](operations.md)의 네 계층 그림과 장애 시험 표를 사용해 책임자·취소·복구를 설계한다.

**🔗 관련 자산**: [pillar-2 VLA 구조](pillar-2.md) · [pillar-4 엣지](pillar-4.md) · [decisions](decisions.md)

---

## 3. 엣지 에이전트 오케스트레이션  🟡 Preview (참조 아키텍처)

**L0 TL;DR**: 오프라인·저지연 현장에서 에이전트를 엣지 디바이스에 배포하는 패턴. AWS **Solutions Guidance("AI Agents to Device Fleets via IoT Greengrass")** 가 실제 참조 아키텍처 — 단 **GA 제품이 아니라 가이던스/샘플코드**.

**고객 니즈/문제**: "공장이 오프라인/저대역이다. 클라우드 없이도 에이전트가 현장에서 판단하게 하고 싶다."

**솔루션 개요** `[1]/[3]`: AWS Guidance = **[IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) 디바이스에 Strands Agents + 로컬 SLM([Ollama](https://ollama.com/))** 배포. GGUF 모델을 S3로 푸시, IoT Core MQTT로 질의, Orchestrator Agent가 전문 에이전트(문서·OPC-UA 등)로 팬아웃. 연결되면 Bedrock 클라우드 모델로 전환. 대상 산업에 **로보틱스** 명시. 2026 패턴: 학습 모델 → Jetson Thor에 Greengrass로 배포, VDA 5050 프로토콜 변환으로 AMR 플릿 조율.

**AWS 매핑**: IoT Greengrass V2 + Strands + 로컬 SLM(Ollama) + IoT Core(MQTT) + S3(모델). 온라인 시 Bedrock/AgentCore로 승격.

**의사결정 기준**: 오프라인·데이터 주권·저지연 → 엣지 에이전트. 항상 연결·복잡 추론 → 클라우드 AgentCore.

**고객 사례**: AWS×SoftServe(위 1번, 데모).

**➡️ 다음 액션**: 오프라인 고객에게 **AWS Greengrass 에이전트 Guidance + 샘플코드를 출발점으로** 제시(GA 제품 아님을 정직히). 온/오프라인 하이브리드(엣지 SLM ↔ 클라우드 AgentCore) 설계.

**🔗 관련 자산**: [pillar-4 엣지 배포](pillar-4.md) · [pillar-1](pillar-1.md) · [MCP+MQTT on AWS IoT Core 패턴](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/) — 공식 블로그. 로봇·엣지 장비를 MCP 툴처럼 다루는 Physical AI 에이전트를 IoT Core(MQTT) 위에 엮는 실전 패턴 — 엣지 운영(P4)과 다수 장비 조율(P5)을 잇는 현행 표준 경로

---

## 4. 플릿 운영 — 제품·제어·클라우드의 경계 { #4-플릿-오케스트레이션--ga-일부--mixed }

**L0 TL;DR**: 현장 플릿의 작업 할당·교통 조율, 장치 운영, 개발 잡 스케줄링은 다른 문제다. 요구에 맞는 기존 플릿 제품·SI·자체 로직을 비교한다.

**참조 범위**: [Amazon DeepFleet](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model)은 Amazon 내부 로봇 조율 사례이며 고객이 구매하는 AgentCore 기능이 아니다 `[3]`. [NVIDIA OSMO](https://developer.nvidia.com/osmo)는 개발·데이터·학습 워크로드용으로 현장 교통 제어와 구분한다.

**AWS 매핑**: IoT Core/Greengrass 연결과 상태 수집, 필요한 저장·분석을 설계한다. 업무 계획에 에이전트가 필요한 경우에만 AgentCore를 검토한다. 경로 충돌·작업 할당·오프라인 복구는 로봇/플릿 솔루션이 담당할 범위를 명시한다.

**FleetWise 정정** `[1]`: [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)는 **신규 고객을 받지 않는다**. 기존 고객은 계속 사용할 수 있지만 신규 로봇 아키텍처의 기본 서비스로 제안하지 않는다([근거](evidence.md#fleetwise-new-customers)).

**고객 사례**: [Certis 순찰 로봇](https://aws.amazon.com/blogs/physical-ai/how-certis-achieved-autonomous-robot-security-patrols-with-aws/)은 공개 AWS 사례다. 다른 고객에게 같은 효과를 보장하지 않는다.

**➡️ 다음 액션**: 기존 플릿 솔루션과의 기능 경계, 작업 완료·단절·사람 개입·복구 요구를 [파일럿 카드](start.md#pilot)에 적고 [운영 시험](operations.md#failure)을 수행한다.

**🔗 관련 자산**: [pillar-2 학습](pillar-2.md) · [pillar-3 OSMO](pillar-3.md)

---

## 5. 안전 & 가드레일  🟢 GA (에이전트층) / 🔵 미해결 (물리-의미 갭)

**L0 TL;DR**: 에이전트가 물리 시스템을 제어할 때 안전은 **계층 방어**로. **AgentCore Policy(Cedar)가 에이전트→툴 호출을 게이팅**하고, 로봇층은 **ISO 결정적 안전 계층**이 맡는다. ⚠️ 현존 표준(ISO)은 물리 안전만 다루고 **LLM 의미적 위험(환각·탈옥)을 커버하는 표준은 아직 없다** — 정직한 열린 문제.

**고객 니즈/문제**: "에이전트가 잘못 판단해서 로봇이 위험 행동을 하면? 어떻게 막나?"

**솔루션 개요** `[1]/[4]`:

- **에이전트층(AWS 네이티브)**: **AgentCore Policy** — Gateway를 통과하는 에이전트→툴 호출을 Cedar로 실시간 allow/deny(ms). 물리 액션 툴 호출을 제약하는 실용 계층. **[Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)** — LLM 입출력(콘텐츠·주제·PII) 필터(액추에이션 자체는 아님).
- **로봇층(기능 안전)**: **[ISO 10218-1/2](https://www.iso.org/standard/73933.html)**(로봇·통합시스템), **ISO/TS 15066**(협동로봇), **ISO 13482**(개인지원로봇). ⚠️ 이들은 **물리 안전만** — LLM 의미적 악용/환각은 미커버.
- **연구**: RoboGuard(안전규칙 grounding), BadRobot(임베디드 LLM 탈옥 공격), LLM 의미적 DoS — 🔵 연구단계. 표준이 기능안전(ISO)과 LLM 위험을 잇지 못하는 **열린 갭**.

**AWS 매핑**: AgentCore Policy(Cedar) + Bedrock Guardrails(에이전트층) + 로봇 온보드 결정적 안전(ISO 준거, AWS 밖).

**의사결정 기준**: 물리 액션 에이전트 → **반드시 계층 방어**(AgentCore Policy로 툴 게이팅 + 로봇 온보드 ISO 안전 계층). 어느 한쪽만으론 불충분. "에이전트가 알아서 안전"은 금지.

**고객 사례**: (프로덕션 안전 사례는 비공개/초기)

**➡️ 다음 액션**: 안전 질문에 **"에이전트층은 AgentCore Policy/Cedar로 툴 호출 게이팅, 로봇층은 ISO 결정적 안전 — 이중 방어"** 를 제시. "LLM 의미 위험 표준은 아직 없다"는 정직히 인정하고 계층 방어로 보완하는 각도.

**🔗 관련 자산**: [pillar-4 엣지](pillar-4.md) · (사내 에이전트 안전 가이드 — 신규 필요 ⚠️)

---

## 6. 물리 세계의 에이전트 표준 — Anthropic MHS & AWS Strands Robots  🟡 Research Preview

**L0 TL;DR**: 2026-08-27 Anthropic이 **[Model Hardware Standard(MHS)](https://www.anthropic.com/news/model-hardware-standard-research-preview)** research preview를 공개 — AI 에이전트가 물리 장치(현미경·liquid handler·로봇 팔)를 **표준화된 드라이버(read/write primitive)**로 조작하고 다중 장치를 병렬 오케스트레이션하게 하는 공유 규격이다. MCP가 데이터·툴에 한 일의 하드웨어 짝. **AWS는 Strands Robots로 MHS를 지원**(preview 참가자 대상 private pre-release), **Doosan Robotics(한국)가 런치 파트너**. ⚠️ research preview — 고객 프로덕션 제안 금지, 방향 지표로만.

**고객 니즈/문제**: "장치마다 맞춤 통합(주~개월)을 반복하고 있다. 에이전트-하드웨어 연결에 표준은 없나?"

**솔루션 개요** `[1]/[3]`:

- **동작 방식**: 장치를 read(예: get temperature)/write(set temperature) primitive 집합으로 노출하는 **표준 드라이버** + 자연어 태그로 생성되는 reference file(그 장치의 측정·조정 가능 항목과 **강제되는 안전 한계(safety limits)** 기재). 에이전트는 3가지 메커니즘(MCP·CLI·code files/API)으로 장치를 제어하고, 순서를 짜고 결과를 관측해 실시간으로 파라미터를 조정한다. model-agnostic — 통합 기간이 주~개월에서 시간~분으로 준다는 것이 핵심 주장.
- **AWS의 자리**: Anthropic 발표문이 "AWS will support MHS through **Strands Robots**, the library for connecting AI agents to physical devices"를 명시. 공개 [strands-labs/robots](https://github.com/strands-labs/robots)(Apache-2.0 — Strands Agents + GR00T VLA + LeRobot 통합 로봇 제어 라이브러리)와 이어지지만, ⚠️ **공개 패키지 자체는 MHS를 언급하지 않는다** — MHS 지원 빌드는 별도의 private pre-release다.
- **한국 관련성** `[3]`: Doosan Robotics가 런치 파트너로 로봇 팔 자동 품질검사(QA)·다중 로봇 협조에 MHS를 테스트 중(Universal Robots·Tecan·QIAGEN 등과 함께).
- **정직한 한계**: LLM은 물리 세계를 텍스트·이미지로 배우므로 **공간·물리 추론에는 전문가 감독이 여전히 필요** — Anthropic 스스로, Genentech 연구진이 "시료의 foaming은 소프트웨어 버그가 아니라 물리적 실패"임을 Claude에게 가르쳐야 했던 예를 든다. 오픈소스화 예정.

**AWS 매핑**: AgentCore(1번)가 에이전트 런타임·Policy 게이트를, MHS/Strands Robots가 장치 연결 표준을 맡는 그림 — 5번 계층 방어의 "툴 게이트" 아래에 **"장치 드라이버 + safety limits"** 층이 하나 더 생기는 셈이다.

**의사결정 기준**: 오늘 설계에 넣을 단계가 아니다(research preview). 다만 장치 통합 백로그가 큰 고객(랩 자동화·다품종 셀)에겐 **워칭 리스트 1순위**로 안내.

**고객 사례**: Doosan Robotics(런치 파트너, 테스트 단계) `[3]`.

**➡️ 다음 액션**: MCP를 이미 쓰는 고객에게 **"MCP는 데이터·툴, MHS는 하드웨어"** 프레임으로 소개하고, 공개되면 Strands Robots 경로로 검증 PoC를 잡는다. 그 전까지의 현행 대안은 [MCP+MQTT on IoT Core 패턴](https://aws.amazon.com/blogs/physical-ai/building-physical-ai-agents-with-mcp-and-mqtt-on-aws-iot-core/)(3번 관련 자산).

**🔗 관련 자산**: [strands-labs/robots](https://github.com/strands-labs/robots) · [pillar-4 엣지](pillar-4.md)

---

## 이 필러의 정직한 현실 (SA 필독)

- **서울 제공과 데이터 처리 위치를 구분한다.** 기능·모델·경로별로 [교차 리전 추론](evidence.md#agentcore-residency)을 확인한다.
- **Policy는 GA(2026-03)** — "프리뷰"라 부르지 말 것.
- **DeepFleet ≠ LLM 에이전트 오케스트레이터.** 창고 로봇 조율 파운데이션 모델(멀티로봇 RL). 오분류 금지.
- **진짜 프로덕션은 플릿 조율(DeepFleet/CoEvolution)과 개발 워크로드(OSMO).** MCP-로봇 연결과 휴머노이드 풀스택 에이전트는 대부분 연구/데모.
- **LLM 의미적 안전 표준은 없다.** ISO는 물리만. 계층 방어(Cedar Policy + ISO 로봇층)가 정직한 답.
- **Lotte 30% 등 국내 수치는 단일 출처** — 하드 인용 전 재확인.

---
_owner: Youngjin · updated: 2026-09 · volatility: 높음 (AgentCore 기능·리전은 접힌 블록에서 관리) · sources: [1] 공식, [3] 벤더/press, [4] 연구/커뮤니티_

<!-- 용어 각주 -->
