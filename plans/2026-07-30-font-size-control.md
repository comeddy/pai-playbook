# 글자 크기 조절 플로팅 버튼 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 우하단 A−/A+ 플로팅 버튼으로 본문 글자 크기를 85~130%(5% 단계)로 조절하고 localStorage로 유지한다.

**Architecture:** CSS는 `html[data-fs="N"]` 속성 선택자로 `.md-typeset`의 단계별 고정 rem 값을 적용, JS는 버튼 생성·클릭 처리·localStorage 저장만 담당. FOUC 방지를 위해 `overrides/main.html` extrahead 인라인 스크립트가 렌더 전에 저장값을 `data-fs`로 복원한다.

**Tech Stack:** mkdocs-material(테마 CSS 변수), vanilla JS, `extra_css`/`extra_javascript`. 테스트 하네스 없음 — 검증은 strict 빌드 + 산출물 grep + 배포 후 클라우드 브라우저 기능 확인.

## Global Constraints

- 단계: 85/90/95/100/105/110/115/120/125/130 (%), 기본 100, localStorage 키 `pai-fs`
- 조절 대상은 `.md-typeset`만 — 헤더·네비·검색·푸터 불변
- Material 기본 본문 크기 `.8rem` 기준: rem 값 = `.8 × 배율` (예: 110% → `.88rem`)
- 헤더 partial 오버라이드 금지, `navigation.instant` 없음(매 페이지 전체 로드 — SPA 이벤트 처리 불필요)
- aria-label/title은 페이지 `<html lang>` 기준 ko/en/zh/ja 분기, 버튼 라벨 텍스트는 `A−`/`A+` 고정
- 게이트: `mkdocs build --strict` exit 0 (이 리포의 커밋 전 필수 게이트)

---

### Task 1: 기능 구현 (CSS + JS + 연결) 및 로컬 빌드 검증

**Files:**
- Create: `docs/stylesheets/font-size.css`
- Create: `docs/javascripts/font-size.js`
- Modify: `overrides/main.html` (extrahead 블록 끝에 2줄 추가)
- Modify: `mkdocs.yml` (`extra:` 블록 위에 최상위 키 `extra_css`/`extra_javascript` 추가)

**Interfaces:**
- Consumes: Material CSS 변수(`--md-default-fg-color*`, `--md-shadow-z2`), `html[lang]`
- Produces: `html[data-fs="N"]` 속성 계약(css↔js↔인라인 스크립트 공유), localStorage 키 `pai-fs`

- [ ] **Step 1: CSS 파일 작성**

`docs/stylesheets/font-size.css` 생성:

```css
/* 글자 크기 조절 — 본문(.md-typeset)만 조절. 단계·키는 javascripts/font-size.js 와 계약 */
html[data-fs="85"]  .md-typeset { font-size: .68rem; }
html[data-fs="90"]  .md-typeset { font-size: .72rem; }
html[data-fs="95"]  .md-typeset { font-size: .76rem; }
html[data-fs="105"] .md-typeset { font-size: .84rem; }
html[data-fs="110"] .md-typeset { font-size: .88rem; }
html[data-fs="115"] .md-typeset { font-size: .92rem; }
html[data-fs="120"] .md-typeset { font-size: .96rem; }
html[data-fs="125"] .md-typeset { font-size: 1rem;   }
html[data-fs="130"] .md-typeset { font-size: 1.04rem; }

.pai-fs-controls {
  position: fixed;
  right: .8rem;
  bottom: .8rem;
  z-index: 3; /* 콘텐츠 위, 헤더·검색 오버레이(z-index 4) 아래 */
  display: flex;
  gap: .25rem;
}
.pai-fs-controls button {
  min-width: 44px;  /* 터치 타깃 */
  min-height: 44px;
  border: none;
  border-radius: .4rem;
  background: var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color);
  font-family: inherit;
  font-size: .7rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: var(--md-shadow-z2);
}
.pai-fs-controls button:hover { color: var(--md-accent-fg-color); }
.pai-fs-controls button:disabled { opacity: .4; cursor: default; }
@media print { .pai-fs-controls { display: none; } }
```

100%는 기본값이라 규칙이 없다(속성 제거 = 원복).

- [ ] **Step 2: JS 파일 작성**

`docs/javascripts/font-size.js` 생성:

```js
/* 글자 크기 조절 버튼 — 저장값 조기 적용은 overrides/main.html extrahead 인라인 스크립트가 담당 */
(function () {
  var STEPS = [85, 90, 95, 100, 105, 110, 115, 120, 125, 130];
  var KEY = "pai-fs";
  var LABELS = {
    ko: ["글자 작게", "글자 크게"],
    en: ["Decrease font size", "Increase font size"],
    zh: ["缩小字号", "放大字号"],
    ja: ["文字を小さく", "文字を大きく"]
  };
  var labels = LABELS[(document.documentElement.lang || "ko").slice(0, 2)] || LABELS.ko;

  var minus = makeButton("A−", labels[0], -1);
  var plus = makeButton("A+", labels[1], +1);
  var box = document.createElement("div");
  box.className = "pai-fs-controls";
  box.appendChild(minus);
  box.appendChild(plus);
  document.body.appendChild(box);
  apply(current());

  function makeButton(text, label, delta) {
    var b = document.createElement("button");
    b.type = "button";
    b.textContent = text;
    b.setAttribute("aria-label", label);
    b.title = label;
    b.addEventListener("click", function () {
      var i = STEPS.indexOf(current()) + delta;
      if (i >= 0 && i < STEPS.length) apply(STEPS[i]);
    });
    return b;
  }
  function current() {
    var v = parseInt(localStorage.getItem(KEY), 10);
    return STEPS.indexOf(v) === -1 ? 100 : v;
  }
  function apply(v) {
    if (v === 100) {
      delete document.documentElement.dataset.fs;
      try { localStorage.removeItem(KEY); } catch (e) {}
    } else {
      document.documentElement.dataset.fs = v;
      try { localStorage.setItem(KEY, v); } catch (e) {}
    }
    minus.disabled = v === STEPS[0];
    plus.disabled = v === STEPS[STEPS.length - 1];
  }
})();
```

- [ ] **Step 3: extrahead에 조기 적용 스크립트 추가**

`overrides/main.html`의 `{% endblock %}` 직전에 추가:

```html
  {#- 글자 크기: 렌더 전에 저장값 적용(FOUC 방지) — 버튼·로직은 javascripts/font-size.js -#}
  <script>try{var f=localStorage.getItem("pai-fs");if(f)document.documentElement.dataset.fs=f}catch(e){}</script>
```

- [ ] **Step 4: mkdocs.yml에 등록**

최상위 레벨(예: `extra:` 키 바로 위)에 추가:

```yaml
extra_css:
  - stylesheets/font-size.css      # 글자 크기 조절 버튼 (font-size.js와 쌍)
extra_javascript:
  - javascripts/font-size.js
```

주의: 이미 `extra_css`/`extra_javascript` 키가 있으면 항목만 추가(중복 키 금지 — YAML 파스 에러).

- [ ] **Step 5: strict 빌드로 검증**

```bash
mkdocs build --strict --site-dir /tmp/claude-1000/-home-ec2-user-pai-playbook/4b8fce32-4272-468e-9f3b-afaa60eaa410/scratchpad/site-check
```

Expected: exit 0. 이어서 산출물 4개 언어에 css/js/인라인이 들어갔는지:

```bash
SITE=/tmp/claude-1000/-home-ec2-user-pai-playbook/4b8fce32-4272-468e-9f3b-afaa60eaa410/scratchpad/site-check
for p in pillar-1 en/pillar-1 zh/pillar-1 ja/pillar-1; do
  grep -l "font-size.css" "$SITE/$p/index.html" && grep -l "font-size.js" "$SITE/$p/index.html" && grep -l 'localStorage.getItem("pai-fs")' "$SITE/$p/index.html"
done
```

Expected: 12줄(3개 파일명 × 4개 언어) 전부 매치.

- [ ] **Step 6: 커밋**

```bash
git add docs/stylesheets/font-size.css docs/javascripts/font-size.js overrides/main.html mkdocs.yml
git commit -m "feat: 글자 크기 조절 플로팅 버튼 — 우하단 A−/A+, 본문 한정 85~130%(5% 단계), localStorage 유지, 4개 언어 aria-label"
```

---

### Task 2: 배포 및 실사이트 기능 검증

**Files:** 없음 (push + 검증만)

**Interfaces:**
- Consumes: Task 1의 커밋, GitHub Actions `deploy-docs` 워크플로우, 클라우드 브라우저 MCP(`mcp__bedrock-agentcore-mcp-server__browser_*`)

- [ ] **Step 1: push 및 배포 완료 대기**

```bash
git push origin main
gh run watch --exit-status $(gh run list --workflow deploy-docs --limit 1 --json databaseId -q '.[0].databaseId')
```

Expected: 워크플로우 success.

- [ ] **Step 2: 정적 반영 확인 (curl)**

```bash
for p in "" en/ zh/ ja/; do
  curl -s "https://comeddy.github.io/pai-playbook/${p}pillar-1/" | grep -c "font-size.css\|font-size.js\|pai-fs"
done
```

Expected: 각 언어 3 이상.

- [ ] **Step 3: 기능 확인 (클라우드 브라우저)**

`start_browser_session` 후:

1. `browser_navigate` → `https://comeddy.github.io/pai-playbook/pillar-1/`
2. `browser_evaluate` → `getComputedStyle(document.querySelector(".md-typeset")).fontSize` 기록 (기본값, 20px 근처)
3. `browser_evaluate` → `document.querySelectorAll(".pai-fs-controls button")[1].click(); document.querySelectorAll(".pai-fs-controls button")[1].click();` (A+ 2회)
4. `browser_evaluate` → fontSize 재측정. Expected: 기본값 × 1.10 (±1px)
5. `browser_navigate` → `https://comeddy.github.io/pai-playbook/en/pillar-1/` (언어 전환 상당). `browser_evaluate` → fontSize. Expected: 110% 유지, `document.documentElement.dataset.fs === "110"`
6. `browser_evaluate` → A− 2회 클릭 후 `document.documentElement.dataset.fs`. Expected: `undefined` (100% 원복) — 세션 종료(`stop_browser_session`)

- [ ] **Step 4: 결과 보고**

측정값(전/후 px, 유지 여부)을 사용자에게 보고. 실패 시 원인 파악 전 수정 금지(systematic-debugging).
