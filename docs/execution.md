# 실행 경로 — 데이터·시뮬레이션·파인튜닝

_최종 갱신: 2026-09 · owner: Youngjin · volatility: 중간_

**L0 TL;DR**: [파일럿 카드](start.md#pilot)를 작성한 뒤 현재 병목에 맞는 경로 하나를 선택한다. 아래는 공개 샘플의 **고정 커밋을 읽어 정리한 실행 가이드**다. 2026-09-15에 원문·명령을 대조했으며, 이 플레이북 변경에서 AWS 리소스나 실기체를 새로 실행하지 않았다. 샘플 작성자의 실측과 플레이북 자체 재현을 구분한다.

## 공통 준비와 결과 기록 { #prepare }

담당자: AWS/IAM·데이터 담당, 로봇·ML 담당, 현장 시험 시 안전 책임자. GPU 할당량·리전·라이선스·데이터 처리 위치를 확인하고 최대 실행 시간과 비용 상한을 정한다. 예산 알림만으로 실행이 자동 중단되지는 않으므로 작업 중지 담당자와 종료 절차를 정한다.

```text
repo commit / container digest / dependency versions:
region / AZ / instance type / instance count:
dataset version / robot-camera configuration / train-eval split:
start-end time / setup-training-evaluation hours / actual cost:
success numerator-denominator / cycle time / interventions / latency:
failure evidence / cleanup result / operator / reviewer:
```

## A. 로봇 데이터 수집·품질 확인 { #data }

**대상**: SO-ARM101 리더/팔로워와 듀얼 카메라에서 실데모를 수집하는 팀. **다른 로봇이나 ROS bag 변환은 별도 어댑터 작업**이며 이 샘플이 자동 해결한다고 가정하지 않는다.

**준비물·버전**: [고정 샘플](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) `[1]`(MIT-0, 교육·데모용). 작성자는 Jetson AGX Thor·JetPack 7에서 검증했다고 명시한다. Greengrass V2가 HEALTHY인 장치, Docker/NVIDIA 런타임, 보정된 로봇·카메라, 동일 리전 S3 버킷·IoT thing group이 필요하다.

```bash
git clone https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass.git
cd sample-lerobot-data-collection-on-aws-iot-greengrass
git checkout 6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e
```

**실행 순서**: 고정 커밋의 `DEPLOYMENT_GUIDE.md` 0~0.2절에서 장치·권한·인증 설정을 준비 → CloudFormation 배포 → `collect.py` 업로드 → 같은 버전의 `recipe.yaml`로 컴포넌트 등록·배포 → 웹 콘솔에서 짧은 녹화 세션 → Save & Next → End Session → S3 결과와 에피소드 재생 확인. 구체 AWS 명령은 그 가이드의 환경별 placeholder를 치환해 실행한다.

**산출물·성공 기준**: 버전이 있는 데이터셋, 에피소드 목록, 카메라/행동 시간 정렬·누락 프레임·단위·성공/실패 라벨 검사 보고서. 합의한 데이터 계약을 만족하고 중단된 업로드를 복구할 수 있어야 한다. 녹화 성공이 학습 품질을 보증하지는 않는다.

**비용·중단**: 장치/운영자 시간 + S3 + 선택적 KVS 영상·전송 + 로그·웹 리소스. [예산 양식](start.md#roi)으로 견적한다. 시간 정렬·로봇 보정·권한·안전 조건 실패 시 추가 수집을 멈춘다.

**정리**: 녹화·영상 스트림을 종료하고 Greengrass 배포에서 해당 컴포넌트를 제거한다. 결과 보존 여부를 먼저 결정한 뒤 이 실험이 만든 CloudFormation 리소스·IoT 인증서/정책·KVS·로그·버킷 잔여물을 확인한다. 공유 리소스는 실험 자원과 구분한다.

## B. 시뮬레이션 학습·평가 { #simulation }

**대상**: ANYmal-C 보행 예제로 클라우드 학습·정책 export를 익히는 팀. 합성 이미지나 다른 로봇 태스크의 성능 검증은 별도 실험이다.

**준비물·버전**: [고정 샘플](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) `[1]`(MIT, 교육용). **Isaac Lab v2.1.0 + Isaac Sim 4.5.0**, 기본 리전 `us-east-1`, `g6e.4xlarge`. 필러의 최신 버전 표와 다르므로 임의 혼합하지 않는다. Terraform ≥1.5, AWS CLI, NGC 접근, GPU 할당량, SSH 키가 필요하다.

```bash
git clone https://github.com/aws-samples/sample-issac-lab-on-aws.git
cd sample-issac-lab-on-aws
git checkout 50ea76d87d873c1d69bed92c450ab144894f437e
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform validate
terraform plan
```

변수 파일에 리전·허용 SSH 주소·키·스토리지 등을 설정한 후 plan을 검토하고 `terraform apply`한다. 샘플은 NGC 키를 state/user data에 저장하므로 공유·장기 환경에서는 시크릿 관리 방식을 먼저 바꾼다. README의 **부트스트랩 → 코어 패키지 설치 → 컨테이너 실행** 순서를 따른다. 준비된 컨테이너 `/workspace/isaaclab` 안의 학습 명령:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py   --task Isaac-Velocity-Rough-Anymal-C-v0 --headless
```

**산출물·성공 기준**: 설정·학습 로그·체크포인트, 별도 평가 실행의 영상·정책 `.pt`/`.onnx`. 보상 곡선뿐 아니라 합의한 지형에서 보행 실패·추종 오차를 측정한다. export 성공은 실기 배포 통과가 아니다.

**비용·중단**: 작성자의 약 2시간/$12는 해당 워크숍 추정이며 서울 g6e.xlarge·ETH 논문의 4~20분 결과와 결합하지 않는다. 인스턴스 준비·학습·평가의 전체 시간, EBS·S3·공인 IPv4·로그를 별도 계산한다. 부트스트랩 실패, 메모리 부족, 상한 도달 시 중단한다.

**정리**: 결과를 별도 보존한 뒤 해당 Terraform 작업 디렉터리에서 `terraform plan -destroy`를 검토하고 `terraform destroy`한다. 보존된 S3 객체·스냅샷·로그·IP 등 잔여 비용을 확인한다. 실물 시험은 [운영 게이트](operations.md#release)를 따르는 별도 단계다.

## C. 파인튜닝과 제한된 엣지 평가 { #finetuning }

**대상**: 학습/평가 데이터가 분리돼 있고 로봇 관측·행동 정의를 가진 팀. 모델을 처음부터 만드는 경로가 아니다.

**준비물·검증 범위**: [고정 샘플](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac) `[1]`(MIT-0). 작성자는 **IL Pattern A(Batch)**의 완료 실행을 보고한다. Pattern B/C(SageMaker/HyperPod)는 배포 검증 미완료, RL은 GPU 실행 미완료이며, 강제 Spot 중단→복구도 실증되지 않았다. Node/npm·CDK, Python 환경(`boto3`, `sagemaker`), S3 데이터, 모델/기반 모델 접근 권한·라이선스, GPU 할당량이 필요하다.

```bash
git clone https://github.com/aws-samples/sample-vla-finetuning.git
cd sample-vla-finetuning
git checkout f21e4a9bf0ec11f40c2298a85951690b61efeaac
npm ci
npm run build
export PAI_AWS_REGION=us-west-2
npm run cdk -- synth PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

예제의 `us-west-2`는 실행 예시다. 데이터 처리 요건과 용량에 맞는 승인된 리전으로 바꾸고 CDK와 CLI에 같은 값을 사용한다.

샘플의 bootstrap·이미지 준비·계정 설정을 완료하고 생성될 자원을 검토한 뒤 Pattern A 스택을 배포한다.

```bash
npm run cdk -- deploy PaiTrainingPlatform-IL-PatternA -c region="$PAI_AWS_REGION"
```

이후 Python 환경을 활성화하고 다음 명령을 실행한다:

```bash
cd containers/vla-ft
python vla_ft_cli.py --help
python vla_ft_cli.py --quickstart --backend batch --region "$PAI_AWS_REGION" --dry-run
```

dry-run도 계정·용량 등의 조회를 할 수 있으며 학습 잡은 제출하지 않는다. **기본 quickstart는 Pattern B를 선택할 수 있어 여기서는 `--backend batch`로 범위를 제한**한다. 계획의 모델·배치·메모리·예상 비용을 확인하고, 번들 데이터 실험에 동의하면 같은 명령의 `--dry-run`을 `--yes`로 바꾼다. 고객 데이터는 `--quickstart` 대신 `--dataset s3://... --model ...`로 지정하고 `--help`의 옵션을 따른다.

**산출물·성공 기준**: 데이터·기반 체크포인트·학습 설정·새 체크포인트의 계보, 기준 모델과 동일 조건의 평가, 성공 분자/분모·반복/미학습 조건·작업 시간·사람 개입. 데모 개수로 성공률이나 완료일을 보장하지 않는다.

**엣지 인계**: 훈련 샘플만으로 실기 배포가 완료되지 않는다. 모델별 export/서빙 경로, 관측 순서·정규화·행동 단위, 장치 호환성, 관측→동작 지연을 검증한다. [P4의 배포 자산](pillar-4.md)과 [운영 게이트](operations.md#release)를 연결해 감독하에 제한적으로 시험한다.

**비용·중단·정리**: 추정치와 실제 청구를 따로 기록한다. 메모리 초과·평가 정체·비용/기간 상한이면 잡을 중단한다. 체크포인트를 보존한 뒤 해당 Batch 잡·컴퓨트 환경의 활성 상태를 확인하고, 실험 전용 CDK 스택을 제거한다. GPU가 0이어도 EFS·S3·NAT·로그 등은 비용이 남을 수 있다. 공유 스택은 소유자와 확인한다.

**➡️ 다음 액션**: 선택한 경로의 준비·실행·평가·정리 기록을 남기고 [파일럿 카드](start.md#pilot)의 다음 단계 승인 여부를 결정한다. 실행 후의 재현 증거는 [근거 기록](evidence.md)에 추가한다.

_owner: Youngjin · updated: 2026-09 · volatility: 중간_
