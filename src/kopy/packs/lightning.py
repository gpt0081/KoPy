"""Official Lightning library pack for KoPy.

Covers the stable, high-value PyTorch Lightning training workflow while
preserving generic Trainer keyword arguments, common Python/ML variable names,
and framework override hook names in upstream form for safe subclassing.
"""

from __future__ import annotations

from .base import LibraryPack


LIGHTNING_PACK = LibraryPack(
    name="lightning",
    module="lightning",
    kopy_module="라이트닝",
    preferred_aliases=("lightning", "L"),
    description="PyTorch Lightning 모델·Trainer·로깅·학습/검증/예측 실행 API 팩",
    members={
        "라이트닝모듈": "LightningModule",
        "라이트닝데이터모듈": "LightningDataModule",
        "트레이너": "Trainer",
        "시드에브리띵": "seed_everything",
        "핏": "fit",
        "밸리데이트": "validate",
        "테스트": "test",
        "프리딕트": "predict",
        "로그": "log",
        "로그딕트": "log_dict",
        "세이브하이퍼파라미터스": "save_hyperparameters",
        "매뉴얼백워드": "manual_backward",
        "옵티마이저스": "optimizers",
        "엘알스케줄러스": "lr_schedulers",
        "토글옵티마이저": "toggle_optimizer",
        "언토글옵티마이저": "untoggle_optimizer",
    },
    member_descriptions={
        "LightningModule": "PyTorch 모델과 학습·검증·테스트 로직을 묶는 Lightning 기본 클래스입니다.",
        "LightningDataModule": "데이터 준비와 DataLoader 구성을 캡슐화하는 기본 클래스입니다.",
        "Trainer": "학습·검증·테스트·예측 루프를 실행하는 Lightning 실행기입니다.",
        "seed_everything": "Python·NumPy·PyTorch 난수 시드를 함께 고정합니다.",
        "log": "Trainer가 수집할 metric을 기록합니다.",
        "save_hyperparameters": "모델 생성 인자를 checkpoint용 hyperparameter로 저장합니다.",
    },
    examples={
        "Trainer": (
            "임포트 라이트닝 애즈 L\ntrainer = L.트레이너(max_epochs=1, accelerator='cpu')",
            "import lightning as L\ntrainer = L.Trainer(max_epochs=1, accelerator='cpu')",
        ),
        "LightningModule": (
            "임포트 라이트닝 애즈 L\n클래스 Model(L.라이트닝모듈):\n    패스",
            "import lightning as L\nclass Model(L.LightningModule):\n    pass",
        ),
        "fit": (
            "trainer.핏(model, train_loader)",
            "trainer.fit(model, train_loader)",
        ),
    },
)
