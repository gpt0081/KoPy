# Kornia Library Pack

KoPy의 `kornia / 코르니아` Library Pack은 PyTorch 텐서 위에서 동작하는 Kornia의 미분가능 컴퓨터비전 API를 한글 음역으로 학습할 수 있게 합니다. 계산은 KoPy가 다시 구현하지 않고 실제 Kornia와 PyTorch가 수행합니다.

## 기준 버전

- Python: 3.12.10
- Kornia: 0.8.3 안정판 계열
- PyTorch: KoPy AI Pack Matrix의 2.13 계열

Kornia 0.8.3은 Python 3.11 이상을 요구하므로 KoPy의 Python 3.12.10 기준과 호환됩니다.

## 설치

```bash
python -m pip install -e . "torch>=2.13,<2.14" "kornia>=0.8.3,<0.9"
```

## canonical 음역

Python 식별자의 `_` 구조와 숫자는 그대로 보존합니다.

- `rgb_to_grayscale` → `알지비_투_그레이스케일`
- `grayscale_to_rgb` → `그레이스케일_투_알지비`
- `rgb_to_hsv` → `알지비_투_에이치에스브이`
- `gaussian_blur2d` → `가우시안_블러2디`
- `median_blur` → `미디안_블러`
- `warp_affine` → `워프_어파인`
- `warp_perspective` → `워프_퍼스펙티브`

예전 `알지비투그레이스케일`, `가우시안블러2디`, `워프어파인` 같은 표기는 기존 KoPy 소스 호환을 위해 입력 alias로 계속 허용하지만, Python → KoPy 변환과 새 학습 자료에서는 위 canonical 표기를 사용합니다.

## 예제

```kopy
임포트 토치
임포트 코르니아 애즈 K

엑스 = 토치.랜드((1, 3, 64, 64))
피처스 = K.컬러.알지비_투_그레이스케일(엑스)
리절트 = K.필터즈.가우시안_블러2디(피처스, (5, 5), (1.5, 1.5))

파이프라인 = K.어그멘테이션.어그멘테이션시퀀셜(
    K.어그멘테이션.랜덤호리즌털플립(p=0.5),
    K.어그멘테이션.랜덤로테이션(degrees=10.0, p=0.5),
)
리절트 = 파이프라인(리절트)
```

대응하는 Python 원문은 다음과 같습니다.

```python
import torch
import kornia as K

X = torch.rand((1, 3, 64, 64))
features = K.color.rgb_to_grayscale(X)
result = K.filters.gaussian_blur2d(features, (5, 5), (1.5, 1.5))

pipeline = K.augmentation.AugmentationSequential(
    K.augmentation.RandomHorizontalFlip(p=0.5),
    K.augmentation.RandomRotation(degrees=10.0, p=0.5),
)
result = pipeline(result)
```

## 주요 지원 범위

- `color`: RGB/grayscale/HSV 변환
- `filters`: Gaussian blur, Sobel, Canny, Laplacian, median blur
- `geometry.transform`: resize, rotate, affine/perspective warp
- `augmentation`: `AugmentationSequential`, flip, rotation, affine, crop, color jitter, normalize
- `morphology`: dilation, erosion, opening, closing
- `metrics`: PSNR, SSIM

## 교육 원칙

KoPy의 기본은 영어 식별자를 한글로 음역하는 것입니다. `_` 구조와 숫자는 유지하며, 문자열·데이터 값은 번역하지 않습니다. Kornia처럼 다른 라이브러리와 이름이 겹칠 수 있는 API는 import된 Library Pack의 namespace 안에서만 음역합니다.

`degrees=`, `p=`, `same_on_batch=`, `keepdim=` 등 아직 영어로 남은 키워드 인자는 영구 예외가 아니라 후속 context-aware 음역 감사 대상입니다. 충돌 여부를 확인하지 않고 Core 전역 번역으로 추가하지 않습니다.

## 실제 런타임 검증

CI는 Windows, Ubuntu, macOS에서 실제 Kornia를 설치하고 다음 흐름을 실행합니다.

1. PyTorch 텐서 생성
2. `rgb_to_grayscale`
3. `gaussian_blur2d`
4. `geometry.transform.resize`
5. `AugmentationSequential(RandomHorizontalFlip(p=1.0))`
6. 출력 shape와 실제 좌우 반전 결과 검증

외부 이미지나 모델 다운로드는 필요하지 않습니다.
