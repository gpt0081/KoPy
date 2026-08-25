# Kornia Library Pack

KoPy 0.5.23의 `kornia / 코르니아` Library Pack은 PyTorch 텐서 위에서 동작하는 Kornia의 미분가능 컴퓨터비전 API를 KoPy 음역으로 학습할 수 있게 합니다. 계산은 KoPy가 다시 구현하지 않고 실제 Kornia와 PyTorch가 수행합니다.

## 기준 버전

- Python: 3.12.10
- Kornia: 0.8.3 안정판 계열
- PyTorch: KoPy AI Pack Matrix의 2.13 계열

Kornia 0.8.3은 Python 3.11 이상을 요구하므로 KoPy의 Python 3.12.10 기준과 호환됩니다.

## 설치

```bash
python -m pip install -e . "torch>=2.13,<2.14" "kornia>=0.8.3,<0.9"
```

## 예제

```kopy
임포트 토치
임포트 코르니아 애즈 K

image = 토치.랜드((1, 3, 64, 64))
gray = K.컬러.알지비투그레이스케일(image)
blurred = K.필터즈.가우시안블러투디(gray, (5, 5), (1.5, 1.5))

augment = K.어그멘테이션.어그멘테이션시퀀셜(
    K.어그멘테이션.랜덤호리즌털플립(p=0.5),
    K.어그멘테이션.랜덤로테이션(degrees=10.0, p=0.5),
)
augmented = augment(blurred)
```

대응하는 Python 원문은 다음과 같습니다.

```python
import torch
import kornia as K

image = torch.rand((1, 3, 64, 64))
gray = K.color.rgb_to_grayscale(image)
blurred = K.filters.gaussian_blur2d(gray, (5, 5), (1.5, 1.5))

augment = K.augmentation.AugmentationSequential(
    K.augmentation.RandomHorizontalFlip(p=0.5),
    K.augmentation.RandomRotation(degrees=10.0, p=0.5),
)
augmented = augment(blurred)
```

## 주요 지원 범위

- `color`: RGB/grayscale/HSV 변환
- `filters`: Gaussian blur, Sobel, Canny, Laplacian, median blur
- `geometry.transform`: resize, rotate, affine/perspective warp
- `augmentation`: `AugmentationSequential`, flip, rotation, affine, crop, color jitter, normalize
- `morphology`: dilation, erosion, opening, closing
- `metrics`: PSNR, SSIM

## 교육 원칙

`image`, `gray`, `blurred`, `augment`, `augmented` 같은 변수명과 `degrees=`, `p=`, `same_on_batch=`, `keepdim=` 같은 키워드 인자는 Python/Kornia 원문에서 자주 접하는 형태라 그대로 유지합니다. KoPy 팩은 라이브러리 namespace가 import된 경우에만 멤버를 번역하며, `resize`, `transform`, `metrics` 같은 흔한 단어를 Core 전역 번역으로 추가하지 않습니다.

## 실제 런타임 검증

CI는 Windows, Ubuntu, macOS에서 실제 Kornia를 설치하고 다음 흐름을 실행합니다.

1. PyTorch 텐서 생성
2. `rgb_to_grayscale`
3. `gaussian_blur2d`
4. `geometry.transform.resize`
5. `AugmentationSequential(RandomHorizontalFlip(p=1.0))`
6. 출력 shape와 실제 좌우 반전 결과 검증

외부 이미지나 모델 다운로드는 필요하지 않습니다.
