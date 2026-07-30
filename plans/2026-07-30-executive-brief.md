# 경영진 브리핑 + 임원 대화 가이드 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 임원이 직접 읽는 "경영진 브리핑"(exec.md)과 SA용 "임원 대화 가이드"(exec-guide.md)를 4개 언어로 발행한다.

**Architecture:** 신규 md 2개를 nav에 추가(가이드 다음, P1 앞). 콘텐츠는 기존 pillar/radar의 검증 판정을 임원 언어로 번역만 한다(새 기술 주장 금지). ko 원본 → translate-sync로 en/zh/ja → 기대값 게이트 30→36 갱신.

**Tech Stack:** MkDocs Material + mkdocs-static-i18n(suffix), scripts/check_translation_sync.py, GitHub Pages CI.

## Global Constraints (스펙 원문 준수)

- 새로운 기술 주장 금지 — 모든 사실·판정은 기존 pillar/radar 문장에 근거하고 딥링크를 단다.
- 전망치는 출처·성격을 문장 안에 명시("○○ 추정, 2035년 전망" 식). `[1]~[4]` 각주는 쓰지 않는다.
- 외부 링크는 삽입 전 전원 `curl -sIL -o /dev/null -w '%{http_code}'` 200 확인.
- 두 페이지 메타데이터: `_최종 갱신: 2026-07 · owner: Youngjin · volatility: 중간_` 헤더 + 동일 값 푸터(`_owner: Youngjin · updated: 2026-07 · volatility: 중간 (...)_`). 헤더/푸터 날짜 불일치는 check_staleness가 exit 1로 잡는다.
- 분량: exec.md 본문 ~1,800자 / exec-guide.md ~2,500자 (한국어 기준, ±20%).
- mkdocs.yml에는 다른 세션의 미커밋 훅크(markdown_extensions의 footnotes)가 있을 수 있다 — **nav 관련 훅크만 선택 스테이징**(`git apply --cached` 패치 기법, 42b4f94 커밋 참조). pillar-*.md는 절대 건드리지 않는다.
- 커밋 메시지는 한국어 관례 + `Co-Authored-By: Claude ...` 라인.

---

### Task 1: 경영진 브리핑 한국어 원본 + nav 등록

**Files:**
- Create: `docs/exec.md`
- Modify: `mkdocs.yml` (nav 블록 — "가이드" 다음 줄에 1행 추가; ko nav만, 번역 nav는 Task 3)

**Interfaces:**
- Produces: `docs/exec.md`의 섹션 앵커(특히 판단 매트릭스 h2)를 Task 2가 딥링크로 소비. nav 라벨 문자열 "경영진 브리핑"을 Task 3의 nav_translations 키로 사용.

- [ ] **Step 1: 콘텐츠에 인용할 근거 문장을 원본에서 수집**

다음을 읽고 사실·표현을 그대로 가져올 목록을 만든다(새 주장 금지 원칙의 실행 방법):
- `docs/radar.md` — Figure 02@BMW "검증 파일럿" 표현, Agility(Halos 행) "9개 현장", 휴머노이드 관련 ⚪ 판정들
- `docs/pillar-1.md` — 데이터 병목 L0 TL;DR, "오픈 사전학습→합성 증강→실데모 파인튜닝" 3단 혼합
- `docs/pillar-2.md` — Unitree H1 on HyperPod(AWS 공식 블로그), LoRA 단일 GPU 사실
- `docs/pillar-3.md` — 시뮬레이션 인프라 GA 판정
- `docs/pillar-5.md` — AgentCore 서울 GA
- `docs/index.md` — 톤·형식 관례

- [ ] **Step 2: `docs/exec.md` 작성**

구조(스펙 §페이지1 그대로 — 아래 골격의 헤딩·표는 확정 문안, 산문만 채운다):

```markdown
# 경영진 브리핑 — Physical AI, 무엇을 하고 무엇을 기다릴 것인가

_최종 갱신: 2026-07 · owner: Youngjin · volatility: 중간_
[← index로](index.md)

> **L0 TL;DR**: 로봇이 파운데이션 모델을 만나 산업이 변곡점에 있다. 단, **지금 투자할
> 것과 지켜볼 것은 다르다**. 이 페이지는 과장 없이 그 구분을 제공한다 — 5분.

## ① 왜 지금인가
(검증 신호 3개: Figure 02@BMW 검증 파일럿 · Agility Digit 9개 현장 6.5만 시간 ·
오픈 파운데이션 모델(π0 Apache-2.0 등) 등장. 전망치 1문장 — 출처·성격 명시)

## ② 우리 산업에는 무슨 의미인가
(제조/물류/자동차 × 2문장. 각 산업 끝에 해당 pillar 딥링크 1개)

## ③ 무엇이 진짜이고 무엇이 과장인가

| 판단 | 의미 | 대표 영역 |
|---|---|---|
| 🟢 **지금 투자** | 검증된 기반 역량 | 로봇 데이터 파이프라인 · 시뮬레이션 인프라 · 합성 데이터 |
| 🟡 **곧 (12~24개월)** | 파일럿 가치 있음 | VLA 파인튜닝 역량 · 엣지 추론 스택 · 에이전트 오케스트레이션 |
| ⚪ **아직** | 관찰 대상 | 휴머노이드 대규모 도입 · 완전 자율 시프트 |

(표 아래 3~4문장: 이 구분이 어디서 오는가 — 상시 검증 체계(radar) 소개 1문장 포함)

## ④ 그래서 무엇부터 하는가
(정직한 답 "데이터부터" + 3단계: 파이프라인 → 시뮬 PoC → 파인튜닝 파일럿)

## ⑤ 왜 AWS와 하는가
(검증 사실 3개만: Unitree H1 RL on HyperPod(AWS 공식 블로그) · AgentCore 서울 리전 GA ·
오픈 모델 셀프호스팅의 자유(락인 없음))

## 검토를 시작한다면
**1일 아키텍처 워크숍**: 귀사 데이터 자산 진단 + 위 판단 매트릭스를 귀사 상황에 적용.
담당 AWS SA 또는 [GitHub](https://github.com/comeddy/pai-playbook)으로 연락.

---
**더 깊이**: [기술 가이드](guide.md) · [P1 데이터](pillar-1.md) · [P3 시뮬레이션](pillar-3.md) · [의사결정 트리](decisions.md)

_owner: Youngjin · updated: 2026-07 · volatility: 중간 (판단 매트릭스는 radar 승격·강등 시 갱신)_
```

- [ ] **Step 3: 외부 링크 전수 curl 200 확인** (본문에 외부 링크를 넣었다면)

```bash
grep -o 'https://[^)]*' docs/exec.md | sort -u | while read u; do
  printf "%s %s\n" "$(curl -sIL -o /dev/null -w '%{http_code}' --max-time 12 "$u")" "$u"; done
```
Expected: 전부 200. 아니면 링크 교체/제거.

- [ ] **Step 4: nav 등록** — `mkdocs.yml` nav의 `- 가이드: guide.md` 다음 줄에:

```yaml
  - "경영진 브리핑": exec.md
```

- [ ] **Step 5: 게이트 실행**

```bash
python3 scripts/check_staleness.py --check   # exec.md 행이 OK로 표시, exit 0
mkdocs build --strict --site-dir /tmp/exec-check   # exit 0 (en/zh/ja는 fallback)
```
Expected: 둘 다 통과. staleness "updated 누락"이면 헤더/푸터 표기 확인.

- [ ] **Step 6: 선택 스테이징 커밋**

```bash
cd /home/ec2-user/pai-playbook
git add docs/exec.md
git diff mkdocs.yml   # nav 훅크와 타 세션 훅크 확인
# nav 훅크만 패치로 추출해 git apply --cached (42b4f94 방식). 타 세션 훅크 미포함 확인:
git diff --cached mkdocs.yml
git commit -m "feat: 경영진 브리핑(exec.md) 한국어 원본 + nav 등록 — 5가지 질문 흐름, 지금/곧/아직 판단 매트릭스

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

### Task 2: 임원 대화 가이드 한국어 원본 + nav 등록

**Files:**
- Create: `docs/exec-guide.md`
- Modify: `mkdocs.yml` (nav — "경영진 브리핑" 다음 줄 1행)

**Interfaces:**
- Consumes: Task 1의 `exec.md` 앵커(5분 피치가 "Brief를 화면에 띄우고 걷는 순서"로 참조).
- Produces: nav 라벨 "임원 대화 가이드" (Task 3 nav_translations 키).

- [ ] **Step 1: `docs/exec-guide.md` 작성**

구조(스펙 §페이지2 — 확정 골격, 산문만 채운다):

```markdown
# 임원 대화 가이드 — SA용

_최종 갱신: 2026-07 · owner: Youngjin · volatility: 중간_
[← index로](index.md)

> **L0 TL;DR**: 임원 미팅 30분 전에 훑는 실전 자산. [경영진 브리핑](exec.md)이
> "보여주는 것"이라면 이 페이지는 "말하는 법"이다.

## 1. 엘리베이터 피치 3종
(30초/2분/5분. 각각 "쓰는 장면" 한 줄. 5분 버전은 exec.md 섹션 순서로 걷기)

## 2. 임원 예상 질문 Top 10
(index FAQ Top 20 형식. 필수 포함 질문: ROI? / 왜 AWS(NVIDIA와 관계)? / 경쟁사는? /
우리가 늦었나? / 얼마 드나? / 인력은? / 언제 성과? / 리스크는? / 파트너 선택 기준? /
첫 프로젝트는? — 답변 3~4문장 + pillar/radar 딥링크)

## 3. 반박·우려 대응
**3박자: 인정 → 프레임 전환 → 검증된 다음 걸음.**
(5개: 휴머노이드 데모 아닌가 / 안전·규제 / 인력 대체 / 하이프 아닌가 / 벤더 락인)

## 4. 산업별 앵글

| 산업 | 훅 | 검증된 사례 | 첫 제안 |
|---|---|---|---|
| 제조 | … | Figure 02@BMW 검증 파일럿 | … |
| 물류 | … | Agility Digit 현장 가동 | … |
| 자동차 | … | Zoox HyperPod 학습 | … |

(사례 없는 산업 행 금지 — 스펙 확정)

## 5. ⚠️ 임원 앞 금지·주의 표현

| ❌ 이렇게 말하지 말 것 | ⭕ 이렇게 말할 것 |
|---|---|
| "옵티머스가 곧 양산됩니다" | "휴머노이드는 검증 파일럿 단계입니다. 저희 제안은 그 전 단계인 데이터·시뮬 인프라입니다" |
| (radar ⚪/🔵 항목을 성숙 역량처럼 인용) | (성숙도 라벨 그대로: "발표는 있었지만 프로덕션 검증 전입니다") |

(2~4행 추가. 마지막에 최신 상태는 [Radar](radar.md) 확인 유도)

_owner: Youngjin · updated: 2026-07 · volatility: 중간_
```

- [ ] **Step 2: nav 등록** — `- "경영진 브리핑": exec.md` 다음 줄에 `- "임원 대화 가이드": exec-guide.md`

- [ ] **Step 3: 게이트** — Task 1 Step 5와 동일 두 명령. Expected: exit 0 × 2.

- [ ] **Step 4: 선택 스테이징 커밋** — Task 1 Step 6과 동일 기법.
커밋 메시지: `feat: 임원 대화 가이드(exec-guide.md) 한국어 원본 + nav 등록 — 피치 3종·Top10·반박 대응·산업 앵글·금지 표현`

### Task 3: 4개 언어 동기화 + nav_translations

**Files:**
- Create: `docs/exec.{en,zh,ja}.md`, `docs/exec-guide.{en,zh,ja}.md`
- Modify: `mkdocs.yml` (en/zh/ja 각 `nav_translations`에 2키씩 추가)

**Interfaces:**
- Consumes: Task 1·2의 ko 원본과 nav 라벨 문자열(번역 키는 ko 라벨과 정확히 일치해야 함).

- [ ] **Step 1: translate-sync 스킬 절차 실행** — `i18n/glossary.md` 로드 → `python3 scripts/check_translation_sync.py --hash docs/exec.md`(exec-guide도)로 해시 → 6개 번역 파일 작성(frontmatter `ko_hash:` 필수, heading 번역 시 본문 앵커 함께).

- [ ] **Step 2: nav_translations 추가** — mkdocs.yml 각 언어 블록에:

```yaml
            "경영진 브리핑": "Executive Brief"        # en
            "임원 대화 가이드": "Executive Conversation Guide"
            "경영진 브리핑": "高管简报"                # zh
            "임원 대화 가이드": "高管对话指南"
            "경영진 브리핑": "経営層ブリーフィング"      # ja
            "임원 대화 가이드": "経営層対話ガイド"
```

- [ ] **Step 3: 게이트**

```bash
python3 scripts/check_translation_sync.py   # 기대: 비동기 0 / 36
mkdocs build --strict --site-dir /tmp/exec-check   # exit 0
```
strict가 번역 heading 앵커로 실패하면 산출물의 `<h2 id=...>`를 읽어 링크를 맞춘다(용어집 규칙).

- [ ] **Step 4: 커밋** — 번역 6파일 + mkdocs.yml nav_translations 훅크만 선택 스테이징.
메시지: `i18n: 경영진 브리핑·임원 대화 가이드 en/zh/ja 동기화 + nav_translations — sync 0/36`

### Task 4: 기대값·규칙 후속 갱신

**Files:**
- Modify: `scripts/radar_scan.md` (검증 명령·주석의 "0/30" → "0/36", 2곳)
- Modify: `docs/maintenance.md` (콘텐츠 원칙 1줄) + `docs/maintenance.{en,zh,ja}.md` (동일 문장 번역 + ko_hash 갱신)
- Modify(외부): radar 스캔 루틴 프롬프트 — RemoteTrigger update로 `trig_01KWwHEnRP6Di1gYTnP5uxJ8`의 "비동기: 0 / 30" → "0 / 36"

**Interfaces:**
- Consumes: Task 3 완료 후의 실제 sync 총수(36) — 반드시 실측값으로 기입.

- [ ] **Step 1: 런북 갱신** — `grep -n "0/30\|0 / 30" scripts/radar_scan.md`로 위치 확인 후 0/36으로.
- [ ] **Step 2: maintenance.md 표준 템플릿 근처에 1줄 추가**: `- **임원 페이지(exec/exec-guide) 원칙**: 새로운 기술 주장 금지 — pillar/radar 검증 판정의 임원 언어 번역만 싣는다.` → 번역 3파일 동일 반영 + ko_hash 재계산.
- [ ] **Step 3: 루틴 프롬프트 갱신** — RemoteTrigger get으로 현 프롬프트 확보 → "0 / 30" 문자열만 "0 / 36"으로 바꿔 update. 응답에서 변경 확인.
- [ ] **Step 4: 게이트 재실행** (sync 0/36 · strict exit 0) 후 커밋.
메시지: `ops: sync 기대값 30→36 후속 — 런북·radar 루틴 프롬프트 갱신, maintenance에 임원 페이지 새 주장 금지 원칙 명문화 (4개 언어)`

### Task 5: 발행 확인 + CHANGELOG

**Files:**
- Modify: `CHANGELOG.md` ([Unreleased] 양 언어 섹션)

- [ ] **Step 1: push 후 CI 확인**

```bash
git push
gh run watch $(gh run list --limit 1 --json databaseId --jq '.[0].databaseId') --exit-status
```
Expected: success.

- [ ] **Step 2: 라이브 4개 언어 확인**

```bash
for p in exec exec-guide en/exec zh/exec-guide ja/exec; do
  printf "%s %s\n" "$(curl -s -o /dev/null -w '%{http_code}' https://comeddy.github.io/pai-playbook/$p/)" "$p"; done
```
Expected: 전부 200.

- [ ] **Step 3: CHANGELOG [Unreleased] Added** (영·한 동일 항목):
`- Add an Executive Brief page (5-question flow with a now/soon/not-yet judgment matrix) and an SA-facing executive conversation guide (pitches, top-10 Q&A, objection handling, industry angles, forbidden claims), in all four languages` / 한국어 대응문.
커밋: `docs: CHANGELOG — 경영진 브리핑·임원 대화 가이드 기록` → push.
