"""LangChain Core RAG/orchestration pack for KoPy.

Only LangChain-Core-specific abstractions are transliterated. Transferable RAG
and Python vocabulary such as documents, query, retriever, invoke(), batch(),
stream(), add_documents(), and similarity_search() stays Python-native.
Dotted upstream paths remain unchanged so learners see the real package layout.
"""

from __future__ import annotations

from .base import LibraryPack


LANGCHAIN_CORE_PACK = LibraryPack(
    name="langchain-core",
    module="langchain_core",
    kopy_module="랭체인코어",
    preferred_aliases=("langchain-core", "langchain_core", "langchain"),
    description="Document·Runnable·prompt·message·in-memory vector store 등 LangChain Core RAG/LLM 공통 추상화 팩",
    members={
        "도큐먼트": "Document",
        "임베딩즈": "Embeddings",
        "인메모리벡터스토어": "InMemoryVectorStore",
        "벡터스토어": "VectorStore",
        "베이스리트리버": "BaseRetriever",
        "러너블람다": "RunnableLambda",
        "러너블패스스루": "RunnablePassthrough",
        "프롬프트템플릿": "PromptTemplate",
        "챗프롬프트템플릿": "ChatPromptTemplate",
        "휴먼메시지": "HumanMessage",
        "에이아이메시지": "AIMessage",
        "시스템메시지": "SystemMessage",
        "스트링아웃풋파서": "StrOutputParser",
        "제이슨아웃풋파서": "JsonOutputParser",
        "인메모리스토어": "InMemoryStore",
        "인메모리바이트스토어": "InMemoryByteStore",
    },
    member_descriptions={
        "Document": "retrieval/RAG workflow에서 text와 metadata를 담는 LangChain Core document 객체입니다.",
        "Embeddings": "document/query text를 vector로 변환하는 provider-neutral embedding interface입니다.",
        "InMemoryVectorStore": "외부 DB 없이 cosine similarity search를 실험할 수 있는 vector store입니다.",
        "VectorStore": "vector store integration이 구현하는 공통 interface입니다.",
        "BaseRetriever": "query를 받아 Document를 반환하는 retriever 공통 추상화입니다.",
        "RunnableLambda": "Python callable을 LangChain Runnable protocol에 연결합니다.",
        "RunnablePassthrough": "입력을 그대로 전달하거나 값을 추가하는 Runnable입니다.",
        "PromptTemplate": "string prompt template을 구성합니다.",
        "ChatPromptTemplate": "role/message 기반 chat prompt를 구성합니다.",
        "HumanMessage": "사용자 역할 chat message입니다.",
        "AIMessage": "AI 역할 chat message입니다.",
        "SystemMessage": "system instruction 역할 chat message입니다.",
        "StrOutputParser": "model output을 string으로 정규화하는 output parser입니다.",
        "JsonOutputParser": "model output을 JSON-compatible object로 parsing합니다.",
        "InMemoryStore": "임시 key-value storage를 제공하는 in-memory store입니다.",
        "InMemoryByteStore": "bytes 값을 저장하는 in-memory store입니다.",
    },
    examples={
        "InMemoryVectorStore": (
            "프롬 랭체인코어.documents 임포트 도큐먼트\n프롬 랭체인코어.embeddings 임포트 임베딩즈\n프롬 랭체인코어.vectorstores 임포트 인메모리벡터스토어\nvector_store = 인메모리벡터스토어(embedding=embedding_model)\nvector_store.add_documents(documents=documents)\nresults = vector_store.similarity_search(query, k=3)",
            "from langchain_core.documents import Document\nfrom langchain_core.embeddings import Embeddings\nfrom langchain_core.vectorstores import InMemoryVectorStore\nvector_store = InMemoryVectorStore(embedding=embedding_model)\nvector_store.add_documents(documents=documents)\nresults = vector_store.similarity_search(query, k=3)",
        ),
    },
)
