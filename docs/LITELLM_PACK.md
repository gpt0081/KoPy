# LiteLLM Library Pack

KoPy의 LiteLLM 팩은 실제 `litellm` Python 패키지를 다시 구현하지 않습니다. LiteLLM API 이름을 한글 음역으로 작성하면 KoPy가 표준 Python으로 되돌리고, 실제 LLM 호출·라우팅은 LiteLLM이 수행합니다.

## 설치

```bash
python -m pip install litellm
```

KoPy의 현재 개발 기준 Python 3.12.10은 LiteLLM 1.98.0의 Python 요구사항(`>=3.10,<3.15`) 안에 들어갑니다.

## 주요 음역

| Python | KoPy |
| --- | --- |
| `litellm` | `라이트엘엘엠` |
| `completion` | `컴플리션` |
| `acompletion` | `에이컴플리션` |
| `embedding` | `임베딩` |
| `aembedding` | `에이임베딩` |
| `image_generation` | `이미지_제너레이션` |
| `aimage_generation` | `에이이미지_제너레이션` |
| `transcription` | `트랜스크립션` |
| `atranscription` | `에이트랜스크립션` |
| `Router` | `라우터` |
| `ModelResponse` | `모델리스폰스` |

## 예시

```kopy
프롬 라이트엘엘엠 임포트 컴플리션

리스폰스 = 컴플리션(
    모델="openai/gpt-5-mini",
    messages=[{"role": "user", "content": "KoPy를 한 문장으로 설명해줘."}],
)
프린트(리스폰스)
```

변환 결과는 표준 Python이다.

```python
from litellm import completion

response = completion(
    model="openai/gpt-5-mini",
    messages=[{"role": "user", "content": "KoPy를 한 문장으로 설명해줘."}],
)
print(response)
```

`model → 모델`은 KoPy의 기존 공통 식별자 규칙이다. 반면 `messages=`, `timeout=`, `api_key=`처럼 많은 라이브러리와 사용자 함수에서 반복되는 키워드는 LiteLLM 팩만을 이유로 전역 음역하지 않는다. 현재 `keyword_arguments`는 비워 둔다. 이는 LiteLLM을 import했다는 이유만으로 다음과 같은 사용자 호출이 바뀌는 것을 막기 위한 안전장치다.

```kopy
def 재시도(메시지즈, 타임아웃=논):
    리턴 메시지즈

결과 = 재시도(메시지즈=[], 타임아웃=1)
```

모델 이름, provider prefix, message role/content, API key 같은 문자열 데이터도 음역하지 않는다.

## Router

```kopy
프롬 라이트엘엘엠 임포트 라우터

라우터객체 = 라우터(model_list=[])
```

`model_list=` 역시 LiteLLM 전용이라고 안전하게 판별할 호출 대상 추적이 없는 현재 구조에서는 Python 원문을 유지한다.

## 테스트 정책

전용 CI는 Windows, Ubuntu, macOS에서 Python 3.12.10과 실제 `litellm==1.98.0`을 설치한다. 공급자 API key나 네트워크 호출 없이 실제 LiteLLM export와 KoPy 번역 결과의 import 가능성을 검증한다. 이렇게 하면 외부 서비스 상태에 테스트가 흔들리지 않으면서도 문서에만 존재하는 가짜 API를 pack에 넣는 문제를 잡을 수 있다.
