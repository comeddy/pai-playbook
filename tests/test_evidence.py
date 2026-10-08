import copy
import datetime as dt
import pytest
import check_evidence as evidence

TODAY = dt.date(2026, 9, 15)


@pytest.fixture
def record(tmp_path):
    for lang in evidence.LANGS:
        (tmp_path / ("pillar-2" + ("" if lang == "ko" else "." + lang) + ".md")).write_text("# page")
    data = {"schema_version": 1, "claims": [{
        "id": "model-license", "checked_on": "2026-09-15", "review_after_days": 30,
        "status": "source-checked", "verified_by": "Source comparison",
        "human_review": "pending", "pages": ["pillar-2.md"],
        "summary": {lang: "Claim" for lang in evidence.LANGS},
        "sources": [{"label": "Official", "url": "https://example.org/license"}],
    }]}
    return data, tmp_path


def test_valid_record(record):
    data, docs = record
    assert evidence.validate(data, docs, TODAY) == []


def test_invalid_root_and_empty_registry(record):
    _, docs = record
    assert evidence.validate([], docs, TODAY)
    assert evidence.validate({"schema_version": 1, "claims": []}, docs, TODAY)


@pytest.mark.parametrize("field,value,match", [
    ("checked_on", "2026-09-16", "future"),
    ("checked_on", "2026-13-01", "invalid checked_on"),
    ("review_after_days", 0, "interval"),
    ("human_review", "complete", "named human_reviewer"),
    ("status", "production-approved", "invalid status"),
    ("sources", [{"label": "x", "url": "file:///tmp/x"}], "HTTPS"),
])
def test_rejects_misleading_or_invalid_record(record, field, value, match):
    data, docs = record
    data["claims"][0][field] = value
    assert any(match in e for e in evidence.validate(data, docs, TODAY))


def test_detects_duplicate_and_missing_translation(record):
    data, docs = record
    data["claims"].append(copy.deepcopy(data["claims"][0]))
    (docs / "pillar-2.ja.md").unlink()
    errors = evidence.validate(data, docs, TODAY)
    assert any("duplicate" in e for e in errors)
    assert any("pillar-2.ja.md" in e for e in errors)


def test_requires_all_localized_summaries(record):
    data, docs = record
    del data["claims"][0]["summary"]["zh"]
    assert any("four languages" in e for e in evidence.validate(data, docs, TODAY))


def test_render_preserves_unrelated_content_and_is_idempotent(record):
    data, _ = record
    text = f"# Title\n\n{evidence.START}\nold\n{evidence.END}\n\nFooter"
    block = evidence.render(data["claims"], "ko")
    updated = evidence.document_with_block(text, block)
    assert updated.startswith("# Title\n\n")
    assert updated.endswith("\n\nFooter")
    assert "[pillar-2](pillar-2.md)" in updated
    assert evidence.document_with_block(updated, block) == updated


def test_missing_or_duplicate_markers_fail():
    with pytest.raises(ValueError):
        evidence.document_with_block("# missing", "x")
    with pytest.raises(ValueError):
        evidence.document_with_block(evidence.START * 2 + evidence.END, "x")
