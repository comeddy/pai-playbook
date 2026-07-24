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


def test_conflicting_updated_dates_fail_check(tmp_path, monkeypatch, capsys):
    """헤더('최종 갱신')와 푸터('updated')가 다르면 조용히 계산하지 말고 exit 1."""
    (tmp_path / "index.md").write_text(
        "# 홈\n_최종 갱신: 2026-01 · owner: x_\n\n본문\n\n_owner: x · updated: 2026-07 · volatility: 낮음_\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(cs, "DOCS", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_staleness.py", "--check", "--today", "2026-07"])
    exited = None
    try:
        cs.main()
    except SystemExit as e:
        exited = e.code
    assert exited == 1
    assert "불일치" in capsys.readouterr().out


def test_single_digit_month_and_field_boundary(tmp_path):
    """단일 자리 월(2026-7)은 허용하고, last_updated: 같은 다른 필드는 매칭하지 않는다."""
    p = tmp_path / "a.md"
    p.write_text("# 제목\n_owner: x · updated: 2026-7 · volatility: 낮음_\nlast_updated: 2020-01\n", encoding="utf-8")
    updated, volatility, conflict = cs.parse_page(p)
    assert updated == (2026, 7)
    assert volatility == "낮음"
    assert conflict is False  # last_updated:는 수집되지 않아야 불일치도 아님


def test_rglob_subdir_and_unreadable(tmp_path, monkeypatch, capsys):
    """하위 디렉터리 문서도 검사되고, 손상 파일은 트레이스백 없이 격리 보고된다."""
    sub = tmp_path / "intro"
    sub.mkdir()
    (sub / "page.md").write_text(
        "# 소개\n_updated: 2026-07 · volatility: 낮음_\n", encoding="utf-8"
    )
    (tmp_path / "broken.md").write_bytes(b"\xff\xfe not utf8")
    monkeypatch.setattr(cs, "DOCS", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_staleness.py", "--check", "--today", "2026-07"])
    exited = None
    try:
        cs.main()  # 손상 파일은 '메타데이터 문제'로 집계 → exit 1 (조용한 통과 금지)
    except SystemExit as e:
        exited = e.code
    assert exited == 1
    out = capsys.readouterr().out
    assert "intro/page.md" in out or "intro\\page.md" in out
    assert "읽기 실패" in out


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
