"""Official Sentence Transformers library pack for KoPy.

The pack focuses on embedding, similarity and semantic-search APIs while keeping
model identifiers, tensor variable conventions and broadly shared keyword
arguments in upstream Python form. All translations remain namespace-scoped.
"""

from __future__ import annotations

from .base import LibraryPack


SENTENCE_TRANSFORMERS_PACK = LibraryPack(
    name="sentence-transformers",
    module="sentence_transformers",
    kopy_module="센텐스트랜스포머스",
    preferred_aliases=("sentence-transformers", "sentence_transformers", "sbert", "st"),
    description="문장 임베딩·유사도·semantic search·CrossEncoder를 위한 Sentence Transformers API 팩",
    members={
        "센텐스트랜스포머": "SentenceTransformer",
        "크로스인코더": "CrossEncoder",
        "스파스인코더": "SparseEncoder",
        "모델즈": "models",
        "유틸": "util",
        "로시즈": "losses",
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
        "보우": "BoW",
        "덴스": "Dense",
        "풀링": "Pooling",
        "노멀라이즈": "Normalize",
        "코사인심": "cos_sim",
        "닷스코어": "dot_score",
        "페어와이즈코사인심": "pairwise_cos_sim",
        "유클리디언심": "euclidean_sim",
        "맨해튼심": "manhattan_sim",
        "시맨틱서치": "semantic_search",
        "패러프레이즈마이닝": "paraphrase_mining",
        "노멀라이즈임베딩스": "normalize_embeddings",
        "트렁케이트임베딩스": "truncate_embeddings",
        "커뮤니티디텍션": "community_detection",
    },
    member_descriptions={
        "SentenceTransformer": "문장·문서·쿼리를 dense embedding으로 변환하는 기본 모델 클래스입니다.",
        "CrossEncoder": "문장 쌍을 함께 입력해 점수나 라벨을 예측하는 cross-encoder 클래스입니다.",
        "SparseEncoder": "희소 임베딩을 생성하는 sparse encoder 클래스입니다.",
        "encode": "텍스트를 embedding으로 변환합니다.",
        "encode_query": "비대칭 검색에서 query용 embedding을 생성합니다.",
        "encode_document": "비대칭 검색에서 corpus 문서용 embedding을 생성합니다.",
        "cos_sim": "두 embedding 집합의 cosine similarity 행렬을 계산합니다.",
        "semantic_search": "query와 corpus embedding 사이의 상위 유사 항목을 찾습니다.",
        "BoW": "외부 pretrained 모델 없이도 구성 가능한 Bag-of-Words embedding 모듈입니다.",
    },
    examples={
        "SentenceTransformer": (
            "프롬 센텐스트랜스포머스 임포트 센텐스트랜스포머\nmodel = 센텐스트랜스포머(\"sentence-transformers/all-MiniLM-L6-v2\")",
            "from sentence_transformers import SentenceTransformer\nmodel = SentenceTransformer(\"sentence-transformers/all-MiniLM-L6-v2\")",
        ),
        "cos_sim": (
            "임포트 센텐스트랜스포머스 애즈 st\nscores = st.유틸.코사인심(query_embeddings, corpus_embeddings)",
            "import sentence_transformers as st\nscores = st.util.cos_sim(query_embeddings, corpus_embeddings)",
        ),
        "semantic_search": (
            "hits = st.유틸.시맨틱서치(query_embeddings, corpus_embeddings, top_k=5)",
            "hits = st.util.semantic_search(query_embeddings, corpus_embeddings, top_k=5)",
        ),
    },
)
