#!/usr/bin/env python3
"""Staleness 검사·배지 주입 — maintenance.md의 갱신 주기 규칙을 CI에서 강제한다.

규칙 (docs/maintenance.md#staleness-규칙):
  volatility 높음 → 1개월 / 중간 → 3개월 / 낮음 → 6개월
  updated(YYYY-MM)가 기준 개월 수를 초과하면 페이지 상단에 '⏳ 검토 필요' 배지.

사용:
  python3 scripts/check_staleness.py --check              # 리포트만 (항상 exit 0)
  python3 scripts/check_staleness.py --inject             # stale 페이지에 배지 주입 (CI 빌드 직전용, 커밋 금지)
  python3 scripts/check_staleness.py --check --today 2027-01   # 날짜 오버라이드 (테스트용)

주입된 배지는 빌드 산출물에만 존재한다 — CI 워크스페이스에서 mkdocs build 직전에 실행되고
저장소에는 커밋되지 않는다. 주간 cron 재배포가 푸시 없이도 배지를 최신으로 유지한다.

번역 파일(`*.en.md`/`*.zh.md`/`*.ja.md`)은 검사하지 않으며, 배지는 존재하는 변형에 해당 언어로 함께 주입된다.
"""
import argparse
import datetime
import pathlib
import re
import sys

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"

# maintenance.md의 주기 규칙과 반드시 일치시킬 것
THRESHOLD_MONTHS = {"높음": 1, "중간": 3, "낮음": 6}

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

RE_UPDATED = re.compile(r"(?:updated|최종 갱신):\s*(\d{4})-(\d{2})")
RE_VOLATILITY = re.compile(r"volatility:\s*(높음|중간|낮음)")


def iter_with_fence(lines):
    """각 라인을 (line, in_fence)로 순회. ```와 ~~~ 펜스 모두 인식하고,
    여는 구분자를 기억해 ~~~ 블록 안의 ```가 상태를 뒤집지 않게 한다.
    펜스 구분자 라인 자체도 in_fence=True로 취급."""
    fence = None
    for line in lines:
        stripped = line.lstrip()
        if fence is None and (stripped.startswith("```") or stripped.startswith("~~~")):
            fence = stripped[:3]
            yield line, True
        elif fence is not None and stripped.startswith(fence):
            fence = None
            yield line, True
        else:
            yield line, fence is not None


def parse_page(path: pathlib.Path):
    """페이지 메타데이터 파싱. 헤더(상단)가 푸터보다 먼저 매칭되도록 첫 매치를 쓴다.

    주의: maintenance.md의 '표준 템플릿' 코드 블록에 placeholder 메타데이터가 있으므로
    코드 펜스(``` 및 ~~~) 내부는 제외하고 스캔한다.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    updated = volatility = None
    for line, in_fence in iter_with_fence(lines):
        if in_fence:
            continue
        if updated is None:
            m = RE_UPDATED.search(line)
            if m:
                updated = (int(m.group(1)), int(m.group(2)))
        if volatility is None:
            m = RE_VOLATILITY.search(line)
            if m:
                volatility = m.group(1)
        if updated and volatility:
            break
    return updated, volatility


def is_translation(path: pathlib.Path) -> bool:
    """index.en.md처럼 언어 suffix가 붙은 번역 파일인지 판별."""
    suf = path.suffixes
    return len(suf) >= 2 and suf[-2].lstrip(".") in LANGS


def months_elapsed(updated, today):
    return (today[0] - updated[0]) * 12 + (today[1] - updated[1])


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="리포트만 출력")
    ap.add_argument("--inject", action="store_true", help="stale 페이지에 배지 주입")
    ap.add_argument("--today", metavar="YYYY-MM", help="현재 연월 오버라이드 (테스트용)")
    args = ap.parse_args()
    if not (args.check or args.inject):
        ap.error("--check 또는 --inject 중 하나는 필요")

    if args.today:
        try:
            y, m = args.today.split("-")
            today = (int(y), int(m))
            if not 1 <= today[1] <= 12:
                raise ValueError
        except ValueError:
            ap.error("--today는 YYYY-MM 형식이어야 함 (월 01~12)")
    else:
        now = datetime.date.today()
        today = (now.year, now.month)

    rows, missing = [], []
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

    print(f"기준일: {today[0]}-{today[1]:02d}")
    print(f"{'페이지':<18} {'updated':<9} {'volatility':<10} {'기준(월)':<8} {'경과(월)':<8} 상태")
    for name, upd, vol, th, el, stale in rows:
        mark = f"{BADGE_MARK}" + (" → 배지 주입" if args.inject else "") if stale else "OK"
        print(f"{name:<18} {upd:<9} {vol:<10} {th:<8} {el:<8} {mark}")
    for name, why in missing:
        print(f"{name:<18} ⚠️ 메타데이터 {why} — maintenance 규칙 위반, 수동 확인 필요")

    stale_count = sum(1 for r in rows if r[5])
    print(f"\nstale: {stale_count} / {len(rows)}" + (f", 메타데이터 누락: {len(missing)}" if missing else ""))
    # 배포를 막지 않는다 — 배지가 곧 알림이다. 메타데이터 누락만 실패 처리(--check 시).
    if args.check and missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
