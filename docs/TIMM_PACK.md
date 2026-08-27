# timm Library Pack

KoPy의 `timm` (PyTorch Image Models) 팩은 모델 탐색, 이미지 모델 생성, 특징 추출, 데이터 변환, optimizer/scheduler 유틸리티를 namespace-scoped 방식으로 음역합니다. 실제 실행은 upstream `timm`과 PyTorch가 담당합니다.

## Compatibility

- KoPy baseline: Python 3.12.10
- Tested library line: `timm>=1.0.28,<1.1`
- Runtime tests do not download pretrained weights or external datasets.

```bash
python -m pip install "torch>=2.13,<2.14" "torchvision>=0.28,<0.29" "timm>=1.0.28,<1.1"
```

## 현재 음역 기준

KoPy의 기본 원칙에 맞춰 영어 API는 가능한 한 한글 음역으로 쓰고, 원 Python 식별자의 `_` 구조와 숫자를 보존합니다.

| KoPy | Python |
| --- | --- |
| `팀엠.크리에이트_모델` | `timm.create_model` |
| `팀엠.리스트_모델즈` | `timm.list_models` |
| `팀엠.리스트_프리트레인드` | `timm.list_pretrained` |
| `모델.포워드_피처스` | `model.forward_features` |
| `모델.포워드_헤드` | `model.forward_head` |
| `모델.리셋_클래시파이어` | `model.reset_classifier` |
| `팀엠.데이터.리졸브_데이터_컨피그` | `timm.data.resolve_data_config` |
| `팀엠.데이터.크리에이트_트랜스폼` | `timm.data.create_transform` |
| `팀엠.옵팀.크리에이트_옵티마이저_브이2` | `timm.optim.create_optimizer_v2` |
| `팀엠.스케줄러.크리에이트_스케줄러_브이2` | `timm.scheduler.create_scheduler_v2` |

`v2`의 `2`를 `투`로 바꾸지 않습니다. 같은 이유로 모델명 문자열인 `"resnet18"`의 `18`도 원 데이터 그대로 둡니다.

이전 `크리에이트모델`, `포워드피처스`, `크리에이트옵티마이저브이투` 표기는 기존 KoPy 소스 호환을 위해 입력 alias로 계속 허용하지만, Python → KoPy 변환과 새 학습 자료에서는 위 canonical 표기를 사용합니다.

## Basic model creation

```python
임포트 팀엠

모델 = 팀엠.크리에이트_모델(
    "resnet18",
    pretrained=펄스,
    num_classes=10,
)
```

Equivalent Python:

```python
import timm

model = timm.create_model(
    "resnet18",
    pretrained=False,
    num_classes=10,
)
```

## Feature extraction

```python
임포트 토치
임포트 팀엠

모델 = 팀엠.크리에이트_모델("resnet18", pretrained=펄스)
엑스 = 토치.랜드엔((1, 3, 224, 224))

위드 토치.노_그라드():
    피처스 = 모델.포워드_피처스(엑스)
```

`모델`, `엑스`, `피처스`처럼 이미 공통 음역이 확정된 학습 식별자는 KoPy 표기를 사용합니다. 문자열 데이터와 숫자는 음역하지 않습니다.

## 아직 감사가 필요한 키워드 인자

`pretrained=`, `num_classes=`, `in_chans=`, `features_only=`, `out_indices=`, `checkpoint_path=`, `drop_rate=`, `global_pool=`은 현재 동작 호환을 위해 아직 Python spelling을 허용합니다. 이것을 영구 영어 예외로 간주하지 않습니다. 다른 팩과의 충돌 및 함수 시그니처 문맥을 검토한 뒤 후속 음역 감사에서 처리합니다.

`timm` 멤버 음역은 `timm / 팀엠`을 import한 코드에서만 활성화됩니다. 따라서 `create_model`, `forward_features` 같은 일반 이름을 전역으로 오염시키지 않습니다.
