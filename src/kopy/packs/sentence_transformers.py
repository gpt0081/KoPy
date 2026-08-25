"""Official Sentence Transformers library pack for KoPy.

The pack focuses on public top-level model classes and instance APIs. Dotted
submodules such as ``sentence_transformers.models`` and ``sentence_transformers.util``
remain upstream Python paths because Sentence Transformers 6.x does not expose
those modules as attributes on ``import sentence_transformers as st``.
"""

from __future__ import annotations

from .base import LibraryPack


SENTENCE_TRANSFORMERS_PACK = LibraryPack(
    name="sentence-transformers",
    module="sentence_transformers",
    kopy_module="센텐스트랜스포머스",
    preferred_aliases=("sentence-transformers", "sentence_transformers", "sbert", "st"),
    description="문장 임베딩·유사도·CrossEncoder·SparseEncoder를 위한 Sentence Transformers API 팩",
    members={
        "센텐스트랜스포머": "SentenceTransformer",
        "크로스인코더": "CrossEncoder",
        "스파스인코더": "SparseEncoder",
        "멀티벡터인코더": "MultiVectorEncoder",
        "시밀래리티펑션": "SimilarityFunction",
        "트레이닝아규먼츠": "SentenceTransformerTrainingArguments",
        "트레이너": "SentenceTransformerTrainer",
        "인코드": "encode",
        "인코드쿼리": "encode_query",
        "인코드도큐먼트": "encode_document",
        "시밀래리티": "similarity",
        "겟센텐스임베딩디멘션": "get_sentence_embedding_dimension",
        "겟맥스시퀀스렝스": "get_max_seq_length",
        "세이브": "save",
        "세이브프리트레인드": "save_pretrained",
    },
    member_descriptions={
        "SentenceTransformer": "문장·문서·쿼리를 dense embedding으로 변환하는 기본 모델 클래스입니다.",
        "CrossEncoder": "문장 쌍을 함께 입력해 점수나 라벨을 예측하는 cross-encoder 클래스입니다.",
        "SparseEncoder": "희소 임베딩을 생성하는 sparse encoder 클래스입니다.",
        "MultiVectorEncoder": "ColBERT 계열처럼 입력 하나를 여러 벡터로 표현하는 encoder 클래스입니다.",
        "SimilarityFunction": "cosine, dot, euclidean 등 similarity 방식을 나타내는 공개 enum입니다.",
        "encode": "텍스트를 embedding으로 변환합니다.",
        "encode_query": "비대칭 검색에서 query용 embedding을 생성합니다.",
        "encode_document": "비대칭 검색에서 corpus 문서용 embedding을 생성합니다.",
        "similarity": "SentenceTransformer가 생성한 embedding 사이의 similarity를 계산합니다.",
    },
    examples={
        "SentenceTransformer": (
            "프롬 센텐스트랜스포머스 임포트 센텐스트랜스포머\nmodel = 센텐스트랜스포머(\"sentence-transformers/all-MiniLM-L6-v2\")",
            "from sentence_transformers import SentenceTransformer\nmodel = SentenceTransformer(\"sentence-transformers/all-MiniLM-L6-v2\")",
        ),
        "similarity": (
            "scores = model.시밀래리티(query_embeddings, corpus_embeddings)",
            "scores = model.similarity(query_embeddings, corpus_embeddings)",
        ),
    },
)
