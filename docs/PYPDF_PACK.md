# pypdf Library Pack

KoPy 0.5.46의 `pypdf` 팩은 PDF 문서를 읽고 텍스트를 추출해 RAG ingestion 단계로 넘기는 기본 흐름을 지원합니다.

기준 라이브러리: `pypdf 6.16.1`  
KoPy 기준 Python: `3.12.10`

## 설치

```bash
python -m pip install "pypdf>=6.16.1,<6.17"
```

## 기본 예제

```kopy
프롬 파이피디에프 임포트 피디에프리더

reader = 피디에프리더("document.pdf")
text = "\n".join(
    page.익스트랙트텍스트() or ""
    포 page 인 reader.pages
)
```

위 코드는 표준 Python의 다음 코드로 변환됩니다.

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")
text = "\n".join(
    page.extract_text() or ""
    for page in reader.pages
)
```

## 지원 범위

주요 음역 API는 다음과 같습니다.

- `PdfReader` → `피디에프리더`
- `PdfWriter` → `피디에프라이터`
- `PageObject` → `페이지오브젝트`
- `Transformation` → `트랜스포메이션`
- `extract_text()` → `익스트랙트텍스트()`
- `add_blank_page()` → `애드블랭크페이지()`
- `add_metadata()` → `애드메타데이터()`
- `add_page()` → `애드페이지()`
- `insert_blank_page()` → `인서트블랭크페이지()`
- `clone_document_from_reader()` → `클론도큐먼트프롬리더()`
- `append_pages_from_reader()` → `어펜드페이지즈프롬리더()`

## 원문으로 유지하는 표현

`reader`, `writer`, `document`, `pages`, `text`, `metadata`, `path`, `stream`, `write()` 같은 표현은 번역하지 않습니다. 이런 이름은 pypdf만의 고유 API가 아니라 Python 문서 처리와 RAG ingestion 코드 전반에서 반복되는 표현이기 때문입니다.

PDF 내부 텍스트, 파일 경로, metadata key/value, PDF content stream 역시 KoPy 번역 대상이 아닙니다.

## RAG에서의 위치

```text
PDF
 ↓
pypdf
 ↓
page text
 ↓
chunking
 ↓
Sentence Transformers / FastEmbed
 ↓
FAISS / Qdrant / Chroma / LanceDB / sqlite-vec
```

pypdf는 OCR 엔진이 아닙니다. 이미지로만 구성된 스캔 PDF에는 별도의 OCR 단계가 필요합니다.

## CLI

```bash
kopy packs pypdf
kopy packs pypdf --json
```
