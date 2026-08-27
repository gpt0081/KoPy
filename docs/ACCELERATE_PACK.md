# KoPy Accelerate Pack

KoPy의 Hugging Face Accelerate 팩은 실제 `accelerate` 라이브러리 위에 한글 음역 인터페이스를 제공합니다. 계산·분산 처리·장치 배치는 원래 Accelerate와 PyTorch가 수행하며 KoPy는 import와 등록된 API 이름만 변환합니다.

기준 안정판: Accelerate 1.14.x

## 음역 원칙

Python API에 `_`가 있으면 KoPy canonical 표기에서도 `_` 구조를 유지합니다. 숫자가 포함된 이름은 숫자를 그대로 둡니다. 이전 compact 표기는 기존 KoPy 소스 호환을 위해 입력 alias로 유지하지만, 새 학습 자료와 Python → KoPy 변환은 canonical 표기를 우선합니다.

대표 대응:

- `prepare_model → 프리페어_모델`
- `prepare_optimizer → 프리페어_옵티마이저`
- `prepare_data_loader → 프리페어_데이터_로더`
- `gather_for_metrics → 개더_포_메트릭스`
- `unwrap_model → 언랩_모델`
- `wait_for_everyone → 웨이트_포_에브리원`
- `save_state → 세이브_스테이트`
- `load_state → 로드_스테이트`
- `set_seed → 셋_시드`
- `infer_auto_device_map → 인퍼_오토_디바이스_맵`
- `load_checkpoint_and_dispatch → 로드_체크포인트_앤드_디스패치`

## 예시

```kopy
프롬 액셀러레이트 임포트 액셀러레이터
임포트 토치

가속기 = 액셀러레이터()
모델 = 토치.엔엔.리니어(3, 1)
옵티마이저 = 토치.옵팀.아담더블유(모델.파라미터스())
모델, 옵티마이저 = 가속기.프리페어(모델, 옵티마이저)
가속기.백워드(손실)
모델 = 가속기.언랩_모델(모델)
가속기.웨이트_포_에브리원()
```

`cpu=`, `mixed_precision=`, `gradient_accumulation_steps=` 같은 키워드 인자는 이번 감사에서 영구 영어 예외로 선언하지 않습니다. 전역 치환은 다른 라이브러리와 충돌할 수 있으므로, 이후 namespace/context-aware 키워드 감사에서 안전성을 확인한 뒤 음역 범위를 넓힙니다.

```bash
kopy packs accelerate
kopy help 액셀러레이트.액셀러레이터
```
