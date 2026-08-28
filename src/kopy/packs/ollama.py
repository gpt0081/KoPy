"""Official Ollama Python client pack for KoPy.

Ollama is a practical bridge between Python applications and locally or
remotely served open models. This pack keeps the real ``ollama`` module and
string/data values intact while transliterating only Ollama API names inside
an activated Ollama namespace.
"""

from __future__ import annotations

from .base import LibraryPack


OLLAMA_PACK = LibraryPack(
    name="ollama",
    module="ollama",
    kopy_module="올라마",
    preferred_aliases=("ollama",),
    description="로컬·원격 Ollama 모델의 chat, generate, embedding과 client API를 위한 공식 Python SDK 팩",
    members={
        "클라이언트": "Client",
        "어싱크클라이언트": "AsyncClient",
        "챗리스폰스": "ChatResponse",
        "제너레이트리스폰스": "GenerateResponse",
        "임베드리스폰스": "EmbedResponse",
        "메시지": "Message",
        "옵션즈": "Options",
        "리스폰스에러": "ResponseError",
        "챗": "chat",
        "제너레이트": "generate",
        "임베드": "embed",
        "풀": "pull",
        "푸시": "push",
        "쇼": "show",
        "크리에이트": "create",
        "카피": "copy",
        "딜리트": "delete",
        "피에스": "ps",
        "웹_서치": "web_search",
        "웹_페치": "web_fetch",
    },
    member_descriptions={
        "Client": "Ollama 서버와 통신하는 동기 클라이언트를 생성합니다.",
        "AsyncClient": "asyncio에서 사용하는 비동기 Ollama 클라이언트를 생성합니다.",
        "ChatResponse": "chat 호출의 구조화된 응답 타입입니다.",
        "GenerateResponse": "generate 호출의 구조화된 응답 타입입니다.",
        "EmbedResponse": "embed 호출의 embedding 응답 타입입니다.",
        "Message": "role/content 등을 갖는 Ollama 대화 메시지 타입입니다.",
        "Options": "temperature 등 모델 실행 옵션을 표현하는 타입입니다.",
        "ResponseError": "Ollama API 오류 응답 예외 타입입니다.",
        "chat": "messages 기반 채팅 응답을 생성합니다.",
        "generate": "prompt 기반 텍스트 응답을 생성합니다.",
        "embed": "텍스트 하나 또는 배치의 embedding을 생성합니다.",
        "pull": "Ollama 모델을 내려받습니다.",
        "push": "Ollama 모델을 원격 저장소로 업로드합니다.",
        "show": "모델 정보와 Modelfile 정보를 조회합니다.",
        "create": "기존 모델/Modelfile을 바탕으로 모델을 생성합니다.",
        "copy": "모델을 다른 이름으로 복사합니다.",
        "delete": "로컬 Ollama 모델을 삭제합니다.",
        "ps": "현재 메모리에 올라온 모델을 조회합니다.",
        "web_search": "Ollama web search API를 호출합니다.",
        "web_fetch": "Ollama web fetch API를 호출합니다.",
    },
    examples={
        "chat": (
            "프롬 올라마 임포트 챗\n리스폰스 = 챗(model='gemma3', messages=[{'role': 'user', 'content': '안녕'}])",
            "from ollama import chat\nresponse = chat(model='gemma3', messages=[{'role': 'user', 'content': '안녕'}])",
        ),
        "Client": (
            "프롬 올라마 임포트 클라이언트\n클라이언트객체 = 클라이언트(host='http://localhost:11434')",
            "from ollama import Client\nclient = Client(host='http://localhost:11434')",
        ),
        "embed": (
            "프롬 올라마 임포트 임베드\n리스폰스 = 임베드(model='embeddinggemma', input='KoPy')",
            "from ollama import embed\nresponse = embed(model='embeddinggemma', input='KoPy')",
        ),
    },
)
