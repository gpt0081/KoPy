# TorchVision Library Pack

KoPy의 TorchVision 팩은 표준 `torchvision` 라이브러리를 다시 구현하지 않습니다. `토치비전` 또는 `torchvision` namespace 안의 KoPy 음역 API를 실제 TorchVision Python API로 변환합니다.

개발/CI 기준은 Python 3.12.10, PyTorch 2.13.x, TorchVision 0.28.x입니다.

## 기본 사용

```kopy
임포트 토치
임포트 토치비전 애즈 tv

image = 토치.원즈((3, 32, 32), 디타입=토치.플로트32)

transform = tv.트랜스폼즈.컴포즈([
    tv.트랜스폼즈.리사이즈((16, 16)),
    tv.트랜스폼즈.노멀라이즈(
        mean=[0.5, 0.5, 0.5],
        std=[0.5, 0.5, 0.5],
    ),
])

피처스 = transform(image)
모델 = tv.모델즈.레스넷18(weights=논)
```

위 코드는 핵심적으로 다음 Python 표현으로 돌아갑니다.

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

`피처스 → features`, `모델 → model`, `디타입 → dtype`처럼 이미 공통 음역 표준에 들어온 표현은 KoPy에서도 음역형을 사용합니다. `image`, `transform`, `weights`, `mean`, `std`처럼 아직 남아 있는 영어는 영구 예외가 아니라 후속 공통 식별자/키워드 감사 대상입니다.

## 숫자와 언더스코어 표준

숫자는 한글 단어로 풀어쓰지 않고 원래 숫자를 그대로 유지하며, Python 식별자의 `_` 구조도 가능한 한 보존합니다.

- `mobilenet_v3_large` → `모빌넷_브이3_라지`
- `efficientnet_b0` → `이피션트넷_비0`
- `vit_b_16` → `브이아이티_비_16`
- `ResNet18_Weights` → `레스넷18_웨이츠`
- `make_grid` → `메이크_그리드`
- `save_image` → `세이브_이미지`
- `box_iou` → `박스_아이오유`
- `clip_boxes_to_image` → `클립_박시즈_투_이미지`
- `remove_small_boxes` → `리무브_스몰_박시즈`

기존 `모빌넷브이스리라지`, `이피션트넷비제로`, `메이크그리드`, `박스아이오유` 같은 표기도 호환 alias로 계속 입력할 수 있지만 Python → KoPy에서는 새 표준형을 출력합니다.

## 지원 범위

- namespace: `transforms`, `models`, `datasets`, `ops`, `utils`, `io`
- transforms: `Compose`, `Resize`, `CenterCrop`, `RandomCrop`, `RandomResizedCrop`, `RandomHorizontalFlip`, `RandomVerticalFlip`, `RandomRotation`, `ColorJitter`, `ToTensor`, `Normalize`
- models: `resnet18`, `resnet50`, `mobilenet_v3_large`, `efficientnet_b0`, `vit_b_16`, `swin_t`
- datasets: `ImageFolder`, `CIFAR10`, `CIFAR100`, `MNIST`, `FashionMNIST`
- utilities/ops: `make_grid`, `save_image`, `box_iou`, `nms`, `clip_boxes_to_image`, `remove_small_boxes`

## 충돌 방지와 남은 감사 항목

TorchVision 고유 멤버는 Core 전역 단어표에 추가하지 않고 namespace-scoped로 처리합니다. 따라서 TorchVision을 import하지 않은 파일에서 `컴포즈`, `리사이즈` 같은 이름을 임의로 바꾸지 않습니다.

`mean=`, `std=`, `inplace=`, `weights=`, `progress=`, `num_classes=`, `download=`, `root=`, `train=` 같은 키워드는 과거에는 충돌 위험 때문에 영어 원형을 영구 유지한다고 문서화했지만, 현재 KoPy 원칙에서는 **후속 감사 대상**입니다. 안전한 공통 음역 또는 문맥 기반 처리가 검증되는 순서대로 한국어 음역을 추가합니다. 특히 `mean`은 `min`과 음역 충돌이 있어 별도의 문맥 처리가 필요합니다.

## 설치

```powershell
python -m pip install "torch>=2.13,<2.14" "torchvision>=0.28,<0.29"
```

## 테스트

CI는 Windows, Ubuntu, macOS에서 실제 TorchVision을 설치해 `Compose + Resize + Normalize`, `resnet18(weights=None)`, `box_iou` 실제 연산을 검증합니다. 외부 이미지나 모델 weight 다운로드는 필요하지 않습니다.
