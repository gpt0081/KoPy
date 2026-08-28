"""LiteLLM Python SDK pack for KoPy.

LiteLLM provides one Python calling surface across many LLM providers. This
pack transliterates stable LiteLLM API names only when the LiteLLM namespace
is active. Provider names, model IDs, message payloads and keyword arguments
remain ordinary Python/data so importing LiteLLM cannot rewrite unrelated
user calls.
"""

from __future__ import annotations

from .base import LibraryPack


LITELLM_PACK = LibraryPack(
    name="litellm",
    module="litellm",
    kopy_module="라이트엘엘엠",
    preferred_aliases=("litellm",),
    description="여러 LLM 공급자를 하나의 completion·embedding 호출면으로 다루는 LiteLLM Python SDK 팩",
    members={
        "컴플리션": "completion",
        "에이컴플리션": "acompletion",
        "임베딩": "embedding",
        "에이임베딩": "aembedding",
        "이미지_제너레이션": "image_generation",
        "에이이미지_제너레이션": "aimage_generation",
        "트랜스크립션": "transcription",
        "에이트랜스크립션": "atranscription",
        "라우터": "Router",
        "모델리스폰스": "ModelResponse",
    },
    member_descriptions={
        "completion": "OpenAI 호환 형태로 여러 공급자의 채팅/텍스트 completion을 호출합니다.",
        "acompletion": "비동기 completion 호출입니다.",
        "embedding": "지원 공급자의 embedding API를 같은 호출면으로 사용합니다.",
        "aembedding": "비동기 embedding 호출입니다.",
        "image_generation": "지원 공급자의 이미지 생성 API를 호출합니다.",
        "aimage_generation": "비동기 이미지 생성 호출입니다.",
        "transcription": "지원 공급자의 음성 전사 API를 호출합니다.",
        "atranscription": "비동기 음성 전사 호출입니다.",
        "Router": "여러 모델 배포 사이의 routing, retry, fallback을 관리합니다.",
        "ModelResponse": "LiteLLM completion 응답의 구조화된 타입입니다.",
    },
    examples={
        "completion": (
            "프롬 라이트엘엘엠 임포트 컴플리션\n리스폰스 = 컴플리션(모델='openai/gpt-5-mini', messages=[{'role': 'user', 'content': '안녕'}])",
            "from litellm import completion\nresponse = completion(model='openai/gpt-5-mini', messages=[{'role': 'user', 'content': '안녕'}])",
        ),
        "embedding": (
            "프롬 라이트엘엘엠 임포트 임베딩\n리스폰스 = 임베딩(모델='text-embedding-3-small', input=['KoPy'])",
            "from litellm import embedding\nresponse = embedding(model='text-embedding-3-small', input=['KoPy'])",
        ),
        "Router": (
            "프롬 라이트엘엘엠 임포트 라우터\n라우터객체 = 라우터(model_list=[])",
            "from litellm import Router\nrouter = Router(model_list=[])",
        ),
    },
)
