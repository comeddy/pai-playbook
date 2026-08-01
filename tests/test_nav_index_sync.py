import pytest

import check_nav_index_sync as ns

MKDOCS_SAMPLE = """site_name: x
nav:
  - 홈: index.md
  - 가이드: guide.md
  - "P1 · 데이터": pillar-1.md

theme:
  name: material
"""

INDEX_SAMPLE = """# 홈

## 페이지 목록

- [guide — 설명](guide.md)
- [pillar-1 — 설명](pillar-1.md)

## 다음 섹션
"""


def test_nav_targets_parses_quoted_and_plain_labels():
    assert ns.nav_targets(MKDOCS_SAMPLE) == ["index.md", "guide.md", "pillar-1.md"]


def test_index_list_targets_scopes_to_section():
    """페이지 목록 섹션 밖의 링크는 세지 않는다."""
    text = INDEX_SAMPLE + "\n- [radar — 밖에 있는 링크](radar.md)\n"
    assert ns.index_list_targets(text) == ["guide.md", "pillar-1.md"]


def test_compare_detects_missing_and_extra():
    missing, extra = ns.compare(
        ["index.md", "guide.md", "exec.md"], ["guide.md", "old-page.md"]
    )
    assert missing == ["exec.md"]        # nav에 있는데 목록에 없음
    assert extra == ["old-page.md"]      # 목록에만 있음
    # index.md 자신은 누락으로 치지 않음
    assert "index.md" not in missing


def test_main_exit_1_on_drift(tmp_path, monkeypatch, capsys):
    (tmp_path / "docs").mkdir()
    (tmp_path / "mkdocs.yml").write_text(MKDOCS_SAMPLE + "  - 신규: exec.md\n", encoding="utf-8")
    # 위 write는 nav 블록 뒤(theme 이후)에 붙어 nav로 안 잡히므로, 제대로 된 파일을 다시 구성
    (tmp_path / "mkdocs.yml").write_text(
        'site_name: x\nnav:\n  - 홈: index.md\n  - 가이드: guide.md\n  - "신규": exec.md\n\ntheme:\n  name: material\n',
        encoding="utf-8",
    )
    (tmp_path / "docs" / "index.md").write_text(INDEX_SAMPLE, encoding="utf-8")
    monkeypatch.setattr(ns, "MKDOCS", tmp_path / "mkdocs.yml")
    monkeypatch.setattr(ns, "INDEX", tmp_path / "docs" / "index.md")
    with pytest.raises(SystemExit) as e:
        ns.main()
    assert e.value.code == 1
    out = capsys.readouterr().out
    assert "exec.md" in out and "누락" in out
    assert "pillar-1.md" in out  # nav에 없는 pillar-1은 '목록에만 존재'로 보고


def test_main_ok_on_real_repo(capsys):
    """실저장소는 현재 동기화 상태여야 한다 (77a412c 수정 후)."""
    ns.main()
    assert "OK" in capsys.readouterr().out
