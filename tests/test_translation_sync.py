import sys

import check_translation_sync as ts


def test_blob_hash_matches_git(tmp_path):
    """git hash-object와 동일한 값이어야 한다 — 빈 파일의 blob SHA-1은 잘 알려진 상수."""
    p = tmp_path / "empty.md"
    p.write_bytes(b"")
    assert ts.blob_hash(p) == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"


def test_recorded_hash_frontmatter_only(tmp_path):
    """선두 frontmatter 블록 안의 ko_hash만 인정한다."""
    h = "a" * 40
    p = tmp_path / "index.en.md"
    p.write_text(f"---\nko_hash: {h}\n---\n# Home\n", encoding="utf-8")
    assert ts.recorded_hash(p) == h

    # 본문에 있는 ko_hash 언급은 무시
    p2 = tmp_path / "index.ja.md"
    p2.write_text(f"# ホーム\n\nko_hash: {h}\n", encoding="utf-8")
    assert ts.recorded_hash(p2) is None


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
