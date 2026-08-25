# TorchVision Library Pack

KoPy의 TorchVision 팩은 표준 `torchvision` 라이브러리를 다시 구현하지 않습니다. `토치비전` 또는 `torchvision` namespace 안의 KoPy 음역 API를 실제 TorchVision Python API로 변환합니다.

개발/CI 기준은 Python 3.12.10, PyTorch 2.13.x, TorchVision 0.28.x입니다.

## 기본 사용

```kopy
임포트 토치
임포트 토치비전 애즈 tv

image = 토치.원즈((3, 32, 32), dtype=토치.플로트32)

transform = tv.트랜스폼즈.컴포즈([
    tv.트랜스폼즈.리사이즈((16, 16)),
    tv.트랜스폼즈.노멀라이즈(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5],
    ),
])

features = transform(image)
model = tv.모델즈.레스넷18(weights=None)
```

위 코드는 핵심적으로 다음 Python 표현을 익히도록 설계돼 있습니다.

```python
import torch
import torchvision as tv

image = torch.ones((3, 32, 32), dtype=torch.float32)
transform = tv.transforms.Compose([
    tv.transforms.Resize((16, 16)),
    tv.transforms.Normalize(mean=[0.5] * 3, std=[0.5] * 3),
])
features = transform(image)
model = tv.models.resnet18(weights=None)
```

`tv`, `image`, `features`, `model`, `weights=` 같은 실제 Python/TorchVision 관례는 학습 가치 때문에 원문 형태를 유지합니다.

## 지원 범위

- namespace: `transforms`, `models`, `datasets`, `ops`, `utils`, `io`
- transforms: `Compose`, `Resize`, `CenterCrop`, `RandomCrop`, `RandomResizedCrop`, `RandomHorizontalFlip`, `RandomVerticalFlip`, `RandomRotation`, `ColorJitter`, `ToTensor`, `Normalize`
- models: `resnet18`, `resnet50`, `mobilenet_v3_large`, `efficientnet_b0`, `vit_b_16`, `swin_t`
- datasets: `ImageFolder`, `CIFAR10`, `CIFAR100`, `MNIST`, `FashionMNIST`
- utilities/ops: `make_grid`, `save_image`, `box_iou`, `nms`, `clip_boxes_to_image`, `remove_small_boxes`

## 충돌 방지

TorchVision 멤버 이름은 Core 전역 단어표에 추가하지 않습니다. 다음 코드는 TorchVision을 import하지 않았기 때문에 KoPy가 임의로 번역하지 않습니다.

```kopy
transform = 컴포즈([리사이즈((224, 224))])
```

`mean=`, `std=`, `inplace=`, `weights=`, `progress=`, `num_classes=`, `download=`, `root=`, `train=` 같은 키워드 인자도 Python 원형을 유지합니다. 이 이름들은 다른 라이브러리나 사용자 코드에서도 흔해서 전역 음역 대상으로 삼기 부적절합니다.

## 설치

```powershell
python -m pip install "torch>=2.13,<2.14" "torchvision>=0.28,<0.29"
```

TorchVision 0.28.0은 Python 3.12용 Windows, Linux, macOS wheel을 제공합니다.

## 테스트

CI는 Windows, Ubuntu, macOS에서 실제 TorchVision 0.28.x를 설치해 다음을 실행합니다.

- `transforms.Compose + Resize + Normalize`
- `models.resnet18(weights=None)` 생성
- `ops.box_iou` 실제 연산 및 수치 결과 확인

외부 이미지, 모델 weight, 인터넷 데이터셋 다운로드 없이 실제 라이브러리 런타임을 검증합니다.
