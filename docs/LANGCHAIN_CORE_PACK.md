# LangChain Core Library Pack

KoPy 0.5.43의 `langchain-core` 팩은 provider에 종속되지 않는 LangChain Core의 공통 RAG/LLM 추상화를 KoPy에서 학습할 수 있게 합니다.

기준 패키지: `langchain-core>=1.6,<1.7`  
KoPy Python 범위: `>=3.12,<3.13`

## 지원 namespace

- Python module: `langchain_core`
- KoPy module: `랭체인코어`
- pack name: `langchain-core`

실제 dotted package path는 그대로 유지합니다.

```kopy
프롬 랭체인코어.documents 임포트 도큐먼트
프롬 랭체인코어.embeddings 임포트 임베딩즈
프롬 랭체인코어.vectorstores 임포트 인메모리벡터스토어
프롬 랭체인코어.runnables 임포트 러너블람다
프롬 랭체인코어.prompts 임포트 프롬프트템플릿
```

## 주요 음역

- `Document` → `도큐먼트`
- `Embeddings` → `임베딩즈`
- `InMemoryVectorStore` → `인메모리벡터스토어`
- `VectorStore` → `벡터스토어`
- `BaseRetriever` → `베이스리트리버`
- `RunnableLambda` → `러너블람다`
- `RunnablePassthrough` → `러너블패스스루`
- `PromptTemplate` → `프롬프트템플릿`
- `ChatPromptTemplate` → `챗프롬프트템플릿`
- `HumanMessage` → `휴먼메시지`
- `AIMessage` → `에이아이메시지`
- `SystemMessage` → `시스템메시지`
- `StrOutputParser` → `스트링아웃풋파서`
- `JsonOutputParser` → `제이슨아웃풋파서`

## 의도적으로 번역하지 않는 표현

다음은 LangChain Core만의 이름이 아니라 Python/RAG 전반에서 반복되는 표현이므로 원문을 유지합니다.

`documents`, `query`, `results`, `retriever`, `vector_store`, `invoke()`, `batch()`, `stream()`, `add_documents()`, `similarity_search()`, `k=`, `metadata=`, `page_content=`

특히 사용자 구현이 override하는 `embed_documents()`와 `embed_query()`도 LangChain의 실제 interface 이름 그대로 작성해야 합니다. KoPy가 framework hook 이름을 바꾸지 않습니다.

## 로컬 vector search 예제

```kopy
프롬 랭체인코어.documents 임포트 도큐먼트
프롬 랭체인코어.embeddings 임포트 임베딩즈
프롬 랭체인코어.vectorstores 임포트 인메모리벡터스토어

class DemoEmbeddings(임베딩즈):
    def embed_documents(self, texts):
        return [self.embed_query(text) for text in texts]

    def embed_query(self, text):
        lowered = text.lower()
        if "python" in lowered or "kopy" in lowered:
            return [1.0, 0.0]
        return [0.0, 1.0]

documents = [
    도큐먼트(page_content="KoPy teaches Python syntax."),
    도큐먼트(page_content="Rubber chemistry uses sulfur vulcanization."),
]

vector_store = 인메모리벡터스토어(embedding=DemoEmbeddings())
vector_store.add_documents(documents=documents)
results = vector_store.similarity_search("Python KoPy", k=1)
```

이 예제는 외부 API 키나 모델 다운로드 없이 실제 `langchain-core`의 `InMemoryVectorStore`를 사용합니다.
