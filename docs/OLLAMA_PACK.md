# Ollama Library Pack

KoPy의 Ollama Pack은 공식 `ollama` Python SDK를 namespace-scoped 방식으로 음역합니다. Ollama 자체를 다시 구현하지 않으며, KoPy 코드는 표준 Python으로 변환된 뒤 실제 `ollama` 패키지를 사용합니다.

설치:

```bash
pip install ollama
```

KoPy의 Python 호환 범위는 그대로 `>=3.12,<3.13`입니다. 현재 CI는 `ollama>=0.6.2,<0.7`을 실제 설치해 검증합니다.

## 기본 채팅

```kopy
프롬 올라마 임포트 챗

리스폰스 = 챗(
    모델="gemma3",
    메시지즈=[
        {"role": "user", "content": "KoPy를 한 문장으로 설명해줘."},
    ],
    스트림=펄스,
)

프린트(리스폰스.message.content)
```

Python에서는 다음 API와 직접 연결됩니다.

```python
from ollama import chat

response = chat(
    model="gemma3",
    messages=[
        {"role": "user", "content": "KoPy를 한 문장으로 설명해줘."},
    ],
    stream=False,
)
```

## 주요 음역

| Python | KoPy |
| --- | --- |
| `Client` | `클라이언트` |
| `AsyncClient` | `어싱크클라이언트` |
| `ChatResponse` | `챗리스폰스` |
| `GenerateResponse` | `제너레이트리스폰스` |
| `EmbedResponse` | `임베드리스폰스` |
| `Message` | `메시지` |
| `Options` | `옵션즈` |
| `ResponseError` | `리스폰스에러` |
| `chat` | `챗` |
| `generate` | `제너레이트` |
| `embed` | `임베드` |
| `pull` | `풀` |
| `show` | `쇼` |
| `ps` | `피에스` |
| `web_search` | `웹_서치` |
| `web_fetch` | `웹_페치` |

업스트림의 언더스코어 구조는 그대로 보존합니다. 예를 들어 `web_search → 웹_서치`, `keep_alive → 킵_얼라이브`입니다.

## 호출 키워드

다음 음역은 Ollama가 활성화된 코드의 **실제 함수 호출 키워드 위치에서만** 적용됩니다.

| Python keyword | KoPy |
| --- | --- |
| `model=` | `모델=` |
| `messages=` | `메시지즈=` |
| `prompt=` | `프롬프트=` |
| `stream=` | `스트림=` |
| `input=` | `인풋=` |
| `format=` | `포맷=` |
| `options=` | `옵션즈=` |
| `keep_alive=` | `킵_얼라이브=` |
| `host=` | `호스트=` |
| `headers=` | `헤더즈=` |
| `timeout=` | `타임아웃=` |

예를 들어 다음 일반 변수는 Ollama Pack 때문에 전역 변환되지 않습니다.

```kopy
메시지즈 = []
킵_얼라이브 = "10m"
```

반면 Ollama 호출 안에서는:

```kopy
리스폰스 = 챗(메시지즈=메시지즈, 킵_얼라이브=킵_얼라이브)
```

표준 Python의 `chat(messages=messages, keep_alive=keep_alive)`로 변환됩니다.

## 로컬 서버와 테스트 범위

실제 채팅·생성·embedding에는 실행 중인 Ollama 서버와 모델이 필요합니다. KoPy CI에서는 외부 모델 다운로드나 서버 실행에 의존하지 않도록 공식 `ollama` 패키지를 설치한 뒤 `Client`, `Message`, `Options`를 실제 생성하고 top-level API가 존재하는지 검증합니다. 따라서 SDK 호환성은 실라이브러리로 확인하되 네트워크와 모델 상태 때문에 CI가 흔들리지 않게 구성합니다.
