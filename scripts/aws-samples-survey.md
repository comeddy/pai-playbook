# aws-samples Physical AI 자산 분기 전수 조사 런북

aws-samples(+awslabs) 조직의 신규 리포와 AWS Workshop Studio의 신규 워크샵을 찾아 필러 관련 자산으로 등재하는 표준 절차. 2026-07-31 수동 조사(PR #4)를 루틴화한 것(워크샵 조사는 2026-08-17 추가).

> **스케줄 소재 (이 저장소 밖):** claude.ai 스케줄 루틴 `pai-playbook aws-samples 분기 조사`,
> cron `0 3 1 */3 *`(1·4·7·10월 1일 03:00 UTC — radar 일간 스캔 02:00 뒤), 모델 claude-sonnet-5,
> 루틴 ID `trig_01Fdmi52CJhMtNbYytGbkDH1`. 관리·수동 실행·중지: https://claude.ai/code/routines
> **일간 radar 스캔과 달리 main 직푸시 금지 — 브랜치 push + PR(불가 시 compare URL 보고)**: 필러 본문을 고치는 작업이라 사람 리뷰를 거친다.

## 절차

1. **검색** (`gh search repos "<키워드>" --owner aws-samples --limit 30 --json fullName,updatedAt,stargazersCount`):
   키워드 최소 셋 — physical-ai / "physical ai" / robotics / embodied / humanoid / isaac / lerobot / "vla robot" / ros2 / jetson / manipulation / gr00t. awslabs도 physical-ai·robotics 2개 키워드로 훑는다.
   1-1. **워크샵 검색** (Workshop Studio는 공개 API 없음 — WebSearch 기반):
   `site:catalog.workshops.aws` + physical AI / robotics / Isaac Sim / SageMaker robotics / IoT robotics 키워드로 훑고, AWS 공식 블로그의 워크샵 소개 글을 보조 소스로 쓴다. 검색이 못 잡는 신규분이 있을 수 있으므로 "전수"가 아닌 최선 노력 조사임을 보고에 명시.
2. **Dedup**: 이미 등재된 리포·워크샵은 제외 —
   `grep -rho "github.com/aws-\(samples\|labs\)[a-zA-Z0-9/-]*" docs/*.md | grep -v '\.\(en\|zh\|ja\)\.' | sort -u`
   `grep -rho "catalog.workshops.aws/[a-zA-Z0-9/._-]*" docs/*.md | grep -v '\.\(en\|zh\|ja\)\.' | sort -u`
3. **제외 기준** (리포: `gh api repos/<owner>/<repo> --jq '[.archived, .pushed_at, .topics]'`):
   아카이브 / 마지막 push 18개월 초과 / RoboMaker 등 폐기 서비스 종속 / 실무 관련성 없는 장난감 데모.
   워크샵: 폐기 서비스 종속 / Physical AI 실무 관련성 없음(범용 ML·IoT 입문은 제외) / 접속 불가.
4. **실체 검증**: 리포는 README 확인(무엇을 배포하고 무엇이 WIP/데모인지 — 캐비앗 문구 그대로 발췌), 워크샵은 개요 페이지에서 다루는 서비스·소요 시간·레벨 확인. URL은 전부 `curl -sIL -o /dev/null -w '%{http_code}'` 200 확인.
5. **편입**: 가장 맞는 필러의 **🔗 관련 자산** 불릿 목록에 기존 형식으로 추가 —
   리포: `- [이름 — 한 줄 정체](URL) — aws-samples. 기능 요약. ⚠️ 성숙도 캐비앗(README 자기 선언 우선)`.
   워크샵: `- [워크샵명 — 한 줄 정체](URL) — AWS Workshop Studio. 다루는 서비스·레벨·소요 시간 요약`.
   신규 0건이면 아무것도 바꾸지 말고 조사 결과만 보고.
6. **4개 언어 동기화**: translate-sync 절차(en/zh/ja 동일 불릿 + `--hash`로 ko_hash 갱신).
7. **게이트**: `python3 scripts/check_translation_sync.py`(**비동기 0** — 총수는 페이지 증가에 따라 변하므로 0만 확인) + `mkdocs build --strict`(exit 0).
8. **CHANGELOG**: 4개 언어 Unreleased > Added에 1줄씩.
9. **브랜치·PR**: `survey/YYYY-MM` 브랜치로 커밋·push → `gh pr create`(제목·본문에 조사 모수/제외 목록/게이트 결과). gh 인증 불가 환경이면 브랜치만 push하고 compare URL(`https://github.com/comeddy/pai-playbook/compare/main...survey/YYYY-MM`)을 보고에 남긴다.

## 원칙

- **README 자기 선언을 넘어서는 주장 금지** — "데모"라고 쓰인 리포를 역량처럼 소개하지 않는다. 워크샵도 개요 페이지가 명시한 범위까지만 서술.
- 편입은 관련 자산 링크까지 — 본문 서술·radar 항목 추가는 사람(owner) 판단.
- 발견했지만 편입 애매한 리포는 GitHub 이슈(enhancement)로 기록 (CLAUDE.md 규칙 5).
