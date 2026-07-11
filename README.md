# Physical AI Playbook (AWS Korea SA)

고객의 Physical AI 질문에 **아키텍처 방향 · AWS 매핑 · 다음 액션**을 5분 안에 제시하기 위한 참조 자산.
콘텐츠는 [`docs/`](docs/index.md), 생성 스펙은 [`physical-ai-playbook-master-prompt.md`](physical-ai-playbook-master-prompt.md).

## 로컬 미리보기

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve   # http://127.0.0.1:8000
```

## 배포 (GitHub Pages)

`main` 푸시 시 [`deploy-docs` 워크플로우](.github/workflows/deploy-docs.yml)가 MkDocs Material로 빌드해 Pages에 배포한다.
저장소 생성 후 1회 설정:

1. GitHub 저장소 **Settings → Pages → Source: GitHub Actions** 선택
2. `mkdocs.yml`의 `site_url`을 실제 Pages URL로 교체

## 콘텐츠 수정 규칙

- 포함 기준·템플릿·승격 파이프라인: [`docs/maintenance.md`](docs/maintenance.md) 준수
- 휘발성 정보(버전·가격·리전)는 본문이 아니라 `<details markdown="1">` 접힌 블록에
- 모든 항목은 성숙도 라벨 + 출처 등급 + `➡️ SA 다음 액션` 필수
