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
import sys

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
    """선두 frontmatter 블록('---' ~ '---') 안의 ko_hash만 인정한다.

    반환: (hash|None, reason) — reason은 'ok' / 'frontmatter 없음' / 'ko_hash 없음'.
    원인을 구분해야 수정 안내가 정확하다(frontmatter 자체가 없는 것과 키 미기재는 다른 실수).
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "frontmatter 없음"
    for line in lines[1:]:
        if line.strip() == "---":
            return None, "ko_hash 없음"
        m = RE_KO_HASH.match(line.strip())
        if m:
            return m.group(1), "ok"
    return None, "ko_hash 없음"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hash", metavar="FILE", help="해당 파일의 blob 해시만 출력하고 종료")
    args = ap.parse_args()
    if args.hash:
        try:
            print(blob_hash(pathlib.Path(args.hash)))
        except OSError as e:
            print(f"오류: {args.hash} 를 읽을 수 없음 ({e.__class__.__name__}: {e})", file=sys.stderr)
            sys.exit(2)
        return

    gha = os.environ.get("GITHUB_ACTIONS") == "true"
    rows = []
    # rglob: 하위 디렉터리 문서도 검사 대상 — 비재귀 glob은 신규 하위 폴더를 조용히 누락시킨다
    for src in sorted(DOCS.rglob("*.md")):
        if is_translation(src):
            continue
        src_name = str(src.relative_to(DOCS))
        try:
            cur = blob_hash(src)
        except OSError:
            # 손상 파일 1개가 검사 전체를 죽이지 않도록 격리 (정책상 exit 0은 유지)
            for lang in LANGS:
                rows.append((src_name, lang, "원본 읽기 실패"))
            continue
        for lang in LANGS:
            variant = src.with_name(f"{src.stem}.{lang}.md")
            if not variant.exists():
                status = "누락"
            else:
                try:
                    rec, reason = recorded_hash(variant)
                except (OSError, UnicodeDecodeError):
                    rec, reason = None, "읽기 실패"
                if rec is None:
                    status = reason
                elif rec != cur:
                    status = "뒤처짐"
                else:
                    status = "OK"
            rows.append((src_name, lang, status))
            if status != "OK" and gha:
                target = variant.name if variant.exists() else src.name
                print(f"::warning file=docs/{target}::{src_name} 번역({lang}) {status} — "
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
