# KoPy (코파이)

KoPy는 Python 문법과 생태계를 그대로 배우면서 영어 예약어·API·주요 식별자를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.47**  
개발 기준 Python: **3.12.10**

## 목표

KoPy의 목적은 Python을 한국어로 대체하는 것이 아니라 **한글 음역을 통해 원문 Python을 자연스럽게 익히도록 돕는 것**입니다.

- 표준 Python 코드는 수정 없이 그대로 실행할 수 있어야 합니다.
- KoPy 표현과 Python 표현을 한 파일에서 혼용할 수 있습니다.
- 기본 원칙은 **영어 식별자와 API 이름을 한글로 음역하는 것**입니다.
- 숫자가 포함된 이름은 숫자를 읽어서 풀어쓰지 않고 **원래 숫자를 그대로 유지**합니다.
- 원문의 언더스코어 구조도 유지합니다.
- 외부 라이브러리 고유 API는 해당 라이브러리가 import된 파일에서만 활성화되는 namespace-scoped Library Pack으로 제공합니다.
- `top_k`처럼 여러 라이브러리·논문에서 반복되어 원문 자체를 익힐 가치가 큰 표준 표현은 예외적으로 영어를 유지할 수 있으며, 그 이유를 문서에 설명합니다.

자세한 규칙은 [`docs/TRANSLITERATION_STANDARD.md`](docs/TRANSLITERATION_STANDARD.md)를 참고하세요.

### 음역 예시

```text
Python                 KoPy
X_train                엑스_트레인
X_test                 엑스_테스트
y_train                와이_트레인
y_test                 와이_테스트
df                     디에프
features               피처스
model                  모델
fit                    핏
predict                프리딕트
preds                  프레즈
target                 타깃
edge_index             엣지_인덱스
embeddings             임베딩즈
query                  쿼리
index                  인덱스
corpus                 코퍼스
retriever              리트리버
response               리스폰스
reference              레퍼런스
document_store         다큐먼트_스토어
vector_store           벡터_스토어
```

숫자는 다음처럼 유지합니다.

```text
BM25                   비엠25
BM25S                  비엠25에스
F1Score                에프1스코어
IndexFlatL2            인덱스플랫엘2
gaussian_blur2d        가우시안블러2디
```

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

현재 공식 Library Pack은 **47개**입니다.

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
| sqlite-vec | SQLite `vec0` virtual table·로컬 KNN vector search |
| Qdrant Client | 벡터DB collection·point 저장·nearest-neighbor query·payload filter |
| Chroma | 로컬·서버 vector DB client·collection 관리·embedding query |
| LanceDB | 로컬·원격 vector DB·vector search·FTS·hybrid retrieval·reranker |
| BM25S | BM25 sparse lexical retrieval·tokenization·ranked document search |
| Tantivy | Rust 기반 로컬 full-text index·schema·query parser·ranked search |
| RapidFuzz | fuzzy string matching·query normalization·중복 제거·후보 추출 |
| ranx | dense·lexical run fusion·rank fusion·IR evaluation |
| ir-measures | nDCG·Precision·Recall·RR·AP 등 표준 retrieval metric 평가 |
| Ragas | RAG sample/dataset·context/faithfulness/factuality 계열 평가 API |
| LlamaIndex Core | Document·Node·ingestion·VectorStoreIndex·retriever 등 RAG pipeline 구성 |
| Haystack | Document·Pipeline·in-memory document store·BM25 retriever 등 RAG orchestration |
| LangChain Core | Document·Embeddings·InMemoryVectorStore·Runnable·prompt 등 provider-neutral RAG/LLM 추상화 |
| pypdf | PDF 읽기·페이지 접근·텍스트 추출·RAG document ingestion |
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

KoPy에서는 실제 ML 코드의 구조를 유지하면서 변수와 주요 API를 음역할 수 있습니다.

```kopy
프롬 사이킷런.model_selection 임포트 트레인테스트스플릿
프롬 사이킷런.preprocessing 임포트 스탠더드스케일러
프롬 사이킷런.linear_model 임포트 로지스틱리그레션

엑스_트레인, 엑스_테스트, 와이_트레인, 와이_테스트 = 트레인테스트스플릿(
    엑스, 와이, test_size=0.2, random_state=42
)

스케일러 = 스탠더드스케일러()
엑스_트레인 = 스케일러.핏트랜스폼(엑스_트레인)
엑스_테스트 = 스케일러.트랜스폼(엑스_테스트)

모델 = 로지스틱리그레션(max_iter=200)
모델.핏(엑스_트레인, 와이_트레인)
프레딕션즈 = 모델.프리딕트(엑스_테스트)
```

`X_train → 엑스_트레인`, `model → 모델`, `fit → 핏`, `predict → 프리딕트`처럼 원문과 음역을 1:1로 연결해 학습하는 것이 목표입니다.

## 검색/RAG 흐름

```text
PDF
 ↓
pypdf document ingestion
 ↓
page text / chunking
 ↓
Sentence Transformers / FastEmbed
             ↓
          embeddings
             ↓
FAISS / USearch / sqlite-vec / Qdrant / Chroma / LanceDB
        + BM25S / Tantivy
        + RapidFuzz fuzzy matching / dedup
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
LlamaIndex Core / Haystack / LangChain Core
Document / retrieval / pipeline / runnable abstractions
```

### Haystack 로컬 BM25 pipeline

```kopy
프롬 헤이스택 임포트 도큐먼트, 파이프라인
프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어
프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠25리트리버

다큐먼트_스토어 = 인메모리도큐먼트스토어()
다큐먼트_스토어.write_documents(다큐먼츠)

리트리버 = 인메모리비엠25리트리버(
    다큐먼트_스토어=다큐먼트_스토어,
    top_k=2,
)
```

`top_k`는 검색·추천·머신러닝에서 "상위 k개"를 뜻하는 매우 널리 쓰이는 표준 인자입니다. 논문과 여러 Python 라이브러리에서 같은 형태로 반복되기 때문에 현재 KoPy에서는 원문을 의도적으로 유지합니다. 이것은 예외이며, **기본 원칙은 영어 식별자의 한글 음역**입니다.

### FAISS 벡터 검색

```kopy
임포트 넘파이 애즈 np
임포트 파이스 애즈 faiss

임베딩즈 = np.어레이([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]], dtype=np.플로트32)
쿼리 = np.어레이([[1.1, 1.0]], dtype=np.플로트32)
인덱스 = faiss.인덱스플랫엘2(임베딩즈.shape[1])
인덱스.add(임베딩즈)
디스턴시즈, 인디시즈 = 인덱스.search(쿼리, 2)
```

### BM25S lexical search

```kopy
임포트 비엠25에스 애즈 bm25s

코퍼스_토큰즈 = bm25s.토크나이즈(코퍼스, show_progress=False)
리트리버 = bm25s.비엠25(코퍼스=코퍼스)
리트리버.index(코퍼스_토큰즈, show_progress=False)
쿼리_토큰즈 = bm25s.토크나이즈([쿼리], show_progress=False)
리절츠 = 리트리버.retrieve(쿼리_토큰즈, k=5, show_progress=False)
```

### pypdf PDF ingestion

```kopy
프롬 파이피디에프 임포트 피디에프리더

리더 = 피디에프리더("document.pdf")
텍스트 = "\n".join(page.익스트랙트텍스트() or "" 포 page 인 리더.pages)
```

파일 경로와 실제 PDF 내용은 데이터이므로 음역하지 않습니다. 이미지로만 구성된 스캔 PDF는 pypdf의 텍스트 추출 대상이 아니므로 별도의 OCR 단계가 필요합니다.

## 음역과 충돌 방지

KoPy 0.5.47부터 변환 레지스트리를 세 층으로 구분합니다.

1. Python 예약어·내장어 Core 음역
2. import된 라이브러리에서만 활성화되는 namespace-scoped Library Pack
3. `엑스_트레인`, `모델`, `쿼리`, `인덱스` 같은 공통 학습 식별자

공통 식별자는 Library Pack 변환 이후 적용합니다. 예를 들어:

```kopy
인덱스 = faiss.인덱스플랫엘2(384)
```

은 다음 Python으로 안전하게 변환됩니다.

```python
index = faiss.IndexFlatL2(384)
```

라이브러리 고유 클래스 `IndexFlatL2`와 변수 `index`를 같은 전역 API 번역으로 취급하지 않기 때문에 namespace 충돌을 줄일 수 있습니다.

## 실제 라이브러리 설치

KoPy는 번역 팩을 제공하며 실제 라이브러리는 일반 Python과 동일하게 별도 설치해야 합니다.

```powershell
python -m pip install numpy pandas polars scipy scikit-learn xgboost lightgbm torch torchvision torch-geometric timm kornia einops jax opencv-python lightning torchmetrics transformers sentence-transformers fastembed faiss-cpu usearch sqlite-vec qdrant-client chromadb lancedb bm25s tantivy rapidfuzz ranx ir-measures ragas llama-index-core haystack-ai langchain-core pypdf datasets tokenizers accelerate peft onnxruntime safetensors optimum sentencepiece optuna matplotlib
```

GUI가 필요 없는 서버·CI에서는 `opencv-python-headless`를 권장합니다.

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
kopy packs
kopy packs bm25s
kopy packs faiss
kopy packs haystack-ai
kopy version
```

편집기/도구 연동용 JSON API에서도 같은 팩 이름을 사용할 수 있습니다.

```powershell
kopy packs --json
kopy packs faiss --json
```

## 주요 문서

- [`docs/TRANSLITERATION_STANDARD.md`](docs/TRANSLITERATION_STANDARD.md)
- [`docs/SENTENCE_TRANSFORMERS_PACK.md`](docs/SENTENCE_TRANSFORMERS_PACK.md)
- [`docs/FASTEMBED_PACK.md`](docs/FASTEMBED_PACK.md)
- [`docs/FAISS_PACK.md`](docs/FAISS_PACK.md)
- [`docs/USEARCH_PACK.md`](docs/USEARCH_PACK.md)
- [`docs/SQLITE_VEC_PACK.md`](docs/SQLITE_VEC_PACK.md)
- [`docs/QDRANT_PACK.md`](docs/QDRANT_PACK.md)
- [`docs/CHROMA_PACK.md`](docs/CHROMA_PACK.md)
- [`docs/LANCEDB_PACK.md`](docs/LANCEDB_PACK.md)
- [`docs/BM25S_PACK.md`](docs/BM25S_PACK.md)
- [`docs/TANTIVY_PACK.md`](docs/TANTIVY_PACK.md)
- [`docs/RAPIDFUZZ_PACK.md`](docs/RAPIDFUZZ_PACK.md)
- [`docs/RANX_PACK.md`](docs/RANX_PACK.md)
- [`docs/IR_MEASURES_PACK.md`](docs/IR_MEASURES_PACK.md)
- [`docs/RAGAS_PACK.md`](docs/RAGAS_PACK.md)
- [`docs/LLAMA_INDEX_CORE_PACK.md`](docs/LLAMA_INDEX_CORE_PACK.md)
- [`docs/HAYSTACK_PACK.md`](docs/HAYSTACK_PACK.md)
- [`docs/LANGCHAIN_CORE_PACK.md`](docs/LANGCHAIN_CORE_PACK.md)
- [`docs/PYPDF_PACK.md`](docs/PYPDF_PACK.md)

그 밖의 Library Pack 문서도 `docs/`에 있습니다.

## 테스트 철학

Python 호환성을 가장 중요한 기준으로 둡니다. AI Library Pack은 GitHub Actions에서 Windows, Linux, macOS에 실제 라이브러리를 설치해 번역 테스트와 runtime smoke test를 수행합니다. 가능한 한 외부 모델·데이터·서버 다운로드 없이 메모리, 임시 파일, SQLite 또는 로컬 저장소에서 실제 라이브러리 코드를 실행합니다.

음역 표준화 변경도 반드시 양방향 변환 테스트를 추가합니다. 문자열·주석·숫자 리터럴은 건드리지 않는지, pack 고유 API와 공통 식별자가 충돌하지 않는지도 검증합니다.

## 다음 작업

0.5.47은 기존 47개 Library Pack 전체를 한 번에 다시 쓰는 릴리스가 아니라 **음역 표준을 확정하고 가장 눈에 띄는 위반부터 고치는 첫 감사 릴리스**입니다.

다음 감사에서는 다음을 계속 점검합니다.

- 기존 47개 팩의 숫자 음역 위반 전수 검사
- README·`docs/`·`examples/`에 남은 불필요한 영어 변수명 검사
- 어색한 음역과 의역 표현 검토
- 공통 식별자 사전 확대 시 Library Pack 충돌 테스트
- 검색/RAG integration 예제를 새 음역 표준으로 통일
