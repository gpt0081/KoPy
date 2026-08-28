# Pydantic AI Library Pack

KoPy의 Pydantic AI 팩은 `pydantic_ai`의 안정적인 최상위 API 이름을 한글 음역으로 사용할 수 있게 합니다. 실제 에이전트 실행과 모델 호출은 원본 Pydantic AI 라이브러리가 담당합니다.

기준 라이브러리: `pydantic-ai==2.35.1`  
KoPy Python 기준: `3.12.10`

## 핵심 음역

| Python | KoPy |
| --- | --- |
| `pydantic_ai` | `파이댄틱에이아이` |
| `Agent` | `에이전트` |
| `RunContext` | `런컨텍스트` |
| `Tool` | `툴` |
| `ModelRetry` | `모델리트라이` |
| `UsageLimits` | `유세이지리밋츠` |
| `AgentRunResult` | `에이전트런리절트` |
| `ToolOutput` | `툴아웃풋` |
| `NativeOutput` | `네이티브아웃풋` |
| `PromptedOutput` | `프롬프티드아웃풋` |
| `TextOutput` | `텍스트아웃풋` |
| `WebSearchTool` | `웹서치툴` |
| `CodeExecutionTool` | `코드엑시큐션툴` |
| `Embedder` | `임베더` |

## 예시

```kopy
프롬 파이댄틱에이아이 임포트 에이전트, 유세이지리밋츠

에이전트객체 = 에이전트(
    'openai:gpt-5-mini',
    system_prompt='간결하게 답하세요',
)
리밋츠 = 유세이지리밋츠(request_limit=3)
```

표준 Python으로 변환하면 다음 의미가 됩니다.

```python
from pydantic_ai import Agent, UsageLimits

agent = Agent(
    'openai:gpt-5-mini',
    system_prompt='간결하게 답하세요',
)
limits = UsageLimits(request_limit=3)
```

## 범용 keyword argument를 음역하지 않는 이유

`system_prompt=`, `deps_type=`, `output_type=`, `request_limit=` 같은 이름은 Pydantic AI 밖의 사용자 함수나 다른 라이브러리에서도 충분히 등장할 수 있습니다. 현재 Library Pack의 keyword-argument scoping은 import된 라이브러리 단위이므로, 이를 팩 전역 번역으로 등록하면 같은 파일의 무관한 함수 호출을 잘못 바꿀 수 있습니다.

따라서 이 팩은 현재 `keyword_arguments={}`를 유지합니다. API 클래스와 함수 이름은 namespace-scoped 음역을 제공하되, 호출 인자는 실제 Python 이름을 함께 익히도록 원문을 유지합니다.

## 런타임 검증

전용 CI는 Windows, Ubuntu, macOS의 Python 3.12.10에서 실제 `pydantic-ai==2.35.1`을 설치합니다. 공급자 API 키나 네트워크 모델 호출 없이 공식 top-level export와 `UsageLimits` 객체 생성, KoPy 변환 후 실제 import 실행을 검증합니다.
