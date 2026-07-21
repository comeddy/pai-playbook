# Radar 자동 스캔 런북

정기 실행되는 "최신 Physical AI 기술·논문·뉴스 → Radar 유입" 자동화의 표준 절차.
`docs/radar.md`의 **`## 🆕 최신 스캔 유입`** 섹션을 새 배치로 갱신한다.

> **스케줄 소재 (이 저장소 밖):** 이 런북은 **claude.ai 스케줄 루틴**이 실행한다 —
> `pai-playbook Radar 주간 자동 스캔`, cron `0 2 * * 1`(매주 월 02:00 UTC), 모델 claude-sonnet-5,
> 루틴 ID `trig_01KWwHEnRP6Di1gYTnP5uxJ8`. `.github/workflows/`에는 없다(거기 있는 월요일 cron은
> staleness 배지 재배포용 00:00 UTC — 별개). 관리·수동 실행·중지: https://claude.ai/code/routines
> 루틴이 만든 커밋은 author가 `Claude Sonnet 5`로 찍힌다.

## 원칙 (반드시 준수)

- **정직성**: 유입 항목은 전부 미검증이다. 라벨은 🔵 Research / ⚪ Hype·로드맵 / 🟡 Preview·발표 중 하나, 출처 등급은 `[4]`(미검증). THE FILTER(ⓐproduction ⓑAWS매핑 ⓒ실제문의 ⓓGA 중 2개 이상)를 **통과하기 전에는 본문(pillar) 승격 금지**.
- **중복 제거**: 이미 radar.md의 다른 표(🔬/🖥️/🤖/🔗/⚰️)나 pillar 본문에 있는 항목은 다시 넣지 않는다.
- **큐레이션**: 한 배치는 **6~10건**으로 제한. "새로 나왔다"만으로는 넣지 않는다 — 실무 관련성(로보틱스 VLA/시뮬/sim-to-real/데이터/에이전트/배포) 기준으로 선별.
- **날짜 표기**: 섹션 제목의 `(YYYY-MM …)`을 실행 월로 갱신.
- **링크 검증**: 유입 항목에 URL을 넣는 경우(선택) **공식 출처만**, 삽입 전 `curl -sIL -o /dev/null -w '%{http_code}'`로 **전수 200 확인** — strict 빌드는 외부 링크를 검사하지 못하므로 이 수동 게이트가 유일한 방어선이다. 404는 폴백(공식 페이지) 또는 제외하고 커밋 메시지에 기록.

## 절차

1. **스캔** (여러 각도, WebSearch 위주 — 헤드리스에서 alphaXiv MCP는 없을 수 있음):
   - arXiv/논문: "vision-language-action / humanoid manipulation / sim-to-real / world action model / physical AI data(로봇 데이터 수집·데이터셋·데이터 파이프라인) 최신"
   - 뉴스·기술: "Physical AI robotics latest news <이번달> · NVIDIA Isaac/GR00T/Cosmos release · AWS Physical AI blog · The Robot Report Physical AI 최신 · IEEE Spectrum Robotics 최신"
   - 경쟁·하드웨어: "humanoid robot foundation model announcement · Gemini/Figure/1X/Tesla 최신"
2. **선별 + 라벨링**: THE FILTER로 거르고 성숙도 라벨·`[4]`·"왜 대기"·"승격 조건" 4열을 채운다. 기존 radar 항목과 dedup.
3. **한국어 갱신**: `docs/radar.md`의 `## 🆕 최신 스캔 유입` 섹션 표를 **통째로 교체**(누적 아님 — 오래된 미검증 항목은 매 배치마다 재평가). 승격됐거나 폐기된 항목은 적절한 섹션으로 이동/제거.
4. **다국어 동기화**: `translate-sync` 스킬 절차로 en/zh/ja 반영 + `ko_hash` 갱신 (`i18n/glossary.md` 준수).
5. **게이트**: `python3 scripts/check_translation_sync.py`(비동기 0/30) + `mkdocs build --strict`(exit 0).
6. **커밋·푸시**: 커밋 메시지에 스캔 날짜·건수·주요 출처를 남긴다. `main` 푸시 → CI가 배포.

## 검증 명령

```bash
python3 scripts/check_translation_sync.py            # 비동기 0/30 확인
mkdocs build --strict --site-dir /tmp/radar-scan     # exit 0 확인
```

## 사람이 할 일 (자동화가 못 하는 것)

- 유입 항목의 **1차 출처 검증**(날짜·버전·라이선스) — 웹 요약은 오기가 잦다.
- THE FILTER 2개 이상 충족 판단 → **본문 승격**은 담당 pillar owner가 수동으로.
