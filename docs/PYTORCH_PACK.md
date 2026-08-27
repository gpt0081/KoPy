# KoPy PyTorch Pack

KoPy의 PyTorch 팩은 실제 PyTorch를 다시 구현하지 않습니다. KoPy 표현을 표준 `torch` API로 번역하고 계산은 설치된 PyTorch가 담당합니다.

대상 기준: PyTorch 2.13.x, Python 3.12.10.

## 설치

```powershell
python -m pip install -e .
python -m pip install "torch>=2.13,<2.14"
```

등록 여부와 설치 상태 확인:

```powershell
kopy packs
kopy packs pytorch
```

## 기본 예제

```kopy
임포트 토치

엑스 = 토치.텐서([[1.0, 2.0]])
모델 = 토치.엔엔.리니어(2, 1)
옵티마이저 = 토치.옵팀.아담더블유(모델.파라미터스(), lr=0.001)

output = 모델(엑스)
loss = output.썸()
옵티마이저.제로_그라드()
loss.백워드()
옵티마이저.스텝()
```

표준 Python으로는 `torch.tensor`, `torch.nn.Linear`, `torch.optim.AdamW`, `parameters`, `sum`, `zero_grad`, `backward`, `step`로 번역됩니다. `엑스`와 `모델`은 공통 학습 식별자라 각각 `X`, `model`로 돌아갑니다.

## 음역 표준

현재 canonical Python → KoPy 표기는 숫자와 언더스코어를 보존합니다.

- `Conv1d` → `컨브1디`
- `Conv2d` → `컨브2디`
- `BatchNorm1d` → `배치노름1디`
- `zero_grad` → `제로_그라드`
- `no_grad` → `노_그라드`
- `inference_mode` → `인퍼런스_모드`
- `state_dict` → `스테이트_딕트`
- `load_state_dict` → `로드_스테이트_딕트`
- `manual_seed` → `매뉴얼_시드`

과거의 `컨브투디`, `제로그라드`, `노그라드`, `스테이트딕트` 같은 표기도 기존 KoPy 코드를 깨지 않도록 입력 alias로 계속 허용하지만 Python → KoPy 역변환에서는 위 표준형을 우선합니다.

## 지원 범위

핵심 텐서 생성과 dtype, shape 조작, 행렬 연산, reduction, 자동미분, `torch.nn` 계층과 손실함수, `torch.optim` 최적화기, `DataLoader`/`TensorDataset`, 저장과 로드의 자주 쓰는 API를 우선 등록합니다.

KoPy 팩은 namespace-scoped 방식이므로 `토치.텐서`, `토치.엔엔.리니어`처럼 PyTorch가 활성화된 문맥에서만 라이브러리 멤버를 번역합니다. NumPy 등 다른 팩과 같은 Python API 이름을 공유하는 경우 동일한 목표 이름일 때만 안전하게 객체 메서드 번역이 가능합니다.

## 아직 감사가 필요한 표현

`lr=`, `requires_grad=` 같은 PyTorch 키워드와 `optimizer`, `loss`, `output` 같은 학습 관례는 현재 공통 식별자 감사의 다음 대상입니다. 예전 문서처럼 이 영어 표기를 영구 예외라고 간주하지 않습니다.

`mean`은 별도 문제입니다. 영어 발음에 가까운 `민`은 이미 Python `min`의 KoPy 핵심 표기와 충돌합니다. 현재 `mean`의 기존 `미인` 표기는 호환성을 위해 유지하며, 문맥 기반으로 `mean`과 `min`을 안전하게 구분할 수 있기 전까지 무리하게 전역 변경하지 않습니다.

숫자 리터럴과 문자열 데이터는 음역하지 않습니다. CUDA, MPS, ROCm 같은 가속기 실행도 사용 가능한 하드웨어와 PyTorch 빌드에 따라 원래 PyTorch가 처리합니다.
