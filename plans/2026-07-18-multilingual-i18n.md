# 다국어(ko/en/zh/ja) 확장 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** pai-playbook(한국어 9페이지)을 mkdocs-static-i18n suffix 방식으로 영어·중국어·일본어까지 4개 언어로 확장하고, `ko_hash` 기반 번역 동기화 추적 + 용어집 + translate-sync 스킬로 1인 운영 체계를 구축한다.

**Architecture:** 한국어가 기본 언어로 루트 URL을 유지하고, 번역은 `docs/<page>.<lang>.md` suffix 파일로 `/en/`, `/zh/`, `/ja/`에 빌드된다. 기존 staleness 자동화는 한국어 원본만 검사하도록 수정하되 배지는 언어 변형에도 주입한다. 번역 신선도는 각 번역 파일 frontmatter의 `ko_hash`(원본 git blob 해시)로 추적하고 CI는 경고만 낸다.

**Tech Stack:** MkDocs 1.6 + Material 9.5, mkdocs-static-i18n(suffix 구조), Python 3.9+(스크립트), pytest(스크립트 테스트, 로컬 전용), GitHub Actions Pages.

**Spec:** `specs/2026-07-18-multilingual-i18n-design.md`

## Global Constraints

- 지원 언어: ko(기본, 루트 URL 유지) / en / zh(간체) / ja. suffix 패턴은 `<page>.<lang>.md` 고정.
- 의존성: `mkdocs-material>=9.5,<10` (기존), `mkdocs-static-i18n>=1.2,<2` (신규). 그 외 런타임 의존성 추가 금지.
- 한국어 배지 리터럴 `!!! warning "⏳ 검토 필요"` 및 한국어 배지 본문은 **바이트 단위로 기존과 동일**해야 한다 — `docs/maintenance.md` 규칙 표와의 계약.
- `check_translation_sync.py`는 **항상 exit 0** (배포 차단 없음 — 확정 정책).
- 모든 커밋 전 `mkdocs build --strict` 통과 필수. 산출물 디렉터리는 스크래치패드 사용(`--site-dir`), 저장소에 site/ 커밋 금지.
- 설계·계획 문서는 저장소 루트 `specs/`, `plans/`에 둔다 (docs/는 MkDocs 소스라 nav 밖 파일이 strict 빌드를 깨움).
- 커밋 메시지는 기존 저장소 관례(한국어 요약) + `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` 푸터.
- pytest는 `requirements.txt`에 추가하지 않는다(문서 빌드에 불필요). 로컬에 없으면 `pip install pytest`.

## File Structure

| 파일 | 책임 | 작업 |
|------|------|------|
| `scripts/check_staleness.py` | staleness 검사·배지 주입 (한국어 원본만 검사, 배지는 4개 언어) | Task 1 수정 |
| `scripts/check_translation_sync.py` | ko_hash 비교 리포트 + GHA warning + `--hash` 헬퍼 | Task 2 신규 |
| `tests/conftest.py`, `tests/test_check_staleness.py`, `tests/test_translation_sync.py` | 스크립트 단위 테스트 | Task 1·2 신규 |
| `mkdocs.yml` | i18n 플러그인·nav_translations·검색 언어 | Task 3 수정 |
| `requirements.txt` | 플러그인 의존성 | Task 3 수정 |
| `.github/workflows/deploy-docs.yml` | sync 검사 스텝 추가 | Task 3 수정 |
| `i18n/glossary.md` | 번역 규칙·용어집 (빌드 미포함) | Task 4 신규 |
| `.claude/skills/translate-sync/SKILL.md` | 번역 동기화 표준 절차 | Task 5 신규 |
| `docs/*.en.md` ×9 | 영어 번역 | Task 6 신규 |
| `docs/*.zh.md` ×9 | 중국어 번역 | Task 7 신규 |
| `docs/*.ja.md` ×9 | 일본어 번역 | Task 8 신규 |

대상 9페이지: `index`, `pillar-1`, `pillar-2`, `pillar-3`, `pillar-4`, `pillar-5`, `decisions`, `radar`, `maintenance`

---

### Task 1: check_staleness.py의 i18n 대응

번역 suffix 파일이 추가되는 순간 현재 스크립트는 "메타데이터 누락"으로 CI를 깨뜨린다(`--check`가 exit 1). 검사 대상에서 번역 파일을 제외하고, stale 시 배지를 존재하는 언어 변형에도 해당 언어로 주입한다.

**Files:**
- Modify: `scripts/check_staleness.py`
- Create: `tests/conftest.py`
- Test: `tests/test_check_staleness.py`

**Interfaces:**
- Produces: `is_translation(path: pathlib.Path) -> bool` (Task 2가 동일 시그니처로 자체 복제), `inject_badge(path, lang: str, volatility: str, updated: tuple, elapsed: int, threshold: int) -> bool`, 모듈 상수 `LANGS = ("en", "zh", "ja")`
- Consumes: 없음 (첫 작업)

- [ ] **Step 1: 테스트 스캐폴드 + 실패하는 테스트 작성**

`tests/conftest.py`:

```python
import pathlib
import sys

# scripts/는 패키지가 아니므로 경로를 직접 추가한다
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
```

`tests/test_check_staleness.py`:

```python
import pathlib
import sys

import check_staleness as cs


def test_is_translation():
    assert cs.is_translation(pathlib.Path("index.en.md"))
    assert cs.is_translation(pathlib.Path("pillar-1.zh.md"))
    assert cs.is_translation(pathlib.Path("radar.ja.md"))
    assert not cs.is_translation(pathlib.Path("index.md"))
    assert not cs.is_translation(pathlib.Path("pillar-1.md"))


def test_inject_badge_language_template(tmp_path):
    p = tmp_path / "index.ja.md"
    p.write_text("---\nko_hash: abc\n---\n# タイトル\n\n本文\n", encoding="utf-8")
    changed = cs.inject_badge(p, "ja", "중간", (2026, 1), 6, 3)
    text = p.read_text(encoding="utf-8")
    assert changed is True
    assert '!!! warning "⏳ 要レビュー"' in text
    # H1 바로 아래에 주입 (frontmatter 위가 아님)
    assert text.index("# タイトル") < text.index("⏳ 要レビュー")
    # 멱등성: 두 번째 호출은 no-op
    assert cs.inject_badge(p, "ja", "중간", (2026, 1), 6, 3) is False


def test_inject_badge_ko_literal_unchanged(tmp_path):
    """한국어 배지는 기존 리터럴과 완전히 동일해야 한다 (maintenance.md 계약)."""
    p = tmp_path / "index.md"
    p.write_text("# 제목\n\n본문\n", encoding="utf-8")
    cs.inject_badge(p, "ko", "중간", (2026, 1), 6, 3)
    text = p.read_text(encoding="utf-8")
    expected = (
        '\n!!! warning "⏳ 검토 필요"\n'
        "    이 페이지의 updated(2026-01)가 volatility "
        "'중간' 기준(3개월)을 3개월 초과했습니다. "
        "내용 검토 후 `updated`를 갱신하세요. "
        "([갱신 규칙](maintenance.md))\n"
    )
    assert expected in text


def test_main_skips_translation_files(tmp_path, monkeypatch, capsys):
    """번역 파일은 메타데이터가 없어도 검사 대상이 아니다 → exit 1 안 됨."""
    (tmp_path / "index.md").write_text(
        "# 홈\n_최종 갱신: 2026-07 · owner: x · volatility: 낮음_\n", encoding="utf-8"
    )
    (tmp_path / "index.en.md").write_text("# Home\n", encoding="utf-8")  # 메타데이터 없음
    monkeypatch.setattr(cs, "DOCS", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_staleness.py", "--check", "--today", "2026-07"])
    cs.main()  # 번역 파일이 검사되면 missing → sys.exit(1) → SystemExit로 테스트 실패
    out = capsys.readouterr().out
    assert "index.en.md" not in out
    assert "index.md" in out


def test_inject_into_existing_variants(tmp_path, monkeypatch):
    """stale 한국어 페이지의 언어 변형에도 해당 언어 배지가 주입된다."""
    (tmp_path / "index.md").write_text(
        "# 홈\n_최종 갱신: 2025-01 · owner: x · volatility: 높음_\n", encoding="utf-8"
    )
    (tmp_path / "index.en.md").write_text("---\nko_hash: abc\n---\n# Home\n", encoding="utf-8")
    # zh/ja 변형은 없음 — 없어도 에러 없이 건너뛰어야 한다
    monkeypatch.setattr(cs, "DOCS", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_staleness.py", "--inject", "--today", "2026-07"])
    cs.main()
    assert '!!! warning "⏳ 검토 필요"' in (tmp_path / "index.md").read_text(encoding="utf-8")
    assert '!!! warning "⏳ Review needed"' in (tmp_path / "index.en.md").read_text(encoding="utf-8")
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `python3 -m pytest tests/test_check_staleness.py -v`
Expected: FAIL — `AttributeError: module 'check_staleness' has no attribute 'is_translation'` (및 `inject_badge()` 시그니처 불일치 TypeError)

- [ ] **Step 3: check_staleness.py 수정**

3a. 모듈 상단 상수 블록 — 기존 `BADGE_MARK`/`BADGE_GUARD` 정의(27~30행)를 다음으로 교체:

```python
# 번역 파일 언어 suffix — 검사·메타데이터 강제는 한국어 원본만, 배지는 변형에도 주입
LANGS = ("en", "zh", "ja")

# 언어별 배지 템플릿. 멱등성 가드는 admonition 첫 줄 전체 형태로 판별한다 —
# maintenance.md 본문(규칙 표)에 "⏳ 검토 필요" 리터럴이 존재하므로 제목 단독 검사는
# 영구 스킵 버그가 된다. ko 리터럴은 maintenance.md 규칙 표와의 계약이므로 변경 금지.
BADGE_TITLE = {
    "ko": "⏳ 검토 필요",
    "en": "⏳ Review needed",
    "zh": "⏳ 需要复核",
    "ja": "⏳ 要レビュー",
}
VOL_LABEL = {
    "ko": {"높음": "높음", "중간": "중간", "낮음": "낮음"},
    "en": {"높음": "high", "중간": "medium", "낮음": "low"},
    "zh": {"높음": "高", "중간": "中", "낮음": "低"},
    "ja": {"높음": "高", "중간": "中", "낮음": "低"},
}
BADGE_BODY = {
    "ko": (
        "    이 페이지의 updated({u})가 volatility "
        "'{v}' 기준({t}개월)을 {o}개월 초과했습니다. "
        "내용 검토 후 `updated`를 갱신하세요. "
        "([갱신 규칙](maintenance.md))\n"
    ),
    "en": (
        "    This page's updated ({u}) exceeds the volatility '{v}' "
        "threshold ({t} months) by {o} month(s). The Korean source needs review; "
        "refresh `updated` after syncing. ([update rules](maintenance.md))\n"
    ),
    "zh": (
        "    本页的 updated（{u}）已超出 volatility“{v}”标准（{t} 个月）{o} 个月。"
        "请以韩文原文为准复核内容后更新 `updated`。（[更新规则](maintenance.md)）\n"
    ),
    "ja": (
        "    このページの updated（{u}）は volatility「{v}」基準（{t}か月）を"
        "{o}か月超過しています。韓国語原文を確認のうえ `updated` を更新してください。"
        "（[更新ルール](maintenance.md)）\n"
    ),
}
# 리포트 출력용 하위 호환 별칭
BADGE_MARK = BADGE_TITLE["ko"]
```

3b. `months_elapsed()` 바로 위(또는 아래)에 추가:

```python
def is_translation(path: pathlib.Path) -> bool:
    """index.en.md처럼 언어 suffix가 붙은 번역 파일인지 판별."""
    suf = path.suffixes
    return len(suf) >= 2 and suf[-2].lstrip(".") in LANGS
```

3c. `inject_badge()` 전체 교체:

```python
def inject_badge(path: pathlib.Path, lang: str, volatility: str, updated, elapsed: int, threshold: int):
    """H1 바로 아래에 해당 언어의 Material admonition 배지 주입. 이미 있으면 건너뜀(멱등)."""
    text = path.read_text(encoding="utf-8")
    guard = f'!!! warning "{BADGE_TITLE[lang]}"'
    if guard in text:
        return False
    badge = f"\n{guard}\n" + BADGE_BODY[lang].format(
        u=f"{updated[0]}-{updated[1]:02d}",
        v=VOL_LABEL[lang][volatility],
        t=threshold,
        o=elapsed - threshold,
    )
    lines = text.splitlines(keepends=True)
    for i, (line, in_fence) in enumerate(iter_with_fence(lines)):
        # 코드 블록 안의 '# 주석'을 H1로 오인하지 않도록 펜스 인식 탐색
        if not in_fence and line.startswith("# "):
            lines.insert(i + 1, badge)
            path.write_text("".join(lines), encoding="utf-8")
            return True
    # H1이 없으면 맨 앞에
    path.write_text(badge + text, encoding="utf-8")
    return True
```

3d. `main()`의 glob 루프 — 시작부에 번역 파일 스킵 추가, inject 분기를 변형 주입으로 확장:

```python
    for path in sorted(DOCS.glob("*.md")):
        if is_translation(path):
            continue
        updated, volatility = parse_page(path)
        if not updated or not volatility:
            missing.append((path.name, "updated 누락" if not updated else "volatility 누락"))
            continue
        threshold = THRESHOLD_MONTHS[volatility]
        elapsed = months_elapsed(updated, today)
        stale = elapsed > threshold
        rows.append((path.name, f"{updated[0]}-{updated[1]:02d}", volatility, threshold, elapsed, stale))
        if stale and args.inject:
            inject_badge(path, "ko", volatility, updated, elapsed, threshold)
            # 존재하는 언어 변형에도 해당 언어 배지 주입 (독자가 어느 언어로 봐도 인지)
            for lang in LANGS:
                variant = path.with_name(f"{path.stem}.{lang}.md")
                if variant.exists():
                    inject_badge(variant, lang, volatility, updated, elapsed, threshold)
```

3e. 모듈 docstring(2~15행)에 한 줄 추가 — "번역 파일(`*.en.md`/`*.zh.md`/`*.ja.md`)은 검사하지 않으며, 배지는 존재하는 변형에 해당 언어로 함께 주입된다."

- [ ] **Step 4: 테스트 통과 확인**

Run: `python3 -m pytest tests/test_check_staleness.py -v`
Expected: 5 passed

- [ ] **Step 5: 실데이터 회귀 확인 (번역 파일 없는 현재 상태에서 출력 불변)**

Run: `python3 scripts/check_staleness.py --check`
Expected: 기존과 동일한 9행 리포트, exit 0. (수정 전 출력을 미리 저장해 diff 비교: `git stash && python3 scripts/check_staleness.py --check > /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/before.txt; git stash pop` 후 비교)

- [ ] **Step 6: 커밋**

```bash
git add scripts/check_staleness.py tests/conftest.py tests/test_check_staleness.py
git commit -m "staleness: 번역 suffix 파일 제외 + 언어별 배지 템플릿 (i18n 선행 작업)"
```

### Task 2: check_translation_sync.py 신규 작성

번역 파일 frontmatter의 `ko_hash`와 현재 한국어 원본의 git blob 해시를 비교해 리포트한다. git 바이너리 없이 순수 파이썬으로 blob 해시를 계산한다(CI·로컬 어디서든 동작). 항상 exit 0.

**Files:**
- Create: `scripts/check_translation_sync.py`
- Test: `tests/test_translation_sync.py`

**Interfaces:**
- Consumes: Task 1의 suffix 규칙과 동일한 `LANGS`/`is_translation` (독립 실행을 위해 자체 정의 — scripts/는 패키지가 아니라 상호 import하지 않는다)
- Produces: CLI `--hash FILE` (blob 해시 stdout 출력 — Task 5 스킬과 Task 6~8 번역 절차가 사용), 리포트 상태 문자열 `OK` / `누락` / `ko_hash 없음` / `뒤처짐`

- [ ] **Step 1: 실패하는 테스트 작성**

`tests/test_translation_sync.py`:

```python
import sys

import check_translation_sync as ts


def test_blob_hash_matches_git(tmp_path):
    """git hash-object와 동일한 값이어야 한다 — 빈 파일의 blob SHA-1은 잘 알려진 상수."""
    p = tmp_path / "empty.md"
    p.write_bytes(b"")
    assert ts.blob_hash(p) == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"


def test_recorded_hash_frontmatter_only(tmp_path):
    """선두 frontmatter 블록 안의 ko_hash만 인정한다."""
    h = "a" * 40
    p = tmp_path / "index.en.md"
    p.write_text(f"---\nko_hash: {h}\n---\n# Home\n", encoding="utf-8")
    assert ts.recorded_hash(p) == h

    # 본문에 있는 ko_hash 언급은 무시
    p2 = tmp_path / "index.ja.md"
    p2.write_text(f"# ホーム\n\nko_hash: {h}\n", encoding="utf-8")
    assert ts.recorded_hash(p2) is None


def test_report_statuses(tmp_path, monkeypatch, capsys):
    src = tmp_path / "index.md"
    src.write_text("# 홈\n", encoding="utf-8")
    cur = ts.blob_hash(src)
    # en: 최신, zh: 뒤처짐, ja: 누락
    (tmp_path / "index.en.md").write_text(f"---\nko_hash: {cur}\n---\n# Home\n", encoding="utf-8")
    (tmp_path / "index.zh.md").write_text(f"---\nko_hash: {'b' * 40}\n---\n# 首页\n", encoding="utf-8")
    monkeypatch.setattr(ts, "DOCS", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_translation_sync.py"])
    ts.main()  # 어떤 상태여도 SystemExit 없이 정상 종료해야 한다 (항상 exit 0 정책)
    out = capsys.readouterr().out
    assert "OK" in out and "뒤처짐" in out and "누락" in out
    assert "비동기: 2 / 3" in out


def test_hash_helper(tmp_path, monkeypatch, capsys):
    p = tmp_path / "x.md"
    p.write_bytes(b"")
    monkeypatch.setattr(sys, "argv", ["check_translation_sync.py", "--hash", str(p)])
    ts.main()
    assert capsys.readouterr().out.strip() == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `python3 -m pytest tests/test_translation_sync.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'check_translation_sync'`

- [ ] **Step 3: 스크립트 구현**

`scripts/check_translation_sync.py` 전체:

```python
#!/usr/bin/env python3
"""번역 동기화 검사 — 각 번역 파일 frontmatter의 ko_hash(번역 시점 원본 blob 해시)와
현재 한국어 원본의 해시를 비교한다.

정책(specs/2026-07-18-multilingual-i18n-design.md): 경고만, 배포 차단 없음 → 항상 exit 0.
GitHub Actions에서는 warning annotation(::warning)을 함께 출력한다.

사용:
  python3 scripts/check_translation_sync.py                      # 전체 리포트
  python3 scripts/check_translation_sync.py --hash docs/index.md # 원본 해시 출력 (번역 frontmatter용)
"""
import argparse
import hashlib
import os
import pathlib
import re

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"
LANGS = ("en", "zh", "ja")
RE_KO_HASH = re.compile(r"^ko_hash:\s*([0-9a-f]{40})\s*$")


def blob_hash(path: pathlib.Path) -> str:
    """git hash-object와 동일한 blob SHA-1 (git 실행 불필요)."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def is_translation(path: pathlib.Path) -> bool:
    """index.en.md처럼 언어 suffix가 붙은 번역 파일인지 판별."""
    suf = path.suffixes
    return len(suf) >= 2 and suf[-2].lstrip(".") in LANGS


def recorded_hash(path: pathlib.Path):
    """선두 frontmatter 블록('---' ~ '---') 안의 ko_hash만 인정한다."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            return None
        m = RE_KO_HASH.match(line.strip())
        if m:
            return m.group(1)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hash", metavar="FILE", help="해당 파일의 blob 해시만 출력하고 종료")
    args = ap.parse_args()
    if args.hash:
        print(blob_hash(pathlib.Path(args.hash)))
        return

    gha = os.environ.get("GITHUB_ACTIONS") == "true"
    rows = []
    for src in sorted(DOCS.glob("*.md")):
        if is_translation(src):
            continue
        cur = blob_hash(src)
        for lang in LANGS:
            variant = src.with_name(f"{src.stem}.{lang}.md")
            if not variant.exists():
                status = "누락"
            elif recorded_hash(variant) is None:
                status = "ko_hash 없음"
            elif recorded_hash(variant) != cur:
                status = "뒤처짐"
            else:
                status = "OK"
            rows.append((src.name, lang, status))
            if status != "OK" and gha:
                target = variant.name if variant.exists() else src.name
                print(f"::warning file=docs/{target}::{src.name} 번역({lang}) {status} — "
                      f"translate-sync 스킬로 동기화하세요")

    print(f"{'원본':<18} {'lang':<5} 상태")
    behind = 0
    for name, lang, status in rows:
        mark = "OK" if status == "OK" else f"⚠️ {status}"
        if status != "OK":
            behind += 1
        print(f"{name:<18} {lang:<5} {mark}")
    print(f"\n비동기: {behind} / {len(rows)}")
    # 정책: 경고만 — 어떤 상태여도 실패하지 않는다 (exit 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `python3 -m pytest tests/ -v`
Expected: 9 passed (Task 1의 5개 + 신규 4개)

- [ ] **Step 5: 실데이터 스모크 (번역 0개 상태)**

Run: `python3 scripts/check_translation_sync.py; echo "exit=$?"`
Expected: 9개 원본 × 3개 언어 = 27행 전부 `⚠️ 누락`, `비동기: 27 / 27`, `exit=0`

- [ ] **Step 6: 커밋**

```bash
git add scripts/check_translation_sync.py tests/test_translation_sync.py
git commit -m "번역 동기화 검사 스크립트 — ko_hash 비교, 경고만 (배포 차단 없음)"
```

---

### Task 3: mkdocs-static-i18n 도입 + CI 스텝

플러그인을 설정하고 번역 파일이 0개인 상태에서 strict 빌드로 4개 언어 트리(fallback)가 생성되는지 검증한다. 인프라를 콘텐츠보다 먼저 검증하는 것이 목적.

**Files:**
- Modify: `mkdocs.yml` (plugins 블록, search lang)
- Modify: `requirements.txt`
- Modify: `.github/workflows/deploy-docs.yml`

**Interfaces:**
- Consumes: Task 2의 `scripts/check_translation_sync.py` (CI 스텝)
- Produces: `/en/`, `/zh/`, `/ja/` URL 트리와 언어 전환 드롭다운 — Task 6~8의 번역 파일이 suffix 규칙대로 자동 편입됨

- [ ] **Step 1: requirements.txt에 플러그인 추가**

```
mkdocs-material>=9.5,<10
mkdocs-static-i18n>=1.2,<2
```

Run: `pip install -r requirements.txt`
Expected: mkdocs-static-i18n 1.2.x 설치 성공

- [ ] **Step 2: mkdocs.yml의 plugins 블록 교체**

기존:

```yaml
plugins:
  - search:
      lang:
        - ko
        - en
```

교체 후 (i18n은 search 뒤에 선언 — 플러그인이 언어별 빌드에서 theme.language와 검색을 자동 재구성):

```yaml
plugins:
  - search:
      lang:
        - ko
        - en
        - ja
        # zh 형태소 분리는 v1 범위 외 (spec YAGNI) — lunr 기본 토크나이저로 수용
  - i18n:
      docs_structure: suffix
      fallback_to_default: true
      languages:
        - locale: ko
          name: 한국어
          default: true
          build: true
        - locale: en
          name: English
          build: true
          site_description: "Physical AI reference asset for AWS Korea SA — architecture direction, AWS mapping, next actions in 5 minutes"
          nav_translations:
            홈: Home
            "P1 · 데이터 수집 & 처리": "P1 · Data Collection & Processing"
            "P2 · 모델 학습 (VLA)": "P2 · Model Training (VLA)"
            "P3 · 시뮬레이션": "P3 · Simulation"
            "P5 · 에이전트 오케스트레이션": "P5 · Agent Orchestration"
            "의사결정 트리": "Decision Trees"
            "Radar (대기열)": "Radar (Queue)"
            "유지보수 규칙": "Maintenance Rules"
        - locale: zh
          name: 中文
          build: true
          site_description: "面向 AWS Korea SA 的 Physical AI 参考资产 — 5 分钟内掌握架构方向、AWS 映射与后续行动"
          nav_translations:
            홈: 首页
            "P1 · 데이터 수집 & 처리": "P1 · 数据采集与处理"
            "P2 · 모델 학습 (VLA)": "P2 · 模型训练 (VLA)"
            "P3 · 시뮬레이션": "P3 · 仿真"
            "P5 · 에이전트 오케스트레이션": "P5 · 智能体编排"
            "의사결정 트리": "决策树"
            "Radar (대기열)": "Radar（队列）"
            "유지보수 규칙": "维护规则"
        - locale: ja
          name: 日本語
          build: true
          site_description: "AWS Korea SA 向け Physical AI リファレンス資産 — アーキテクチャの方向性・AWS マッピング・次のアクションを5分で"
          nav_translations:
            홈: ホーム
            "P1 · 데이터 수집 & 처리": "P1 · データ収集と処理"
            "P2 · 모델 학습 (VLA)": "P2 · モデル学習 (VLA)"
            "P3 · 시뮬레이션": "P3 · シミュレーション"
            "P5 · 에이전트 오케스트레이션": "P5 · エージェントオーケストレーション"
            "의사결정 트리": "意思決定ツリー"
            "Radar (대기열)": "Radar（キュー）"
            "유지보수 규칙": "メンテナンスルール"
```

주의: `"P4 · Sim-to-Real"`은 전 언어 동일 표기라 `nav_translations`에서 생략한다. `search.lang`의 `zh` 미포함이 strict 빌드를 깨면(플러그인이 zh 빌드에서 검색 언어를 요구하는 경우) `zh`를 추가하되, `jieba` 미설치 경고는 수용한다(검색 품질은 범위 외).

- [ ] **Step 3: strict 빌드로 4개 언어 fallback 트리 검증**

Run: `mkdocs build --strict --site-dir /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/site-i18n && ls /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/site-i18n`
Expected: exit 0. 산출물에 `en/ zh/ ja/` 디렉터리 존재, 각 디렉터리에 9페이지(한국어 fallback). 루트는 기존 한국어 그대로.

Run: `grep -c 'alternate' /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/site-i18n/index.html`
Expected: 1 이상 (언어 전환 드롭다운 마크업 존재)

- [ ] **Step 4: deploy-docs.yml에 sync 검사 스텝 추가**

`- run: python scripts/check_staleness.py --check` 앞에 삽입:

```yaml
      # 번역 동기화 검사 — 뒤처진 번역은 warning annotation만 (배포 차단 없음)
      - run: python scripts/check_translation_sync.py
```

- [ ] **Step 5: staleness 스크립트와의 상호작용 회귀 확인**

Run: `python3 scripts/check_staleness.py --check && python3 -m pytest tests/ -q`
Expected: 리포트 9행(번역 파일 미검사), 테스트 9 passed

- [ ] **Step 6: 커밋**

```bash
git add mkdocs.yml requirements.txt .github/workflows/deploy-docs.yml
git commit -m "i18n: mkdocs-static-i18n 도입 (ko 루트 유지, en/zh/ja fallback 빌드) + CI sync 검사"
```

### Task 4: 용어집 i18n/glossary.md

번역 일관성의 단일 소스. 빌드에 포함되지 않는 운영 파일(`docs/` 밖이므로 MkDocs가 보지 않음). 작성 전 9개 페이지를 전수 스캔해 반복 등장 용어를 확정한다.

**Files:**
- Create: `i18n/glossary.md`

**Interfaces:**
- Produces: Task 5 스킬과 Task 6~8 번역 절차가 반드시 로드하는 규칙 문서
- Consumes: `docs/*.md` 9개 (용어 추출 소스)

- [ ] **Step 1: 페이지 전수 스캔으로 용어 후보 추출**

Run: `grep -hoE "(Sim-to-Real|VLA|GA|OXE|DROID|LeRobot|RLDS|Isaac [A-Za-z]+|Cosmos( WFM)?|GR00T|OpenVLA|π0|RT-2-X|AgiBot World|Open X-Embodiment|텔레옵|teleop)" docs/*.md | sort | uniq -c | sort -rn`
Expected: 빈도순 용어 목록 — 아래 초안 표에 누락된 고빈도 용어가 있으면 추가한다.

- [ ] **Step 2: glossary.md 작성**

`i18n/glossary.md` (아래 골격에 Step 1 결과를 반영해 확정):

```markdown
# 번역 용어집 & 규칙 (ko → en/zh/ja)

빌드 미포함 운영 파일. translate-sync 스킬과 모든 번역 작업이 이 파일을 먼저 로드한다.

## 1. 번역 금지 (원문 유지)

Physical AI, Sim-to-Real, VLA, GA, Radar, TL;DR, L0/L1/L2,
Open X-Embodiment(OXE), DROID, AgiBot World, LeRobot, RLDS,
Isaac Sim, Isaac Lab, SDG, Replicator, Cosmos, Cosmos WFM, GR00T, OpenVLA, π0, RT-2-X,
AWS 서비스명 전부(SageMaker, S3, Batch, ...), 모델·데이터셋·라이선스 이름(CC-BY-4.0 등)

## 2. 고정 역어

| ko | en | zh | ja |
|----|----|----|----|
| 텔레옵 | teleoperation | 遥操作 | テレオペレーション |
| 합성 데이터 | synthetic data | 合成数据 | 合成データ |
| 의사결정 트리 | decision tree | 决策树 | 意思決定ツリー |
| 대기열 | queue | 队列 | キュー |
| 유지보수 규칙 | maintenance rules | 维护规则 | メンテナンスルール |
| 갱신 규칙 | update rules | 更新规则 | 更新ルール |
| 검토 필요 | review needed | 需要复核 | 要レビュー |
| 참조 아키텍처 | reference architecture | 参考架构 | リファレンスアーキテクチャ |
| 사전학습 | pretraining | 预训练 | 事前学習 |
| 파인튜닝 | fine-tuning | 微调 | ファインチューニング |
| 필러 | pillar | 支柱 | ピラー |

(Step 1 스캔 결과에 따라 행 추가)

## 3. 구조 보존 규칙 (기계적 — 위반 시 빌드나 자동화가 깨짐)

- **frontmatter**: 모든 번역 파일은 `---\nko_hash: <40자 hex>\n---`로 시작. 해시는
  `python3 scripts/check_translation_sync.py --hash docs/<원본>.md`로 계산.
- **앵커 링크**: heading을 번역하면 슬러그가 바뀐다 → 본문 내 `#...` 링크를 번역된
  heading에 맞춰 반드시 함께 갱신. 게이트는 `mkdocs build --strict`.
  strict가 통과 못 하면 빌드 산출물의 실제 `<h2 id>`를 읽어 링크를 맞춘다
  (이모지 포함 heading은 사전 계산 슬러그가 자주 틀린다 — 2026-07-11 실측).
- **유지**: 상태 배지(🟢 GA 등)·이모지·인용 마커 `[1]`·코드 블록·URL·표 구조·
  admonition 구문(`!!! warning "..."`)·`<details markdown="1">` 블록은 그대로.
- **페이지 메타데이터 라인**: `_최종 갱신: ... · owner: ... · volatility: ..._`은
  라벨만 번역(en: `_Last updated: ... · owner: ... · volatility: medium_` 식),
  값(연월·owner·수준)은 원본과 동일하게 유지.
- **페이지 간 링크**: `[← index로](index.md)` 같은 상대 링크는 파일명 그대로 둔다
  (플러그인이 언어별로 자동 해석). 링크 텍스트만 번역.

## 4. 문체

- **en**: 간결한 기술 문서체. 불필요한 관사·수동태 줄이기.
- **zh**: 간체(简体). 영문 용어는 원문 유지, 전각 괄호（）사용.
- **ja**: です・ます체. 카타카나 표기는 위 고정 역어 표를 따른다.
- 공통: 원문의 직설적·실무적 톤 유지 ("라이선스가 지뢰밭" 같은 표현은 순화하지 않고
  등가 표현으로 — en: "a licensing minefield").
```

- [ ] **Step 3: 커밋**

```bash
git add i18n/glossary.md
git commit -m "i18n: 번역 용어집 — 금지 용어·고정 역어·구조 보존 규칙·문체"
```

---

### Task 5: translate-sync 프로젝트 스킬

"번역 동기화해줘" 한마디로 탐지→번역→검증까지 수행하는 절차의 코드화.

**Files:**
- Create: `.claude/skills/translate-sync/SKILL.md`

**Interfaces:**
- Consumes: `scripts/check_translation_sync.py` (탐지·해시), `i18n/glossary.md` (규칙)
- Produces: 이후 모든 번역 갱신 세션의 표준 진입점

- [ ] **Step 1: SKILL.md 작성**

`.claude/skills/translate-sync/SKILL.md` 전체:

```markdown
---
name: translate-sync
description: Use when Korean source pages under docs/ have changed and en/zh/ja translations need creating or re-syncing — detects drift via ko_hash, translates only changed files using i18n/glossary.md, and gates on mkdocs build --strict
---

# 번역 동기화 (ko → en/zh/ja)

## 절차 (순서 고정)

1. **탐지**: `python3 scripts/check_translation_sync.py` 실행.
   `OK`가 아닌 (원본, 언어) 쌍만 이후 단계의 대상이다. 전체 재번역 금지.
2. **규칙 로드**: `i18n/glossary.md`를 읽는다. 번역 금지 용어·고정 역어·
   구조 보존 규칙·문체를 그대로 따른다.
3. **번역**: 대상 파일마다
   a. 해시 계산: `python3 scripts/check_translation_sync.py --hash docs/<원본>.md`
   b. `docs/<원본stem>.<lang>.md`를 frontmatter(`ko_hash: <해시>`)부터 작성/갱신.
      '뒤처짐' 상태면 원본의 변경 부분(git diff)을 확인해 해당 부분 위주로 갱신.
   c. heading 번역 시 본문 내 앵커 링크(`#...`)를 함께 갱신.
4. **해시 검증**: `python3 scripts/check_translation_sync.py` 재실행 →
   작업 대상이 전부 `OK`인지 확인.
5. **빌드 게이트**: `mkdocs build --strict --site-dir <scratchpad>/site-check`.
   앵커 오류 시: 산출물의 실제 heading id(`grep '<h[23] id=' <산출물>.html`)를
   읽어 링크를 맞춘다. 사전 계산 슬러그를 신뢰하지 말 것.
6. **커밋 전 확인**: 통과 결과(OK 개수, strict exit 0)를 사용자에게 보여주고
   커밋한다. 실패 상태로 완료 선언 금지.

## 주의

- 배지 admonition(`!!! warning "⏳ ..."`)이 원본에 있으면 그것은 CI 주입분이
  커밋된 사고다 — 번역하지 말고 사용자에게 보고.
- radar.md·maintenance.md의 표는 구조가 곧 데이터다. 열 추가/삭제 금지.
```

- [ ] **Step 2: 스킬 로드 스모크**

새 Claude Code 세션 없이 확인: `cat .claude/skills/translate-sync/SKILL.md` 로 frontmatter가 `---`로 열리고 `name`/`description` 키가 있는지 육안 확인.
Expected: frontmatter 유효 (다음 세션부터 스킬 목록에 노출)

- [ ] **Step 3: 커밋**

```bash
git add .claude/skills/translate-sync/SKILL.md
git commit -m "skill: translate-sync — 번역 동기화 표준 절차 (탐지→용어집→번역→strict 게이트)"
```

### Task 6: 영어 번역 (9페이지)

첫 언어이므로 워크플로우 검증을 겸한다. 이후 zh/ja는 같은 절차의 반복.

**Files:**
- Create: `docs/index.en.md`, `docs/pillar-1.en.md`, `docs/pillar-2.en.md`, `docs/pillar-3.en.md`, `docs/pillar-4.en.md`, `docs/pillar-5.en.md`, `docs/decisions.en.md`, `docs/radar.en.md`, `docs/maintenance.en.md`

**Interfaces:**
- Consumes: `i18n/glossary.md` (Task 4), `--hash` 헬퍼 (Task 2), suffix 빌드 규칙 (Task 3)
- Produces: `/en/` 라이브 콘텐츠. 파일 골격 규약 — 첫 3줄이 `---` / `ko_hash: <40자>` / `---`

- [ ] **Step 1: 용어집 로드 후 9개 파일 번역 생성**

각 원본 파일 `docs/<f>.md`에 대해 (f ∈ {index, pillar-1..5, decisions, radar, maintenance}):

```bash
python3 scripts/check_translation_sync.py --hash docs/<f>.md   # 해시 확보
```

`docs/<f>.en.md` 생성 — 정확한 골격:

```markdown
---
ko_hash: <위 명령의 40자 출력>
---
# <H1 번역>

<본문 전체 번역 — i18n/glossary.md의 금지 용어·고정 역어·구조 보존 규칙·문체 준수>
```

번역 시 기계적 체크(용어집 3장과 동일, 재확인용): 상태 배지·이모지·`[1]` 마커·코드 블록·URL·표 구조 유지 / heading 번역 시 본문 앵커 링크 동시 갱신 / 메타데이터 라인은 라벨만 번역 / 페이지 간 상대 링크 파일명 유지.

- [ ] **Step 2: 동기화 상태 확인**

Run: `python3 scripts/check_translation_sync.py`
Expected: `en` 9행 전부 `OK` (zh/ja 18행은 `누락` — 정상)

- [ ] **Step 3: strict 빌드 게이트**

Run: `mkdocs build --strict --site-dir /tmp/claude-1000/-home-ec2-user-pai-playbook/895b2259-bf14-4fbb-b7cb-0275dfdce536/scratchpad/site-i18n`
Expected: exit 0. 실패 시(대부분 앵커): 산출물 `en/<페이지>/index.html`의 실제 `<h2 id=`/`<h3 id=`를 grep해 본문 링크를 맞추고 재실행. 통과할 때까지 반복.

- [ ] **Step 4: 스팟 체크**

Run: `grep -L "^ko_hash:" docs/*.en.md | head; ls docs/*.en.md | wc -l`
Expected: grep 출력 없음(전 파일 frontmatter 보유), 파일 수 9

Run: `grep -c "지뢰밭\|합니다\|하세요" docs/pillar-1.en.md || true`
Expected: 0 (한국어 잔존 없음 — 다른 파일 2~3개도 무작위 확인)

- [ ] **Step 5: 커밋**

```bash
git add docs/*.en.md
git commit -m "i18n: 영어 번역 9페이지 (ko_hash 동기화, strict 빌드 통과)"
```

---

### Task 7: 중국어(간체) 번역 (9페이지)

**Files:**
- Create: `docs/index.zh.md` ~ `docs/maintenance.zh.md` (9개, Task 6과 동일 목록의 `.zh.md`)

**Interfaces:** Task 6과 동일 (Consumes: glossary/`--hash`/suffix 규칙, Produces: `/zh/` 콘텐츠)

- [ ] **Step 1: 9개 파일 번역 생성** — Task 6 Step 1과 동일 절차. 골격도 동일:

```markdown
---
ko_hash: <40자 해시>
---
# <H1 중국어 번역>

<본문 — 간체, 영문 용어 원문 유지, 전각 괄호（）>
```

- [ ] **Step 2: 동기화 확인** — Run: `python3 scripts/check_translation_sync.py` / Expected: en·zh 18행 `OK`, ja 9행 `누락`

- [ ] **Step 3: strict 빌드 게이트** — Task 6 Step 3과 동일 명령. Expected: exit 0 (앵커 실패 시 동일 복구 절차)

- [ ] **Step 4: 스팟 체크** — Run: `grep -L "^ko_hash:" docs/*.zh.md | head; ls docs/*.zh.md | wc -l` / Expected: grep 출력 없음, 9

- [ ] **Step 5: 커밋**

```bash
git add docs/*.zh.md
git commit -m "i18n: 중국어(간체) 번역 9페이지"
```

---

### Task 8: 일본어 번역 (9페이지)

**Files:**
- Create: `docs/index.ja.md` ~ `docs/maintenance.ja.md` (9개)

**Interfaces:** Task 6과 동일 (Produces: `/ja/` 콘텐츠)

- [ ] **Step 1: 9개 파일 번역 생성** — 동일 절차·골격 (본문: です・ます체, 카타카나는 용어집 고정 역어)

- [ ] **Step 2: 동기화 확인** — Run: `python3 scripts/check_translation_sync.py` / Expected: **27행 전부 `OK`, `비동기: 0 / 27`**

- [ ] **Step 3: strict 빌드 게이트** — 동일 명령. Expected: exit 0

- [ ] **Step 4: 스팟 체크** — Run: `grep -L "^ko_hash:" docs/*.ja.md | head; ls docs/*.ja.md | wc -l` / Expected: grep 출력 없음, 9

- [ ] **Step 5: staleness 배지 통합 확인 (전 언어 주입 리허설)**

Run: `python3 scripts/check_staleness.py --inject --today 2027-06 && git diff --stat docs/ | tail -3 && git checkout -- docs/`
Expected: stale해진 페이지의 ko + en/zh/ja 변형 전부에 배지 주입됨(diff에 4배수 파일), `git checkout`으로 원복 완료 확인

- [ ] **Step 6: 커밋**

```bash
git add docs/*.ja.md
git commit -m "i18n: 일본어 번역 9페이지 — 4개 언어 동기화 완료 (비동기 0/27)"
```

---

### Task 9: 배포 및 라이브 검증

**Files:** 없음 (push + 검증만)

**Interfaces:**
- Consumes: Task 1~8 전부
- Produces: 라이브 4개 언어 사이트

- [ ] **Step 1: push 및 CI 관찰**

```bash
git push origin main
gh run watch --exit-status
```

Expected: deploy-docs 성공. 로그에서 `check_translation_sync.py` 스텝이 `비동기: 0 / 27` 출력 확인.

- [ ] **Step 2: 라이브 URL 4종 점검**

```bash
for p in "" "en/" "zh/" "ja/"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -L "https://comeddy.github.io/pai-playbook/$p")
  echo "/$p -> $code"
done
```

Expected: 4행 전부 200

- [ ] **Step 3: 언어 전환 드롭다운 + 콘텐츠 실물 확인**

```bash
curl -s https://comeddy.github.io/pai-playbook/ | grep -c 'alternate'
curl -s https://comeddy.github.io/pai-playbook/en/pillar-1/ | grep -c "Data Collection"
curl -s https://comeddy.github.io/pai-playbook/ja/ | grep -c "ホーム\|データ"
```

Expected: 각각 1 이상

- [ ] **Step 4: 기존 한국어 URL 회귀 확인**

Run: `for p in "" "pillar-1/" "decisions/" "radar/" "maintenance/"; do curl -s -o /dev/null -w "/$p -> %{http_code}\n" -L "https://comeddy.github.io/pai-playbook/$p"; done`
Expected: 전부 200 (URL 보존 계약 유지)

---

## Self-Review 결과

- **스펙 커버리지**: 스펙 §1(구조/URL)→Task 3·6~8, §2(mkdocs.yml)→Task 3, §3(동기화 추적)→Task 2·3, §4(staleness 수정)→Task 1, §5(용어집+스킬)→Task 4·5, §6(검증)→각 Task 게이트+Task 9, 작업 순서·YAGNI 범위 외 항목 준수 — 누락 없음.
- **타입/시그니처 일관성**: `inject_badge(path, lang, volatility, updated, elapsed, threshold)`(Task 1 정의 = 테스트 사용 일치), `blob_hash`/`recorded_hash`/`--hash`(Task 2 정의 = Task 5·6 사용 일치), suffix 패턴·`LANGS` 튜플 전 Task 동일.
- **placeholder 스캔**: 통과. 유일한 열린 항목(용어집 행 추가)은 Step 1 스캔 명령의 출력을 입력으로 하는 명시적 절차로 정의됨.



