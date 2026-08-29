# 12. Library Pack

## 학습 목표

- Library Pack이 외부 라이브러리를 재구현하지 않는다는 점을 이해합니다.
- `LibraryPack`과 중앙 registry 구조를 읽습니다.
- import가 팩 활성화 경계가 되는 이유를 설명합니다.
- 현재 등록된 팩 전체를 코드에서 동적으로 조회합니다.

## 구조

`src/kopy/packs/base.py`의 `LibraryPack`은 다음 정보를 가집니다.

- 실제 Python 모듈명과 KoPy 모듈 음역
- 선호 별칭
- 멤버 이름 양방향 매핑
- 호출 키워드 인자 매핑
- 설명과 학습 예제

`src/kopy/packs/registry.py`가 모든 공식 팩의 단일 목록을 제공합니다. 외부 계산, 학습, 검색은 원래 라이브러리가 수행하고 KoPy는 소스 이름만 표준 Python으로 변환합니다.

## 현재 팩 영역

| 영역 | 팩 |
| --- | --- |
| 데이터·과학계산 | NumPy, pandas, Polars, SciPy |
| 전통 ML | scikit-learn, XGBoost, LightGBM, Optuna |
| 딥러닝·비전 | PyTorch, TorchVision, PyTorch Geometric, timm, Kornia, einops, JAX, Lightning, TorchMetrics, OpenCV |
| NLP·LLM | Transformers, Tokenizers, SentencePiece, Sentence Transformers, Ollama, LiteLLM, Pydantic AI, OpenAI Agents SDK |
| Hugging Face·추론 | Datasets, Accelerate, PEFT, Optimum, Safetensors, ONNX Runtime |
| 검색·DB | FAISS, USearch, sqlite-vec, Qdrant, Chroma, LanceDB, BM25S, Tantivy, RapidFuzz |
| 검색·RAG 구성과 평가 | ranx, ir-measures, Ragas, LlamaIndex Core, Haystack, LangChain Core, FastEmbed, pypdf |
| 실험·시각화 | MLflow, Matplotlib |

정확한 현재 목록은 하드코딩하지 말고 실행 시 registry에서 확인합니다.

```powershell
kopy packs
kopy packs numpy
python "학습_코스/12_라이브러리_팩/예제/pack_index.py"
```

`sample.kpy`는 NumPy가 설치되어 있으면 실행할 수 있습니다. 설치되어 있지 않아도 `kopy translate`로 변환은 확인할 수 있습니다.

```powershell
kopy translate "학습_코스/12_라이브러리_팩/예제/sample.kpy"
```

각 팩의 실제 API 설명과 실행 예제는 저장소의 `docs/*_PACK.md`와 `examples/`에 있습니다. 이 강의는 51개 외부 라이브러리 사용법을 한꺼번에 가르치지 않고, 팩의 공통 구조와 확장 방법을 가르칩니다.

## 문제

registry에서 팩 수, 정렬된 이름, 전체 멤버 수, 현재 설치된 팩 이름을 계산하세요.

```powershell
python -m unittest "학습_코스.12_라이브러리_팩.문제.test_exercise" -v
```

## 스스로 설명할 것

1. 모든 팩 멤버를 Core 전역 단어표에 넣으면 어떤 충돌이 생기는가?
2. 번역 테스트와 실제 라이브러리 런타임 테스트는 무엇이 다른가?
3. 새 팩 추가 시 registry·문서·예제·CI를 함께 갱신해야 하는 이유는 무엇인가?
