# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 API를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.24**  
개발 기준 Python: **3.12.10**

## 목표

KoPy의 목적은 Python을 한국어로 대체하는 것이 아니라 **원문 Python을 자연스럽게 익히도록 돕는 것**입니다.

- 표준 Python 코드는 수정 없이 그대로 실행할 수 있어야 합니다.
- KoPy 표현과 Python 표현을 한 파일에서 혼용할 수 있습니다.
- `X_train`, `X_test`, `df`, `features`, `model`, `fit`, `predict`처럼 실제 Python/데이터 과학에서 자주 보는 관례는 학습 가치가 있으면 의도적으로 남깁니다.
- 외부 라이브러리 API 번역은 해당 라이브러리가 import된 파일에서만 활성화되는 namespace-scoped Library Pack으로 제공합니다.
- 서로 다른 라이브러리에서 의미가 겹칠 수 있는 키워드 인자는 가능한 한 Python 원형을 유지합니다.

## KoPy v0.5 방향: AI 개발

Library Pack은 외부 라이브러리를 다시 구현하지 않습니다. KoPy 표현을 표준 Python 표현으로 바꾸고 실제 계산·학습·추론·시각화·실험 추적은 원래 Python 라이브러리가 담당합니다.

```text
KoPy 코드
   ↓
KoPy Core + 활성 Library Pack
   ↓
표준 Python 코드
   ↓
CPython + 실제 Python 라이브러리
```

현재 공식 Library Pack은 **25개**입니다.

| 팩 | 주요 범위 |
| --- | --- |
| NumPy | 배열·통계·선형대수·난수 |
| pandas | DataFrame·정제·집계·파일 입출력 |
| Polars | DataFrame·expression·group-by·lazy query·파일 입출력 |
| SciPy | 최적화·통계·희소행렬·선형대수·신호·적분 |
| scikit-learn | 전처리·모델 학습·평가·파이프라인 |
| XGBoost | 그래디언트 부스팅 분류·회귀·DMatrix·Booster |
| LightGBM | 그래디언트 부스팅 분류·회귀·Dataset·Booster |
| PyTorch | 텐서·자동미분·신경망·최적화 |
| TorchVision | 이미지 변환·비전 모델·데이터셋·detection ops |
| timm | 이미지 모델 탐색·생성·특징 추출·학습 유틸리티 |
| Kornia | 미분가능 이미지 처리·증강·필터·기하·비전 메트릭 |
| einops | 텐서 차원 재배열·축약·반복·패킹·einsum |
| JAX | 자동미분·JIT·벡터화·가속 배열 계산 |
| OpenCV | 이미지·영상 전처리·엣지·윤곽선·DNN·비디오 I/O |
| Transformers | 사전학습 모델·생성·Trainer |
| Datasets | 데이터 로딩·전처리·분할 |
| Tokenizers | 고속 토큰화·Encoding·어휘 모델 |
| Accelerate | 장치·분산 학습 준비와 실행 |
| PEFT | LoRA 등 파라미터 효율 미세조정 |
| ONNX Runtime | ONNX 모델 로딩·실행 공급자·최적화·추론 |
| Safetensors | AI 텐서의 안전한 저장·로드·부분 읽기 |
| Optimum | 모델 작업·export 구성·하드웨어 최적화 흐름 연결 |
| SentencePiece | 서브워드 토크나이저 학습·인코딩·디코딩·어휘 조회 |
| MLflow | experiment/run·파라미터·메트릭·태그·아티팩트 추적 |
| Matplotlib | 학습 곡선·분포·이미지·일반 데이터 시각화 |

## 기계학습 예시

KoPy는 영문 ML 관례를 지우지 않습니다. 변수명은 실제 Python 교재와 코드에서 흔한 형태를 남기면서 API만 KoPy 표현으로 익힐 수 있습니다.

```kopy
프롬 사이킷런.model_selection 임포트 트레인테스트스플릿
프롬 사이킷런.preprocessing 임포트 스탠더드스케일러
프롬 사이킷런.linear_model 임포트 로지스틱리그레션

X_train, X_test, y_train, y_test = 트레인테스트스플릿(
    X, y, test_size=0.2, random_state=42
)

스케일러 = 스탠더드스케일러()
X_train = 스케일러.핏트랜스폼(X_train)
X_test = 스케일러.트랜스폼(X_test)

model = 로지스틱리그레션(max_iter=200)
model.핏(X_train, y_train)
predictions = model.프리딕트(X_test)
```

## TorchVision 예시

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

`tv`, `image`, `features`, `model`, `weights=`, `mean=`, `std=` 같은 실제 Python/TorchVision 관례는 학습 가치가 있어 원문 형태를 유지합니다. 자세한 범위는 [`docs/TORCHVISION_PACK.md`](docs/TORCHVISION_PACK.md)를 참고하세요.

## timm 예시

```kopy
임포트 토치
임포트 팀엠

model = 팀엠.크리에이트모델(
    "resnet18",
    pretrained=False,
    num_classes=10,
)

x = 토치.랜드엔((1, 3, 224, 224))
위드 토치.노그라드():
    features = model.포워드피처스(x)
```

`model`, `x`, `features`, `pretrained=`, `num_classes=`는 실제 Python/timm 코드에서 자주 보는 관례라 원문 형태를 유지합니다. 자세한 범위는 [`docs/TIMM_PACK.md`](docs/TIMM_PACK.md)를 참고하세요.

## Kornia 예시

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

`image`, `gray`, `blurred`, `augment`, `augmented`, `degrees=`, `p=`는 실제 Python/Kornia 코드를 읽는 데 도움이 되므로 원문 형태를 유지합니다. 자세한 범위는 [`docs/KORNIA_PACK.md`](docs/KORNIA_PACK.md)를 참고하세요.

## einops 예시

```kopy
임포트 넘파이 애즈 np
프롬 에이놉스 임포트 리어레인지, 리듀스, 리피트

images = np.에이레인지(2 * 4 * 4 * 3, dtype=np.플로트64).리셰이프(2, 4, 4, 3)
features = 리어레인지(images, "batch height width channels -> batch channels height width")
pooled = 리듀스(features, "batch channels height width -> batch channels", "mean")
batch = 리피트(pooled[0], "channels -> batch channels", batch=3)
```

Einops의 pattern 문자열과 `batch=`, `channels=` 같은 축 이름은 실제 Python/einops 코드를 읽는 데 핵심이므로 번역하지 않습니다. `mean` 축약 예제는 backend 차이를 피하기 위해 부동소수점 입력을 사용합니다. 자세한 범위는 [`docs/EINOPS_PACK.md`](docs/EINOPS_PACK.md)를 참고하세요.

## 다른 팩 예시

### Polars

```kopy
임포트 폴라스 애즈 pl

df = pl.데이터프레임({"label": ["A", "A", "B"], "x": [1, 2, 3]})
features = df.위드컬럼즈((pl.컬("x") * 2).에일리어스("x2"))
summary = features.그룹바이("label").어그(pl.컬("x2").미인())
```

### XGBoost

```kopy
임포트 엑스지부스트 애즈 xgb
model = xgb.엑스지비클래시파이어(n_estimators=20, max_depth=2, tree_method="hist")
model.핏(X_train, y_train)
predictions = model.프리딕트(X_test)
```

### LightGBM

```kopy
임포트 라이트지비엠 애즈 lgb
model = lgb.엘지비엠클래시파이어(n_estimators=20, num_leaves=4, n_jobs=1)
model.핏(X_train, y_train)
predictions = model.프리딕트(X_test)
```

### JAX

```kopy
임포트 잭스
임포트 잭스.numpy 애즈 jnp

X = jnp.어레이([1.0, 2.0, 3.0])
loss_fn = lambda x: jnp.썸(jnp.스퀘어(x))
grad_fn = 잭스.짓(잭스.그라드(loss_fn))
grads = grad_fn(X)
```

`jax.numpy`, `jax.random` 같은 dotted submodule 경로는 Python 원형을 유지하고 API 멤버만 namespace-scoped 방식으로 음역합니다.

### OpenCV

```kopy
임포트 오픈씨브이 애즈 cv2
resized = cv2.리사이즈(image, (224, 224))
gray = cv2.씨브이티컬러(resized, cv2.COLOR_BGR2GRAY)
edges = cv2.캐니(gray, 50, 150)
```

### Matplotlib

```kopy
임포트 맷플롯립.pyplot 애즈 plt
figure, ax = plt.서브플롯츠()
ax.플롯([1, 2, 3], [1.0, 0.7, 0.5], marker="o", label="loss")
ax.셋타이틀("Training loss")
ax.레전드()
figure.세이브피그("loss.png")
```

## 충돌 방지 원칙

외부 라이브러리 API는 Core 전역 단어표에 섞지 않습니다. 해당 라이브러리를 import한 파일에서만 관련 규칙이 활성화됩니다. 여러 활성 팩이 같은 KoPy 철자를 서로 다른 Python API로 정의하면 KoPy는 임의로 추측하지 않고 모호한 표현을 번역하지 않습니다.

다음처럼 여러 라이브러리에서 공유될 수 있는 키워드 인자는 Python 원형을 유지합니다.

```text
device= providers= test_size= return_tensors= target_modules=
metadata= framework= vocab_size= run_name= method= bounds=
axis= dtype= marker= label= figsize= dpi= cmap=
n_estimators= max_depth= learning_rate= objective= tree_method=
n_jobs= num_boost_round= num_leaves= min_child_samples=
verbosity= random_state= has_header= separator= schema= strict=
shape= static_argnums= static_argnames= in_axes= out_axes= has_aux=
interpolation= scalefactor= size= swapRB= crop= thickness=
mean= std= inplace= weights= progress= num_classes= download= root= train=
pretrained= in_chans= features_only= out_indices= checkpoint_path= drop_rate= global_pool=
degrees= p= same_on_batch= keepdim= align_corners= padding_mode=
```

Einops의 pattern 안에 쓰는 `batch`, `channels`, `height`, `width` 같은 축 이름과 동일한 axis-length keyword도 사용자가 정하는 표준 표현이므로 KoPy 전역 번역 대상이 아닙니다.

## 실제 라이브러리 설치

KoPy는 번역 팩을 제공하며 실제 라이브러리는 일반 Python과 동일하게 별도 설치해야 합니다.

기본 AI/데이터 스택 예시:

```powershell
python -m pip install numpy pandas polars scipy scikit-learn xgboost lightgbm torch torchvision timm kornia einops jax opencv-python transformers datasets tokenizers accelerate peft onnxruntime safetensors optimum sentencepiece matplotlib
```

GUI가 필요 없는 서버·CI에서는 `opencv-python-headless`를 권장합니다. OpenCV 패키지 변형들은 모두 같은 `cv2` namespace를 사용하므로 한 환경에 여러 변형을 동시에 설치하지 마세요.

pandas 3.x 환경에서 MLflow tracking client를 함께 쓰려면:

```powershell
python -m pip install "mlflow-skinny>=3.15,<3.16"
```

full MLflow 3.15는 별도 가상환경 설치를 권장합니다.

## 개발용 설치

```powershell
git clone https://github.com/gpt0081/KoPy.git
cd KoPy
python -m pip install -e .
```

## 주요 CLI

```powershell
kopy run examples\hello.kpy
kopy check examples\hello.kpy
kopy translate examples\hello.kpy
kopy convert-python example.py
kopy help 프린트
kopy help np.어레이
kopy explain examples\hello.kpy
kopy learn examples\hello.kpy
kopy words
kopy packs
kopy packs polars
kopy packs scipy
kopy packs xgboost
kopy packs lightgbm
kopy packs torchvision
kopy packs timm
kopy packs kornia
kopy packs einops
kopy packs jax
kopy packs opencv
kopy packs matplotlib
kopy version
```

편집기/도구 연동용 JSON API:

```powershell
kopy words --json
kopy info --json
kopy diagnose examples\hello.kpy --json
kopy packs --json
kopy packs torchvision --json
kopy packs timm --json
kopy packs kornia --json
kopy packs einops --json
```

## Core 예시

```kopy
이름 = 인풋("이름: ")
나이 = 인트(인풋("나이: "))

이프 나이 >= 20:
    프린트(이름, "성인입니다.")
엘스:
    프린트(이름, "미성년자입니다.")
```

KoPy는 Python 문법 자체를 바꾸지 않고 표준 Python으로 변환한 뒤 CPython에서 실행합니다.

## 문서와 예제

각 Library Pack의 상세 범위는 `docs/`에, 실행 예제는 `examples/`에 있습니다. 대표 문서:

- [`docs/POLARS_PACK.md`](docs/POLARS_PACK.md)
- [`docs/SCIPY_PACK.md`](docs/SCIPY_PACK.md)
- [`docs/XGBOOST_PACK.md`](docs/XGBOOST_PACK.md)
- [`docs/LIGHTGBM_PACK.md`](docs/LIGHTGBM_PACK.md)
- [`docs/PYTORCH_PACK.md`](docs/PYTORCH_PACK.md)
- [`docs/TORCHVISION_PACK.md`](docs/TORCHVISION_PACK.md)
- [`docs/TIMM_PACK.md`](docs/TIMM_PACK.md)
- [`docs/KORNIA_PACK.md`](docs/KORNIA_PACK.md)
- [`docs/EINOPS_PACK.md`](docs/EINOPS_PACK.md)
- [`docs/JAX_PACK.md`](docs/JAX_PACK.md)
- [`docs/OPENCV_PACK.md`](docs/OPENCV_PACK.md)
- [`docs/TRANSFORMERS_PACK.md`](docs/TRANSFORMERS_PACK.md)
- [`docs/MLFLOW_PACK.md`](docs/MLFLOW_PACK.md)
- [`docs/MATPLOTLIB_PACK.md`](docs/MATPLOTLIB_PACK.md)

## 테스트 철학

Python 호환성을 가장 중요한 기준으로 둡니다. AI Library Pack은 GitHub Actions에서 Windows, Linux, macOS에 실제 라이브러리를 설치해 번역 테스트와 runtime smoke test를 수행합니다. 가능한 한 외부 모델·데이터·서버 다운로드 없이 메모리, 임시 파일, SQLite 또는 로컬 저장소에서 실제 라이브러리 코드를 실행합니다.

## 구조

```text
src/kopy
   ├─ words.py
   ├─ packs/
   │   ├─ base.py
   │   ├─ registry.py
   │   ├─ numpy.py
   │   ├─ pandas.py
   │   ├─ polars.py
   │   ├─ scipy.py
   │   ├─ sklearn.py
   │   ├─ xgboost.py
   │   ├─ lightgbm.py
   │   ├─ torch.py
   │   ├─ torchvision.py
   │   ├─ timm.py
   │   ├─ kornia.py
   │   ├─ einops.py
   │   ├─ jax.py
   │   ├─ opencv.py
   │   ├─ transformers.py
   │   ├─ datasets.py
   │   ├─ tokenizers.py
   │   ├─ accelerate.py
   │   ├─ peft.py
   │   ├─ onnxruntime.py
   │   ├─ safetensors.py
   │   ├─ optimum.py
   │   ├─ sentencepiece.py
   │   ├─ mlflow.py
   │   └─ matplotlib.py
   ├─ translator.py
   ├─ spelling.py
   ├─ education.py
   ├─ runtime.py
   ├─ editor.py
   └─ cli.py
```

## 다음 AI 확장 후보

- TensorBoard
- PyTorch Lightning

새 팩은 단순 인기보다 KoPy의 교육 가치, Python 3.12.10 호환성, namespace-scoped 번역 가능성, 실제 cross-platform 테스트 가능성을 함께 보고 선택합니다.

## 버전 정책

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다. 현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License