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

    # Lightning이 이름으로 찾는 framework override hook은 Python 원형 유지
    def training_step(self, batch, batch_idx):
        X_train, y_train = batch
        predictions = self(X_train)
        loss = 토치.엔엔.엠에스이로스()(predictions, y_train)
        self.로그("train_loss", loss)
        return loss

    def configure_optimizers(self):
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
| `.로그()` | `.log()` |
| `.로그딕트()` | `.log_dict()` |
| `.세이브하이퍼파라미터스()` | `.save_hyperparameters()` |
| `.매뉴얼백워드()` | `.manual_backward()` |

## framework override hook은 영어 원형 유지

`training_step`, `validation_step`, `test_step`, `predict_step`, `configure_optimizers`는 Lightning이 subclass에서 **정확한 메서드 이름으로 검색하는 framework hook**입니다. 현재 KoPy Library Pack은 import된 namespace와 객체 attribute만 안전하게 번역하며, 클래스 본문의 bare method definition을 전역 치환하지 않습니다.

따라서 이 hook들을 억지로 전역 번역하지 않습니다. 이는 Python 호환성을 지키면서 실제 Lightning 원문 코드를 자연스럽게 익히게 하는 KoPy의 교육 목적에도 맞습니다.

## 그 밖에 원문으로 남기는 것

`model`, `trainer`, `train_loader`, `X_train`, `y_train`, `predictions` 같은 변수명은 실제 Python/ML 자료에서 매우 자주 보이므로 학습 연결성을 위해 그대로 둘 수 있습니다.

또한 `max_epochs=`, `accelerator=`, `devices=`, `logger=`, `callbacks=`, `precision=`, `strategy=`, `enable_checkpointing=`, `limit_train_batches=` 같은 Trainer 키워드 인자는 다른 라이브러리·사용자 코드와 충돌할 가능성이 있어 KoPy 전역 번역 대상이 아닙니다.

Lightning API 음역은 `lightning` 팩이 import된 파일에서만 활성화됩니다. 따라서 `fit`, `predict`, `log`처럼 일반적인 이름을 Core 전역 단어로 추가하지 않습니다.

## 테스트

CI에서는 Windows, Ubuntu, macOS의 Python 3.12.10 환경에 실제 Lightning 2.6.x와 PyTorch를 설치하고, 작은 `LightningModule`과 메모리 상의 `TensorDataset`으로 CPU `Trainer.fit()` 한 배치를 실행합니다. 외부 데이터셋, GPU, logger 서버, checkpoint 다운로드는 필요하지 않습니다.
