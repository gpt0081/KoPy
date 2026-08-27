# KoPy (코파이)

KoPy는 표준 Python과 호환되면서 영어 예약어·API·주요 식별자를 **한글 음역**으로도 쓸 수 있게 하는 학습 레이어입니다.

현재 Core 버전: **0.5.48**  
개발 기준 Python: **3.12.10**

## 목표

KoPy의 목적은 Python을 한국어로 대체하는 것이 아닙니다. 한글 음역과 원문 Python을 1:1로 연결해, KoPy를 공부하면 실제 Python 코드도 자연스럽게 읽도록 만드는 것이 목표입니다.

- 표준 Python 코드는 수정 없이 그대로 실행할 수 있어야 합니다.
- KoPy 표현과 Python 표현을 한 파일에서 혼용할 수 있습니다.
- 기본은 **영어 식별자와 API 이름의 한글 음역**입니다.
- 숫자는 읽어 쓰지 않고 **원래 숫자를 그대로 유지**합니다.
- 언더스코어 구조도 유지합니다.
- 문자열·주석·데이터 값은 음역하지 않습니다.
- 라이브러리 API는 해당 라이브러리가 import된 코드에서만 활성화되는 namespace-scoped Library Pack으로 제공합니다.
- `top_k`처럼 원문 자체를 익힐 교육 가치가 큰 표준 표현만 명시적인 예외로 둘 수 있습니다.

자세한 기준은 [`docs/TRANSLITERATION_STANDARD.md`](docs/TRANSLITERATION_STANDARD.md)를 참고하세요.

## 음역 예시

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

숫자는 그대로 남깁니다.

```text
BM25                   비엠25
BM25S                  비엠25에스
F1Score                에프1스코어
IndexFlatL2            인덱스플랫엘2
gaussian_blur2d        가우시안블러2디
```

## 일반 메서드와 namespace

`add`, `search`, `retrieve`, `run`, `get`처럼 여러 라이브러리에서 반복되는 메서드를 전역으로 바꾸면 충돌 위험이 있습니다. KoPy는 영어로 방치하는 대신 **활성 Library Pack 안에서만** 음역합니다.

```kopy
# FAISS
인덱스.애드(임베딩즈)
디스턴시즈, 인디시즈 = 인덱스.서치(쿼리, 2)

# BM25S
리절츠 = 리트리버.리트리브(쿼리_토큰즈, k=5)

# Chroma
collection.업서트(ids=ids, embeddings=임베딩즈)

# Haystack
pipeline.애드컴포넌트("retriever", 리트리버)
리절트 = pipeline.런(인풋)
```

해당 팩을 import하지 않은 코드의 `서치`, `리트리브`, `업서트`, `런`을 KoPy가 임의로 추측해 바꾸지는 않습니다.

`client`, `collection`, `pipeline`, 일부 키워드 인자처럼 아직 영어로 보이는 항목은 영구 예외로 확정한 것이 아닙니다. 공통 식별자로 추가했을 때 기존 47개 팩의 class/variable shadowing과 역변환이 함께 바뀌므로 별도 전수 감사 대상으로 남겨 둡니다.

## AI 개발 Library Pack

Library Pack은 외부 라이브러리를 다시 구현하지 않습니다. KoPy 코드를 표준 Python으로 변환하고 실제 계산·학습·검색은 원래 라이브러리가 수행합니다.

현재 공식 Library Pack은 **47개**입니다.

| 영역 | 팩 |
| --- | --- |
| 데이터·과학계산 | NumPy, pandas, Polars, SciPy |
| 전통 ML | scikit-learn, XGBoost, LightGBM, Optuna |
| 딥러닝 | PyTorch, Lightning, TorchMetrics, einops, JAX |
| 컴퓨터 비전 | TorchVision, OpenCV, timm, Kornia |
| NLP·LLM | Transformers, Tokenizers, SentencePiece, Sentence Transformers |
| Hugging Face 학습·배포 | Datasets, Accelerate, PEFT, Optimum, Safetensors |
| 그래프 AI | PyTorch Geometric |
| 추론·실험 | ONNX Runtime, MLflow, Matplotlib |
| 임베딩·reranking | FastEmbed |
| 벡터 검색·DB | FAISS, USearch, sqlite-vec, Qdrant Client, Chroma, LanceDB |
| lexical·full-text 검색 | BM25S, Tantivy, RapidFuzz |
| fusion·검색 평가 | ranx, ir-measures |
| RAG 평가 | Ragas |
| RAG orchestration | LlamaIndex Core, Haystack, LangChain Core |
| 문서 ingestion | pypdf |

## 기계학습 예시

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

`X_train → 엑스_트레인`, `model → 모델`, `fit → 핏`, `predict → 프리딕트`처럼 원문과 음역을 연결해 학습합니다.

## 검색/RAG 예시

### Haystack 로컬 BM25

```kopy
프롬 헤이스택 임포트 도큐먼트, 파이프라인
프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어
프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠25리트리버

다큐먼트_스토어 = 인메모리도큐먼트스토어()
다큐먼트_스토어.라이트도큐먼츠(다큐먼츠)

리트리버 = 인메모리비엠25리트리버(
    다큐먼트_스토어=다큐먼트_스토어,
    top_k=2,
)

pipeline = 파이프라인()
pipeline.애드컴포넌트("retriever", 리트리버)
리절트 = pipeline.런({"retriever": {"query": 쿼리}})
```

`top_k`는 검색·추천·머신러닝에서 “상위 k개”를 뜻하며 논문과 여러 Python 라이브러리에서 거의 같은 형태로 반복됩니다. 그래서 현재는 원문을 유지합니다. **이것은 명시적 예외이며 기본은 음역입니다.**

### FAISS 벡터 검색

```kopy
임포트 넘파이 애즈 np
임포트 파이스 애즈 faiss

임베딩즈 = np.어레이([[0.0, 0.0], [1.0, 1.0]], dtype=np.플로트32)
쿼리 = np.어레이([[0.9, 1.0]], dtype=np.플로트32)
인덱스 = faiss.인덱스플랫엘2(임베딩즈.shape[1])
인덱스.애드(임베딩즈)
디스턴시즈, 인디시즈 = 인덱스.서치(쿼리, 2)
```

### BM25S lexical search

```kopy
임포트 비엠25에스 애즈 bm25s

코퍼스_토큰즈 = bm25s.토크나이즈(코퍼스, show_progress=False)
리트리버 = bm25s.비엠25(코퍼스=코퍼스)
리트리버.인덱스(코퍼스_토큰즈, show_progress=False)
쿼리_토큰즈 = bm25s.토크나이즈([쿼리], show_progress=False)
리절츠 = 리트리버.리트리브(쿼리_토큰즈, k=5, show_progress=False)
```

### Chroma 벡터DB

```kopy
임포트 크로마 애즈 chroma

client = chroma.클라이언트()
collection = client.크리에이트컬렉션(name="docs", embedding_function=None)
collection.애드(ids=ids, embeddings=임베딩즈, documents=다큐먼츠)
리절트 = collection.쿼리(query_embeddings=query_embeddings, n_results=2)
```

여기 남아 있는 `client`, `collection`, `query_embeddings`, 일부 키워드 인자는 다음 공통 식별자/시그니처 감사 대상입니다. `top_k` 같은 교육적 예외와 단순 미완성 항목을 구분해 문서화합니다.

## pypdf PDF ingestion

```kopy
프롬 파이피디에프 임포트 피디에프리더

리더 = 피디에프리더("document.pdf")
텍스트 = "\n".join(page.익스트랙트텍스트() or "" 포 page 인 리더.pages)
```

파일 경로와 실제 PDF 내용은 데이터이므로 음역하지 않습니다. 이미지로만 구성된 PDF는 별도 OCR 단계가 필요합니다.

## 설치

```powershell
git clone https://github.com/gpt0081/KoPy.git
cd KoPy
python -m pip install -e .
```

실제 Library Pack 의존성은 일반 Python과 동일하게 필요한 것만 설치합니다.

## CLI

```powershell
kopy run examples\hello.kpy
kopy check examples\hello.kpy
kopy translate examples\hello.kpy
kopy convert-python example.py
kopy packs
kopy packs faiss
kopy packs bm25s
kopy packs haystack-ai
kopy version
```

## 문서

- [`docs/TRANSLITERATION_STANDARD.md`](docs/TRANSLITERATION_STANDARD.md)
- [`docs/FAISS_PACK.md`](docs/FAISS_PACK.md)
- [`docs/BM25S_PACK.md`](docs/BM25S_PACK.md)
- [`docs/CHROMA_PACK.md`](docs/CHROMA_PACK.md)
- [`docs/HAYSTACK_PACK.md`](docs/HAYSTACK_PACK.md)
- 그 밖의 팩별 문서는 `docs/`에 있습니다.

## 테스트 원칙

Python 호환성이 최우선입니다. Library Pack 변경은 실제 라이브러리를 설치한 Windows, Linux, macOS CI와 runtime smoke test로 확인합니다. 문자열·주석·숫자 리터럴이 변하지 않는지, pack 고유 API와 공통 식별자가 충돌하지 않는지도 검증합니다.

0.5.47에서 공통 식별자와 숫자 보존 규칙을 확립했고, **0.5.48은 FAISS·BM25S·Chroma·Haystack의 검색/RAG 메서드를 namespace-scoped 음역으로 확장한 두 번째 감사 단계**입니다. 다음 감사에서는 공통 변수명, 키워드 인자, 나머지 팩 예제를 같은 기준으로 계속 점검합니다.
