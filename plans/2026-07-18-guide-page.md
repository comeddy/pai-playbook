# 가이드 페이지 신설 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 플레이북의 동작 전과정을 설명하는 `docs/guide.md`를 신설하고 상단 탭바(navigation.tabs)로 노출하며 4개 언어로 동기화한다.

**Architecture:** 한국어 원본 페이지 + mkdocs.yml(탭바·nav·nav_translations)을 한 태스크로 만들고(따로 하면 strict 빌드가 깨짐), 번역 3개를 두 번째 태스크로, 배포 검증을 세 번째로. 기존 i18n 파이프라인(ko_hash·strict 게이트)을 그대로 사용.

**Tech Stack:** MkDocs Material(navigation.tabs), mkdocs-static-i18n, 기존 scripts/check_*.py

**Spec:** `specs/2026-07-18-guide-page-design.md`

## Global Constraints

- 새 ko 페이지는 staleness 계약 필수: 메타데이터 라인에 `최종 갱신: 2026-07`·`volatility: 낮음` 포함 (누락 시 CI `--check` exit 1)
- 번역 파일은 첫 3줄이 `---` / `ko_hash: <40자>` / `---`, 역어·구조는 `i18n/glossary.md` 준수
- 커밋 전 `mkdocs build --strict` 통과 필수 (산출물은 scratchpad `--site-dir`)
- sync 기대값: 이 작업 후 **비동기 0/30** (10페이지 × 3언어)
- 커밋 메시지는 한국어 요약 + `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` 푸터

## File Structure

| 파일 | 책임 | 작업 |
|------|------|------|
| `docs/guide.md` | 동작 전과정 설명 (ko 원본) | Task 1 신규 |
| `mkdocs.yml` | navigation.tabs + nav 항목 + nav_translations ×3 | Task 1 수정 |
| `docs/guide.en.md` / `guide.zh.md` / `guide.ja.md` | 번역 | Task 2 신규 |

---

### Task 1: guide.md (ko) + mkdocs.yml

**Files:**
- Create: `docs/guide.md`
- Modify: `mkdocs.yml` (theme.features, nav, plugins.i18n.languages[].nav_translations)

**Interfaces:**
- Produces: `docs/guide.md`의 H2 제목들(번역 태스크가 앵커 기준으로 사용), nav 키 `가이드`(nav_translations 키와 일치해야 함)
- Consumes: 기존 앵커 `maintenance.md#포함-기준-the-filter`, `maintenance.md#슬랙--playbook-승격-파이프라인`, `maintenance.md#표준-템플릿` (전부 기존 strict 빌드에서 검증된 실존 앵커)

- [ ] **Step 1: docs/guide.md 작성** — 아래 내용 그대로 (전문):

````markdown
# 가이드 — 이 Playbook은 어떻게 동작하는가

_최종 갱신: 2026-07 · owner: comeddy · volatility: 낮음(프로세스 페이지 — 파이프라인 변경 시에만 갱신)_
[← index로](index.md)

> **L0 TL;DR**: 이 사이트는 뉴스 아카이브가 아니라 **검증 파이프라인**이다. 새로 등장한 기술·논문·발표는 곧바로 본문에 실리지 않는다 — 자동 스캔이 후보를 모으고, 사람이 1차 출처로 검증하고, 4개 중 2개 관문(THE FILTER)을 통과한 것만 본문에 오른다. 실린 뒤에도 신선도를 자동 감시하고, 4개 언어로 동기화되며, 빌드 게이트를 통과해야 배포된다.

---

## 한눈에 보는 전과정

```
[후보 발견]
 ├─ 🤖 주간 자동 스캔 (매주 월 02:00 UTC — arXiv·웹)
 ├─ 💬 SA 제보 (승격 파이프라인)
 └─ 🔍 수동 조사
        │
        ▼
[Radar 대기열]  ← 전부 "미검증 [4]" 라벨, 고객 제안 사용 금지
        │
        ▼
[1차 출처 검증]  ← 사람 + 검증 에이전트 (공식 발표·논문 원문 대조)
        │
        ▼
[THE FILTER]  ⓐ production 검증  ⓑ AWS 매핑  ⓒ 실제 문의  ⓓ GA
        │                                          │
        │ 2개 이상 충족                             │ 미달
        ▼                                          ▼
[필러 본문 승격]                          [Radar에 한 줄 유지]
 (owner가 표준 템플릿으로)                 (승격 조건 명시)
        │
        ▼
[실린 뒤에도]
 ├─ ⏳ 신선도 자동 감시 (volatility별 1/3/6개월 초과 시 배지)
 ├─ 🌐 4개 언어 동기화 (ko 원본 → ko_hash → en/zh/ja)
 └─ ✅ strict 빌드 게이트 (앵커·링크 검증) → GitHub Pages 자동 배포
```

---

## ① 어떻게 만들어졌나

이 플레이북은 완결된 스펙 문서([마스터 프롬프트](https://github.com/comeddy/pai-playbook/blob/main/physical-ai-playbook-master-prompt.md))로부터 생성됐다. 정보 구조(5개 필러 + 의사결정 트리 + Radar + 유지보수 규칙)와 포함 기준이 스펙에 고정되어 있고, 페이지마다 **적대적 검증**(사실 오류·과장을 찾는 별도 검증 단계)을 거쳤다. 실제로 이 단계에서 버전 오기·라이선스 오류 등이 잡혔다 — "생성했으니 믿는다"가 아니라 "생성한 것도 검증한다"가 원칙이다.

## ② 무엇이 실리고, 무엇이 걸러지나

모든 항목은 [THE FILTER](maintenance.md#포함-기준-the-filter)를 통과해야 본문에 실린다: ⓐ production 검증 ⓑ AWS 매핑 가능 ⓒ 실제 문의 이력 ⓓ GA(또는 로드맵) — **4개 중 2개 이상**. "새로 나왔다", "데모가 인상적이다"는 포함 사유가 아니다. 실린 항목에는 성숙도 라벨(🟢 GA / 🟡 Preview / 🔵 Research / ⚪ Hype)과 출처 등급(`[1]` 공식 문서 ~ `[4]` 미검증)이 붙는다 — 라벨 읽는 법은 [홈](index.md)에 있다.

## ③ Radar와 주간 자동 스캔

필터를 아직 통과하지 못한 것들은 [Radar(대기열)](radar.md)에 한 줄로 존재한다. **매주 월요일 02:00 UTC**에 자동 스캔이 돌아 최신 논문·뉴스를 Radar의 "최신 스캔 유입" 섹션에 채운다. 중요한 것: **자동 유입분은 전부 미검증 `[4]`로 격리**되며, 고객 제안에 쓰면 안 된다. 자동화는 후보를 대기열에 올리는 것까지만 한다.

## ④ 검증과 승격 — 사람의 몫

유입 항목의 1차 출처 확인(공식 발표·논문 원문·라이선스 대조)과 승격 판단은 **사람(owner)** 이 한다. 자동 스캔은 그럴듯한 오류(예: 존재하지 않는 제품 세대명)를 만들 수 있어, 검증 없이는 승격되지 않는다. 통과하면 owner가 [표준 템플릿](maintenance.md#표준-템플릿)으로 해당 필러에 편입하고 Radar에서 제거한다. 전체 절차는 [승격 파이프라인](maintenance.md#슬랙--playbook-승격-파이프라인) 참고.

## ⑤ 신선도 자동 감시

실린 항목도 낡는다. 페이지마다 변동성(volatility) 등급이 있고 — 높음 1개월 / 중간 3개월 / 낮음 6개월 — 갱신 없이 기준을 초과하면 배포 시 해당 페이지(4개 언어 전부)에 **"⏳ 검토 필요" 배지가 자동 주입**된다. 매주 재배포가 돌므로 푸시가 없어도 배지는 최신 상태를 유지한다. 배지가 보이면 그 페이지는 재검토 대기 중이라는 뜻이다.

## ⑥ 4개 언어 동기화

**한국어가 원본**이고 영어·중국어·일본어는 파생물이다. 각 번역 파일은 번역 시점의 원본 지문(ko_hash)을 기록하고 있어, 원본이 바뀌면 어느 번역이 뒤처졌는지 자동 감지된다(CI 경고). 용어는 공용 용어집으로 4개 언어에서 일관되게 유지된다. 언어 전환은 페이지 우측 상단 드롭다운.

## ⑦ 배포 파이프라인

`main`에 푸시되면 CI가 신선도 검사·번역 동기화 검사를 돌리고 **strict 빌드**(깨진 링크·앵커가 하나라도 있으면 실패)를 통과한 경우에만 GitHub Pages로 배포한다. 즉, 지금 보고 있는 모든 페이지는 이 게이트를 통과한 상태다.

---

## 역할별 안내

| 나는… | 이렇게 쓰면 된다 |
|---|---|
| **그냥 읽는 사람** | [홈](index.md)의 FAQ Top 20 또는 필러로 진입. 라벨(🟢🟡🔵⚪)과 출처 등급(`[1]`~`[4]`)만 알면 신뢰 수준을 바로 읽을 수 있다 |
| **항목을 제보하고 싶은 사람** | [승격 파이프라인](maintenance.md#슬랙--playbook-승격-파이프라인)으로 제보. THE FILTER 4개 중 몇 개를 충족하는지 함께 적으면 빠르다 |
| **owner** | 주간 자동 유입 검토 → 1차 검증 → 승격/유지 판단. [유지보수 규칙](maintenance.md) 전체 참고 |
````

- [ ] **Step 2: mkdocs.yml 수정 3곳**

2a. `theme.features` 목록 맨 앞에 추가:

```yaml
  features:
    - navigation.tabs      # 상단 가로 탭바 — 가이드 등 전 페이지를 헤더에 노출
```

2b. `nav`의 `- 홈: index.md` 바로 다음 줄에 삽입:

```yaml
  - 가이드: guide.md
```

2c. `plugins.i18n.languages`의 en/zh/ja 각 `nav_translations` 블록(홈 번역 줄 다음)에 추가:

```yaml
            가이드: Guide        # en
            가이드: 指南         # zh
            가이드: ガイド       # ja
```

- [ ] **Step 3: 게이트 검증**

Run:
```bash
python3 scripts/check_staleness.py --check
mkdocs build --strict --site-dir /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/site-guide
grep -c 'md-tabs' /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/site-guide/index.html
```
Expected: staleness 리포트 10행(guide 포함) exit 0 · strict exit 0 · md-tabs 1 이상(탭바 렌더). sync는 아직 guide 번역이 없어 3행 "누락"이 정상(커밋 가능 — 경고만).

- [ ] **Step 4: 커밋**

```bash
git add docs/guide.md mkdocs.yml
git commit -m "guide: 동작 전과정 가이드 페이지 신설 + 상단 탭바(navigation.tabs)"
```

---

### Task 2: 번역 3개 (en/zh/ja)

**Files:**
- Create: `docs/guide.en.md`, `docs/guide.zh.md`, `docs/guide.ja.md`

**Interfaces:**
- Consumes: `docs/guide.md`(원본), `i18n/glossary.md`(역어·구조 규칙), `scripts/check_translation_sync.py --hash`(해시 헬퍼)
- Produces: sync 0/30 상태

- [ ] **Step 1: 해시 확보 후 3개 파일 생성** — 각 파일 골격:

```markdown
---
ko_hash: <python3 scripts/check_translation_sync.py --hash docs/guide.md 출력>
---
# <H1 번역>

<본문 전체 번역>
```

번역 규칙(기존 확립 관례): 메타데이터 라벨만 번역·값 유지(`Last updated:`/`最终更新:`/`最終更新:`, volatility low/低/低) / ASCII 다이어그램 내부 텍스트도 번역하되 박스 구조·화살표 유지 / 상대 링크 파일명 유지·링크 텍스트만 번역 / **cross-page 앵커(`maintenance.md#...`)는 각 언어 maintenance 번역본의 실제 heading 슬러그로 교체** (en: `#inclusion-criteria-the-filter`·`#standard-template`·`#slack--playbook-promotion-pipeline`, zh: `#纳入标准-the-filter`·`#标准模板`·`#slack--playbook-晋升管道`, ja: `#包含基準-the-filter`·`#標準テンプレート`·`#slack--playbook-昇格パイプライン` — 전부 기존 radar 번역에서 실측 검증된 앵커) / 표·이모지·굵기 구조 보존 / 역할별 안내 표의 용어는 glossary 고정 역어.

- [ ] **Step 2: 게이트 검증**

Run:
```bash
python3 scripts/check_translation_sync.py | tail -1
mkdocs build --strict --site-dir /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/site-guide
grep -LP '^ko_hash:' docs/guide.*.md | grep -v 'docs/guide.md' ; ls docs/guide.*.md | wc -l
```
Expected: `비동기: 0 / 30` · strict exit 0 (heading 번역→본문 앵커 실측 교정, 실패 시 산출물 `<h2 id>` grep) · 파일 4개(원본 포함)·frontmatter 누락 0

- [ ] **Step 3: 한국어 잔존 확인**

Run: `grep -cP '[\x{AC00}-\x{D7A3}]' docs/guide.en.md docs/guide.zh.md docs/guide.ja.md`
Expected: 전부 0 (ko_hash 라인은 한글 없음)

- [ ] **Step 4: 커밋**

```bash
git add docs/guide.en.md docs/guide.zh.md docs/guide.ja.md
git commit -m "guide: 영어·중국어·일본어 번역 (비동기 0/30)"
```

---

### Task 3: 배포 및 라이브 검증

**Files:** 없음 (push + 검증)

- [ ] **Step 1: push + CI**

```bash
git push origin main
RID=$(gh run list --limit 1 --json databaseId -q '.[0].databaseId'); gh run watch "$RID" --exit-status
```
Expected: deploy-docs 성공

- [ ] **Step 2: 라이브 4개 언어 + 탭바**

```bash
for p in "guide" "en/guide" "zh/guide" "ja/guide"; do curl -s -o /dev/null -w "/$p -> %{http_code}\n" -L "https://comeddy.github.io/pai-playbook/$p/"; done
curl -s https://comeddy.github.io/pai-playbook/ | grep -c 'md-tabs'
```
Expected: 4행 전부 200 · md-tabs ≥ 1

---

## Self-Review 결과

- **스펙 커버리지**: §1(페이지 구조·전문)→Task 1 Step 1, §2(mkdocs 3곳)→Task 1 Step 2, §3(번역)→Task 2, §4(검증 4종: staleness 10p·sync 0/30·strict+탭바·라이브)→Task 1 Step 3 + Task 2 Step 2 + Task 3 — 누락 없음.
- **placeholder 스캔**: 통과 (guide.md 전문 포함, 앵커는 실측 검증된 값 명시).
- **일관성**: nav 키 `가이드` = nav_translations 키 일치, sync 0/30 = 10페이지×3언어 일치.
