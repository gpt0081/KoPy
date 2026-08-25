# timm Library Pack

KoPy 0.5.22 adds a namespace-scoped pack for `timm` (PyTorch Image Models).
The pack is intended for model discovery, image-model construction, feature
extraction, and common training utilities while leaving execution to upstream
`timm` and PyTorch.

## Compatibility

- KoPy baseline: Python 3.12.10
- Tested library line: `timm>=1.0.28,<1.1`
- `timm` 1.0.28 supports Python 3.12 and uses the Apache-2.0 license.
- Runtime tests do not download pretrained weights or external datasets.

Install the optional library separately:

```bash
python -m pip install "torch>=2.13,<2.14" "torchvision>=0.28,<0.29" "timm>=1.0.28,<1.1"
```

## Basic model creation

KoPy:

```python
임포트 팀엠

model = 팀엠.크리에이트모델(
    "resnet18",
    pretrained=False,
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

model = 팀엠.크리에이트모델("resnet18", pretrained=False)
x = 토치.랜드엔((1, 3, 224, 224))

위드 토치.노그라드():
    features = model.포워드피처스(x)
```

`model`, `x`, `features` are deliberately left as conventional Python/ML
variable names. KoPy is a bridge toward reading normal Python code, so learning
material should expose common upstream conventions instead of translating every
identifier.

## Representative mappings

| KoPy | Python |
| --- | --- |
| `팀엠.크리에이트모델` | `timm.create_model` |
| `팀엠.리스트모델즈` | `timm.list_models` |
| `팀엠.리스트프리트레인드` | `timm.list_pretrained` |
| `model.포워드피처스` | `model.forward_features` |
| `model.포워드헤드` | `model.forward_head` |
| `model.리셋클래시파이어` | `model.reset_classifier` |
| `팀엠.데이터.리졸브데이터컨피그` | `timm.data.resolve_data_config` |
| `팀엠.데이터.크리에이트트랜스폼` | `timm.data.create_transform` |
| `팀엠.옵팀.크리에이트옵티마이저브이투` | `timm.optim.create_optimizer_v2` |

## Keyword-argument policy

Common arguments such as `pretrained=`, `num_classes=`, `in_chans=`,
`features_only=`, `out_indices=`, `checkpoint_path=`, `drop_rate=`, and
`global_pool=` remain in standard Python spelling. They are not promoted into
KoPy's global translation table because several libraries use the same names
with different semantics.

`timm` members become translatable only after the `timm / 팀엠` module is
imported. Bare names such as `크리에이트모델` are therefore not globally
rewritten.
