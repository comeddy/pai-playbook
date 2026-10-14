#!/usr/bin/env python3
"""갱신 경로 등록부(refresh.yml) 검사 — 갱신 주체 없이 조용히 낡는 페이지를 배포 단계에서 막는다.

배경: docs/news.md는 생성 후 갱신 경로가 없어 원천 블로그 글 4건이 3주간 누락됐다(2026-10-14).
메타 줄은 책임자만, staleness 배지는 자기 신고 날짜만 본다 — "무엇이 갱신을 촉발하는가"는
어디에도 선언되지 않았다. 이 검사는 그 선언을 강제한다.

규칙:
  1. mkdocs.yml nav의 모든 .md(한국어 원본)는 refresh.yml에 항목이 있어야 하고, 그 역도 성립.
  2. mode는 routine / owner / event 중 하나, by·trigger는 빈 값 금지.
  3. mode: routine → runbook 파일이 존재하고, 그 runbook이 docs/<page>를 언급해야 한다
     (루틴이 실제로 그 페이지를 다루는지 — news.md 누락의 직접 원인).
  4. source가 있으면 rss(http/https URL)·since(YYYY-MM-DD)·grace_days(0 이상 정수) 필수,
     exclude 항목은 url과 reason(제외 사유)이 모두 있어야 한다 — 이유 없는 제외는 누락과 구별되지 않는다.

사용:
  python3 scripts/check_refresh_paths.py    # 위반 시 exit 1
"""
import datetime
import pathlib
import sys

import yaml

from check_nav_index_sync import nav_targets

ROOT = pathlib.Path(__file__).resolve().parent.parent
MKDOCS = ROOT / "mkdocs.yml"
REGISTRY = ROOT / "refresh.yml"
MODES = ("routine", "owner", "event")


def load_registry(text: str) -> dict:
    data = yaml.safe_load(text) or {}
    pages = data.get("pages")
    if not isinstance(pages, dict):
        sys.exit("오류: refresh.yml에 'pages:' 매핑이 없음")
    return pages


def validate(nav: list, pages: dict, root: pathlib.Path = ROOT) -> list:
    """위반 메시지 목록 반환 (빈 목록 = 통과)."""
    errors = []
    nav_set, reg_set = set(nav), set(pages)
    for p in sorted(nav_set - reg_set):
        errors.append(f"{p}: nav에 있는데 refresh.yml에 갱신 경로가 없음 — mode/by/trigger를 선언할 것")
    for p in sorted(reg_set - nav_set):
        errors.append(f"{p}: refresh.yml에만 있음 — nav에서 삭제됐거나 오탈자")

    for page, e in sorted(pages.items()):
        if not isinstance(e, dict):
            errors.append(f"{page}: 항목이 매핑이 아님")
            continue
        mode = e.get("mode")
        if mode not in MODES:
            errors.append(f"{page}: mode '{mode}'는 {'/'.join(MODES)} 중 하나여야 함")
        for key in ("by", "trigger"):
            if not str(e.get(key) or "").strip():
                errors.append(f"{page}: {key} 비어 있음 — 갱신 주체·촉발 조건을 적을 것")
        if mode == "routine":
            rb = e.get("runbook")
            rb_path = root / rb if rb else None
            if not rb_path or not rb_path.is_file():
                errors.append(f"{page}: mode routine인데 runbook 파일이 없음 ({rb})")
            elif f"docs/{page}" not in rb_path.read_text(encoding="utf-8"):
                errors.append(f"{page}: runbook {rb}가 docs/{page}를 언급하지 않음 — 루틴이 이 페이지를 다루지 않는다")
        src = e.get("source")
        if src is not None:
            if not isinstance(src, dict):
                errors.append(f"{page}: source가 매핑이 아님")
                continue
            if not str(src.get("rss", "")).startswith(("http://", "https://")):
                errors.append(f"{page}: source.rss가 http(s) URL이 아님")
            since = src.get("since")
            try:
                datetime.date.fromisoformat(str(since))
            except ValueError:
                errors.append(f"{page}: source.since '{since}'가 YYYY-MM-DD가 아님")
            g = src.get("grace_days")
            if not isinstance(g, int) or isinstance(g, bool) or g < 0:
                errors.append(f"{page}: source.grace_days는 0 이상 정수여야 함")
            for x in src.get("exclude") or []:
                if not (isinstance(x, dict) and str(x.get("url", "")).startswith("http")
                        and str(x.get("reason") or "").strip()):
                    errors.append(f"{page}: source.exclude 항목에 url·reason이 모두 필요함 ({x})")
        msd = e.get("max_silence_days")
        if msd is not None and (not isinstance(msd, int) or isinstance(msd, bool) or msd <= 0):
            errors.append(f"{page}: max_silence_days는 양의 정수여야 함")
    return errors


def main():
    nav = nav_targets(MKDOCS.read_text(encoding="utf-8"))
    pages = load_registry(REGISTRY.read_text(encoding="utf-8"))
    errors = validate(nav, pages)
    modes = {}
    for e in pages.values():
        if isinstance(e, dict):
            modes[e.get("mode")] = modes.get(e.get("mode"), 0) + 1
    watched = sum(1 for e in pages.values() if isinstance(e, dict) and e.get("source"))
    print(f"갱신 경로 {len(pages)}개 · " + " · ".join(f"{m} {n}" for m, n in sorted(modes.items(), key=str))
          + f" · 소스 감시 {watched}개")
    for msg in errors:
        print(f"⚠️ {msg}")
    if errors:
        sys.exit(1)
    print("OK — nav의 모든 페이지에 갱신 경로가 선언됨")


if __name__ == "__main__":
    main()
