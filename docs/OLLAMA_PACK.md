# Ollama Library Pack

KoPy의 Ollama Pack은 공식 `ollama` Python SDK를 namespace-scoped 방식으로 음역합니다. Ollama 자체를 다시 구현하지 않으며, KoPy 코드는 표준 Python으로 변환된 뒤 실제 `ollama` 패키지를 사용합니다.

설치:

```bash
pip install ollama
```

KoPy의 Python 호환 범위는 그대로 `>=3.12,<3.13`입니다. 현재 CI는 `ollama==0.6.2`를 실제 설치해 검증합니다.

## 기본 채팅

```kopy
프롬 올라마 임포트 챗

리스폰스 = 챗(
    모델="gemma3",
    messages=[
        {"role": "user", "content": "KoPy를 한 문장으로 설명해줘."},
    ],
    stream=펄스,
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
| `push` | `푸시` |
| `show` | `쇼` |
| `create` | `크리에이트` |
| `copy` | `카피` |
| `delete` | `딜리트` |
| `ps` | `피에스` |
| `web_search` | `웹_서치` |
| `web_fetch` | `웹_페치` |

업스트림의 언더스코어 구조는 그대로 보존합니다. 예를 들어 `web_search → 웹_서치`입니다.

## 호출 키워드와 충돌 회피

Ollama Pack 자체의 `keyword_arguments`는 현재 비워 둡니다. `messages=`, `prompt=`, `stream=`, `input=`, `format=`, `options=`, `keep_alive=`, `host=`, `headers=`, `timeout=` 같은 이름을 팩 단위로 등록하면, Ollama import가 있는 같은 파일의 사용자 정의 함수 호출까지 잘못 바꿀 수 있기 때문입니다.

단, `model → 모델`은 Ollama 전용 키워드가 아니라 KoPy가 이미 공통 식별자로 지원하는 canonical 음역입니다. 따라서 Python→KoPy 변환에서는 `model=`이 `모델=`로 표시되고, KoPy→Python에서는 `모델=`이 표준 `model=`로 복원됩니다. 이는 Ollama Pack 전용 전역 번역을 새로 추가한 것이 아닙니다.

따라서 다음 코드는 안전하게 처리됩니다.

```kopy
프롬 올라마 임포트 챗

def 재시도(타임아웃):
    리턴 타임아웃

재시도(타임아웃=1)
리스폰스 = 챗(모델="gemma3", messages=[])
```

`타임아웃=`은 사용자 함수 호출에서 그대로 유지되고, `모델=`은 기존 KoPy 공통 식별자 규칙에 따라 `model=`로 복원됩니다. Ollama 전용 호출 대상을 정확히 식별하는 call-target scoping이 구현되기 전에는 추가 호출 키워드를 팩 전용 음역으로 등록하지 않습니다.

## 로컬 서버와 테스트 범위

실제 채팅·생성·embedding에는 실행 중인 Ollama 서버와 모델이 필요합니다. KoPy CI에서는 외부 모델 다운로드나 서버 실행에 의존하지 않도록 공식 `ollama` 패키지를 설치한 뒤 `Client`, `Message`, `Options`를 실제 생성하고 top-level API가 존재하는지 검증합니다. 따라서 SDK 호환성은 실라이브러리로 확인하되 네트워크와 모델 상태 때문에 CI가 흔들리지 않게 구성합니다.
