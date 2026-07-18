# 가독성 롤아웃 설계 — pillar-1/2/4/5 (Mermaid + 선별 링크)

- 날짜: 2026-07-18
- 상태: 승인됨 (파일럿 `specs/2026-07-18-pillar3-visual-links-design.md` 스타일의 라이브 확인 후 사용자 승인)
- 범위: pillar-1/2/4/5 × 4개 언어. decisions는 범위 외(별도 요청 시).

## 파일럿에서 확정된 패턴 (그대로 적용)

- 다이어그램: **페이지당 2~3개**, "아키텍처 경로"나 "분기 선택" 성격의 섹션에만. graph LR/TD, 노드 ID·방향은 4개 언어 공유, 라벨만 번역, 제품명 번역 금지, 펜스 앞뒤 빈 줄. 참조 구현: `docs/pillar-3.md`의 3개.
- 링크: 굵은 제품명 **첫 등장 1곳씩만**, 공식 출처만, 삽입 전 curl 검증(200 아니면 대체/제외), 기존 링크와 중복 금지. 페이지당 6~10곳.
- 콘텐츠 불변: 문장 수정·삭제 금지 — 다이어그램 삽입과 링크 마크업 래핑만.

## 페이지별 다이어그램 주제 (구현자가 실제 본문에 맞춰 확정 — 주제 이탈 시 report에 근거 기록)

| 페이지 | 후보 주제 (2~3개) |
|--------|------------------|
| pillar-1 (데이터) | ① 데이터 3원천(텔레옵·오픈 데이터셋·합성)→S3 데이터레이크→학습 파이프라인 흐름 ② 오픈 데이터셋 라이선스 분기(상업 가능? OXE/DROID/AgiBot) ③ (선택) 합성 데이터 SDG 파이프라인 |
| pillar-2 (VLA 학습) | ① 오픈 VLA 모델 선택 분기(라이선스: π/OpenVLA 상업 vs GR00T 확인 필요) ② 학습 스택 사다리(단일 G7e LoRA → HyperPod → P6e 초대형) |
| pillar-4 (Sim-to-Real) | ① sim-to-real 파이프라인(시뮬 학습→도메인 랜덤라이제이션→실기체 검증) ② 엣지 배포 경로(정책→ONNX/TensorRT→Jetson/Greengrass) |
| pillar-5 (에이전트) | ① System 2(LLM 플래너)/System 1(로봇 컨트롤러) 계층 아키텍처(Bedrock AgentCore 중심) ② (선택) 플릿 오케스트레이션 흐름 |

## 링크 정책 (파일럿과 동일)

각 페이지의 굵은 제품·서비스명 첫 등장에 공식 URL. 후보 예: HyperPod·SageMaker·Bedrock AgentCore·IoT Greengrass·LeRobot·OpenVLA·openpi·GR00T·Open X-Embodiment·DROID·TensorRT·Jetson 등 — 구현자가 본문 스캔으로 확정하고 **전수 curl 검증 후** 적용, 확정표를 report에 기록.

## 검증 (페이지·태스크마다)

- staleness --check exit 0 · sync 비동기 0/30 · `mkdocs build --strict` exit 0
- 언어당 `class="mermaid"` = 해당 페이지 다이어그램 수 · 신규 링크 전부 검증표와 일치
- 콘텐츠 불변: diff에서 문장 삭제/수정 0 (마크업 래핑·삽입만)
- 전체 완료 후 push → CI → 라이브 4개 언어 확인
