# Lightning Library Pack

KoPy 0.5.26의 `lightning / 라이트닝` 팩은 PyTorch Lightning의 모델·Trainer 중심 학습 흐름을 한글 음역 API로 익히면서 실제 Python/Lightning 관례를 함께 보존합니다.

기준 런타임은 Python 3.12.10과 Lightning 2.6.x입니다. 실제 학습은 KoPy가 아니라 upstream Lightning/PyTorch가 수행합니다.

## 설치

```powershell
python -m pip install "lightning>=2.6.5,<2.7"
```

## 기본 예시

```kopy
임포트 라이트닝 애즈 L
임포트 토치

class Model(L.라이트닝모듈):
    def __init__(self):
        super().__init__()
        self.layer = 토치.엔엔.리니어(4, 1)

    def forward(self, x):
        return self.layer(x)

    def 트레이닝스텝(self, batch, batch_idx):
        X_train, y_train = batch
        predictions = self(X_train)
        loss = 토치.엔엔.엠에스이로스()(predictions, y_train)
        self.로그("train_loss", loss)
        return loss

    def 컨피규어옵티마이저스(self):
        return 토치.옵팀.아담(self.파라미터스(), lr=0.001)

model = Model()
trainer = L.트레이너(max_epochs=5, accelerator="cpu", devices=1)
trainer.핏(model, train_loader)
```

## 주요 번역

| KoPy | Python |
| --- | --- |
| `라이트닝.라이트닝모듈` | `lightning.LightningModule` |
| `라이트닝.라이트닝데이터모듈` | `lightning.LightningDataModule` |
| `라이트닝.트레이너` | `lightning.Trainer` |
| `라이트닝.시드에브리띵` | `lightning.seed_everything` |
| `.핏()` | `.fit()` |
| `.밸리데이트()` | `.validate()` |
| `.테스트()` | `.test()` |
| `.프리딕트()` | `.predict()` |
| `.트레이닝스텝()` | `.training_step()` |
| `.밸리데이션스텝()` | `.validation_step()` |
| `.컨피규어옵티마이저스()` | `.configure_optimizers()` |
| `.로그()` | `.log()` |
| `.세이브하이퍼파라미터스()` | `.save_hyperparameters()` |

## 원문으로 남기는 것

`model`, `trainer`, `train_loader`, `X_train`, `y_train`, `predictions` 같은 변수명은 실제 Python/ML 자료에서 매우 자주 보이므로 학습 연결성을 위해 그대로 둘 수 있습니다.

또한 `max_epochs=`, `accelerator=`, `devices=`, `logger=`, `callbacks=`, `precision=`, `strategy=`, `enable_checkpointing=`, `limit_train_batches=` 같은 Trainer 키워드 인자는 다른 라이브러리·사용자 코드와 충돌할 가능성이 있어 KoPy 전역 번역 대상이 아닙니다.

Lightning API 음역은 `lightning` 팩이 import된 파일에서만 활성화됩니다. 따라서 `fit`, `predict`, `log`처럼 일반적인 이름을 Core 전역 단어로 추가하지 않습니다.

## 테스트

CI에서는 Windows, Ubuntu, macOS의 Python 3.12.10 환경에 실제 Lightning 2.6.x와 PyTorch를 설치하고, 작은 `LightningModule`과 메모리 상의 `TensorDataset`으로 CPU `Trainer.fit()` 한 배치를 실행합니다. 외부 데이터셋, GPU, logger 서버, checkpoint 다운로드는 필요하지 않습니다.
