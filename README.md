# Physical AI Playbook

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC--BY--4.0-green)](LICENSE)
[![Build](https://img.shields.io/github/actions/workflow/status/comeddy/pai-playbook/deploy-docs.yml?branch=main)](https://github.com/comeddy/pai-playbook/actions/workflows/deploy-docs.yml)
[![Site](https://img.shields.io/badge/site-live-blue)](https://comeddy.github.io/pai-playbook/)
[![Release](https://img.shields.io/github/v/release/comeddy/pai-playbook)](CHANGELOG.md)
[![English](https://img.shields.io/badge/lang-English-blue)](#english)
[![한국어](https://img.shields.io/badge/lang-%ED%95%9C%EA%B5%AD%EC%96%B4-red)](#한국어)

A verification-first Physical AI reference for AWS solutions architects — architecture direction, AWS mapping, and next actions in four languages.
AWS SA를 위한 검증 우선 Physical AI 참조 자산 — 아키텍처 방향·AWS 매핑·다음 액션을 4개 언어로 제공합니다.

---

# English

## Overview

Physical AI Playbook is a curated reference site that lets an AWS solutions architect answer a customer's Physical AI question — robotics simulation, VLA model training, sim-to-real, data pipelines, agentic orchestration — with architecture direction, AWS mapping, and a concrete next action in under five minutes. Unlike a news archive, every item must pass a verification gate (THE FILTER) before it enters the body, and the site continuously monitors its own freshness and translation drift. The site is published in Korean (source), English, Chinese, and Japanese at [comeddy.github.io/pai-playbook](https://comeddy.github.io/pai-playbook/).

> **Disclaimer**: This is a personal project. It is **not** official AWS (Amazon Web Services) documentation and does not represent AWS positions. Service specifications, pricing, and regional availability on this site must always be re-verified against the [official AWS documentation](https://docs.aws.amazon.com/).

## Features

- **Verification pipeline (THE FILTER)** — candidates enter a Radar queue as unverified, and only items meeting 2 of 4 criteria (production-validated, AWS-mappable, real inquiry history, GA) are promoted to the body with maturity labels and source grades.
- **Four-language i18n with drift detection** — Korean is the source of truth; each translation records a `ko_hash` fingerprint so CI automatically flags translations that fall behind.
- **Weekly automated radar scan** — a scheduled cloud agent scans recent papers and news every Monday and refreshes the Radar intake section across all four languages.
- **Automatic staleness badges** — every page carries volatility metadata (1/3/6-month review cadence); CI injects a "review needed" badge when a page is overdue, refreshed by a weekly redeploy.
- **Strict build gate** — every deploy must pass `mkdocs build --strict`, so no broken link or anchor ever reaches the live site.

## Prerequisites

- Python >= 3.9
- Git
- pip (packages are pinned in `requirements.txt`)

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/comeddy/pai-playbook.git
cd pai-playbook

# 2. Install dependencies (MkDocs Material + i18n plugin)
pip install -r requirements.txt

# 3. (Optional) install pytest for the script test suite
pip install pytest
```

## Usage

```bash
# Serve the site locally with live reload
mkdocs serve
# -> open http://127.0.0.1:8000

# Validate everything the CI validates (broken links/anchors fail the build)
mkdocs build --strict

# Check page freshness (volatility-based review cadence)
python3 scripts/check_staleness.py --check
# -> prints a 10-row report; exit 1 only when page metadata is missing

# Check translation drift against the Korean source
python3 scripts/check_translation_sync.py
# -> "비동기: 0 / 30" means all 30 translations are in sync
```

Pushing to `main` triggers the GitHub Actions workflow, which runs the checks above and deploys to GitHub Pages.

## Project Structure

```text
pai-playbook/
├── docs/                  # site content: 10 Korean source pages + .en/.zh/.ja translations
├── i18n/glossary.md       # translation rules: fixed renderings, do-not-translate terms
├── scripts/
│   ├── check_staleness.py         # freshness check + badge injection (CI)
│   ├── check_translation_sync.py  # ko_hash drift detection (CI, warn-only)
│   └── radar_scan.md              # runbook for the weekly automated radar scan
├── tests/                 # pytest suite for the scripts
├── specs/ , plans/        # design specs and implementation plans
├── .github/workflows/     # deploy-docs: gates + GitHub Pages deploy + weekly cron
├── mkdocs.yml             # MkDocs Material + static-i18n configuration
└── physical-ai-playbook-master-prompt.md  # the generation spec for the content
```

## Testing

```bash
# Run the script test suite
python3 -m pytest tests/ -v

# Quick run
python3 -m pytest tests/ -q
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/your-topic`.
3. Commit using Conventional Commits: `feat: add X`, `fix: correct Y`, `docs: update Z`.
4. Push the branch: `git push origin feat/your-topic`.
5. Open a Pull Request.

Content contributions must follow the promotion pipeline described on the [maintenance page](https://comeddy.github.io/pai-playbook/maintenance/): new items go to the Radar first and are promoted only after passing THE FILTER. When you edit a Korean source page, update the translations and their `ko_hash` (see `.claude/skills/translate-sync/`), and make sure `mkdocs build --strict` passes before opening the PR.

## License

This project is licensed under the Creative Commons Attribution 4.0 International License — see the [LICENSE](LICENSE) file.

## Contact

- Maintainer: [comeddy](https://github.com/comeddy)
- Issues: [github.com/comeddy/pai-playbook/issues](https://github.com/comeddy/pai-playbook/issues)
- Email: comeddy@gmail.com
- Changelog: [CHANGELOG.md](CHANGELOG.md) · [Releases](https://github.com/comeddy/pai-playbook/releases)

---

# 한국어

## 개요

Physical AI Playbook은 AWS 솔루션즈 아키텍트가 고객의 Physical AI 질문 — 로보틱스 시뮬레이션, VLA 모델 학습, sim-to-real, 데이터 파이프라인, 에이전트 오케스트레이션 — 에 대해 아키텍처 방향·AWS 매핑·다음 액션을 5분 안에 제시할 수 있게 하는 큐레이션 참조 사이트입니다. 뉴스 아카이브와 달리 모든 항목은 검증 관문(THE FILTER)을 통과해야 본문에 실리며, 사이트 스스로 신선도와 번역 표류를 상시 감시합니다. 한국어(원본)·영어·중국어·일본어 4개 언어로 [comeddy.github.io/pai-playbook](https://comeddy.github.io/pai-playbook/)에 배포됩니다.

> **면책 안내**: 이 사이트는 개인 프로젝트이며, **AWS(Amazon Web Services)의 공식 문서·공식 입장이 아닙니다.** 이 사이트의 서비스 사양·가격·리전 지원은 반드시 [AWS 공식 문서](https://docs.aws.amazon.com/)에서 재확인합니다.

## 주요 기능

- **검증 파이프라인 (THE FILTER)** — 후보는 미검증 상태로 Radar 대기열에 먼저 들어가고, 4개 기준(production 검증·AWS 매핑·실제 문의 이력·GA) 중 2개 이상을 충족한 항목만 성숙도 라벨·출처 등급과 함께 본문으로 승격됩니다.
- **표류 감지가 있는 4개 언어 i18n** — 한국어가 원본이며, 각 번역은 `ko_hash` 지문을 기록해 원본보다 뒤처진 번역을 CI가 자동으로 경고합니다.
- **주간 자동 Radar 스캔** — 스케줄된 클라우드 에이전트가 매주 월요일 최신 논문·뉴스를 스캔해 4개 언어의 Radar 유입 섹션을 갱신합니다.
- **자동 신선도 배지** — 모든 페이지가 변동성 메타데이터(1/3/6개월 검토 주기)를 가지며, 기한이 지나면 CI가 "검토 필요" 배지를 자동 주입하고 주간 재배포로 최신 상태를 유지합니다.
- **strict 빌드 게이트** — 모든 배포는 `mkdocs build --strict`를 통과해야 하므로, 깨진 링크·앵커는 라이브 사이트에 도달하지 못합니다.

## 사전 요구 사항

- Python >= 3.9
- Git
- pip (패키지는 `requirements.txt`에 고정되어 있습니다)

## 설치 방법

```bash
# 1. 저장소를 복제합니다
git clone https://github.com/comeddy/pai-playbook.git
cd pai-playbook

# 2. 의존성을 설치합니다 (MkDocs Material + i18n 플러그인)
pip install -r requirements.txt

# 3. (선택) 스크립트 테스트용 pytest를 설치합니다
pip install pytest
```

## 사용법

```bash
# 로컬에서 라이브 리로드로 사이트를 띄웁니다
mkdocs serve
# -> http://127.0.0.1:8000 접속

# CI와 동일한 검증을 수행합니다 (깨진 링크/앵커는 빌드 실패)
mkdocs build --strict

# 페이지 신선도를 검사합니다 (변동성 기반 검토 주기)
python3 scripts/check_staleness.py --check
# -> 10행 리포트 출력; 페이지 메타데이터 누락 시에만 exit 1

# 한국어 원본 대비 번역 표류를 검사합니다
python3 scripts/check_translation_sync.py
# -> "비동기: 0 / 30" 이면 30개 번역 전부 동기화 상태
```

`main`에 푸시하면 GitHub Actions 워크플로우가 위 검사를 수행한 뒤 GitHub Pages로 배포합니다.

## 프로젝트 구조

```text
pai-playbook/
├── docs/                  # 사이트 콘텐츠: 한국어 원본 10페이지 + .en/.zh/.ja 번역
├── i18n/glossary.md       # 번역 규칙: 고정 역어, 번역 금지 용어
├── scripts/
│   ├── check_staleness.py         # 신선도 검사 + 배지 주입 (CI)
│   ├── check_translation_sync.py  # ko_hash 표류 감지 (CI, 경고만)
│   └── radar_scan.md              # 주간 자동 Radar 스캔 런북
├── tests/                 # 스크립트 pytest 테스트
├── specs/ , plans/        # 설계 스펙과 구현 계획
├── .github/workflows/     # deploy-docs: 게이트 + GitHub Pages 배포 + 주간 cron
├── mkdocs.yml             # MkDocs Material + static-i18n 설정
└── physical-ai-playbook-master-prompt.md  # 콘텐츠 생성 스펙
```

## 테스트

```bash
# 스크립트 테스트를 실행합니다
python3 -m pytest tests/ -v

# 간단 실행
python3 -m pytest tests/ -q
```

## 기여 방법

1. 저장소를 Fork합니다.
2. 기능 브랜치를 만듭니다: `git checkout -b feat/your-topic`.
3. Conventional Commits 형식으로 커밋합니다: `feat: add X`, `fix: correct Y`, `docs: update Z`.
4. 브랜치를 푸시합니다: `git push origin feat/your-topic`.
5. Pull Request를 엽니다.

콘텐츠 기여는 [유지보수 페이지](https://comeddy.github.io/pai-playbook/maintenance/)의 승격 파이프라인을 따라야 합니다: 새 항목은 Radar에 먼저 올라가고 THE FILTER 통과 후에만 승격됩니다. 한국어 원본을 수정한 경우 번역과 `ko_hash`를 함께 갱신하고(`.claude/skills/translate-sync/` 참고), PR 전에 `mkdocs build --strict` 통과를 확인해 주십시오.

## 라이선스

이 프로젝트는 Creative Commons Attribution 4.0 International 라이선스를 따릅니다 — [LICENSE](LICENSE) 파일을 확인해 주십시오.

## 연락처

- 메인테이너: [comeddy](https://github.com/comeddy)
- 이슈: [github.com/comeddy/pai-playbook/issues](https://github.com/comeddy/pai-playbook/issues)
- 이메일: comeddy@gmail.com
- 변경 이력: [CHANGELOG.md](CHANGELOG.md) · [Releases](https://github.com/comeddy/pai-playbook/releases)
