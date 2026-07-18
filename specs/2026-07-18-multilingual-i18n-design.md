# 다국어(ko/en/zh/ja) 확장 설계

- 날짜: 2026-07-18
- 상태: 승인됨
- 범위: pai-playbook을 한국어 단일에서 영어·중국어·일본어 포함 4개 언어로 확장하고, 1인 운영 가능한 번역 동기화 체계를 구축한다.

## 확정된 운영 결정

| 결정 | 선택 | 근거 |
|------|------|------|
| 번역 생산 | Claude 자동 번역 | 1인 운영에 현실적. 용어집으로 품질 관리 |
| 실행 위치 | 로컬 Claude Code 세션 | API 키 별도 관리 불필요, 커밋 전 육안 확인 가능 |
| 미동기화 정책 | CI 경고만 (독자용 배지 없음, 배포 차단 없음) | 최소 운영 부담 |
| 구조 | `mkdocs-static-i18n` 플러그인, suffix 방식 | 단일 빌드, 기존 한국어 URL 전부 보존, 미번역 fallback |

## 1. 사이트 구조 & URL

suffix 방식 파일 배치:

| 언어 | 파일 예 | URL |
|------|---------|-----|
| 한국어 (기본) | `docs/index.md` | `/pai-playbook/` — 기존 URL 보존 |
| 영어 | `docs/index.en.md` | `/pai-playbook/en/` |
| 중국어(간체) | `docs/index.zh.md` | `/pai-playbook/zh/` |
| 일본어 | `docs/index.ja.md` | `/pai-playbook/ja/` |

- 대상 페이지: 9개 전부 (index, pillar-1~5, decisions, radar, maintenance)
- 미번역 파일은 한국어로 자동 fallback → 부분 번역 상태로도 배포 가능
- Material 헤더에 언어 전환 드롭다운 자동 생성 (플러그인이 `theme.alternate` 상당을 구성)

## 2. mkdocs.yml 변경

- `plugins:`에 `i18n` 추가:
  - `languages:` — ko(default, build), en, zh, ja 선언. 언어별 `name`은 해당 언어 표기(한국어/English/中文/日本語)
  - 언어별 `nav_translations:` — nav 제목 9개 × en/zh/ja
  - 언어별 `site_description` 오버라이드
- `theme.language`는 플러그인이 언어별 빌드에서 자동 전환
- 검색: 플러그인이 언어별 설정 주입. zh/ja 형태소 분리 품질은 v1에서 수용 (YAGNI — 불만 발생 시 개선)
- 의존성: `requirements.txt`에 `mkdocs-static-i18n` 추가 (버전 고정)

## 3. 번역 동기화 추적

- 각 번역 파일 상단 frontmatter에 원본 추적 해시 기록:
  ```yaml
  ---
  ko_hash: <번역 시점의 git hash-object docs/<원본>.md 값>
  ---
  ```
- 새 스크립트 `scripts/check_translation_sync.py`:
  - 한국어 원본 각각에 대해 `git hash-object` 현재값 계산
  - 각 번역 파일의 `ko_hash`와 비교
  - 불일치 또는 번역 파일 부재 시 GitHub Actions warning annotation(`::warning file=...`) 출력
  - **항상 exit 0** (배포 차단 없음 — 확정 정책)
  - 로컬 실행 시에도 사람이 읽을 수 있는 리포트 출력 (translate-sync 스킬이 탐지 단계에서 재사용)
- `deploy-docs.yml`의 build job에 스텝 1개 추가 (staleness 검사 뒤, mkdocs build 앞)

## 4. 기존 staleness 스크립트 수정 (필수 선행)

현재 `scripts/check_staleness.py`는 `docs/*.md` 전체를 glob하고 메타데이터 누락 시 실패한다.
번역 suffix 파일이 추가되는 순간 CI가 깨지므로 다음을 수정:

- glob에서 `*.en.md`, `*.zh.md`, `*.ja.md` 제외 — 검사·메타데이터 강제는 한국어 원본만
- `--inject`: 한국어 페이지가 기준 초과 시 해당 페이지의 존재하는 언어 변형 파일에도 배지 주입
  - 배지 문구는 스크립트 내 4개 언어 템플릿 (ko/en/zh/ja)
  - 멱등성 가드는 기존과 동일한 방식(admonition 전체 형태 판별)을 언어별 템플릿에 적용

## 5. 용어집 + 프로젝트 스킬

- `i18n/glossary.md` (빌드 미포함 운영 파일):
  - 번역 금지 용어 (Sim-to-Real, VLA, GA, Radar 등 — 실제 목록은 구현 시 페이지 전수 스캔으로 확정)
  - 언어별 고정 역어 표
  - 스타일 규칙 (문체, 제품명 표기, 배지 이모지 유지 등)
- `.claude/skills/translate-sync/SKILL.md` — "번역 동기화" 요청 시의 표준 절차:
  1. `check_translation_sync.py`로 뒤처진/누락 파일 탐지
  2. `i18n/glossary.md` 로드
  3. 변경된 파일만 번역 생성·갱신 (전체 재번역 금지)
  4. 번역 파일의 `ko_hash` 갱신
  5. `mkdocs build --strict`로 앵커·링크 검증 (통과 전 완료 선언 금지)

## 6. 검증 계획

- `mkdocs build --strict` 통과 — 앵커 27개가 언어별 번역 heading에 대해 재검증됨.
  **번역 시 앵커 링크(`#한국어-슬러그`)가 최대 리스크**: 번역본에서 heading이 번역되면
  앵커 슬러그도 바뀌므로, 본문 내 앵커 링크도 함께 갱신해야 함. strict 빌드가 게이트.
- 초기 번역 후: 4개 언어 × 9페이지 로컬 빌드 확인, 언어 드롭다운 동작 확인
- CI 그린 확인 후 라이브 URL 4종(`/`, `/en/`, `/zh/`, `/ja/`) HTTP 200 점검

## 작업 순서

1. 인프라: 플러그인 도입 + mkdocs.yml + staleness 스크립트 수정 + sync 스크립트 + CI 스텝
2. 운영 도구: 용어집 초안(페이지 전수 스캔 기반) + translate-sync 스킬
3. 영어 9페이지 번역 (앵커 갱신 포함, strict 빌드 게이트)
4. 중국어·일본어 번역 (동일 절차)
5. 배포 및 라이브 검증

## 범위 외 (YAGNI)

- zh/ja 검색 형태소 분리 개선
- 독자용 "번역 오래됨" 배너
- 번역 PR 자동화 (CI 내 번역)
- 언어별 상이한 콘텐츠 구조
