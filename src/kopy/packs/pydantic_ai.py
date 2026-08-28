"""Pydantic AI agent framework pack for KoPy.

Only stable, top-level Pydantic AI API names are transliterated. Common
constructor and method keyword arguments intentionally remain ordinary Python
so importing this pack cannot rewrite unrelated user-defined calls.
"""

from __future__ import annotations

from .base import LibraryPack


PYDANTIC_AI_PACK = LibraryPack(
    name="pydantic-ai",
    module="pydantic_ai",
    kopy_module="파이댄틱에이아이",
    preferred_aliases=("pydantic_ai",),
    description="타입 안전한 AI 에이전트·도구 호출·구조화 출력을 위한 Pydantic AI 팩",
    members={
        "에이전트": "Agent",
        "런컨텍스트": "RunContext",
        "툴": "Tool",
        "모델리트라이": "ModelRetry",
        "유세이지리밋츠": "UsageLimits",
        "모델세팅즈": "ModelSettings",
        "에이전트런리절트": "AgentRunResult",
        "바이너리콘텐츠": "BinaryContent",
        "이미지유알엘": "ImageUrl",
        "툴아웃풋": "ToolOutput",
        "네이티브아웃풋": "NativeOutput",
        "프롬프티드아웃풋": "PromptedOutput",
        "텍스트아웃풋": "TextOutput",
        "웹서치툴": "WebSearchTool",
        "코드엑시큐션툴": "CodeExecutionTool",
        "임베더": "Embedder",
    },
    member_descriptions={
        "Agent": "모델, 도구, 지시문과 출력 타입을 묶는 Pydantic AI의 핵심 에이전트입니다.",
        "RunContext": "도구와 의존성 함수에 현재 에이전트 실행 문맥을 전달합니다.",
        "Tool": "일반 Python 함수를 에이전트 도구 정의로 감쌉니다.",
        "ModelRetry": "모델 또는 도구가 재시도해야 함을 알리는 예외입니다.",
        "UsageLimits": "요청 수와 토큰 사용량 같은 실행 한도를 정의합니다.",
        "ModelSettings": "모델 호출 설정 타입입니다.",
        "AgentRunResult": "에이전트 실행의 최종 결과와 사용량 정보를 담습니다.",
        "BinaryContent": "멀티모달 요청에 넣는 바이너리 콘텐츠입니다.",
        "ImageUrl": "URL 기반 이미지 입력을 표현합니다.",
        "ToolOutput": "도구 호출 기반 구조화 출력 설정입니다.",
        "NativeOutput": "모델 공급자의 native structured output을 사용합니다.",
        "PromptedOutput": "프롬프트 기반 구조화 출력을 사용합니다.",
        "TextOutput": "텍스트 출력 함수를 정의합니다.",
        "WebSearchTool": "지원 모델의 네이티브 웹 검색 도구입니다.",
        "CodeExecutionTool": "지원 모델의 네이티브 코드 실행 도구입니다.",
        "Embedder": "Pydantic AI의 embedding 호출 인터페이스입니다.",
    },
    examples={
        "Agent": (
            "프롬 파이댄틱에이아이 임포트 에이전트\n에이전트객체 = 에이전트('openai:gpt-5-mini', system_prompt='간결하게 답하세요')",
            "from pydantic_ai import Agent\nagent = Agent('openai:gpt-5-mini', system_prompt='간결하게 답하세요')",
        ),
        "RunContext": (
            "프롬 파이댄틱에이아이 임포트 런컨텍스트\n컨텍스트타입 = 런컨텍스트",
            "from pydantic_ai import RunContext\ncontext_type = RunContext",
        ),
        "UsageLimits": (
            "프롬 파이댄틱에이아이 임포트 유세이지리밋츠\n리밋츠 = 유세이지리밋츠(request_limit=3)",
            "from pydantic_ai import UsageLimits\nlimits = UsageLimits(request_limit=3)",
        ),
    },
)
