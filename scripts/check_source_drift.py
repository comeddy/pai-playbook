#!/usr/bin/env python3
"""소스 드리프트 감시 — refresh.yml에 source/max_silence_days를 선언한 페이지를 실제 소스와 대조한다.

check_refresh_paths.py가 "갱신 경로가 선언됐는가"를 보는 정적 게이트라면, 이 스크립트는
"그 경로가 실제로 돌고 있는가"를 매일 확인하는 감시자다. 클라우드 루틴은 egress가 막힐 수 있으므로
GitHub Actions(.github/workflows/source-drift.yml)에서 독립적으로 실행한다.

검사:
  - source.rss: 피드 글 중 since 이후 발행 + grace_days 경과 + 페이지에 링크가 없고 exclude에도 없는 글 = 드리프트
  - max_silence_days: 페이지 마지막 커밋이 이 일수를 넘으면 = 루틴 정지 의심

사용:
  python3 scripts/check_source_drift.py            # 리포트, 드리프트 시 exit 1, 소스 접속 실패 시 exit 2
  python3 scripts/check_source_drift.py --issue    # + GitHub 이슈 생성/갱신/종료 (gh CLI, CI용)
  python3 scripts/check_source_drift.py --today 2026-10-14   # 날짜 오버라이드 (테스트용)
"""
import argparse
import datetime
import email.utils
import pathlib
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from check_refresh_paths import REGISTRY, load_registry

ROOT = pathlib.Path(__file__).resolve().parent.parent
ISSUE_TITLE = "[source-drift] 외부 소스 대비 미반영·정지 페이지"
ISSUE_LABEL = "source-drift"


def norm_url(u: str) -> str:
    """퍼센트 인코딩·후행 슬래시·스킴 차이를 흡수한 비교용 URL."""
    u = urllib.parse.unquote(u.strip()).split("#")[0].rstrip("/")
    return re.sub(r"^http://", "https://", u)


def parse_feed(xml_text: str) -> list:
    """RSS 2.0 <item> → [(title, link, date)]. pubDate 없는 글은 제외.
    DTD가 있는 문서는 거부한다 — RSS에는 필요 없고, 엔티티 확장(billion laughs) 경로를 닫는다."""
    if "<!DOCTYPE" in xml_text[:2000].upper():
        raise ValueError("DTD가 포함된 피드는 처리하지 않음")
    items = []
    for it in ET.fromstring(xml_text).iter("item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        pub = it.findtext("pubDate")
        if not link or not pub:
            continue
        items.append((title, link, email.utils.parsedate_to_datetime(pub).date()))
    return items


def page_links(text: str) -> set:
    return {norm_url(u) for u in re.findall(r"https?://[^\s)\]>\"']+", text)}


def missing_items(items, page_text, since, grace_days, today, exclude=()):
    """페이지에 반영돼야 하는데 없는 글 목록 (발행일 오름차순). exclude는 의도적 제외 URL."""
    linked = page_links(page_text) | {norm_url(u) for u in exclude}
    out = [
        (t, l, d) for t, l, d in items
        if d >= since and (today - d).days >= grace_days and norm_url(l) not in linked
    ]
    return sorted(out, key=lambda x: x[2])


def last_commit_date(page: str):
    r = subprocess.run(["git", "log", "-1", "--format=%cs", "--", f"docs/{page}"],
                       cwd=ROOT, capture_output=True, text=True)
    s = r.stdout.strip()
    return datetime.date.fromisoformat(s) if s else None


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "pai-playbook-source-drift/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def run_checks(pages: dict, today: datetime.date):
    """(findings, fetch_errors) — findings는 이슈 본문용 마크다운 줄 목록."""
    findings, errors = [], []
    for page, e in sorted(pages.items()):
        src = e.get("source") or {}
        if src.get("rss"):
            try:
                items = parse_feed(fetch(src["rss"]))
            except Exception as ex:  # 네트워크·파싱 실패는 드리프트가 아니라 감시 실패
                errors.append(f"{page}: 소스 접속/파싱 실패 ({src['rss']}): {ex}")
                continue
            text = (ROOT / "docs" / page).read_text(encoding="utf-8")
            since = datetime.date.fromisoformat(str(src["since"]))
            excl = [x["url"] for x in src.get("exclude") or []]
            miss = missing_items(items, text, since, src.get("grace_days", 0), today, excl)
            for t, l, d in miss:
                findings.append(f"- `docs/{page}` 미반영: {d} [{t}]({l}) — 발행 후 {(today - d).days}일 "
                                f"(유예 {src.get('grace_days', 0)}일, 갱신 주체: {e.get('by')})")
        msd = e.get("max_silence_days")
        if msd:
            last = last_commit_date(page)
            if last and (today - last).days > msd:
                findings.append(f"- `docs/{page}` 커밋 정지: 마지막 커밋 {last} ({(today - last).days}일 전, "
                                f"기준 {msd}일) — 루틴 실행 로그 확인 필요 ({e.get('by')})")
    return findings, errors


def gh(*args):
    return subprocess.run(["gh", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def sync_issue(findings: list, today: datetime.date):
    """드리프트가 있으면 열린 이슈 1개를 생성/본문 갱신, 없으면 열린 이슈를 닫는다 (멱등)."""
    num = gh("issue", "list", "--label", ISSUE_LABEL, "--state", "open",
             "--json", "number", "--jq", ".[0].number // empty")
    if findings:
        body = (f"자동 감시(`scripts/check_source_drift.py`, {today}) 결과 — 갱신 경로는 "
                "[refresh.yml](../blob/main/refresh.yml)에 선언돼 있으나 실제 소스를 따라가지 못하고 있다.\n\n"
                + "\n".join(findings)
                + "\n\n반영되면 다음 감시 실행이 이 이슈를 자동으로 닫는다.")
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(body)
        if num:
            gh("issue", "edit", num, "--body-file", f.name)
            print(f"이슈 #{num} 본문 갱신")
        else:
            subprocess.run(["gh", "label", "create", ISSUE_LABEL, "--color", "D93F0B",
                            "--description", "외부 소스 대비 미반영·정지 페이지 (자동 감시)"],
                           cwd=ROOT, capture_output=True)
            url = gh("issue", "create", "--title", ISSUE_TITLE, "--label", ISSUE_LABEL,
                     "--label", "documentation", "--body-file", f.name)
            print(f"이슈 생성: {url}")
    elif num:
        gh("issue", "close", num, "--comment", f"{today} 감시: 드리프트 0건 — 자동 종료")
        print(f"이슈 #{num} 종료 (드리프트 해소)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--issue", action="store_true", help="GitHub 이슈 생성/갱신/종료 (gh CLI 필요)")
    ap.add_argument("--today", help="YYYY-MM-DD 날짜 오버라이드")
    a = ap.parse_args()
    today = datetime.date.fromisoformat(a.today) if a.today else datetime.date.today()
    pages = load_registry(REGISTRY.read_text(encoding="utf-8"))
    findings, errors = run_checks(pages, today)
    for msg in errors:
        print(f"::warning::{msg}")
    for line in findings:
        print(line)
    if errors:
        # 감시 실패 시 이슈는 건드리지 않는다 — 접속 실패를 '드리프트 해소'로 오판해 닫지 않도록
        sys.exit(2)
    if a.issue:
        sync_issue(findings, today)
    if findings:
        print(f"드리프트 {len(findings)}건")
        sys.exit(1)
    print("OK — 소스 드리프트 0건")


if __name__ == "__main__":
    main()
