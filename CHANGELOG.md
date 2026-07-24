# Changelog

[![English](https://img.shields.io/badge/lang-English-blue)](#english)
[![한국어](https://img.shields.io/badge/lang-%ED%95%9C%EA%B5%AD%EC%96%B4-red)](#korean)

---

<a id="english"></a>

# English

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Versions are git-tagged (v1.0.0+).

## [Unreleased]

### Added

- Register 8 verified AWS official Physical AI repos (7 aws-samples + 1 awslabs) as related assets across pillars, each with maturity caveats, in all four languages: AWS Physical AI Toolchain (OSMO on EKS) and Self-improving Physical AI and Agentic AI Robot (pillar 5), Physical AI Scaffolding Kit (pillars 2-3), Embodied AI Platform (pillar 2), VLA Simulator — 1-click benchmarking of 7 VLA models on EC2 (pillar 3), Android PAI data collector app and VAMS visual asset management (pillar 1)

### Changed

- Update the Radar RLDX-1 entry: replace "no AWS connection found" with a simulation-benchmarking-scoped connection (the aws-samples VLA Simulator runs RLDX-1 on EC2 within its non-commercial license; no commercial positioning)
- Record the 2026-07-20 weekly scan intake in the Radar (8 items) and its primary-source verification results (0 promoted, 6 corrected), in all four languages
- Expand the weekly scan runbook scope: add physical AI data (robot data collection and datasets) to the arXiv query, and The Robot Report and IEEE Spectrum Robotics to the news sources

## [1.4.0] - 2026-07-19

### Added

- Add a standalone intro landing page at `/intro/` (self-contained HTML) and expand it to four languages (`/intro/en|zh|ja/`) with hreflang alternates and language switchers in both the header nav and the footer
- Introduce a multi-verifier scheme for primary-source verification: an optional `verified by:` metadata field (the owner stays a single person), a "Verifiers (multiple allowed)" role in the promotion pipeline, and a verifier input on the promotion issue form — applied across all four languages
- Add a bilingual CHANGELOG with git tags (v1.0.0–v1.3.0), GitHub Releases, and a README release badge
- Add `docs/CNAME` groundwork for the `pai.zerojin.art` custom domain (domain not yet activated)

## [1.3.0] - 2026-07-19

### Added

- Register verified AWS official workshops: Bedrock AgentCore Getting Started, AgentCore Deep Dive (pillar 5), and IoT TwinMaker end-to-end (pillar 3)
- Place the Physical AI E2E workshop (Korean) in pillar 2 (GR00T VLA fine-tuning track) and pillar 3 (Isaac Lab RL track)
- Add execution assets: LeRobot teleop data collection on Greengrass sample (aws-samples), Omniverse digital twin hands-on (Korean), and an internal AWS-NVIDIA robotics reference architecture (marked internal-only)

### Fixed

- Disambiguate "국내" (domestic) in all translations to explicit Korean/韩国/韓国 (30 spots) — Chinese readers previously read it as "in China"; add a glossary rule to prevent regression
- Unify spelling 워크샵 → 워크숍 (standard orthography) and 실재 → 실제 after a full 4-language proofreading sweep (40 files, only these findings)

## [1.2.0] - 2026-07-18

### Added

- Add a "Guide" page explaining the full verification pipeline (candidate discovery → Radar → THE FILTER → promotion → monitoring), exposed via top tab navigation
- Expand the FAQ from Top 10 to Top 20 with a source column (items 11–20 from public-community research)
- Add the Radar "latest scan intake" section with a weekly automated scan (cloud routine, Mondays 02:00 UTC) and its runbook
- Add 18 Mermaid diagrams across pillars, decision trees, guide, and maintenance; replace all ASCII diagrams
- Add ~46 curated official links on first occurrences of bold product names (all pre-verified with curl)
- Register verified workshop assets: NVIDIA Isaac Lab on AWS, and the self-built pai-sim-isaaclab hands-on (promoted into the next-action line)
- Add footer social links (GitHub repo, LinkedIn, Bluesky), a bilingual README, and a CC-BY-4.0 LICENSE

### Changed

- Rename the home title to "Physical AI Playbook 안내"; rename the action label "SA 다음 액션" to "다음 액션" (118 spots); rename the promotion-pipeline heading (with all cross-page anchors updated)
- Update radar intake entries after primary-source verification (promote Apptronik Apollo 2, correct the Atlas misnomer, correct AgiBot/1X NEO claims)

### Fixed

- Fix a list-rendering bug where bullets collapsed into paragraphs: insert 160 missing blank lines before lists (5 pillars × 4 languages)

## [1.1.0] - 2026-07-18

### Added

- Publish the site in four languages: English, Chinese (Simplified), and Japanese translations of all pages, with Korean as the source of truth (mkdocs-static-i18n suffix structure, language switcher)
- Add ko_hash-based translation drift detection (`scripts/check_translation_sync.py`, warn-only CI step)
- Add the translation glossary (`i18n/glossary.md`) and the translate-sync skill (detect → glossary → translate changed files → strict-build gate)
- Extend the staleness badge to inject per-language badges into translated pages
- Add multilingual site links to the README

### Changed

- Remove `navigation.instant` (documented incompatibility with the i18n language switcher)

## [1.0.0] - 2026-07-11

### Added

- Initial release: 8 pages (home, pillars 1–5, decision trees, Radar, maintenance) generated from the master prompt with per-page adversarial fact-checking
- MkDocs Material site with GitHub Actions deploy to GitHub Pages (strict-build gate: broken links/anchors fail the deploy)
- Automated staleness badges based on per-page volatility (1/3/6-month review cadence), refreshed by a weekly cron redeploy
- Promotion issue form with the THE FILTER checklist built in
- Owner assignment for pillar pages

[Unreleased]: https://github.com/comeddy/pai-playbook/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/comeddy/pai-playbook/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/comeddy/pai-playbook/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/comeddy/pai-playbook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/comeddy/pai-playbook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/comeddy/pai-playbook/releases/tag/v1.0.0

---

<a id="korean"></a>

# 한국어

이 프로젝트의 주요 변경 사항을 이 파일에 기록합니다.
형식은 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)를 따르고, [Semantic Versioning](https://semver.org/spec/v2.0.0.html)을 준수합니다. 버전은 git 태그(v1.0.0+)로 관리합니다.

## [Unreleased]

### Added

- 검증된 AWS 공식 Physical AI 리포 8종(aws-samples 7 + awslabs 1)을 필러별 관련 자산으로 등재, 각각 성숙도 캐비앗 명시, 4개 언어 반영: AWS Physical AI Toolchain(OSMO on EKS)·Self-improving Physical AI·Agentic AI Robot(pillar 5), Physical AI Scaffolding Kit(pillar 2~3), Embodied AI Platform(pillar 2), VLA Simulator — 7개 VLA 모델 원클릭 EC2 벤치마킹(pillar 3), Android PAI 데이터 수집 앱·VAMS 시각 자산 관리(pillar 1)

### Changed

- Radar RLDX-1 항목 갱신: "AWS 연계 근거 없음" 표기를 시뮬레이션 벤치마킹 한정 연계로 교체(aws-samples VLA Simulator가 비상업 라이선스 허용 범위 내에서 RLDX-1을 EC2에서 구동, 상업 포지셔닝 불가)
- Radar에 2026-07-20 주간 스캔 유입(8건)과 1차 출처 검증 결과(승격 0건, 정정 6건) 기록, 4개 언어 반영
- 주간 스캔 런북 범위 확장: arXiv 쿼리에 physical AI data(로봇 데이터 수집·데이터셋) 추가, 뉴스 소스에 The Robot Report·IEEE Spectrum Robotics 추가

## [1.4.0] - 2026-07-19

### Added

- `/intro/` 독립 랜딩 페이지 추가(단일 HTML) 및 4개 언어 확장(`/intro/en|zh|ja/`) — hreflang 대체 링크와 header nav·footer 양쪽 언어 전환기 포함
- 1차 출처 검증자 다인 체계 도입: 선택 `검증:` 메타데이터 필드(owner는 1명 유지), 승격 파이프라인 "검증 담당(복수 가능)" 역할, 승격 이슈 폼 검증자 입력 필드 — 4개 언어 반영
- 이중 언어 CHANGELOG·git 태그(v1.0.0~v1.3.0)·GitHub Releases·README 릴리스 뱃지 추가
- `pai.zerojin.art` 커스텀 도메인용 `docs/CNAME` 기반 작업 추가(도메인 미활성)

## [1.3.0] - 2026-07-19

### Added

- 검증된 AWS 공식 워크숍 등재: Bedrock AgentCore 시작·Deep Dive(pillar 5), IoT TwinMaker E2E(pillar 3)
- Physical AI E2E 워크숍(한국어)을 pillar 2(GR00T VLA 파인튜닝 트랙)와 pillar 3(Isaac Lab RL 트랙)에 배치
- 실행 자산 추가: LeRobot 텔레옵 수집 on Greengrass 샘플(aws-samples), Omniverse 디지털 트윈 핸즈온(한국어), 사내 AWS·NVIDIA 로보틱스 참조 아키텍처(사내 전용 표기)

### Fixed

- 번역본의 "국내" 모호함을 Korean/韩国/韓国으로 명시(30곳) — 중국어 독자에게 중국으로 읽히던 문제, 용어집 규칙으로 재발 방지
- 4개 언어 전수 교정(40개 파일) 결과 반영: 워크샵 → 워크숍 표기 통일, 실재 → 실제 수정

## [1.2.0] - 2026-07-18

### Added

- 검증 파이프라인 전과정(후보 발견 → Radar → THE FILTER → 승격 → 감시)을 설명하는 "가이드" 페이지 신설, 상단 탭 내비게이션으로 노출
- FAQ를 Top 10에서 Top 20으로 확장하고 출처 열 추가(11~20번은 공개 커뮤니티 조사 기반)
- Radar "최신 스캔 유입" 섹션 + 주간 자동 스캔(클라우드 루틴, 매주 월 02:00 UTC) + 런북 추가
- 필러·의사결정 트리·가이드·유지보수에 Mermaid 다이어그램 18개 추가, ASCII 다이어그램 전량 대체
- 굵은 제품명 첫 등장에 선별 공식 링크 약 46곳 추가(전수 curl 사전 검증)
- 검증된 워크숍 자산 등재: NVIDIA Isaac Lab on AWS, 자체 개발 pai-sim-isaaclab 핸즈온(다음 액션으로 승격)
- 푸터 소셜 링크(GitHub 저장소·LinkedIn·Bluesky), 이중 언어 README, CC-BY-4.0 LICENSE 추가

### Changed

- 홈 제목을 "Physical AI Playbook 안내"로 변경, 액션 라벨 "SA 다음 액션"을 "다음 액션"으로 변경(118곳), 승격 파이프라인 제목 변경(교차 페이지 앵커 일괄 갱신)
- 1차 출처 검증 결과를 Radar 유입 항목에 반영(Apptronik Apollo 2 승격, Atlas 오칭 정정, AgiBot·1X NEO 주장 정정)

### Fixed

- 불릿이 문단으로 뭉개지던 목록 렌더링 버그 수정: 목록 앞 빈 줄 160곳 삽입(필러 5개 × 4개 언어)

## [1.1.0] - 2026-07-18

### Added

- 사이트 4개 언어 발행: 전 페이지의 영어·중국어(간체)·일본어 번역, 한국어를 원본으로 유지(mkdocs-static-i18n suffix 구조, 언어 전환기)
- ko_hash 기반 번역 표류 감지 추가(`scripts/check_translation_sync.py`, 경고 전용 CI 스텝)
- 번역 용어집(`i18n/glossary.md`)과 translate-sync 스킬 추가(탐지 → 용어집 → 변경분 번역 → strict 빌드 게이트)
- staleness 배지를 번역 페이지에도 언어별로 주입하도록 확장
- README에 다국어 사이트 링크 추가

### Changed

- `navigation.instant` 제거(i18n 언어 전환기와의 문서화된 비호환)

## [1.0.0] - 2026-07-11

### Added

- 최초 릴리스: 마스터 프롬프트로 생성한 8페이지(홈·필러 1~5·의사결정 트리·Radar·유지보수), 페이지별 적대적 사실 검증 수행
- MkDocs Material 사이트 + GitHub Actions의 GitHub Pages 배포(strict 빌드 게이트: 깨진 링크·앵커는 배포 실패)
- 페이지별 변동성 기반 staleness 배지 자동화(1/3/6개월 검토 주기), 주간 cron 재배포로 갱신
- THE FILTER 체크리스트를 내장한 승격 이슈 폼 추가
- 필러 페이지 owner 지정

[Unreleased]: https://github.com/comeddy/pai-playbook/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/comeddy/pai-playbook/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/comeddy/pai-playbook/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/comeddy/pai-playbook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/comeddy/pai-playbook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/comeddy/pai-playbook/releases/tag/v1.0.0
