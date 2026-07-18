---
name: translate-sync
description: Use when Korean source pages under docs/ have changed and en/zh/ja translations need creating or re-syncing — detects drift via ko_hash, translates only changed files using i18n/glossary.md, and gates on mkdocs build --strict
---

# 번역 동기화 (ko → en/zh/ja)

## 절차 (순서 고정)

1. **탐지**: `python3 scripts/check_translation_sync.py` 실행.
   `OK`가 아닌 (원본, 언어) 쌍만 이후 단계의 대상이다. 전체 재번역 금지.
2. **규칙 로드**: `i18n/glossary.md`를 읽는다. 번역 금지 용어·고정 역어·
   구조 보존 규칙·문체를 그대로 따른다.
3. **번역**: 대상 파일마다
   a. 해시 계산: `python3 scripts/check_translation_sync.py --hash docs/<원본>.md`
   b. `docs/<원본stem>.<lang>.md`를 frontmatter(`ko_hash: <해시>`)부터 작성/갱신.
      '뒤처짐' 상태면 원본의 변경 부분(git diff)을 확인해 해당 부분 위주로 갱신.
   c. heading 번역 시 본문 내 앵커 링크(`#...`)를 함께 갱신.
4. **해시 검증**: `python3 scripts/check_translation_sync.py` 재실행 →
   작업 대상이 전부 `OK`인지 확인.
5. **빌드 게이트**: `mkdocs build --strict --site-dir <scratchpad>/site-check`.
   앵커 오류 시: 산출물의 실제 heading id(`grep '<h[23] id=' <산출물>.html`)를
   읽어 링크를 맞춘다. 사전 계산 슬러그를 신뢰하지 말 것.
6. **커밋 전 확인**: 통과 결과(OK 개수, strict exit 0)를 사용자에게 보여주고
   커밋한다. 실패 상태로 완료 선언 금지.

## 주의

- 배지 admonition(`!!! warning "⏳ ..."`)이 원본에 있으면 그것은 CI 주입분이
  커밋된 사고다 — 번역하지 말고 사용자에게 보고.
- radar.md·maintenance.md의 표는 구조가 곧 데이터다. 열 추가/삭제 금지.
