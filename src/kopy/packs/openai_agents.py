"""OpenAI Agents SDK pack for KoPy.

Only stable top-level SDK API names are transliterated. Common constructor and
method keyword arguments intentionally remain ordinary Python so importing this
pack cannot rewrite unrelated user-defined calls.
"""

from __future__ import annotations

from .base import LibraryPack


OPENAI_AGENTS_PACK = LibraryPack(
    name="openai-agents",
    module="agents",
    kopy_module="에이전츠",
    preferred_aliases=("agents",),
    description="에이전트 실행·도구·핸드오프·가드레일을 위한 OpenAI Agents SDK 팩",
    members={
        "에이전트": "Agent",
        "러너": "Runner",
        "런컨피그": "RunConfig",
        "런컨텍스트래퍼": "RunContextWrapper",
        "런리절트": "RunResult",
        "런리절트스트리밍": "RunResultStreaming",
        "런스테이트": "RunState",
        "모델세팅즈": "ModelSettings",
        "펑션툴": "FunctionTool",
        "펑션_툴": "function_tool",
        "핸드오프": "Handoff",
        "핸드오프_만들기": "handoff",
        "인풋가드레일": "InputGuardrail",
        "아웃풋가드레일": "OutputGuardrail",
        "인풋_가드레일": "input_guardrail",
        "아웃풋_가드레일": "output_guardrail",
        "런훅스": "RunHooks",
        "에이전트훅스": "AgentHooks",
        "에스큐라이트세션": "SQLiteSession",
        "트레이스": "trace",
    },
    keyword_arguments={},
    member_descriptions={
        "Agent": "지시문, 모델, 도구, 핸드오프를 묶는 Agents SDK 핵심 에이전트입니다.",
        "Runner": "에이전트를 동기·비동기·스트리밍 방식으로 실행합니다.",
        "RunConfig": "한 번의 실행에 적용할 모델·도구·추적 설정을 정의합니다.",
        "RunContextWrapper": "도구와 훅에 실행 문맥과 사용량 상태를 전달합니다.",
        "RunResult": "완료된 에이전트 실행 결과를 담습니다.",
        "RunResultStreaming": "스트리밍 실행 결과와 이벤트를 제공합니다.",
        "RunState": "중단된 실행을 저장하고 승인 후 재개할 때 사용합니다.",
        "ModelSettings": "모델 호출 파라미터를 정의합니다.",
        "FunctionTool": "Python 함수를 에이전트 도구로 표현합니다.",
        "function_tool": "Python 함수를 FunctionTool로 감싸는 데코레이터입니다.",
        "Handoff": "한 에이전트에서 다른 에이전트로의 위임을 표현합니다.",
        "handoff": "핸드오프 정의를 만드는 도우미입니다.",
        "InputGuardrail": "에이전트 입력에 적용되는 가드레일 타입입니다.",
        "OutputGuardrail": "에이전트 출력에 적용되는 가드레일 타입입니다.",
        "input_guardrail": "입력 가드레일 함수를 등록하는 데코레이터입니다.",
        "output_guardrail": "출력 가드레일 함수를 등록하는 데코레이터입니다.",
        "RunHooks": "전체 실행 수명주기 훅의 기본 타입입니다.",
        "AgentHooks": "개별 에이전트 수명주기 훅의 기본 타입입니다.",
        "SQLiteSession": "SQLite 기반 대화 세션 저장소입니다.",
        "trace": "에이전트 워크플로 추적 범위를 만드는 컨텍스트 도우미입니다.",
    },
    examples={
        "Agent": (
            "프롬 에이전츠 임포트 에이전트, 러너\n도우미 = 에이전트(name='Assistant', instructions='간결하게 답하세요')",
            "from agents import Agent, Runner\nassistant = Agent(name='Assistant', instructions='간결하게 답하세요')",
        ),
        "RunConfig": (
            "프롬 에이전츠 임포트 런컨피그\n설정 = 런컨피그()",
            "from agents import RunConfig\nconfig = RunConfig()",
        ),
    },
)
