# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 API를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.32**  
개발 기준 Python: **3.12.10**

## 목표

KoPy의 목적은 Python을 한국어로 대체하는 것이 아니라 **원문 Python을 자연스럽게 익히도록 돕는 것**입니다.

- 표준 Python 코드는 수정 없이 그대로 실행할 수 있어야 합니다.
- KoPy 표현과 Python 표현을 한 파일에서 혼용할 수 있습니다.
- `X_train`, `X_test`, `df`, `features`, `model`, `fit`, `predict`, `preds`, `target`, `edge_index`, `embeddings`, `query`, `index`처럼 실제 Python/데이터 과학·검색 코드에서 자주 보는 관례는 학습 가치가 있으면 의도적으로 남깁니다.
- 외부 라이브러리 API 번역은 해당 라이브러리가 import된 파일에서만 활성화되는 namespace-scoped Library Pack으로 제공합니다.
- 서로 다른 라이브러리에서 의미가 겹칠 수 있는 일반 메서드와 키워드 인자는 가능한 한 Python 원형을 유지합니다.

## KoPy v0.5 방향: AI 개발

Library Pack은 외부 라이브러리를 다시 구현하지 않습니다. KoPy 표현을 표준 Python 표현으로 바꾸고 실제 계산·학습·추론·시각화·평가·실험 추적·검색은 원래 Python 라이브러리가 담당합니다.

```text
KoPy 코드
   ↓
KoPy Core + 활성 Library Pack
   ↓
표준 Python 코드
   ↓
CPython + 실제 Python 라이브러리
```

현재 공식 Library Pack은 **33개**입니다.

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
| PyTorch Geometric | 그래프 데이터·GNN layer·pooling·graph utility |
| timm | 이미지 모델 탐색·생성·특징 추출·학습 유틸리티 |
| Kornia | 미분가능 이미지 처리·증강·필터·기하·비전 메트릭 |
| einops | 텐서 차원 재배열·축약·반복·패킹·einsum |
| JAX | 자동미분·JIT·벡터화·가속 배열 계산 |
| Lightning | PyTorch 모델·Trainer·학습/검증/테스트/예측 실행·로깅 |
| TorchMetrics | 분류·회귀 등 모델 평가 metric과 MetricCollection |
| OpenCV | 이미지·영상 전처리·엣지·윤곽선·DNN·비디오 I/O |
| Transformers | 사전학습 모델·생성·Trainer |
| Sentence Transformers | 임베딩·유사도·semantic search·reranking 모델 API |
| FAISS | 벡터 인덱스·nearest-neighbor 검색·L2/IP·IVF·HNSW |
| Qdrant Client | 벡터DB collection·point 저장·nearest-neighbor query·payload filter |
| Chroma | 로컬·서버 vector DB client·collection 관리·embedding query |
| Datasets | 데이터 로딩·전처리·분할 |
| Tokenizers | 고속 토큰화·Encoding·어휘 모델 |
| Accelerate | 장치·분산 학습 준비와 실행 |
| PEFT | LoRA 등 파라미터 효율 미세조정 |
| ONNX Runtime | ONNX 모델 로딩·실행 공급자·최적화·추론 |
| Safetensors | AI 텐서의 안전한 저장·로드·부분 읽기 |
| Optimum | 모델 작업·export 구성·하드웨어 최적화 흐름 연결 |
| SentencePiece | 서브워드 토크나이저 학습·인코딩·디코딩·어휘 조회 |
| Optuna | Study/Trial 기반 하이퍼파라미터 탐색·최적화 |
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

## FAISS 벡터 검색 예시

```kopy
임포트 넘파이 애즈 np
임포트 파이스 애즈 faiss

embeddings = np.어레이([
    [0.0, 0.0],
    [1.0, 1.0],
    [2.0, 2.0],
], dtype=np.플로트32)

query = np.어레이([[1.1, 1.0]], dtype=np.플로트32)
index = faiss.인덱스플랫엘투(embeddings.shape[1])
index.add(embeddings)
distances, indices = index.search(query, 2)
```

`embeddings`, `query`, `index`, `distances`, `indices`와 `add()`, `search()`는 실제 vector search/RAG 코드에서 반복적으로 등장하고 다른 라이브러리에서도 널리 쓰이는 표현이므로 Python 원형을 유지합니다. FAISS 고유 클래스와 함수만 namespace-scoped 방식으로 음역합니다. 자세한 범위는 [`docs/FAISS_PACK.md`](docs/FAISS_PACK.md)를 참고하세요.

## Qdrant 벡터DB 예시

```kopy
프롬 큐드란트 임포트 큐드란트클라이언트
프롬 큐드란트.models 임포트 벡터파람스, 디스턴스, 포인트스트럭트

client = 큐드란트클라이언트(":memory:")
client.크리에이트컬렉션(
    collection_name="docs",
    vectors_config=벡터파람스(size=384, distance=디스턴스.COSINE),
)

client.upsert(collection_name="docs", points=points)
result = client.쿼리포인츠(
    collection_name="docs",
    query=query,
    limit=5,
)
```

모듈 음역 `큐드란트`와 클래스 음역 `큐드란트클라이언트`는 `from ... import ...` 변환의 모호성을 피하기 위해 의도적으로 구분합니다. `client`, `collection`, `points`, `query`, `result`, `payload`, `score`, `vector`와 `collection_name=`, `vectors_config=`, `with_payload=`, `limit=` 같은 실제 Qdrant/RAG 관례는 Python 원형을 유지합니다. `upsert()`, `scroll()`, `retrieve()`, `delete()`, `count()` 역시 데이터베이스·검색 라이브러리 전반에서 흔한 메서드라 번역하지 않습니다. 자세한 범위는 [`docs/QDRANT_PACK.md`](docs/QDRANT_PACK.md)를 참고하세요.

## Chroma 벡터DB 예시

```kopy
임포트 크로마 애즈 chroma

client = chroma.클라이언트()
collection = client.크리에이트컬렉션(
    name="docs",
    embedding_function=None,
)

collection.add(
    ids=["a", "b"],
    embeddings=[[1.0, 0.0], [0.0, 1.0]],
    documents=["alpha", "beta"],
)

result = collection.query(
    query_embeddings=[[0.99, 0.01]],
    n_results=2,
)
```

`collection`, `ids`, `documents`, `embeddings`, `query_embeddings`, `result`, `metadata`와 `add()`, `query()`, `upsert()`, `get()`, `update()`, `delete()`, `count()`은 실제 vector DB/RAG 코드에서 널리 쓰이는 표현이므로 Python 원형을 유지합니다. `name=`, `embedding_function=`, `ids=`, `embeddings=`, `documents=`, `query_embeddings=`, `n_results=`, `where=` 같은 키워드 인자도 번역하지 않습니다. Chroma 고유 client·collection 관리 API만 namespace-scoped 방식으로 음역합니다. 자세한 범위는 [`docs/CHROMA_PACK.md`](docs/CHROMA_PACK.md)를 참고하세요.

## PyTorch Geometric 예시

```kopy
임포트 토치
프롬 토치지오메트릭.data 임포트 데이터
프롬 토치지오메트릭.nn 임포트 지씨엔컨브, 글로벌미인풀
프롬 토치지오메트릭.utils 임포트 투언디렉티드

x = 토치.텐서([
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0],
], dtype=토치.플로트32)

edge_index = 토치.텐서([
    [0, 1],
    [1, 2],
], dtype=토치.인트64)

edge_index = 투언디렉티드(edge_index)
graph = 데이터(x=x, edge_index=edge_index)

conv = 지씨엔컨브(in_channels=2, out_channels=4)
node_embeddings = conv(graph.x, graph.edge_index)

batch = 토치.제로즈(graph.num_nodes, dtype=토치.인트64)
graph_embedding = 글로벌미인풀(node_embeddings, batch)
```

`x`, `edge_index`, `batch`, `graph`, `node_embeddings`, `model` 같은 실제 PyTorch Geometric 관례와 `in_channels=`, `out_channels=`, `heads=`, `num_neighbors=` 같은 키워드 인자는 Python 원형으로 유지합니다. `torch_geometric.data`, `torch_geometric.nn`, `torch_geometric.utils` 같은 dotted submodule 경로도 실제 Python 구조를 익힐 수 있도록 원문을 유지합니다. 자세한 범위는 [`docs/PYTORCH_GEOMETRIC_PACK.md`](docs/PYTORCH_GEOMETRIC_PACK.md)를 참고하세요.

## Sentence Transformers 예시

```kopy
임포트 센텐스트랜스포머스 애즈 st
프롬 sentence_transformers.util 임포트 semantic_search

model = st.센텐스트랜스포머("sentence-transformers/all-MiniLM-L6-v2")
embeddings = model.인코드(sentences, convert_to_tensor=True)
query_embeddings = model.인코드(query, convert_to_tensor=True)
scores = model.시밀래리티(query_embeddings, embeddings)
hits = semantic_search(query_embeddings, embeddings, top_k=2)
```

`model`, `sentences`, `embeddings`, `query_embeddings`, `batch_size=`, `convert_to_tensor=`, `top_k=` 같은 실제 Python/Sentence Transformers 관례는 원문 형태를 유지합니다. Sentence Transformers 6.x에서 `models`, `util`은 `import sentence_transformers as st`의 공개 top-level 속성이 아니므로 `sentence_transformers.models`, `sentence_transformers.util` 같은 dotted submodule 경로도 실제 Python 원문을 유지합니다. 자세한 범위는 [`docs/SENTENCE_TRANSFORMERS_PACK.md`](docs/SENTENCE_TRANSFORMERS_PACK.md)를 참고하세요.

## Lightning 예시

```kopy
임포트 라이트닝 애즈 L
임포트 토치

class Model(L.라이트닝모듈):
    def __init__(self):
        super().__init__()
        self.layer = 토치.엔엔.리니어(4, 1)

    def forward(self, x):
        return self.layer(x)

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

`training_step`, `validation_step`, `test_step`, `predict_step`, `configure_optimizers`는 Lightning이 정확한 이름으로 찾는 framework override hook이므로 Python 원형을 유지합니다. `model`, `trainer`, `X_train`, `y_train`과 Trainer 키워드 인자도 실제 Lightning 코드를 익히기 위해 원문 형태를 유지합니다. 자세한 범위는 [`docs/LIGHTNING_PACK.md`](docs/LIGHTNING_PACK.md)를 참고하세요.

## TorchMetrics 예시

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

`preds`, `target`, `metric`, `accuracy`, `f1` 같은 실제 Python/TorchMetrics 관례와 `task=`, `num_classes=`, `average=`, `threshold=` 같은 키워드 인자는 원문 형태를 유지합니다. `update()`, `compute()`, `reset()`, `clone()`, `plot()`도 여러 라이브러리에서 널리 쓰이는 일반 메서드이므로 음역하지 않습니다. 자세한 범위는 [`docs/TORCHMETRICS_PACK.md`](docs/TORCHMETRICS_PACK.md)를 참고하세요.

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

Einops의 pattern 문자열과 `batch=`, `channels=` 같은 축 이름은 실제 Python/einops 코드를 읽는 데 핵심이므로 번역하지 않습니다. 자세한 범위는 [`docs/EINOPS_PACK.md`](docs/EINOPS_PACK.md)를 참고하세요.

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

### Optuna

```kopy
임포트 옵튜나

def objective(trial):
    learning_rate = trial.서제스트플로트("learning_rate", 1e-4, 1e-1, log=True)
    max_depth = trial.서제스트인트("max_depth", 2, 8)
    return (learning_rate - 0.01) ** 2 + (max_depth - 4) ** 2

study = 옵튜나.크리에이트스터디(direction="minimize")
study.옵티마이즈(objective, n_trials=20)
프린트(study.베스트파람스)
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
direction= study_name= storage= sampler= pruner= n_trials= timeout=
callbacks= catch= gc_after_trial= show_progress_bar= log=
max_epochs= accelerator= devices= logger= precision= strategy=
enable_checkpointing= limit_train_batches= enable_progress_bar= enable_model_summary=
task= average= threshold= batch_size= convert_to_tensor= normalize_embeddings= top_k=
in_channels= out_channels= heads= add_self_loops= num_neighbors=
collection_name= vectors_config= with_payload= limit=
name= embedding_function= ids= embeddings= documents= query_embeddings= n_results= where=
```

TorchMetrics의 `update`, `compute`, `reset`, `clone`, `plot`처럼 일반적인 lifecycle 메서드와 FAISS의 `add`, `search`, `train`, `reset`, `remove_ids`, `reconstruct`, Qdrant의 `upsert`, `scroll`, `retrieve`, `delete`, `count`, Chroma의 `add`, `query`, `upsert`, `get`, `update`, `delete`, `count`처럼 여러 라이브러리에서 반복되는 일반 메서드도 전역 번역 대상이 아닙니다. Einops의 pattern 안에 쓰는 `batch`, `channels`, `height`, `width` 같은 축 이름과 동일한 axis-length keyword도 사용자가 정하는 표준 표현이므로 그대로 둡니다.

## 실제 라이브러리 설치

KoPy는 번역 팩을 제공하며 실제 라이브러리는 일반 Python과 동일하게 별도 설치해야 합니다.

기본 AI/데이터/검색 스택 예시:

```powershell
python -m pip install numpy pandas polars scipy scikit-learn xgboost lightgbm torch torchvision torch-geometric timm kornia einops jax opencv-python lightning torchmetrics transformers sentence-transformers faiss-cpu qdrant-client chromadb datasets tokenizers accelerate peft onnxruntime safetensors optimum sentencepiece optuna matplotlib
```

GUI가 필요 없는 서버·CI에서는 `opencv-python-headless`를 권장합니다. OpenCV 패키지 변형들은 모두 같은 `cv2` namespace를 사용하므로 한 환경에 여러 변형을 동시에 설치하지 마세요.

PyTorch Geometric의 기본 팩 테스트는 `torch-geometric`과 PyTorch만 사용합니다. `pyg-lib`, `torch-scatter`, `torch-sparse` 같은 선택적 가속 패키지는 KoPy 기본 설치에 강제하지 않습니다.

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
kopy packs torch-geometric
kopy packs timm
kopy packs kornia
kopy packs einops
kopy packs jax
kopy packs opencv
kopy packs lightning
kopy packs torchmetrics
kopy packs sentence-transformers
kopy packs faiss
kopy packs qdrant
kopy packs chroma
kopy packs optuna
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
kopy packs torch-geometric --json
kopy packs timm --json
kopy packs kornia --json
kopy packs einops --json
kopy packs lightning --json
kopy packs torchmetrics --json
kopy packs sentence-transformers --json
kopy packs faiss --json
kopy packs qdrant --json
kopy packs chroma --json
kopy packs optuna --json
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
- [`docs/PYTORCH_GEOMETRIC_PACK.md`](docs/PYTORCH_GEOMETRIC_PACK.md)
- [`docs/TIMM_PACK.md`](docs/TIMM_PACK.md)
- [`docs/KORNIA_PACK.md`](docs/KORNIA_PACK.md)
- [`docs/EINOPS_PACK.md`](docs/EINOPS_PACK.md)
- [`docs/JAX_PACK.md`](docs/JAX_PACK.md)
- [`docs/LIGHTNING_PACK.md`](docs/LIGHTNING_PACK.md)
- [`docs/TORCHMETRICS_PACK.md`](docs/TORCHMETRICS_PACK.md)
- [`docs/OPENCV_PACK.md`](docs/OPENCV_PACK.md)
- [`docs/TRANSFORMERS_PACK.md`](docs/TRANSFORMERS_PACK.md)
- [`docs/SENTENCE_TRANSFORMERS_PACK.md`](docs/SENTENCE_TRANSFORMERS_PACK.md)
- [`docs/FAISS_PACK.md`](docs/FAISS_PACK.md)
- [`docs/QDRANT_PACK.md`](docs/QDRANT_PACK.md)
- [`docs/CHROMA_PACK.md`](docs/CHROMA_PACK.md)
- [`docs/OPTUNA_PACK.md`](docs/OPTUNA_PACK.md)
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
   │   ├─ torch_geometric.py
   │   ├─ timm.py
   │   ├─ kornia.py
   │   ├─ einops.py
   │   ├─ jax.py
   │   ├─ lightning.py
   │   ├─ torchmetrics.py
   │   ├─ opencv.py
   │   ├─ transformers.py
   │   ├─ sentence_transformers.py
   │   ├─ faiss.py
   │   ├─ qdrant.py
   │   ├─ chroma.py
   │   ├─ datasets.py
   │   ├─ tokenizers.py
   │   ├─ accelerate.py
   │   ├─ peft.py
   │   ├─ onnxruntime.py
   │   ├─ safetensors.py
   │   ├─ optimum.py
   │   ├─ sentencepiece.py
   │   ├─ optuna.py
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

검색/RAG 방향을 우선합니다.

- BM25 / lexical search
- Hybrid retrieval
- Reranking / retrieval evaluation

새 팩은 단순 인기보다 KoPy의 교육 가치, Python 3.12.10 호환성, namespace-scoped 번역 가능성, 실제 cross-platform 테스트 가능성을 함께 보고 선택합니다.

## 버전 정책

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다. 현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License