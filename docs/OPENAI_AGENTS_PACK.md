# OpenAI Agents Library Pack

KoPy의 OpenAI Agents 팩은 `openai-agents` 패키지의 공개 `agents` 네임스페이스를 한국어 음역으로 학습할 수 있게 합니다. 라이브러리를 다시 구현하지 않으며, KoPy 코드를 표준 Python으로 변환한 뒤 실제 실행은 OpenAI Agents SDK가 담당합니다.

## 설치

```bash
python -m pip install "openai-agents==0.22.0"
```

KoPy의 개발 기준 Python 3.12 계열과 호환됩니다. OpenAI Agents 0.22.0은 Python 3.10 이상을 지원합니다.

## 주요 음역

| KoPy | Python |
| --- | --- |
| `에이전트` | `Agent` |
| `러너` | `Runner` |
| `런컨피그` | `RunConfig` |
| `런컨텍스트래퍼` | `RunContextWrapper` |
| `런리절트` | `RunResult` |
| `런스테이트` | `RunState` |
| `펑션_툴` | `function_tool` |
| `핸드오프` | `Handoff` |
| `핸드오프_만들기` | `handoff` |
| `인풋_가드레일` | `input_guardrail` |
| `아웃풋_가드레일` | `output_guardrail` |
| `에스큐라이트세션` | `SQLiteSession` |
| `트레이스` | `trace` |

## 예제

```python
프롬 에이전츠 임포트 에이전트, 러너

도우미 = 에이전트(
    name="Assistant",
    instructions="간결하게 답하세요",
)

# 실제 모델 호출에는 OPENAI_API_KEY가 필요합니다.
# 결과 = 러너.run_sync(도우미, "KoPy를 한 문장으로 설명해줘")
```

변환 후 핵심 부분은 다음과 같습니다.

```python
from agents import Agent, Runner

도우미 = Agent(
    name="Assistant",
    instructions="간결하게 답하세요",
)
```

## 왜 keyword argument는 번역하지 않나

`name=`, `instructions=`, `tools=`, `model=`, `max_turns=` 같은 이름은 Agents SDK 밖에서도 매우 흔합니다. 파일에 `agents` import가 있다는 이유만으로 이런 키워드를 전역 변환하면 사용자 함수나 다른 라이브러리 호출을 망가뜨릴 수 있습니다.

따라서 이 팩의 `keyword_arguments`는 비어 있습니다. SDK 고유 타입과 함수 이름만 네임스페이스 범위에서 음역하고, 호출 인자는 원래 Python 표기를 유지합니다. 이는 KoPy 학습 코드가 원문 Python 관례도 함께 익히게 한다는 방향과도 맞습니다.

## 테스트

전용 CI는 Windows, Ubuntu, macOS에서 Python 3.12.10과 실제 `openai-agents==0.22.0`을 설치합니다. 네임스페이스 변환, 역변환, 범용 키워드 비오염, 실제 `Agent`/`RunConfig` 객체 생성까지 검증하며 네트워크 모델 호출은 하지 않습니다.
