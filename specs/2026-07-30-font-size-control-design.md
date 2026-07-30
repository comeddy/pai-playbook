# 글자 크기 조절 플로팅 버튼 — 설계

_2026-07-30 · 승인됨 (배치: 우하단 플로팅 — 사용자 선택)_

## 목적

독자가 본문 글자 크기를 사이트 안에서 조절·유지할 수 있게 한다. 브라우저 줌과 달리
본문만 확대되어 레이아웃(헤더·네비·사이드바)이 유지된다.

## 동작 사양

- 우하단 고정 플로팅 버튼 2개: `A−` / `A+`.
- 클릭당 5% 단계, 범위 **85% ~ 130%**, 기본 100%
  (85/90/95/100/105/110/115/120/125/130 — 총 10단계). 한계값에서 해당 버튼 `disabled`.
- 조절 대상: 본문 콘텐츠 `.md-typeset`만. 헤더·네비·검색·푸터는 불변.
- 상태 저장: `localStorage['pai-fs']` (정수 %, 예: `110`). 페이지 이동·재방문·언어
  전환 후에도 유지 (4개 언어가 같은 origin이므로 공유됨).
- FOUC 방지: `overrides/main.html` extrahead의 인라인 1줄 스크립트가 렌더 전에
  `document.documentElement.dataset.fs = localStorage['pai-fs']`를 적용.
- 접근성: 버튼은 `<button>` 요소, `aria-label`을 페이지 `<html lang>`에 따라
  ko/en/zh/ja 4개 언어 분기. 터치 타깃 최소 44×44px(모바일에서도 유지).

## 구현 구조

| 파일 | 역할 |
|---|---|
| `docs/stylesheets/font-size.css` | 버튼 스타일(테마 CSS 변수 사용, 라이트/다크 대응) + `html[data-fs="…"] .md-typeset { font-size: … }` 단계별 규칙 |
| `docs/javascripts/font-size.js` | 버튼 DOM 생성·클릭 처리·localStorage 저장·disabled 토글 |
| `overrides/main.html` | extrahead에 저장값 조기 적용 인라인 스크립트 1줄 추가 (기존 PWA 블록 유지) |
| `mkdocs.yml` | `extra_css`·`extra_javascript` 등록 |

- CSS는 단계별 고정 rem 값을 명시한다(Material 기본 `.8rem`에 배율을 적용해 산출,
  예: 110% → `.88rem`) — 런타임 계산 없이 검증 가능.
- 버튼 컨테이너는 `z-index`를 Material 오버레이(검색·사이드바)보다 낮게 두어 검색
  모달을 가리지 않는다.

## 충돌·제약 검토

- Material back-to-top 버튼은 상단 중앙 표시라 겹치지 않음.
- 헤더 partial 오버라이드 없음 → 테마 업그레이드 안전.
- `navigation.instant` 미사용(이 리포는 static-i18n 비호환으로 제거)이므로 페이지
  전환마다 전체 로드 → js가 매 로드에서 실행되면 충분, SPA 이벤트 핸들링 불필요.

## 검증 기준

1. `mkdocs build --strict` exit 0.
2. 빌드 산출물 HTML에 버튼 마크업·css/js 링크 존재 (4개 언어 산출물 각각).
3. 배포 후 실제 페이지에서: 클릭 시 본문만 확대, 새로고침·언어 전환 후 유지,
   85%/130% 한계에서 버튼 비활성.

## 범위 제외 (YAGNI)

- 리셋 버튼·현재 % 표시·슬라이더·폰트 패밀리 변경 — 요청 없음, 2버튼으로 충분.
