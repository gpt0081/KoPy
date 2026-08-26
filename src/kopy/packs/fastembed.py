"""Official FastEmbed embedding and reranking pack for KoPy.

The pack transliterates FastEmbed-specific class names while preserving
transferable retrieval vocabulary such as ``model_name``, ``documents``,
``query``, ``scores``, ``embed()``, and ``rerank()`` in upstream Python form.
Dotted submodule paths such as ``fastembed.rerank.cross_encoder`` remain
Python-native so KoPy learners keep seeing the real package structure.
"""

from __future__ import annotations

from .base import LibraryPack


FASTEMBED_PACK = LibraryPack(
    name="fastembed",
    module="fastembed",
    kopy_module="패스트임베드",
    preferred_aliases=("fastembed", "fe"),
    description="ONNX 기반 text/sparse/late-interaction embedding과 cross-encoder reranking을 위한 FastEmbed API 팩",
    members={
        "텍스트임베딩": "TextEmbedding",
        "스파스텍스트임베딩": "SparseTextEmbedding",
        "레이트인터랙션텍스트임베딩": "LateInteractionTextEmbedding",
        "이미지임베딩": "ImageEmbedding",
        "텍스트크로스인코더": "TextCrossEncoder",
    },
    member_descriptions={
        "TextEmbedding": "검색용 dense text embedding을 ONNX Runtime으로 생성합니다.",
        "SparseTextEmbedding": "sparse retrieval에 사용할 sparse text embedding을 생성합니다.",
        "LateInteractionTextEmbedding": "ColBERT 계열 late-interaction text embedding을 생성합니다.",
        "ImageEmbedding": "지원되는 vision 모델로 image embedding을 생성합니다.",
        "TextCrossEncoder": "query-document 쌍을 cross-encoder로 점수화해 reranking합니다.",
    },
    examples={
        "TextEmbedding": (
            "프롬 패스트임베드 임포트 텍스트임베딩\nmodel = 텍스트임베딩(model_name='BAAI/bge-small-en-v1.5')\nembeddings = list(model.embed(documents))",
            "from fastembed import TextEmbedding\nmodel = TextEmbedding(model_name='BAAI/bge-small-en-v1.5')\nembeddings = list(model.embed(documents))",
        ),
        "TextCrossEncoder": (
            "프롬 패스트임베드.rerank.cross_encoder 임포트 텍스트크로스인코더\nreranker = 텍스트크로스인코더(model_name='Xenova/ms-marco-MiniLM-L-6-v2')\nscores = list(reranker.rerank(query, documents))",
            "from fastembed.rerank.cross_encoder import TextCrossEncoder\nreranker = TextCrossEncoder(model_name='Xenova/ms-marco-MiniLM-L-6-v2')\nscores = list(reranker.rerank(query, documents))",
        ),
    },
)
