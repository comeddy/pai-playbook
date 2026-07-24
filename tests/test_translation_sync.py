import sys

import check_translation_sync as ts


def test_blob_hash_matches_git(tmp_path):
    """git hash-object와 동일한 값이어야 한다 — 빈 파일의 blob SHA-1은 잘 알려진 상수."""
    p = tmp_path / "empty.md"
    p.write_bytes(b"")
    assert ts.blob_hash(p) == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"


def test_recorded_hash_frontmatter_only(tmp_path):
    """선두 frontmatter 블록 안의 ko_hash만 인정하고, 실패 원인을 구분한다."""
    h = "a" * 40
    p = tmp_path / "index.en.md"
    p.write_text(f"---\nko_hash: {h}\n---\n# Home\n", encoding="utf-8")
    assert ts.recorded_hash(p) == (h, "ok")

    # 본문에 있는 ko_hash 언급은 무시 — frontmatter 자체가 없는 케이스
    p2 = tmp_path / "index.ja.md"
    p2.write_text(f"# ホーム\n\nko_hash: {h}\n", encoding="utf-8")
    assert ts.recorded_hash(p2) == (None, "frontmatter 없음")

    # frontmatter는 있으나 ko_hash 키가 없는 케이스
    p3 = tmp_path / "index.zh.md"
    p3.write_text("---\ntitle: x\n---\n# 首页\n", encoding="utf-8")
    assert ts.recorded_hash(p3) == (None, "ko_hash 없음")


def test_report_statuses(tmp_path, monkeypatch, capsys):
    src = tmp_path / "index.md"
    src.write_text("# 홈\n", encoding="utf-8")
    cur = ts.blob_hash(src)
    # en: 최신, zh: 뒤처짐, ja: 누락
    (tmp_path / "index.en.md").write_text(f"---\nko_hash: {cur}\n---\n# Home\n", encoding="utf-8")
    (tmp_path / "index.zh.md").write_text(f"---\nko_hash: {'b' * 40}\n---\n# 首页\n", encoding="utf-8")
    monkeypatch.setattr(ts, "DOCS", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_translation_sync.py"])
    ts.main()  # 어떤 상태여도 SystemExit 없이 정상 종료해야 한다 (항상 exit 0 정책)
    out = capsys.readouterr().out
    assert "OK" in out and "뒤처짐" in out and "누락" in out
    assert "비동기: 2 / 3" in out


def test_hash_helper(tmp_path, monkeypatch, capsys):
    p = tmp_path / "x.md"
    p.write_bytes(b"")
    monkeypatch.setattr(sys, "argv", ["check_translation_sync.py", "--hash", str(p)])
    ts.main()
    assert capsys.readouterr().out.strip() == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"


def test_hash_helper_missing_file(tmp_path, monkeypatch, capsys):
    """--hash 대상이 없으면 트레이스백 대신 친화적 에러 + exit 2."""
    monkeypatch.setattr(sys, "argv", ["check_translation_sync.py", "--hash", str(tmp_path / "nope.md")])
    try:
        ts.main()
        raised = None
    except SystemExit as e:
        raised = e.code
    assert raised == 2
    assert "읽을 수 없음" in capsys.readouterr().err


def test_rglob_subdir_and_unreadable(tmp_path, monkeypatch, capsys):
    """하위 디렉터리 원본도 검사되고, 손상 번역 파일은 '읽기 실패'로 격리된다."""
    sub = tmp_path / "intro"
    sub.mkdir()
    (sub / "page.md").write_text("# 소개\n", encoding="utf-8")
    src = tmp_path / "index.md"
    src.write_text("# 홈\n", encoding="utf-8")
    (tmp_path / "index.en.md").write_bytes(b"---\xff\xfe broken")  # 비UTF-8
    monkeypatch.setattr(ts, "DOCS", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_translation_sync.py"])
    ts.main()  # 크래시 없이 exit 0 정책 유지
    out = capsys.readouterr().out
    assert "intro/page.md" in out or "intro\\page.md" in out
    assert "읽기 실패" in out
