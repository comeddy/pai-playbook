# 번역 용어집 & 규칙 (ko → en/zh/ja)

빌드 미포함 운영 파일. translate-sync 스킬과 모든 번역 작업이 이 파일을 먼저 로드한다.

## 1. 번역 금지 (원문 유지)

Physical AI, Sim-to-Real, VLA, GA, Radar, TL;DR, L0/L1/L2,
Open X-Embodiment(OXE), DROID, AgiBot World, LeRobot, RLDS,
Isaac Sim, Isaac Lab, Isaac OSMO, SDG, Replicator, Cosmos, Cosmos WFM, GR00T, OpenVLA, π0, RT-2-X,
AWS 서비스명 전부(SageMaker, S3, Batch, ...), 모델·데이터셋·라이선스 이름(CC-BY-4.0 등)

## 2. 고정 역어

| ko | en | zh | ja |
|----|----|----|----|
| 텔레옵 | teleoperation | 遥操作 | テレオペレーション |
| 합성 데이터 | synthetic data | 合成数据 | 合成データ |
| 의사결정 트리 | decision tree | 决策树 | 意思決定ツリー |
| 대기열 | queue | 队列 | キュー |
| 유지보수 규칙 | maintenance rules | 维护规则 | メンテナンスルール |
| 갱신 규칙 | update rules | 更新规则 | 更新ルール |
| 검토 필요 | review needed | 需要复核 | 要レビュー |
| 참조 아키텍처 | reference architecture | 参考架构 | リファレンスアーキテクチャ |
| 사전학습 | pretraining | 预训练 | 事前学習 |
| 파인튜닝 | fine-tuning | 微调 | ファインチューニング |
| 필러 | pillar | 支柱 | ピラー |
| 파운데이션 모델 | foundation model | 基础模型 | 基盤モデル |
| 시뮬레이션 | simulation | 仿真 | シミュレーション |
| 시뮬레이터 | simulator | 仿真器 | シミュレーター |
| 정책(policy) | policy | 策略 | ポリシー |
| 추론 | inference | 推理 | 推論 |
| 배포 | deployment | 部署 | デプロイ |
| 매니퓰레이션 | manipulation | 操作(机械臂操作) | マニピュレーション |
| 그리퍼 | gripper | 夹爪 | グリッパー |
| 로봇 학습 | robot learning | 机器人学习 | ロボット学習 |
| 궤적 | trajectory | 轨迹 | 軌跡 |
| 에피소드 | episode | 回合(episode) | エピソード |
| 데이터 파이프라인 | data pipeline | 数据管道 | データパイプライン |
| 파이프라인 | pipeline | 管道 | パイプライン |
| 데이터셋 | dataset | 数据集 | データセット |
| 디지털 트윈 | digital twin | 数字孪生 | デジタルツイン |
| 도메인 갭 | domain gap | 域间差异 | ドメインギャップ |
| 도메인 랜덤라이제이션 | domain randomization | 域随机化 | ドメインランダマイゼーション |
| 강화학습 | reinforcement learning | 强化学习 | 強化学習 |
| 모방학습 | imitation learning | 模仿学习 | 模倣学習 |
| 라벨링 | labeling | 标注 | ラベリング |
| 어노테이션 | annotation | 标注 | アノテーション |
| 체크포인트 | checkpoint | 检查点 | チェックポイント |
| 분산 학습 | distributed training | 分布式训练 | 分散学習 |
| 처리량 | throughput | 吞吐量 | スループット |
| 아키텍처 | architecture | 架构 | アーキテクチャ |
| 런타임 | runtime | 运行时 | ランタイム |
| 프로덕션 | production | 生产环境 | 本番環境 |
| 엣지 | edge | 边缘 | エッジ |
| 클라우드 | cloud | 云 | クラウド |
| 온디바이스 | on-device | 端侧 | オンデバイス |
| 엔드투엔드 | end-to-end | 端到端 | エンドツーエンド |
| 워크플로우 | workflow | 工作流 | ワークフロー |

## 3. 구조 보존 규칙 (기계적 — 위반 시 빌드나 자동화가 깨짐)

- **frontmatter**: 모든 번역 파일은 `---\nko_hash: <40자 hex>\n---`로 시작. 해시는
  `python3 scripts/check_translation_sync.py --hash docs/<원본>.md`로 계산.
- **앵커 링크**: heading을 번역하면 슬러그가 바뀐다 → 본문 내 `#...` 링크를 번역된
  heading에 맞춰 반드시 함께 갱신. 게이트는 `mkdocs build --strict`.
  strict가 통과 못 하면 빌드 산출물의 실제 `<h2 id>`를 읽어 링크를 맞춘다
  (이모지 포함 heading은 사전 계산 슬러그가 자주 틀린다 — 2026-07-11 실측).
- **유지**: 상태 배지(🟢 GA 등)·이모지·인용 마커 `[1]`·코드 블록·URL·표 구조·
  admonition 구문(`!!! warning "..."`)·`<details markdown="1">` 블록은 그대로.
- **페이지 메타데이터 라인**: `_최종 갱신: ... · owner: ... · volatility: ..._`은
  라벨만 번역(en: `_Last updated: ... · owner: ... · volatility: medium_` 식),
  값(연월·owner·수준)은 원본과 동일하게 유지. 단 원문의 volatility 값은 한국어
  (낮음/중간/높음)이므로 en/zh/ja에서는 등가 표현으로 옮긴다
  (en: low/medium/high, zh: 低/中/高, ja: 低/中/高). 연월·owner는 그대로.
- **페이지 간 링크**: `[← index로](index.md)` 같은 상대 링크는 파일명 그대로 둔다
  (플러그인이 언어별로 자동 해석). 링크 텍스트만 번역.

## 4. 문체

- **en**: 간결한 기술 문서체. 불필요한 관사·수동태 줄이기.
- **zh**: 간체(简体). 영문 용어는 원문 유지, 전각 괄호（）사용.
- **ja**: です・ます체. 카타카나 표기는 위 고정 역어 표를 따른다.
- 공통: 원문의 직설적·실무적 톤 유지 ("라이선스가 지뢰밭" 같은 표현은 순화하지 않고
  등가 표현으로 — en: "a licensing minefield").
