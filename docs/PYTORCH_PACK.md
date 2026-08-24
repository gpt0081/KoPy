# KoPy PyTorch Pack

KoPy 0.5.3의 PyTorch 팩은 실제 PyTorch를 다시 구현하지 않습니다. KoPy 표현을 표준 `torch` API로 번역하고 계산은 설치된 PyTorch가 담당합니다.

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

x = 토치.텐서([[1.0, 2.0]])
모델 = 토치.엔엔.리니어(2, 1)
옵티마이저 = 토치.옵팀.아담더블유(모델.파라미터스(), lr=0.001)

출력 = 모델(x)
손실 = 출력.썸()
옵티마이저.제로그라드()
손실.백워드()
옵티마이저.스텝()
```

표준 Python으로는 `torch.tensor`, `torch.nn.Linear`, `torch.optim.AdamW`, `parameters`, `sum`, `zero_grad`, `backward`, `step`로 번역됩니다.

## 지원 범위

핵심 텐서 생성과 dtype, shape 조작, 행렬 연산, reduction, 자동미분, `torch.nn` 계층과 손실함수, `torch.optim` 최적화기, `DataLoader`/`TensorDataset`, 저장과 로드의 자주 쓰는 API를 우선 등록합니다.

KoPy 팩은 namespace-scoped 방식이므로 `토치.텐서`, `토치.엔엔.리니어`처럼 PyTorch가 활성화된 문맥에서만 번역합니다. NumPy 등 다른 팩과 같은 Python API 이름을 공유하는 경우 동일한 목표 이름일 때만 안전하게 객체 메서드 번역이 가능합니다.

## 의도적으로 번역하지 않는 것

`lr=`, `requires_grad=`, `dtype=`, `device=` 같은 키워드 인자 이름은 아직 Python 원형을 유지합니다. 키워드 인자를 전역 단어 치환으로 처리하면 라이브러리 간 의미 충돌 위험이 있기 때문입니다.

CUDA, MPS, ROCm 같은 가속기 자체도 KoPy가 구현하지 않습니다. 사용 가능한 하드웨어와 PyTorch 빌드에 따라 원래 PyTorch가 처리합니다.
