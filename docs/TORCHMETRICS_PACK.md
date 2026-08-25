# TorchMetrics Library Pack

KoPy의 TorchMetrics 팩은 PyTorch 모델 평가에서 자주 사용하는 metric 클래스 이름을 한국어 음역으로 제공하면서 실제 TorchMetrics API와 학습 관례를 유지합니다.

기준 버전은 TorchMetrics 1.9.x이며 KoPy의 Python 3.12.10 범위에서 실제 라이브러리로 테스트합니다.

## 기본 사용

```kopy
임포트 토치
임포트 토치메트릭스 애즈 tm

preds = 토치.텐서([0, 1, 1, 0])
target = 토치.텐서([0, 1, 0, 0])

accuracy = tm.애큐러시(task="binary")
f1 = tm.에프원스코어(task="binary")

프린트(accuracy(preds, target))
프린트(f1(preds, target))
```

대응하는 Python은 다음과 같습니다.

```python
import torch
import torchmetrics as tm

preds = torch.tensor([0, 1, 1, 0])
target = torch.tensor([0, 1, 0, 0])

accuracy = tm.Accuracy(task="binary")
f1 = tm.F1Score(task="binary")

print(accuracy(preds, target))
print(f1(preds, target))
```

## 지원 범위

대표적으로 다음 이름을 지원합니다.

- `Metric` → `메트릭`
- `MetricCollection` → `메트릭컬렉션`
- `Accuracy` → `애큐러시`
- `Precision` → `프리시전`
- `Recall` → `리콜`
- `F1Score` → `에프원스코어`
- `AUROC` → `에이유알오씨`
- `AveragePrecision` → `애버리지프리시전`
- `ConfusionMatrix` → `컨퓨전매트릭스`
- `MeanMetric` → `미인메트릭`
- `SumMetric` → `썸메트릭`

## 일부 이름을 번역하지 않는 이유

`update()`, `compute()`, `reset()`, `clone()`, `plot()` 같은 lifecycle 메서드는 TorchMetrics에서 중요하지만 다른 Python 객체와 라이브러리에서도 널리 쓰이는 일반 이름입니다. KoPy는 이런 이름을 전역 음역하지 않고 원문 Python API로 남깁니다.

```kopy
임포트 토치메트릭스 애즈 tm

metric = tm.애큐러시(task="binary")
metric.update(preds, target)
score = metric.compute()
metric.reset()
```

`task=`, `num_classes=`, `average=`, `threshold=` 같은 키워드 인자와 `preds`, `target`, `metric`, `accuracy`, `f1` 같은 변수명도 원문 Python/TorchMetrics 학습 연결성을 위해 그대로 두는 것을 권장합니다.
