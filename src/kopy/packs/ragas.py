"""Official Ragas evaluation pack for KoPy.

The pack transliterates Ragas-specific dataset and metric entry points while
preserving transferable RAG/evaluation vocabulary such as ``user_input``,
``response``, ``reference``, ``retrieved_contexts``, ``score()``, ``ascore()``,
and ``evaluate()`` in upstream Python form. Dotted package paths such as
``ragas.metrics.collections`` remain Python-native so learners keep seeing the
real package structure.
"""

from __future__ import annotations

from .base import LibraryPack


RAGAS_PACK = LibraryPack(
    name="ragas",
    module="ragas",
    kopy_module="라가스",
    preferred_aliases=("ragas",),
    description="RAG/LLM 응답·검색 문맥을 dataset과 deterministic/LLM metric으로 평가하는 Ragas API 팩",
    members={
        "이밸류에이션데이터셋": "EvaluationDataset",
        "싱글턴샘플": "SingleTurnSample",
        "멀티턴샘플": "MultiTurnSample",
        "논엘엘엠스트링시밀래리티": "NonLLMStringSimilarity",
        "디스턴스메저": "DistanceMeasure",
        "이그잭트매치": "ExactMatch",
        "스트링프레즌스": "StringPresence",
        "컨텍스트프리시전": "ContextPrecision",
        "컨텍스트리콜": "ContextRecall",
        "페이스풀니스": "Faithfulness",
        "리스폰스그라운디드니스": "ResponseGroundedness",
        "팩추얼코렉트니스": "FactualCorrectness",
        "시맨틱시밀래리티": "SemanticSimilarity",
    },
    member_descriptions={
        "EvaluationDataset": "RAG/LLM 평가 샘플을 묶는 Ragas evaluation dataset입니다.",
        "SingleTurnSample": "질문·응답·reference·retrieved contexts를 담는 단일 턴 평가 샘플입니다.",
        "MultiTurnSample": "여러 메시지로 구성된 대화형 평가 샘플입니다.",
        "NonLLMStringSimilarity": "LLM 없이 문자열 거리 기반으로 response와 reference 유사도를 계산합니다.",
        "DistanceMeasure": "Levenshtein, Hamming, Jaro 등 문자열 거리 방식을 선택합니다.",
        "ExactMatch": "reference와 response의 정확 일치 여부를 평가하는 deterministic metric입니다.",
        "StringPresence": "reference 문자열 존재 여부를 평가하는 deterministic metric입니다.",
        "ContextPrecision": "retrieved contexts의 정밀도를 평가하는 RAG metric입니다.",
        "ContextRecall": "retrieved contexts가 reference 정보를 얼마나 회수했는지 평가합니다.",
        "Faithfulness": "생성 응답이 제공된 context에 근거하는지 평가합니다.",
        "ResponseGroundedness": "응답의 주장들이 retrieved context에 근거하는지 평가합니다.",
        "FactualCorrectness": "응답의 사실적 정확성을 평가합니다.",
        "SemanticSimilarity": "response와 reference의 의미 유사도를 평가합니다.",
    },
    examples={
        "EvaluationDataset": (
            "프롬 라가스 임포트 이밸류에이션데이터셋, 싱글턴샘플\nsample = 싱글턴샘플(user_input=query, response=response, reference=reference, retrieved_contexts=contexts)\ndataset = 이밸류에이션데이터셋(samples=[sample])",
            "from ragas import EvaluationDataset, SingleTurnSample\nsample = SingleTurnSample(user_input=query, response=response, reference=reference, retrieved_contexts=contexts)\ndataset = EvaluationDataset(samples=[sample])",
        ),
        "NonLLMStringSimilarity": (
            "프롬 라가스.metrics.collections 임포트 논엘엘엠스트링시밀래리티, 디스턴스메저\nmetric = 논엘엘엠스트링시밀래리티(distance_measure=디스턴스메저.LEVENSHTEIN)\nresult = metric.score(reference=reference, response=response)",
            "from ragas.metrics.collections import NonLLMStringSimilarity, DistanceMeasure\nmetric = NonLLMStringSimilarity(distance_measure=DistanceMeasure.LEVENSHTEIN)\nresult = metric.score(reference=reference, response=response)",
        ),
    },
)
