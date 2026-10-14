# Radar 자동 스캔 런북

정기 실행되는 "최신 Physical AI 기술·논문·뉴스 → Radar 유입" 자동화의 표준 절차.
`docs/radar.md`의 **`## 🆕 최신 스캔 유입`** 섹션을 새 배치로 갱신하고, AWS Physical AI 블로그의 미반영 글을 **`docs/news.md`(새 소식)**에 추가한다(2026-10-14 추가 — 아래 '새 소식 갱신' 절).

> **스케줄 소재 (이 저장소 밖):** 이 런북은 **claude.ai 스케줄 루틴**이 실행한다 —
> `pai-playbook Radar 일간 자동 스캔`, cron `0 2 * * *`(매일 02:00 UTC — 2026-07-24 주간→일간 전환), 모델 claude-sonnet-5,
> 루틴 ID `trig_01KWwHEnRP6Di1gYTnP5uxJ8`. `.github/workflows/`에는 없다(거기 있는 매일 00:00 UTC cron은
> staleness 배지 재배포용 — 별개). 관리·수동 실행·중지: https://claude.ai/code/routines
> 루틴이 만든 커밋은 author가 `Claude Sonnet 5`로 찍힌다.

## 원칙 (반드시 준수)

- **정직성**: 유입 항목은 전부 미검증이다. 라벨은 🔵 Research / ⚪ Hype·로드맵 / 🟡 Preview·발표 중 하나, 출처 등급은 `[4]`(미검증). 수록에는 고객 문제·정확한 1차 출처/버전/확인일·근거/사용 범위·소유자/다음 액션이 모두 필요하다. AWS 매핑과 로드맵만으로 승격하지 않는다. **본문 승격은 사람 owner의 검토 후에만** 수행한다.
- **중복 제거**: 이미 radar.md의 다른 표(🔬/🖥️/🤖/🔗/⚰️)나 pillar 본문에 있는 항목은 다시 넣지 않는다.
- **큐레이션**: 유입 표는 **최대 ~10행** 유지. 일간 주기에서는 **하루 신규 0~3건이 정상**이며 "새로 나왔다"만으로는 넣지 않는다 — 실무 관련성(로보틱스 VLA/시뮬/sim-to-real/데이터/에이전트/배포) 기준으로 선별. **Radar 신규 0건 + 기존 항목 정정 없음 + 새 소식 추가 0건이면 커밋하지 않는다.**
- **날짜 표기**: 섹션 제목의 `(YYYY-MM …)`을 실행 월로 갱신.
- **용어 각주 유지**: 신규 유입 항목에 SA가 바로 이해하기 어려운 용어가 들어오면 **같은 커밋에서 `[^라벨]` 각주로 처리**한다(CLAUDE.md 용어 각주 관례). radar 하단 `<!-- 용어 각주 -->` 블록의 기존 라벨 재사용 우선, 새 정의는 1~2문장, 마커는 **페이지 본문 첫 등장 위치 1곳에만**(헤딩·mermaid 금지), 4개 언어 동일 라벨·정의 블록 동일 개수·순서. 행 제거로 마커가 모두 사라진 정의는 함께 삭제한다(렌더링은 안 되지만 소스 잔재 방지).
- **링크 검증**: 유입 항목의 **항목명에는 가능하면 1차 확인용 공식 출처 바로가기를 부착**한다(2026-07-29부터 radar 전 항목 관례 — 사람이 "왜 대기"를 직접 검증하는 진입점). **공식 출처만**, 삽입 전 `curl -sIL -o /dev/null -w '%{http_code}'`로 **전수 200 확인** — strict 빌드는 외부 링크를 검사하지 못하므로 이 수동 게이트가 유일한 방어선이다. 404는 폴백(공식 페이지) 또는 제외하고 커밋 메시지에 기록.

## 절차

0. **staleness 알림** (보고 전용): `python3 scripts/check_staleness.py --check` 실행. 최종 보고는 **반드시 staleness 상태 줄로 시작** — 0건이면 `✅ staleness: 0`, 있으면 `⏳ STALE (owner 검토 필요): <페이지> (<경과>/<기준> 개월), …`. 페이지의 owner/updated/volatility를 수정해 stale을 해소하는 것은 금지 — 그건 owner(사람)의 몫이다.
1. **스캔** (여러 각도, WebSearch 위주 — 헤드리스에서 alphaXiv MCP는 없을 수 있음):
   - arXiv/논문: "vision-language-action / humanoid manipulation / sim-to-real / world action model / physical AI data(로봇 데이터 수집·데이터셋·데이터 파이프라인) 최신"
   - 뉴스·기술: "Physical AI robotics latest news <이번달> · NVIDIA Isaac/GR00T/Cosmos release · AWS Physical AI blog · The Robot Report Physical AI 최신 · IEEE Spectrum Robotics 최신"
   - 경쟁·하드웨어: "humanoid robot foundation model announcement · Gemini/Figure/1X/Tesla 최신"
   - AWS 워크샵: "AWS Workshop Studio(catalog.workshops.aws) physical AI · robotics · Isaac Sim · SageMaker robotics 신규 워크샵" — 신규 워크샵은 뉴스가 아니라 SA 실습 자산이므로, 유입 표 대신 해당 필러 **🔗 관련 자산** 편입 후보로 보고에 남긴다(편입 자체는 aws-samples 분기 조사와 동일하게 사람 리뷰 경로).
2. **선별 + 라벨링**: THE FILTER로 거르고 성숙도 라벨·`[4]`·"왜 주목받는가"(의미·시사점 1줄)·"왜 대기"·"승격 조건" **5열**을 채운다(2026-08-08부터 radar 전 섹션 공통 표 구조). 기존 radar 항목과 dedup.
3. **한국어 갱신**: `docs/radar.md`의 `## 🆕 최신 스캔 유입` 섹션 표를 **재평가 + 신규 추가** 방식으로 갱신 — 기존 행 중 여전히 유효·검증 대기인 것은 유지, 낡았거나 반박된 것은 제거, 신규를 추가하고 **~10행 상한**(초과 시 오래된·관련성 낮은 것부터 제거). 승격됐거나 폐기된 항목은 적절한 섹션으로 이동/제거.
4. **다국어 동기화**: `translate-sync` 스킬 절차로 en/zh/ja 반영 + `ko_hash` 갱신 (`i18n/glossary.md` 준수).
5. **게이트**: `python3 scripts/check_translation_sync.py`(비동기 0) + `mkdocs build --strict`(exit 0).
6. **커밋·푸시**: 변경한 `docs/radar.*`·`docs/news.*` 파일만 커밋한다. 커밋 메시지에 스캔 날짜·건수·주요 출처(새 소식 추가분은 글 제목·발행일, 링크 검증 방식)를 남긴다. `main` 푸시 → CI가 배포.

## 새 소식 갱신 (docs/news.md — 2026-10-14 추가)

배경: '새 소식'은 2026-09-19 생성 후 갱신 단계가 없어 블로그 신규 글 4건이 3주 넘게 누락됐다. Radar 스캔과 같은 실행에서 아래를 수행한다. Radar와 달리 **선별하지 않는다** — AWS Physical AI 블로그의 글은 전부 수록 대상이다(같은 기술이 Radar에도 있으면 둘 다 둔다).

1. **피드 수집**: `curl -s -m 20 https://aws.amazon.com/blogs/physical-ai/feed/` → 실패(egress 차단)하면 WebFetch로 같은 URL → 그것도 실패하면 WebSearch `site:aws.amazon.com/blogs/physical-ai`. **어느 방식으로 얻었는지 기록**한다.
2. **미반영 글 찾기**: 피드의 각 `<link>`가 `docs/news.md`에 없으면 미반영이다. 표의 가장 오래된 발행일보다 이전 글은 대상이 아니다. 한 번에 최대 5건(오래된 글부터).
3. **본문 작성(ko)**: 각 글의 원문을 읽고(WebFetch 가능하면 본문, 불가하면 피드 요약) 기존 항목과 **같은 형식**으로 추가한다 — `## 제목 { #영문-앵커 }` 섹션(가장 최신 기존 섹션 바로 위, 발행일 내림차순)과 `## 최근 자료 한눈에` 표의 행(발행일 순서 위치).
   - 발행일 줄: `**발행일: YYYY-MM-DD · [AWS Physical AI](<원문 URL>) `[4]` · ⏳ 원문 대조 대기 (자동 스캔 YYYY-MM-DD)**` — 자동 추가분은 **`[4]` + ⏳ 표시 필수**. owner가 원문을 대조한 뒤 `[3]`으로 바꾸고 ⏳ 표시를 지운다(자동화는 기존 항목의 등급·표시를 바꾸지 않는다).
   - 본문 2~3문장: 무엇을 하는 글인지, 쓰는 AWS·NVIDIA 구성 요소, 코드·저장소 위치.
   - **읽을 때 확인할 범위**(정직성 핵심): 글의 성격(공식 가이드/고객 사례/산업 개요), **공개 여부**(공개 저장소인지, 계정팀 제공인지), 벤더 자체 표현과 실측의 구분, 시뮬레이션·오프라인 평가와 실기 성공률의 구분. 원문에 없는 수치·주장을 만들지 않는다.
   - **다음 액션**: 실제 존재하는 필러·워크숍 앵커로만 링크(strict 빌드가 앵커를 검사).
4. **메타데이터**: TL;DR의 '목록 확인일'은 **1번에서 피드를 실제로 받은 경우에만** 실행일로 바꾼다(WebSearch 대체 시 그대로 둔다). 페이지 `_owner · updated · volatility_` 줄은 건드리지 않는다 — owner가 대조 후 갱신한다.
5. **링크**: 원문·저장소 링크는 `curl -sIL -o /dev/null -w '%{http_code}'` 200 확인. egress 차단으로 확인 못 하면 커밋 메시지에 "링크 미검증(egress)"이라고 남긴다.
6. **용어 각주·번역**: Radar와 같은 각주 규칙(news.md 하단 `<!-- 용어 각주 -->`, 마커는 본문 첫 등장 1곳 — 새 섹션이 위에 들어가 첫 등장 위치가 바뀌면 마커를 옮긴다), translate-sync로 en/zh/ja + `ko_hash`.
7. **보고**: 최종 보고에 `📰 새 소식: N건 추가(원문 대조 대기)` 또는 `📰 새 소식: 0건` 한 줄을 넣는다.

## 검증 명령

```bash
python3 scripts/check_translation_sync.py            # 비동기 0 확인
mkdocs build --strict --site-dir /tmp/radar-scan     # exit 0 확인
```

## 사람이 할 일 (자동화가 못 하는 것)

- 유입 항목의 **1차 출처 검증**(날짜·버전·라이선스) — 웹 요약은 오기가 잦다.
- THE FILTER 수록 조건을 모두 확인 → **본문 승격**은 담당 pillar owner가 검토 범위를 기록한 후 수동으로.
