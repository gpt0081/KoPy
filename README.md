# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 API를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.42**  
개발 기준 Python: **3.12.10**

## 목표

KoPy의 목적은 Python을 한국어로 대체하는 것이 아니라 **원문 Python을 자연스럽게 익히도록 돕는 것**입니다.

- 표준 Python 코드는 수정 없이 그대로 실행할 수 있어야 합니다.
- KoPy 표현과 Python 표현을 한 파일에서 혼용할 수 있습니다.
- `X_train`, `X_test`, `df`, `features`, `model`, `fit`, `predict`, `preds`, `target`, `edge_index`, `embeddings`, `query`, `index`, `corpus`, `retriever`, `response`, `reference`처럼 실제 Python/AI·검색 코드에서 자주 보는 관례는 학습 가치가 있으면 의도적으로 남깁니다.
- 외부 라이브러리 API 번역은 해당 라이브러리가 import된 파일에서만 활성화되는 namespace-scoped Library Pack으로 제공합니다.
- 서로 다른 라이브러리에서 의미가 겹칠 수 있는 일반 메서드와 키워드 인자는 가능한 한 Python 원형을 유지합니다.

## KoPy v0.5 방향: AI 개발

Library Pack은 외부 라이브러리를 다시 구현하지 않습니다. KoPy 표현을 표준 Python 표현으로 바꾸고 실제 계산·학습·추론·검색·평가는 원래 Python 라이브러리가 담당합니다.

```text
KoPy 코드
   ↓
KoPy Core + 활성 Library Pack
   ↓
표준 Python 코드
   ↓
CPython + 실제 Python 라이브러리
```

현재 공식 Library Pack은 **43개**입니다.

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
| USearch | 경량 로컬 ANN index·cosine/L2/IP 검색·벡터 양자화 |
| sqlite-vec | SQLite 내부 vec0 virtual table·로컬 KNN vector search |
| Qdrant Client | 벡터DB collection·point 저장·nearest-neighbor query·payload filter |
| Chroma | 로컬·서버 vector DB client·collection 관리·embedding query |
| LanceDB | 로컬·원격 vector DB·vector search·FTS·hybrid retrieval·reranker |
| BM25S | BM25 sparse lexical retrieval·tokenization·ranked document search |
| ranx | dense·lexical run fusion·rank fusion·IR evaluation |
| ir-measures | nDCG·Precision·Recall·RR·AP 등 표준 retrieval metric 평가 |
| Ragas | RAG sample/dataset·context/faithfulness/factuality 계열 평가 API |
| LlamaIndex Core | Document·Node·ingestion·VectorStoreIndex·retriever 등 RAG pipeline 구성 |
| Haystack | Document·Pipeline·in-memory document store·BM25 retriever 등 RAG orchestration |
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

KoPy는 영문 ML 관례를 지우지 않습니다.

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

```text
Sentence Transformers / FastEmbed
             ↓
          embeddings
             ↓
FAISS / USearch / sqlite-vec / Qdrant / Chroma / LanceDB
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
LlamaIndex Core / Haystack
Document / ingestion / retrieval / pipeline orchestration
```

### sqlite-vec 로컬 SQLite vector search

```kopy
임포트 sqlite3
임포트 에스큐엘라이트벡 애즈 sv

connection = sqlite3.connect(":memory:")
connection.enable_load_extension(True)
sv.로드(connection)
connection.enable_load_extension(False)

connection.execute(
    "CREATE VIRTUAL TABLE vec_items USING vec0(embedding float[3])"
)
connection.execute(
    "INSERT INTO vec_items(rowid, embedding) VALUES (?, ?)",
    [1, sv.시리얼라이즈플로트32([1.0, 0.0, 0.0])],
)

query = [0.95, 0.05, 0.0]
rows = connection.execute(
    "SELECT rowid, distance FROM vec_items "
    "WHERE embedding MATCH ? ORDER BY distance LIMIT 2",
    [sv.시리얼라이즈플로트32(query)],
).fetchall()
```

`connection`, `query`, `embedding`, `rowid`, `distance`, `execute()`, `fetchall()`과 SQL 문법은 실제 SQLite/vector-search 학습을 위해 원형을 유지합니다. KoPy는 SQL 문자열을 번역하지 않습니다. 일부 macOS Python 빌드는 SQLite loadable extension을 지원하지 않으므로 자세한 플랫폼 설명은 [`docs/SQLITE_VEC_PACK.md`](docs/SQLITE_VEC_PACK.md)를 참고하세요.

### Haystack 로컬 BM25 pipeline

```kopy
프롬 헤이스택 임포트 도큐먼트, 파이프라인
프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어
프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠이십오리트리버

documents = [
    도큐먼트(content="KoPy teaches Python syntax and AI libraries."),
    도큐먼트(content="Haystack composes retrieval and RAG pipelines."),
]

document_store = 인메모리도큐먼트스토어()
document_store.write_documents(documents)
retriever = 인메모리비엠이십오리트리버(document_store=document_store, top_k=2)
pipeline = 파이프라인()
pipeline.add_component("retriever", retriever)
result = pipeline.run({"retriever": {"query": query}})
```

### FAISS 벡터 검색

```kopy
임포트 넘파이 애즈 np
임포트 파이스 애즈 faiss

embeddings = np.어레이([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]], dtype=np.플로트32)
query = np.어레이([[1.1, 1.0]], dtype=np.플로트32)
index = faiss.인덱스플랫엘투(embeddings.shape[1])
index.add(embeddings)
distances, indices = index.search(query, 2)
```

## 충돌 방지 원칙

외부 라이브러리 API는 Core 전역 단어표에 섞지 않습니다. 해당 라이브러리를 import한 파일에서만 관련 규칙이 활성화됩니다. 여러 활성 팩이 같은 KoPy 철자를 서로 다른 Python API로 정의하면 KoPy는 임의로 추측하지 않고 모호한 표현을 번역하지 않습니다.

다음과 같은 일반적인 이름은 가능한 한 Python 원형을 유지합니다.

```text
device= providers= test_size= return_tensors= target_modules=
axis= dtype= batch_size= top_k= limit= name= ids= embeddings=
query_embeddings= n_results= collection_name= vectors_config=
show_progress= method= backend= norm= metric= model_name=
user_input= response= reference= retrieved_contexts=
similarity_top_k= embed_model= storage_context= transformations=
document_store= ndim= connectivity= expansion_add= expansion_search=

add() search() train() reset() update() compute() get() query()
upsert() retrieve() delete() count() index() save() load()
evaluate() compare() embed() rerank() score() ascore()
from_documents() as_retriever() insert() refresh()
connect() create_table() open_table() limit() to_list()
add_component() run() write_documents()
execute() fetchone() fetchall()
```

## 실제 라이브러리 설치

KoPy는 번역 팩을 제공하며 실제 라이브러리는 일반 Python과 동일하게 별도 설치해야 합니다.

```powershell
python -m pip install numpy pandas polars scipy scikit-learn xgboost lightgbm torch torchvision torch-geometric timm kornia einops jax opencv-python lightning torchmetrics transformers sentence-transformers fastembed faiss-cpu usearch sqlite-vec qdrant-client chromadb lancedb bm25s ranx ir-measures ragas llama-index-core haystack-ai datasets tokenizers accelerate peft onnxruntime safetensors optimum sentencepiece optuna matplotlib
```

GUI가 필요 없는 서버·CI에서는 `opencv-python-headless`를 권장합니다. OpenCV 패키지 변형들은 모두 같은 `cv2` namespace를 사용하므로 한 환경에 여러 변형을 동시에 설치하지 마세요.

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
kopy packs usearch
kopy packs sqlite-vec
kopy packs qdrant
kopy packs chroma
kopy packs lancedb
kopy packs bm25s
kopy packs ranx
kopy packs ir-measures
kopy packs ragas
kopy packs llama-index-core
kopy packs haystack-ai
kopy version
```

편집기/도구 연동용 JSON API에서도 같은 팩 이름을 사용할 수 있습니다.

```powershell
kopy packs --json
kopy packs sqlite-vec --json
kopy packs haystack-ai --json
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

## 검색/RAG 문서

- [`docs/SENTENCE_TRANSFORMERS_PACK.md`](docs/SENTENCE_TRANSFORMERS_PACK.md)
- [`docs/FASTEMBED_PACK.md`](docs/FASTEMBED_PACK.md)
- [`docs/FAISS_PACK.md`](docs/FAISS_PACK.md)
- [`docs/USEARCH_PACK.md`](docs/USEARCH_PACK.md)
- [`docs/SQLITE_VEC_PACK.md`](docs/SQLITE_VEC_PACK.md)
- [`docs/QDRANT_PACK.md`](docs/QDRANT_PACK.md)
- [`docs/CHROMA_PACK.md`](docs/CHROMA_PACK.md)
- [`docs/LANCEDB_PACK.md`](docs/LANCEDB_PACK.md)
- [`docs/BM25S_PACK.md`](docs/BM25S_PACK.md)
- [`docs/RANX_PACK.md`](docs/RANX_PACK.md)
- [`docs/IR_MEASURES_PACK.md`](docs/IR_MEASURES_PACK.md)
- [`docs/RAGAS_PACK.md`](docs/RAGAS_PACK.md)
- [`docs/LLAMA_INDEX_CORE_PACK.md`](docs/LLAMA_INDEX_CORE_PACK.md)
- [`docs/HAYSTACK_PACK.md`](docs/HAYSTACK_PACK.md)

그 밖의 Library Pack 문서도 `docs/`에 있습니다.

## 테스트 철학

Python 호환성을 가장 중요한 기준으로 둡니다. AI Library Pack은 GitHub Actions에서 Windows, Linux, macOS에 실제 라이브러리를 설치해 번역 테스트와 runtime smoke test를 수행합니다. 가능한 한 외부 모델·데이터·서버 다운로드 없이 메모리, 임시 파일, SQLite 또는 로컬 저장소에서 실제 라이브러리 코드를 실행합니다.

`sqlite-vec`는 Python의 SQLite 빌드가 loadable extension을 지원해야 실제 runtime test를 실행할 수 있습니다. 일반 matrix에서는 capability를 검사하고, macOS에서는 별도 Homebrew Python 3.12 환경에서도 실제 `vec0` KNN 검색을 검증합니다.

## 다음 AI 확장 후보

검색/RAG 방향을 우선합니다.

- LlamaIndex/Haystack과 Qdrant·Chroma·LanceDB·sqlite-vec를 실제로 연결하는 integration 예제
- embedding → retrieval → reranking → generation을 함께 다루는 완전 로컬 end-to-end RAG 예제
- RAG pipeline observability/tracing 계층

새 라이브러리를 무작정 늘리기보다 이미 지원하는 검색/RAG 팩들이 실제 하나의 파이프라인에서 연결되는지를 우선 검증합니다.

## 버전 정책

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다. 현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License