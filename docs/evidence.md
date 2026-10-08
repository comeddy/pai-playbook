# 근거 기록 — 주장별 확인일·범위·검토 상태

_최종 갱신: 2026-09 · owner: Youngjin · volatility: 중간_

**L0 TL;DR**: 페이지 수정일은 모든 주장의 재검증일이 아니다. 아래는 이번 검토에서 수정한 핵심 주장 7개의 기록이다. 나머지 기존 주장은 아직 이 레지스트리로 이관되지 않았으며 전수 검증을 뜻하지 않는다.

`source-checked`는 명시한 1차 출처와 대조한 상태, `withdrawn`은 기존 일반화·약속을 철회한 상태, `reproduction-pending`은 실실행 재현 대기다. 모두 **사람 검토 대기**이며 AWS의 공식 승인·보증을 뜻하지 않는다. 원문 확인과 실험 재현, 현장 배포 승인은 별도 단계다.

원본 데이터는 [claims.json](assets/claims.json)이다. 표시는 이 파일에서 생성하며 CI는 필수 필드·4개 언어·영향 페이지·날짜·표시 동기화를 검사한다. 기한 초과는 경고로 보고한다. CI는 외부 원문의 진실성이나 현장 적합성을 판정하지 않는다.

<!-- evidence:start -->

### openvla-license { #openvla-license }

OpenVLA는 코드(MIT)와 Llama-2 파생 사전학습 가중치(Llama Community License)를 구분한다. 상용 판단은 선택한 가중치·기반 모델·데이터 조건까지 확인한다. 코드 LICENSE만으로 상용 가능을 판정하지 않는다.

- 확인일: 2026-09-15 · 상태: `source-checked` · 검토 주기(일): 30
- 대조 담당: Codex (source comparison) · 사람 검토: 대기
- 영향 페이지: [pillar-2](pillar-2.md) · [decisions](decisions.md) · [exec](exec.md)
- 출처: [OpenVLA README](https://github.com/openvla/openvla#pretrained-vlas)

### agentcore-residency { #agentcore-residency }

AgentCore의 제공 리전·저장 리전·추론 처리 리전은 별개다. Memory는 APAC 내 여러 리전에서 추론할 수 있고 서울발 Evaluations는 글로벌 교차 리전 추론 대상이다. 국내 처리 요건은 사용하는 기능·모델·경로별로 검토한다.

- 확인일: 2026-09-15 · 상태: `source-checked` · 검토 주기(일): 30
- 대조 담당: Codex (source comparison) · 사람 검토: 대기
- 영향 페이지: [pillar-5](pillar-5.md) · [decisions](decisions.md) · [exec](exec.md) · [operations](operations.md)
- 출처: [AWS cross-region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html) · [AWS Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-cross-region-inference.html)

### fleetwise-new-customers { #fleetwise-new-customers }

IoT FleetWise는 신규 고객을 받지 않는다. 기존 고객은 계속 사용할 수 있으므로 종료 서비스라고 단정하지 않는다. 신규 로봇 플릿 아키텍처의 기본 옵션으로 제안하지 않는다.

- 확인일: 2026-09-15 · 상태: `source-checked` · 검토 주기(일): 30
- 대조 담당: Codex (source comparison) · 사람 검토: 대기
- 영향 페이지: [pillar-5](pillar-5.md) · [radar](radar.md)
- 출처: [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)

### action-chunking { #action-chunking }

동작 출력 수와 새 관측에 반응하는 빈도는 다르다. chunk 길이에 추론 Hz를 곱해 피드백 제어 주파수로 쓰지 않는다. PI는 chunk 사이 전환·지연 처리를 별도 문제로 설명한다. Helix의 S1/S2는 모두 온보드이며 클라우드 배치의 증거가 아니다.

- 확인일: 2026-09-15 · 상태: `source-checked` · 검토 주기(일): 90
- 대조 담당: Codex (source comparison) · 사람 검토: 대기
- 영향 페이지: [pillar-2](pillar-2.md) · [pillar-4](pillar-4.md) · [pillar-5](pillar-5.md) · [decisions](decisions.md) · [operations](operations.md)
- 출처: [PI real-time chunking](https://www.physicalintelligence.company/research/real_time_chunking) · [Figure Helix](https://www.figure.ai/news/helix)

### simulation-cost { #simulation-cost }

기존 ‘서울 g6e.xlarge + 4~20분 = 학습 한 판 $11~12’ 일반화를 철회한다. $0.98/시간과 4~20분의 산술 결과는 약 $0.07~0.33일 뿐, 해당 인스턴스 실측이 아니다. 샘플의 약 2시간/$12는 다른 설정의 작성자 추정으로 별도 취급한다.

- 확인일: 2026-09-15 · 상태: `withdrawn` · 검토 주기(일): 30
- 대조 담당: Codex (source comparison) · 사람 검토: 대기
- 영향 페이지: [pillar-3](pillar-3.md) · [execution](execution.md) · [exec](exec.md)
- 출처: [Pinned simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [ETH parallel RL paper](https://arxiv.org/abs/2109.11978)

### finetuning-outcomes { #finetuning-outcomes }

‘100~500 데모 → 80%+ 성공’, ‘100 데모면 1일 PoC 성과’라는 공통 약속을 철회한다. 데이터·태스크·모델·학습 설정·평가 조건을 고정한 실험 없이 성공률·완료 기간을 제시하지 않는다.

- 확인일: 2026-09-15 · 상태: `withdrawn` · 검토 주기(일): 90
- 대조 담당: Codex (source comparison) · 사람 검토: 대기
- 영향 페이지: [pillar-2](pillar-2.md) · [exec-guide](exec-guide.md) · [decisions](decisions.md) · [execution](execution.md)
- 출처: [OpenVLA fine-tuning](https://github.com/openvla/openvla#fine-tuning-openvla-via-lora)

### execution-samples { #execution-samples }

3개 샘플의 커밋·README·명령을 대조했다. 이번 개정에서 AWS·실기 실행은 하지 않았다. 파인튜닝 샘플은 작성자의 Pattern A 실실행 보고만 있으며 B/C·RL과 강제 중단 복구를 동등하게 검증됐다고 쓰지 않는다.

- 확인일: 2026-09-15 · 상태: `reproduction-pending` · 검토 주기(일): 30
- 대조 담당: Codex (source comparison) · 사람 검토: 대기
- 영향 페이지: [execution](execution.md) · [pillar-1](pillar-1.md) · [pillar-2](pillar-2.md) · [pillar-3](pillar-3.md)
- 출처: [Data sample](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) · [Simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [Training sample](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac)

<!-- evidence:end -->

## 갱신·분담 절차 { #review }

소유자 Youngjin은 검토 작업을 배정한다. 라이선스, AWS 서비스·리전, 로봇 제어·안전, 재현 실험 분야별 사람 검토자는 **배정 대기**이며 이름을 임의로 채우지 않는다. 원문 대조자를 기록하고 사람이 확인한 경우에만 `human_review: complete`와 실명 검토자를 함께 남긴다.

주장이 바뀌면 `pages`에 적힌 원본·요약·번역을 함께 수정하고, 확인일과 근거를 갱신한다. `python3 scripts/check_evidence.py --render` → 번역 해시 갱신 → 전체 검사 순서로 반영한다. 링크 200 응답, 빌드 통과, 번역 해시는 사실 검증의 대체물이 아니다.

_owner: Youngjin · updated: 2026-09 · volatility: 중간_
