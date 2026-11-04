import datetime

import check_refresh_paths as rp
import check_source_drift as sd

OK = {"mode": "owner", "by": "Youngjin", "trigger": "volatility 주기 검토"}


def test_real_registry_covers_nav():
    nav = rp.nav_targets(rp.MKDOCS.read_text(encoding="utf-8"))
    pages = rp.load_registry(rp.REGISTRY.read_text(encoding="utf-8"))
    assert rp.validate(nav, pages) == []


def test_missing_and_extra_pages_reported():
    errs = rp.validate(["a.md", "b.md"], {"a.md": OK, "c.md": OK})
    assert any(e.startswith("b.md: nav에 있는데") for e in errs)
    assert any(e.startswith("c.md: refresh.yml에만") for e in errs)


def test_bad_mode_and_empty_trigger():
    errs = rp.validate(["a.md"], {"a.md": {"mode": "sometimes", "by": "x", "trigger": " "}})
    assert any("mode 'sometimes'" in e for e in errs)
    assert any("trigger 비어" in e for e in errs)


def test_routine_runbook_must_mention_page(tmp_path):
    (tmp_path / "rb.md").write_text("docs/other.md 만 다룸", encoding="utf-8")
    e = {"mode": "routine", "by": "trig", "trigger": "daily", "runbook": "rb.md"}
    errs = rp.validate(["news.md"], {"news.md": e}, root=tmp_path)
    assert any("docs/news.md를 언급하지 않음" in m for m in errs)
    (tmp_path / "rb.md").write_text("docs/news.md 갱신 절차", encoding="utf-8")
    assert rp.validate(["news.md"], {"news.md": e}, root=tmp_path) == []


def test_exclude_requires_reason():
    e = dict(OK, source={"rss": "https://x/feed", "since": "2026-07-01", "grace_days": 3,
                         "exclude": [{"url": "https://x/a"}]})
    assert any("url·reason" in m for m in rp.validate(["a.md"], {"a.md": e}))


FEED = """<?xml version="1.0"?><rss><channel>
<item><title>New</title><link>https://x/blog/new/</link><pubDate>Wed, 07 Oct 2026 21:04:06 +0000</pubDate></item>
<item><title>Fresh</title><link>https://x/blog/fresh/</link><pubDate>Tue, 13 Oct 2026 10:00:00 +0000</pubDate></item>
<item><title>Listed</title><link>https://x/blog/%CF%800/</link><pubDate>Thu, 10 Sep 2026 16:38:50 +0000</pubDate></item>
<item><title>Skipped</title><link>https://x/blog/skip/</link><pubDate>Wed, 05 Aug 2026 18:28:10 +0000</pubDate></item>
<item><title>Old</title><link>https://x/blog/old/</link><pubDate>Mon, 01 Jun 2026 00:00:00 +0000</pubDate></item>
</channel></rss>"""


def test_missing_items_respects_since_grace_exclude_and_encoding():
    items = sd.parse_feed(FEED)
    page = "본문 [π0](https://x/blog/π0) 링크"  # 인코딩 차이·후행 슬래시 흡수
    miss = sd.missing_items(items, page, datetime.date(2026, 7, 15), 3,
                            datetime.date(2026, 10, 14), exclude=["https://x/blog/skip/"])
    # Fresh는 유예(3일) 안, Old는 since 이전, Listed는 수록, Skipped는 의도적 제외
    assert [t for t, _, _ in miss] == ["New"]


def test_feed_with_dtd_rejected():
    import pytest
    with pytest.raises(ValueError):
        sd.parse_feed('<?xml version="1.0"?><!DOCTYPE r [<!ENTITY a "x">]><rss></rss>')


def test_review_alert_must_be_bool_on_owner_page():
    assert rp.validate(["a.md"], {"a.md": dict(OK, review_alert=True)}) == []
    assert any("review_alert" in m for m in rp.validate(["a.md"], {"a.md": dict(OK, review_alert="yes")}))
    e = {"mode": "event", "by": "x", "trigger": "y", "review_alert": True}
    assert any("review_alert" in m for m in rp.validate(["a.md"], {"a.md": e}))


def test_review_overdue_uses_volatility_threshold():
    # 높음 1개월: 2026-09 → 2026-11 은 2개월 경과 → 초과
    assert sd.review_overdue((2026, 9), "높음", datetime.date(2026, 11, 4)) == (2, 1)
    assert sd.review_overdue((2026, 10), "높음", datetime.date(2026, 11, 4)) is None
    # 중간 3개월: 2개월 경과는 기한 내
    assert sd.review_overdue((2026, 9), "중간", datetime.date(2026, 11, 4)) is None
    # 메타가 없으면 판단하지 않는다(메타 누락은 빌드 게이트가 잡음)
    assert sd.review_overdue(None, "높음", datetime.date(2026, 11, 4)) is None


def test_run_checks_reports_overdue_owner_page(tmp_path, monkeypatch):
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "p.md").write_text(
        "# P\n_최종 갱신: 2026-09 · owner: Youngjin · volatility: 높음_\n", encoding="utf-8")
    monkeypatch.setattr(sd, "ROOT", tmp_path)
    findings, errors = sd.run_checks({"p.md": dict(OK, review_alert=True)}, datetime.date(2026, 11, 4))
    assert errors == []
    assert len(findings) == 1 and "검토 기한 초과" in findings[0] and "2026-09" in findings[0]
    findings, _ = sd.run_checks({"p.md": OK}, datetime.date(2026, 11, 4))  # 필드 없으면 감시 안 함
    assert findings == []
