#!/usr/bin/env python3
"""nav ↔ 홈 '페이지 목록' 동기화 검사 — 새 페이지가 nav에만 추가되고
홈 목록에서 누락되는 드리프트를 CI에서 잡는다 (issue #5).

규칙: mkdocs.yml nav의 모든 .md 대상(index.md 자신 제외)은
docs/index.md의 '## 페이지 목록' 섹션에 링크로 존재해야 하고, 그 역도 성립.
한국어 원본만 검사한다 — 번역본 동기화는 ko_hash 체계가 담당.

사용:
  python3 scripts/check_nav_index_sync.py    # 불일치 시 exit 1
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MKDOCS = ROOT / "mkdocs.yml"
INDEX = ROOT / "docs" / "index.md"


def nav_targets(mkdocs_text: str):
    """nav: 블록의 .md 대상 목록 (들여쓰기 텍스트 파싱 —
    mkdocs.yml은 !!python 태그 때문에 yaml.safe_load 불가)."""
    lines = mkdocs_text.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.rstrip() == "nav:")
    except StopIteration:
        sys.exit("오류: mkdocs.yml에서 'nav:' 블록을 찾지 못함")
    targets = []
    for line in lines[start + 1:]:
        if line.strip() and not line.startswith(" "):  # 다음 최상위 키
            break
        m = re.match(r"\s+-\s+.*?:\s*(\S+\.md)\s*$", line)
        if m:
            targets.append(m.group(1))
    return targets


def index_list_targets(index_text: str):
    """'## 페이지 목록' 섹션 안의 '- [...](*.md)' 링크 대상 목록."""
    m = re.search(r"^## 페이지 목록\n(.*?)(?=^## |\Z)", index_text, re.M | re.S)
    if not m:
        sys.exit("오류: docs/index.md에서 '## 페이지 목록' 섹션을 찾지 못함 — 섹션 제목이 바뀌었으면 이 스크립트도 갱신할 것")
    return re.findall(r"^- \[[^\]]+\]\(([^)#]+\.md)\)", m.group(1), re.M)


def compare(nav: list, index_list: list):
    """(누락, 잉여) 집합 반환 — 누락 = nav에 있는데 목록에 없음."""
    nav_set = set(nav) - {"index.md"}  # 홈 자신은 목록 대상 아님
    idx_set = set(index_list)
    return sorted(nav_set - idx_set), sorted(idx_set - nav_set)


def main():
    nav = nav_targets(MKDOCS.read_text(encoding="utf-8"))
    idx = index_list_targets(INDEX.read_text(encoding="utf-8"))
    missing, extra = compare(nav, idx)
    print(f"nav 페이지 {len(set(nav)) - 1}개 · 홈 페이지 목록 {len(set(idx))}개")
    for f in missing:
        print(f"⚠️ 홈 '페이지 목록' 누락: {f} — nav에는 있음. docs/index.md(4개 언어) 목록에 추가할 것")
    for f in extra:
        print(f"⚠️ 홈 '페이지 목록'에만 존재: {f} — nav에 없음 (오탈자 또는 삭제된 페이지)")
    if missing or extra:
        sys.exit(1)
    print("OK — nav ↔ 홈 페이지 목록 일치")


if __name__ == "__main__":
    main()
