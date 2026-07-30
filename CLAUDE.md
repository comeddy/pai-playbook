# pai-playbook — Claude 세션 규칙

AWS Korea SA용 Physical AI Playbook. MkDocs Material, 4개 언어(ko 원본 + en/zh/ja suffix 번역), GitHub Pages 배포(main 푸시 → deploy-docs).

## 문서 수정 시 반드시

1. **ko가 원본** — docs/*.md(한국어)를 고치면 en/zh/ja 번역본도 같은 변경을 반영하고, `python3 scripts/check_translation_sync.py --hash docs/<파일>.md`로 새 해시를 얻어 각 번역본 frontmatter `ko_hash:`를 갱신한다. 상세 절차는 `.claude/skills/translate-sync/SKILL.md`.
2. **용어 각주 관례 (지속)** — 내용을 추가·갱신할 때 SA가 바로 이해하기 어려운 용어는 같은 변경 안에서 `[^용어]` 각주로 처리한다. 기존 각주 id 재사용 우선, 새 용어는 페이지 하단 `<!-- 용어 각주 -->` 블록에 "**용어** — 1~2문장 설명" 추가(공식 영상 있으면 🎥 링크 — `https://www.youtube.com/oembed?url=...`로 실존 검증 후 부착). 마커는 본문 첫 등장 위치에만, 헤딩·mermaid 블록 금지. 4개 언어 동일 적용(마커 id·URL 동일). 규칙 원문: docs/maintenance.md 표준 템플릿 절.
3. **커밋 전 게이트 (둘 다 통과 필수)** — `python3 scripts/check_translation_sync.py`(비동기 0/30) + `mkdocs build --strict`(exit 0). 실패 상태로 커밋 금지.
4. **번역 규칙** — `i18n/glossary.md`의 금지 용어·고정 역어·문체를 따른다.

## 콘텐츠 원칙

- 정직성: 미검증 항목은 출처 등급 `[4]` 유지, 성숙 단계로 포장 금지. Radar 유입 항목의 필러 본문 승격은 사람(담당 필러 owner)의 일.
- 모든 페이지·항목에 `_owner · updated · volatility_` 메타 라인 필수 (누락 시 CI 빌드 실패).
- 항목명에는 1차 확인용 공식 출처 바로가기 링크 부착(curl 200 검증).
