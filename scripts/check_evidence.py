#!/usr/bin/env python3
"""Validate claim records and their four-language rendered documentation.

--render updates only the marked blocks. Default mode is read-only and fails on
invalid records or rendering drift. Review-age warnings do not certify facts.
"""
import argparse
import datetime as dt
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("ko", "en", "zh", "ja")
START = "<!-- evidence:start -->"
END = "<!-- evidence:end -->"
STATUSES = {"source-checked", "withdrawn", "reproduction-pending"}
LABELS = {
    "ko": ("확인일", "상태", "검토 주기(일)", "대조 담당", "사람 검토", "영향 페이지", "출처", "대기"),
    "en": ("Checked", "Status", "Review interval (days)", "Compared by", "Human review", "Affected pages", "Sources", "pending"),
    "zh": ("确认日期", "状态", "复核周期（天）", "对照者", "人工复核", "影响页面", "来源", "待定"),
    "ja": ("確認日", "状態", "確認周期（日）", "照合担当", "人による確認", "影響ページ", "出典", "未実施"),
}


def validate(data, docs, today):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("claims"), list):
        return ["schema_version=1 and claims list are required"]
    if not data["claims"]:
        return ["claims must not be empty"]
    seen = set()
    for claim in data["claims"]:
        if not isinstance(claim, dict):
            errors.append("claim must be an object")
            continue
        cid = claim.get("id", "")
        if not isinstance(cid, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", cid):
            errors.append(f"invalid claim id: {cid!r}")
            cid = repr(cid)
        if cid in seen:
            errors.append(f"duplicate claim: {cid}")
        seen.add(cid)
        try:
            checked = dt.date.fromisoformat(claim.get("checked_on", ""))
            if checked > today:
                errors.append(f"{cid}: check date is in the future")
        except (ValueError, TypeError):
            errors.append(f"{cid}: invalid checked_on")
        interval = claim.get("review_after_days")
        if type(interval) is not int or not 1 <= interval <= 366:
            errors.append(f"{cid}: invalid review interval")
        if not isinstance(claim.get("status"), str) or claim["status"] not in STATUSES:
            errors.append(f"{cid}: invalid status")
        if not isinstance(claim.get("verified_by"), str) or not claim["verified_by"].strip():
            errors.append(f"{cid}: verified_by is required")
        if claim.get("human_review") not in ("pending", "complete"):
            errors.append(f"{cid}: invalid human_review")
        if claim.get("human_review") == "complete" and not claim.get("human_reviewer"):
            errors.append(f"{cid}: completed review requires a named human_reviewer")
        summaries = claim.get("summary", {})
        if not isinstance(summaries, dict) or any(
                not isinstance(summaries.get(lang), str) or not summaries[lang].strip()
                for lang in LANGS):
            errors.append(f"{cid}: summaries in all four languages are required")
        pages = claim.get("pages")
        if not isinstance(pages, list) or not pages:
            errors.append(f"{cid}: affected pages are required")
        else:
            for page in pages:
                if not isinstance(page, str) or not re.fullmatch(r"[a-z0-9-]+\.md", page):
                    errors.append(f"{cid}: invalid affected page {page!r}")
                    continue
                for lang in LANGS:
                    name = page if lang == "ko" else page[:-3] + "." + lang + ".md"
                    if not (docs / name).is_file():
                        errors.append(f"{cid}: missing affected page {name}")
        sources = claim.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{cid}: sources are required")
        else:
            for source in sources:
                if not isinstance(source, dict):
                    errors.append(f"{cid}: source must be an object")
                    continue
                url = source.get("url", "")
                if not isinstance(url, str):
                    url = ""
                parsed = urlparse(url)
                if parsed.scheme != "https" or not parsed.netloc or not source.get("label"):
                    errors.append(f"{cid}: source needs an HTTPS URL and label")
    return errors


def render(claims, lang):
    checked, status, days, verifier, human, pages, sources, pending = LABELS[lang]
    blocks = []
    for c in claims:
        page_links = " · ".join(f"[{p[:-3]}]({p})" for p in c["pages"])
        source_links = " · ".join(f"[{s['label']}]({s['url']})" for s in c["sources"])
        reviewer = c.get("human_reviewer") if c["human_review"] == "complete" else pending
        blocks.append(
            f"### {c['id']} {{ #{c['id']} }}\n\n{c['summary'][lang]}\n\n"
            f"- {checked}: {c['checked_on']} · {status}: `{c['status']}` · {days}: {c['review_after_days']}\n"
            f"- {verifier}: {c['verified_by']} · {human}: {reviewer}\n"
            f"- {pages}: {page_links}\n"
            f"- {sources}: {source_links}"
        )
    return "\n\n".join(blocks)


def document_with_block(text, block):
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("exactly one evidence marker pair is required")
    before, rest = text.split(START)
    _, after = rest.split(END)
    return before + START + "\n\n" + block + "\n\n" + END + after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads((ROOT / "docs/assets/claims.json").read_text())
        errors = validate(data, ROOT / "docs", dt.date.today())
        if errors:
            raise ValueError("\n".join(errors))
        for lang in LANGS:
            name = "evidence" + ("" if lang == "ko" else "." + lang) + ".md"
            page = ROOT / "docs" / name
            old = page.read_text()
            new = document_with_block(old, render(data["claims"], lang))
            if args.render:
                page.write_text(new)
            elif new != old:
                errors.append(f"{name}: run python3 scripts/check_evidence.py --render")
        if errors:
            raise ValueError("\n".join(errors))
        for claim in data["claims"]:
            age = (dt.date.today() - dt.date.fromisoformat(claim["checked_on"])).days
            if age > claim["review_after_days"]:
                print(f"::warning file=docs/evidence.md::Review overdue: {claim['id']} ({age} days)")
        pending = sum(c["human_review"] == "pending" for c in data["claims"])
        print(f"Evidence: {len(data['claims'])} records · 4 languages in sync · human review pending: {pending}")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Evidence validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
