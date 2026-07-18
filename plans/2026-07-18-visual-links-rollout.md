# 가독성 롤아웃 구현 계획 (pillar-1/2/4/5)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 파일럿(pillar-3)에서 승인된 패턴 — Mermaid 다이어그램 2~3개 + 선별 공식 링크 — 을 pillar-1/2/4/5 × 4개 언어에 적용하고 배포한다.

**Architecture:** 필러당 1개 태스크(ko 설계·적용 + 번역 3개 동기화 + 게이트 + 커밋)로 4개 태스크, 마지막에 배포·라이브 검증 1개. 각 태스크는 독립적이라 순차 실행하며 개별 리뷰를 거친다. 참조 구현은 `docs/pillar-3.md`(다이어그램 스타일)와 `docs/pillar-3.en.md`(번역 규칙).

**Tech Stack:** 기존 mermaid fence(구축 완료), i18n 파이프라인, glossary §3 mermaid 규칙

**Spec:** `specs/2026-07-18-visual-links-rollout-design.md`

## Global Constraints

- 다이어그램 페이지당 **2~3개**, 링크 페이지당 **6~10곳**(첫 등장 1곳씩, 공식 출처, 사전 curl 검증 — 200 아니면 대체/제외하고 report 확정표 기록)
- 노드 ID·방향(LR/TD)·화살표·`<br>`·이모지는 4개 언어 동일, **라벨만 번역**, 제품명 번역 금지 (`i18n/glossary.md` §3 mermaid 규칙)
- **콘텐츠 불변**: 기존 문장 수정·삭제 금지 — 펜스 삽입(앞뒤 빈 줄)과 링크 마크업 래핑만
- 게이트(태스크마다): `check_staleness.py --check` exit 0 · sync **0/30** · strict exit 0 · 언어당 mermaid 수 일치
- 커밋 메시지 한국어 + `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` 푸터

---

### Task 1: pillar-1 (데이터 수집 & 처리)

**Files:** Modify: `docs/pillar-1.md`, `docs/pillar-1.{en,zh,ja}.md`

- [ ] **Step 1: ko 본문 읽고 다이어그램 2~3개 설계·삽입** — 스펙 후보 주제: ① 데이터 3원천(텔레옵·오픈 데이터셋·합성)→S3→학습 파이프라인 (graph LR) ② 오픈 데이터셋 라이선스 분기(OXE 컴포넌트별/DROID CC-BY/AgiBot 비상업) (graph TD) ③ 선택: SDG 파이프라인. 실제 본문 구조에 맞춰 확정하고 이탈 시 report에 근거. 스타일은 `docs/pillar-3.md`의 3개 참조(노드 5~8개, 라벨 간결).
- [ ] **Step 2: 링크 후보 본문 스캔 → curl 전수 검증 → 첫 등장에 적용** — 후보 예: Open X-Embodiment(arXiv/GitHub), DROID(droid-dataset.github.io), LeRobot(GitHub), Isaac Sim Replicator(NVIDIA docs), Cosmos(이미 pillar-3에 링크했지만 페이지별 첫 등장은 독립 — pillar-1 첫 등장에 적용 가능). 6~10곳, 확정표 report 기록.
- [ ] **Step 3: 번역 3개 동기화** — 같은 위치·구조로 삽입, 라벨 번역, URL 동일, ko_hash 갱신 (`--hash docs/pillar-1.md`).
- [ ] **Step 4: 게이트** — staleness exit 0 · sync 0/30 · strict exit 0 · 언어당 mermaid = 설계 수 · `git diff` 콘텐츠 불변 확인(삭제줄은 링크 래핑 쌍뿐).
- [ ] **Step 5: 커밋** — `pillar-1: Mermaid 다이어그램 N개 + 공식 링크 M곳 (가독성 롤아웃, 4개 언어)`

### Task 2: pillar-2 (모델 학습 VLA)

**Files:** Modify: `docs/pillar-2.md`, `docs/pillar-2.{en,zh,ja}.md`

- [ ] **Step 1: 다이어그램 2~3개** — 후보: ① 오픈 VLA 선택 분기(상용 출시→π Apache-2.0/OpenVLA MIT, GR00T→라이브 모델카드 확인) (graph TD) ② 학습 스택 사다리(단일 G7e LoRA → HyperPod 멀티노드 → P6e-GB200 초대형, Trainium은 미검증 ⚠️) (graph TD/LR).
- [ ] **Step 2: 링크 6~10곳** — 후보: openpi(GitHub), OpenVLA(GitHub), Isaac GR00T(GitHub), SageMaker HyperPod(AWS), LeRobot(GitHub), Capacity Blocks(AWS). curl 검증·확정표.
- [ ] **Step 3~5**: Task 1과 동일 절차 (대상 pillar-2, 해시 `--hash docs/pillar-2.md`).

### Task 3: pillar-4 (Sim-to-Real)

**Files:** Modify: `docs/pillar-4.md`, `docs/pillar-4.{en,zh,ja}.md`

- [ ] **Step 1: 다이어그램 2~3개** — 후보: ① sim-to-real 파이프라인(시뮬 학습→도메인 랜덤라이제이션→실기체 소량 검증→배포) (graph LR) ② 엣지 배포 경로(학습 정책→ONNX/TensorRT 최적화→Jetson + IoT Greengrass) (graph LR/TD).
- [ ] **Step 2: 링크 6~10곳** — 후보: TensorRT(NVIDIA), Jetson(NVIDIA), IoT Greengrass V2(AWS), ONNX(onnx.ai), SageMaker Neo(AWS). curl 검증·확정표.
- [ ] **Step 3~5**: 동일 절차 (pillar-4).

### Task 4: pillar-5 (에이전트 오케스트레이션)

**Files:** Modify: `docs/pillar-5.md`, `docs/pillar-5.{en,zh,ja}.md`

- [ ] **Step 1: 다이어그램 2~3개** — 후보: ① System 2(LLM 플래너, Bedrock AgentCore)/System 1(실시간 로봇 컨트롤러) 계층 + 지연 경계(클라우드 vs 엣지) (graph TD) ② 선택: 플릿 오케스트레이션 흐름.
- [ ] **Step 2: 링크 6~10곳** — 후보: Bedrock AgentCore(AWS), MCP(modelcontextprotocol.io), ROS 2(docs.ros.org), NASA JPL ROSA(GitHub). curl 검증·확정표.
- [ ] **Step 3~5**: 동일 절차 (pillar-5).

### Task 5: 배포 및 라이브 검증

- [ ] **Step 1**: `git push origin main` → `gh run watch --exit-status` 성공
- [ ] **Step 2**: 라이브 4개 언어 × 4개 필러에서 `class="mermaid"` 수 = 설계 수, 신규 링크 샘플 존재 (CDN 캐시 ~10분 대기 허용)

---

## Self-Review 결과

- **스펙 커버리지**: 페이지별 주제표→Task 1-4 Step 1, 링크 정책·검증→각 Step 2, 4개 언어·glossary 규칙→각 Step 3, 검증 목록→각 Step 4 + Task 5 — 누락 없음.
- **placeholder**: 다이어그램 정확 코드는 의도적으로 구현자 판단(본문 적합성) — 파일럿이 참조 구현이며 스타일 제약(노드 수·방향·라벨 규칙)이 계약. i18n 계획 Task 6~8(번역 생성) 전례와 동일한 생성형 태스크 구조.
- **일관성**: 게이트 기대값(0/30, mermaid=설계 수) 전 태스크 동일.
