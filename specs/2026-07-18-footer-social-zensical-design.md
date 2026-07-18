# 푸터 소셜 링크 + Zensical 전환 대기 등재 설계

- 날짜: 2026-07-18
- 상태: 승인됨

## 배경 (조사 확정 사실, 2026-07)

- FastAPI는 실제로 Zensical로 이전("Made with Zensical" 푸터, GitHub/Discord/X/Bluesky/LinkedIn 소셜).
- Zensical v0.0.50: mkdocs.yml 네이티브 호환이나 **mkdocs-static-i18n은 Tier 2 백로그(미지원)**, 다국어는 로드맵 stretch goal, 업스트림 플러그인은 frozen.
- 따라서 **지금 전환하면 4개 언어 아키텍처가 깨짐** → 전환은 대기, 허위 "Made with Zensical" 표기는 하지 않음(정직성 원칙).

## 결정

1. **소셜 링크 4종** — `mkdocs.yml` `extra.social` (전역 → 4개 언어 푸터 자동 적용):
   github.com/comeddy · linkedin.com/in/comeddy · x.com/comeddy · bsky.app/profile/comeddy.bsky.social
   (아이콘: fontawesome/brands/{github, linkedin, x-twitter, bluesky})
2. **Zensical 전환 대기** — `docs/maintenance.md` "알려진 기술 부채"에 1행 추가 (Radar는 Physical AI 콘텐츠 전용이므로 인프라 부채는 maintenance):
   전환 조건 = Zensical의 static-i18n 지원(또는 네이티브 다국어) 출시 + strict 검증·한국어 슬러그 호환 확인. 그때까지 푸터 표기는 사실대로 유지.
   → ko 수정이므로 en/zh/ja 동기화 + ko_hash 갱신.
3. "Made with Material for MkDocs" 표기는 변경하지 않음 — 실제 전환 시 자동 변경.

## 검증

- `mkdocs build --strict` exit 0, sync 비동기 0/30
- 라이브: 4개 언어 푸터에 소셜 아이콘 4종 href 존재
