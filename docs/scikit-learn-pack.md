# KoPy scikit-learn 팩

KoPy 0.5.2는 고전적 머신러닝 작업을 위한 scikit-learn 팩을 제공합니다. 실제 계산과 모델 학습은 설치된 `scikit-learn`이 수행하고 KoPy는 등록된 모듈/API 이름만 번역합니다.

## 설치

```bash
python -m pip install "scikit-learn>=1.9,<1.10"
```

KoPy 팩 상태 확인:

```bash
kopy packs
kopy packs scikit-learn
kopy help 사이킷런.스탠더드스케일러
```

## 예제

```kopy
프롬 사이킷런.model_selection 임포트 트레인테스트스플릿
프롬 사이킷런.preprocessing 임포트 스탠더드스케일러
프롬 사이킷런.linear_model 임포트 로지스틱리그레션

X_train, X_test, y_train, y_test = 트레인테스트스플릿(X, y, test_size=0.2)
스케일러 = 스탠더드스케일러()
X_train = 스케일러.핏트랜스폼(X_train)
모델 = 로지스틱리그레션()
모델.핏(X_train, y_train)
예측 = 모델.프리딕트(X_test)
```

현재 라이브러리 하위 모듈 경로(`model_selection`, `preprocessing`, `linear_model`, `metrics` 등)는 Python 원래 이름을 유지합니다. KoPy가 번역하는 부분은 루트 모듈 이름과 팩에 등록된 클래스·함수·메서드입니다. 이 제한은 잘못된 전역 추측을 피하기 위한 것입니다.

지원 범위는 전처리, train/test split, 교차검증, 파이프라인, 주요 선형/트리/앙상블/SVM/KNN 추정기, KMeans/PCA, 공통 `fit`/`predict`/`transform` 메서드, 분류·회귀 평가 지표입니다.
