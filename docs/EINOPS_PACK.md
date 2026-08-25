# Einops Library Pack

KoPy 0.5.24의 `einops / 에이놉스` 팩은 딥러닝에서 자주 쓰는 텐서 차원 변환을 KoPy 음역 API로 연습할 수 있게 합니다. 실제 계산은 upstream einops가 NumPy, PyTorch, JAX 등 원래 텐서 backend에서 수행합니다.

기준 안정판은 **einops 0.8.2**입니다. KoPy 자체 Python 기준은 기존과 동일한 **Python 3.12.10**이며, einops 0.8.2는 Python 3.9 이상을 지원합니다.

## 지원 namespace

```kopy
임포트 에이놉스
프롬 에이놉스 임포트 리어레인지, 리듀스, 리피트
```

주요 매핑:

| KoPy | Python | 용도 |
| --- | --- | --- |
| `리어레인지` | `rearrange` | 축 재배열·reshape·stack/concat 계열 표현 |
| `리듀스` | `reduce` | mean/sum/max 등 축약 |
| `리피트` | `repeat` | 반복·broadcast 형태 표현 |
| `아인섬` | `einsum` | 이름 붙은 축 기반 tensor product |
| `팩` | `pack` | 여러 tensor를 `*` 축으로 묶기 |
| `언팩` | `unpack` | pack 결과 복원 |
| `파스셰이프` | `parse_shape` | 축 이름과 길이 해석 |
| `애즈넘파이` | `asnumpy` | 지원 tensor를 NumPy ndarray로 변환 |

## 학습 원칙

Einops의 핵심 학습 대상은 함수 이름보다도 **pattern 문자열 자체**입니다. 따라서 다음 표현은 번역하지 않습니다.

```text
"batch height width channels -> batch channels height width"
"b c h w -> b c"
"channels -> batch channels"
```

`batch=`, `height=`, `width=`, `channels=` 같은 axis-length keyword도 사용자가 pattern에서 직접 정한 축 이름이므로 Python/einops 원형을 유지합니다. KoPy 전용 한국어 표기법을 새로 만들지 않습니다.

이렇게 해야 KoPy로 익힌 tensor shape 사고가 실제 논문 구현과 PyTorch/JAX 코드를 읽을 때 그대로 이어집니다.

## 예제

```kopy
임포트 넘파이 애즈 np
프롬 에이놉스 임포트 리어레인지, 리듀스, 리피트

images = np.에이레인지(2 * 4 * 4 * 3).리셰이프(2, 4, 4, 3)
features = 리어레인지(
    images,
    "batch height width channels -> batch channels height width",
)
pooled = 리듀스(
    features,
    "batch channels height width -> batch channels",
    "mean",
)
batch = 리피트(pooled[0], "channels -> batch channels", batch=3)
```

대응하는 표준 Python:

```python
import numpy as np
from einops import rearrange, reduce, repeat

images = np.arange(2 * 4 * 4 * 3).reshape(2, 4, 4, 3)
features = rearrange(
    images,
    "batch height width channels -> batch channels height width",
)
pooled = reduce(
    features,
    "batch channels height width -> batch channels",
    "mean",
)
batch = repeat(pooled[0], "channels -> batch channels", batch=3)
```

## 실제 라이브러리 설치

```powershell
python -m pip install "einops>=0.8.2,<0.9"
```

개발판 `0.9.0.dev0` 대신 안정판 0.8.2 계열을 CI 기준으로 사용합니다.

## 테스트 범위

`tests/test_einops_runtime.py`는 실제 einops와 NumPy를 사용해 다음을 검증합니다.

- `rearrange`의 실제 축 순서 변경
- `reduce(..., "mean")` 결과
- `repeat` 실제 반복 결과
- `pack` / `unpack` 왕복
- `parse_shape` 축 이름/길이 해석

외부 모델, 데이터셋, GPU 또는 네트워크 다운로드는 필요하지 않습니다.
