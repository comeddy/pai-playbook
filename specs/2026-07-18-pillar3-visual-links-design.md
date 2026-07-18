# pillar-3 가독성 파일럿 설계 — Mermaid 다이어그램 + 선별 하이퍼링크

- 날짜: 2026-07-18
- 상태: 승인됨
- 범위: pillar-3(시뮬레이션) 4개 언어에 다이어그램 3개와 선별 링크를 추가하는 파일럿. 라이브 확인 후 마음에 들면 나머지 필러로 롤아웃(별도 스펙).

## 확정된 결정

| 결정 | 선택 |
|------|------|
| 이미지 조달 | **Mermaid 다이어그램 기본** + 재배포 허용 라이선스가 명확한 공식 이미지만 예외 (파일럿에서는 Mermaid만 사용) |
| 범위 | pillar-3 파일럿 → 승인 후 롤아웃 |
| 링크 정책 | 전부가 아니라 **항목당 1~2개**, 굵은 제품명 **첫 등장**에만, **공식 출처만**, 삽입 전 URL 전수 검증 |

## 1. Mermaid 기반 (mkdocs.yml)

`markdown_extensions`의 `pymdownx.superfences`에 custom fence 추가:

```yaml
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
```

주의: 기존 `pymdownx.superfences`는 목록의 단순 항목 — custom_fences 딕셔너리 형태로 교체. Material 테마가 mermaid class를 감지해 네이티브 렌더(다크모드 자동).

## 2. 다이어그램 3개 (ko 원본 배치)

- **§1 Isaac Sim & Isaac Lab on AWS** — "AWS 매핑" 뒤: GUI 경로(사용자→NICE DCV→EC2 G6e/G7e+Isaac Sim AMI)와 헤드리스 경로(Isaac Lab 컨테이너→AWS Batch MNP) 이중 경로 flowchart (graph LR)
- **§2 대규모 병렬 RL** — "솔루션 개요" 뒤: 단일 GPU(수천 환경) → 스케일 필요 분기 → Batch MNP(+EFS/ECR) flowchart
- **§3 오픈소스 대안** — "의사결정 기준" 근처: "무엇이 우선인가?" 분기 — 포토리얼·SDG→Isaac Sim / 미분가능·크로스벤더 GPU→MuJoCo/MJX / ROS 2·CPU→Gazebo / Genesis→PoC만 ⚪

스타일 규칙: graph LR/TD, 노드 라벨은 짧게, 이모지 최소(성숙도 표시용만), 페이지당 3개 초과 금지(과유불급).

## 3. 선별 하이퍼링크 (후보 — 구현 시 전수 URL 검증 후 확정)

| 굵은 용어(첫 등장) | 링크 |
|---|---|
| Isaac Lab | github.com/isaac-sim/IsaacLab |
| Isaac Sim Development Workstation AMI | AWS Marketplace 목록 페이지 |
| NICE DCV | aws.amazon.com/hpc/dcv/ |
| AWS Batch Multi-Node Parallel | AWS 공식 문서 |
| MuJoCo | github.com/google-deepmind/mujoco |
| MuJoCo Playground | playground.mujoco.org (검증 필요) |
| Gazebo | gazebosim.org |
| Genesis | github.com/Genesis-Embodied-AI/Genesis |
| Cosmos 3 | NVIDIA 공식 Cosmos 페이지 |
| AWS IoT TwinMaker | aws.amazon.com/iot-twinmaker/ |

규칙: 404/리다이렉트 이상은 제외하거나 대체. 이미 링크가 있는 용어(관련 자산 줄 등)는 중복 링크 금지.

## 4. 4개 언어 동기화

- mermaid 라벨은 번역, **구조·방향(LR/TD)·노드 ID는 유지**. 링크 URL은 4개 언어 동일.
- `i18n/glossary.md` §3에 규칙 1줄 추가: "mermaid 코드 펜스: 내부 라벨 텍스트는 번역하되 노드 ID·화살표·방향 선언은 유지" (현행 '코드 블록 유지' 규칙과의 충돌 해소)
- ko_hash 갱신은 기존 절차.

## 5. 검증

- `mkdocs build --strict` exit 0 + 산출물 pillar-3 HTML에 `class="mermaid"` 3개(언어당)
- sync 비동기 0/30
- 추가된 외부 링크 전수 curl HTTP 200 (또는 명시적 3xx 최종 200)
- 라이브 4개 언어에서 다이어그램 렌더 확인

## 범위 외 (YAGNI)

- 나머지 필러·decisions 적용 (파일럿 승인 후 별도)
- 외부 이미지 자산 (파일럿에서는 미사용)
- Mermaid 테마 커스터마이징
