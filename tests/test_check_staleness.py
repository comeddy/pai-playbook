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
