# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 API를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.38**  
개발 기준 Python: **3.12.10**

## 목표

KoPy의 목적은 Python을 한국어로 대체하는 것이 아니라 **원문 Python을 자연스럽게 익히도록 돕는 것**입니다.

- 표준 Python 코드는 수정 없이 그대로 실행할 수 있어야 합니다.
- KoPy 표현과 Python 표현을 한 파일에서 혼용할 수 있습니다.
- `X_train`, `X_test`, `df`, `features`, `model`, `fit`, `predict`, `preds`, `target`, `edge_index`, `embeddings`, `query`, `index`, `corpus`, `retriever`, `response`, `reference`처럼 실제 Python/AI·검색 코드에서 자주 보는 관례는 학습 가치가 있으면 의도적으로 남깁니다.
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

현재 공식 Library Pack은 **39개**입니다.

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
| Lightning | PyTorch Trainer·학습/검증/테스트/예측 실행·로깅 |
| TorchMetrics | 분류·회귀 등 모델 평가 metric과 MetricCollection |
| OpenCV | 이미지·영상 전처리·엣지·윤곽선·DNN·비디오 I/O |
| Transformers | 사전학습 모델·생성·Trainer |
| Sentence Transformers | 임베딩·유사도·semantic search·reranking 모델 API |
| FastEmbed | ONNX 기반 dense/sparse embedding·late interaction·cross-encoder reranking |
| FAISS | 벡터 인덱스·nearest-neighbor 검색·L2/IP·IVF·HNSW |
| Qdrant Client | 벡터DB collection·point 저장·nearest-neighbor query·payload filter |
| Chroma | 로컬·서버 vector DB client·collection 관리·embedding query |
| BM25S | BM25 sparse lexical retrieval·tokenization·ranked document search |
| ranx | dense·lexical run fusion·rank fusion·IR evaluation |
| ir-measures | nDCG·Precision·Recall·RR·AP 등 표준 retrieval metric 평가 |
| Ragas | RAG sample/dataset·context/faithfulness/factuality 계열 평가 API |
| LlamaIndex Core | Document·Node·ingestion·VectorStoreIndex·retriever 등 RAG pipeline 구성 |
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

scaler = 스탠더드스케일러()
X_train = scaler.핏트랜스폼(X_train)
X_test = scaler.트랜스폼(X_test)

model = 로지스틱리그레션(max_iter=200)
model.핏(X_train, y_train)
predictions = model.프리딕트(X_test)
```

## 검색/RAG 흐름

현재 KoPy의 검색 스택은 dense retrieval, lexical retrieval, hybrid fusion, reranking, retrieval evaluation, end-to-end RAG evaluation에 더해 core RAG pipeline orchestration까지 이어집니다.

```text
Sentence Transformers / FastEmbed
             ↓
          embeddings
             ↓
FAISS / Qdrant / Chroma
        + BM25S
             ↓
            ranx
      hybrid rank fusion
             ↓
 FastEmbed CrossEncoder
          reranking
             ↓
       ir-measures
   retrieval evaluation
             ↓
           Ragas
  end-to-end RAG evaluation
             ↑
      LlamaIndex Core
Document / ingestion / index / retriever orchestration
```

### FAISS 벡터 검색

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

`embeddings`, `query`, `index`, `distances`, `indices`와 `add()`, `search()`는 실제 vector search/RAG 코드에서 반복적으로 등장하므로 Python 원형을 유지합니다. 자세한 범위는 [`docs/FAISS_PACK.md`](docs/FAISS_PACK.md)를 참고하세요.

### BM25S lexical search

```kopy
임포트 비엠이십오에스 애즈 bm25s

corpus_tokens = bm25s.토크나이즈(corpus, show_progress=False)
retriever = bm25s.비엠이십오(corpus=corpus)
retriever.index(corpus_tokens, show_progress=False)

query_tokens = bm25s.토크나이즈([query], show_progress=False)
results = retriever.retrieve(query_tokens, k=5, show_progress=False)
```

`corpus`, `query`, `retriever`, `results`, `index()`, `retrieve()`는 정보검색 전반에서 재사용되는 핵심 표현이므로 Python 원형을 유지합니다. 자세한 범위는 [`docs/BM25S_PACK.md`](docs/BM25S_PACK.md)를 참고하세요.

### FastEmbed cross-encoder reranking

```kopy
프롬 패스트임베드.rerank.cross_encoder 임포트 텍스트크로스인코더

reranker = 텍스트크로스인코더(
    model_name="Xenova/ms-marco-MiniLM-L-6-v2",
)
scores = list(reranker.rerank(query, documents))
```

`query`, `documents`, `scores`, `model_name`, `embed()`, `rerank()`는 검색/RAG 원문 코드 전반에서 반복되는 표현이므로 Python 원형을 유지합니다. `fastembed.rerank.cross_encoder` 같은 실제 dotted package 구조도 그대로 노출합니다. 자세한 범위는 [`docs/FASTEMBED_PACK.md`](docs/FASTEMBED_PACK.md)를 참고하세요.

### ir-measures retrieval evaluation

```kopy
프롬 아이알메저스 임포트 캘크어그리게이트, nDCG, P, RR

metrics = 캘크어그리게이트(
    [nDCG@10, P@5, RR],
    qrels,
    run,
)
```

`qrels`, `run`, `query_id`, `doc_id`, `score`와 `nDCG`, `P`, `R`, `RR`, `AP`, `MAP` 같은 표준 IR 표현은 논문·benchmark·원문 Python에서 그대로 쓰이므로 번역하지 않습니다. 자세한 범위는 [`docs/IR_MEASURES_PACK.md`](docs/IR_MEASURES_PACK.md)를 참고하세요.

### Ragas end-to-end RAG evaluation

```kopy
프롬 라가스 임포트 이밸류에이션데이터셋, 싱글턴샘플
프롬 라가스.metrics.collections 임포트 논엘엘엠스트링시밀래리티, 디스턴스메저

sample = 싱글턴샘플(
    user_input=query,
    response=response,
    reference=reference,
    retrieved_contexts=contexts,
)

dataset = 이밸류에이션데이터셋(samples=[sample])
metric = 논엘엘엠스트링시밀래리티(
    distance_measure=디스턴스메저.LEVENSHTEIN,
)
result = metric.score(reference=reference, response=response)
```

`query`, `response`, `reference`, `contexts`, `user_input`, `retrieved_contexts`, `score()`, `ascore()`, `evaluate()` 같은 RAG 공통 표현은 Python 원형을 유지합니다. `ragas.metrics.collections` 같은 실제 dotted package 구조도 그대로 노출합니다. 자세한 범위는 [`docs/RAGAS_PACK.md`](docs/RAGAS_PACK.md)를 참고하세요.

### LlamaIndex Core RAG orchestration

```kopy
프롬 라마인덱스.core 임포트 도큐먼트, 벡터스토어인덱스, 목임베딩

documents = [
    도큐먼트(text="KoPy teaches Python through transliteration."),
    도큐먼트(text="LlamaIndex composes retrieval augmented generation pipelines."),
]

index = 벡터스토어인덱스.from_documents(
    documents,
    embed_model=목임베딩(embed_dim=8),
    show_progress=False,
)
retriever = index.as_retriever(similarity_top_k=2)
nodes = retriever.retrieve(query)
```

`documents`, `nodes`, `query`, `index`, `retriever`, `from_documents()`, `as_retriever()`, `retrieve()` 같은 RAG 공통 표현은 Python 원형을 유지합니다. `llama_index.core.node_parser` 같은 실제 dotted package 구조도 그대로 노출합니다. 자세한 범위는 [`docs/LLAMA_INDEX_CORE_PACK.md`](docs/LLAMA_INDEX_CORE_PACK.md)를 참고하세요.

## 충돌 방지 원칙

외부 라이브러리 API는 Core 전역 단어표에 섞지 않습니다. 해당 라이브러리를 import한 파일에서만 관련 규칙이 활성화됩니다. 여러 활성 팩이 같은 KoPy 철자를 서로 다른 Python API로 정의하면 KoPy는 임의로 추측하지 않고 모호한 표현을 번역하지 않습니다.

예를 들어 다음과 같은 키워드와 일반 메서드는 Python 원형을 유지합니다.

```text
device= providers= test_size= return_tensors= target_modules=
axis= dtype= batch_size= top_k= limit= name= ids= embeddings=
query_embeddings= n_results= collection_name= vectors_config=
show_progress= stopwords= stemmer= method= backend= norm= metric=
model_name= user_input= response= reference= retrieved_contexts=
similarity_top_k= embed_model= storage_context= transformations=

add() search() train() reset() update() compute() get() query()
upsert() retrieve() delete() count() index() save() load()
evaluate() compare() embed() rerank() score() ascore()
from_documents() as_retriever() insert() refresh()
```

이 원칙은 Python 원문 학습을 돕고, 서로 다른 Library Pack 사이의 모호한 전역 번역을 막기 위한 것입니다.

## 실제 라이브러리 설치

KoPy는 번역 팩을 제공하며 실제 라이브러리는 일반 Python과 동일하게 별도 설치해야 합니다.

기본 AI/데이터/검색 스택 예시:

```powershell
python -m pip install numpy pandas polars scipy scikit-learn xgboost lightgbm torch torchvision torch-geometric timm kornia einops jax opencv-python lightning torchmetrics transformers sentence-transformers fastembed faiss-cpu qdrant-client chromadb bm25s ranx ir-measures ragas llama-index-core datasets tokenizers accelerate peft onnxruntime safetensors optimum sentencepiece optuna matplotlib
```

GUI가 필요 없는 서버·CI에서는 `opencv-python-headless`를 권장합니다. OpenCV 패키지 변형들은 모두 같은 `cv2` namespace를 사용하므로 한 환경에 여러 변형을 동시에 설치하지 마세요.

Ragas 0.4.3은 일부 최신 LangChain 조합과 import 호환 문제가 있어 KoPy CI에서는 Ragas 전용 격리 호환성 job을 사용합니다. 실제 프로젝트에서도 충돌이 생기면 Ragas를 별도 가상환경 또는 명시적으로 고정한 의존성 조합에서 사용하는 편이 안전합니다. 상세 내용은 [`docs/RAGAS_PACK.md`](docs/RAGAS_PACK.md)를 참고하세요.

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
kopy explain examples\hello.kpy
kopy learn examples\hello.kpy
kopy words
kopy packs
kopy packs sentence-transformers
kopy packs fastembed
kopy packs faiss
kopy packs qdrant
kopy packs chroma
kopy packs bm25s
kopy packs ranx
kopy packs ir-measures
kopy packs ragas
kopy packs llama-index-core
kopy version
```

편집기/도구 연동용 JSON API:

```powershell
kopy words --json
kopy info --json
kopy diagnose examples\hello.kpy --json
kopy packs --json
kopy packs sentence-transformers --json
kopy packs fastembed --json
kopy packs faiss --json
kopy packs qdrant --json
kopy packs chroma --json
kopy packs bm25s --json
kopy packs ranx --json
kopy packs ir-measures --json
kopy packs ragas --json
kopy packs llama-index-core --json
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

각 Library Pack의 상세 범위는 `docs/`에, 실행 예제는 `examples/`에 있습니다. 검색/RAG 관련 대표 문서:

- [`docs/SENTENCE_TRANSFORMERS_PACK.md`](docs/SENTENCE_TRANSFORMERS_PACK.md)
- [`docs/FASTEMBED_PACK.md`](docs/FASTEMBED_PACK.md)
- [`docs/FAISS_PACK.md`](docs/FAISS_PACK.md)
- [`docs/QDRANT_PACK.md`](docs/QDRANT_PACK.md)
- [`docs/CHROMA_PACK.md`](docs/CHROMA_PACK.md)
- [`docs/BM25S_PACK.md`](docs/BM25S_PACK.md)
- [`docs/RANX_PACK.md`](docs/RANX_PACK.md)
- [`docs/IR_MEASURES_PACK.md`](docs/IR_MEASURES_PACK.md)
- [`docs/RAGAS_PACK.md`](docs/RAGAS_PACK.md)
- [`docs/LLAMA_INDEX_CORE_PACK.md`](docs/LLAMA_INDEX_CORE_PACK.md)

그 밖의 Library Pack 문서도 `docs/`에 있습니다.

## 테스트 철학

Python 호환성을 가장 중요한 기준으로 둡니다. AI Library Pack은 GitHub Actions에서 Windows, Linux, macOS에 실제 라이브러리를 설치해 번역 테스트와 runtime smoke test를 수행합니다. 가능한 한 외부 모델·데이터·서버 다운로드 없이 메모리, 임시 파일, SQLite 또는 로컬 저장소에서 실제 라이브러리 코드를 실행합니다. 외부 모델이 필요한 팩은 버전과 모델을 고정하고 결과의 핵심 성질을 검증합니다.

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
   │   ├─ fastembed.py
   │   ├─ faiss.py
   │   ├─ qdrant.py
   │   ├─ chroma.py
   │   ├─ bm25s.py
   │   ├─ ranx.py
   │   ├─ ir_measures.py
   │   ├─ ragas.py
   │   ├─ llama_index.py
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

- LlamaIndex vector-store/embedding/LLM integrations와 KoPy 기존 팩 연결
- retrieval + generation을 함께 다루는 완전 로컬 end-to-end RAG 예제
- RAG pipeline observability/tracing 계층

현재 검색 스택은 dense vector search(FAISS/Qdrant/Chroma) + sparse lexical search(BM25S) + ranx rank fusion + FastEmbed cross-encoder reranking + ir-measures 표준 retrieval evaluation + Ragas end-to-end RAG evaluation + LlamaIndex Core orchestration까지 이어집니다. 다음 단계에서도 특정 프레임워크의 과도하게 일반적인 메서드를 전역 음역하지 않는 원칙을 유지합니다.

## 버전 정책

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다. 현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License