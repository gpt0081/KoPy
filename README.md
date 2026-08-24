# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 API를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.4**  
개발 기준 Python: **3.12.10**

## KoPy v0.5 방향: AI 개발

v0.5부터 KoPy는 Python Core를 넘어 AI 개발 생태계로 확장합니다.

현재 공식 AI 라이브러리 팩:

- **NumPy**: 배열·통계·선형대수·난수
- **pandas**: DataFrame·정제·집계·파일 입출력
- **scikit-learn**: 전처리·모델 학습·평가·파이프라인
- **PyTorch**: 텐서·자동미분·신경망·최적화
- **Hugging Face Transformers**: 토크나이저·사전학습 모델·생성·Trainer

Library Pack은 실제 외부 라이브러리를 다시 구현하지 않습니다. 라이브러리가 import된 파일에서만 해당 API 이름을 KoPy 표현과 Python 표현 사이에서 번역하고, 실제 계산과 모델 실행은 원래 Python 라이브러리가 담당합니다.

```text
KoPy 코드
   ↓
KoPy Core + 활성 Library Pack
   ↓
표준 Python 코드
   ↓
CPython + NumPy / pandas / scikit-learn / PyTorch / Transformers
```

## Transformers 예시

```kopy
프롬 트랜스포머스 임포트 오토토크나이저, 오토모델포코절엘엠

토크나이저 = 오토토크나이저.프롬프리트레인드("local-model")
모델 = 오토모델포코절엘엠.프롬프리트레인드("local-model")
입력값 = 토크나이저("안녕하세요", return_tensors="pt")
출력 = 모델.제너레이트(**입력값)
텍스트 = 토크나이저.배치디코드(출력)
```

이는 다음 표준 Python 흐름으로 변환됩니다.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("local-model")
model = AutoModelForCausalLM.from_pretrained("local-model")
inputs = tokenizer("안녕하세요", return_tensors="pt")
outputs = model.generate(**inputs)
text = tokenizer.batch_decode(outputs)
```

`return_tensors`, `input_ids`, `model`, `tokenizer`, `device` 같은 키워드 인자 이름은 아직 Python 원형을 유지합니다. 라이브러리마다 같은 이름을 다른 의미로 사용할 수 있으므로 전역 치환하지 않습니다.

## NumPy 예시

```kopy
임포트 넘파이 애즈 np

x = np.어레이([1, 2, 3, 4], np.플로트32)
y = x.리셰이프(2, 2)
평균 = np.미인(y)
크기 = np.린알지.노름(y)

프린트(평균)
프린트(크기)
```

## 라이브러리 팩의 충돌 방지 원칙

외부 라이브러리 API는 Core 전역 단어표에 섞지 않습니다.

```kopy
임포트 넘파이 애즈 np
x = np.어레이([1, 2, 3])
```

처럼 해당 라이브러리를 import한 파일에서만 관련 규칙이 활성화됩니다. 여러 활성 팩이 같은 KoPy 철자를 서로 다른 Python API로 정의하면 KoPy는 임의로 추측하지 않고 모호한 표현을 번역하지 않습니다.

실제 라이브러리는 일반 Python과 동일하게 별도 설치해야 합니다.

```powershell
python -m pip install numpy pandas scikit-learn torch transformers
```

상태 확인:

```powershell
kopy packs
kopy packs numpy
kopy packs pandas
kopy packs scikit-learn
kopy packs pytorch
kopy packs transformers
```

## Core 예시

```kopy
이름 = 인풋("이름: ")
나이 = 인트(인풋("나이: "))

이프 나이 >= 20:
    프린트(이름, "성인입니다.")
엘스:
    프린트(이름, "미성년자입니다.")
```

KoPy는 Python 문법 자체를 바꾸지 않고 표준 Python으로 변환한 뒤 CPython에서 실행합니다.

## 개발용 설치

```powershell
git clone https://github.com/gpt0081/KoPy.git
cd KoPy
python -m pip install -e .
```

editable install 이후 일반적인 Core 소스 변경은 다시 설치할 필요가 없습니다.

```powershell
git pull
kopy version
```

`pyproject.toml`의 설치 메타데이터나 console script가 바뀐 경우에는 다시 설치합니다.

```powershell
python -m pip install -e .
```

## CLI

```powershell
kopy run examples\hello.kpy
kopy check examples\hello.kpy
kopy translate examples\hello.kpy
kopy to-kopy example.py
kopy convert-python example.py
kopy help 프린트
kopy help np.어레이
kopy help 트랜스포머스.오토토크나이저
kopy explain examples\hello.kpy
kopy learn examples\hello.kpy
kopy words
kopy packs
kopy packs transformers
kopy spelling status
kopy version
```

## Python → KoPy 변환

Core뿐 아니라 활성 라이브러리 팩도 역변환합니다.

Python:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("local-model")
```

KoPy:

```kopy
프롬 트랜스포머스 임포트 오토토크나이저

tokenizer = 오토토크나이저.프롬프리트레인드("local-model")
```

문자열과 주석은 변환하지 않습니다.

## 교육형 오류와 코드 설명

```powershell
kopy explain examples\hello.kpy
```

KoPy는 코드를 실행하지 않고 AST를 읽어 변수 저장, 조건문, 반복문, 함수 정의, 호출 등의 흐름을 한국어로 설명합니다. LLM이 필요하지 않으며 오프라인입니다.

## 편집기용 Core API

```powershell
kopy words --json
kopy info --json
kopy diagnose examples\hello.kpy --json
kopy packs --json
kopy packs transformers --json
```

VS Code 확장은 별도 Core 단어표나 오타 알고리즘을 유지하지 않고 KoPy Core를 사용합니다.

## 테스트 철학

KoPy는 Python 호환성을 가장 중요한 기준으로 둡니다.

```text
Python 소스 → CPython

Python 소스 → KoPy 변환 → 다시 Python 변환 → CPython
```

AI 라이브러리 팩은 GitHub Actions에서 Windows, Linux, macOS 각각에 실제 라이브러리를 설치해 전체 테스트와 런타임 smoke test를 수행합니다. Transformers 테스트는 네트워크 모델 다운로드에 의존하지 않고 작은 BERT 모델을 로컬 메모리에서 직접 구성합니다.

## 구조

```text
src/kopy
   ├─ words.py          Python Core 단어·설명·예제
   ├─ packs/
   │   ├─ base.py       라이브러리 팩 규격
   │   ├─ registry.py   팩 등록부
   │   ├─ numpy.py
   │   ├─ pandas.py
   │   ├─ sklearn.py
   │   ├─ torch.py
   │   └─ transformers.py
   ├─ translator.py     KoPy ↔ Python + 활성 팩 변환
   ├─ spelling.py
   ├─ education.py
   ├─ runtime.py
   ├─ editor.py
   └─ cli.py
```

## 다음 AI 확장 후보

- Hugging Face Datasets
- Matplotlib
- tokenizers / sentencepiece 계열
- ONNX Runtime

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다. 현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License
