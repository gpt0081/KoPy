# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 API를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.0**  
개발 기준 Python: **3.12.10**

## KoPy v0.5 방향: AI 개발

v0.5부터 KoPy는 Python Core를 넘어 AI 개발 생태계로 확장합니다.

- 라이브러리별 단어를 Core `words.py`에 섞지 않는 **Library Pack** 구조
- 첫 공식 팩: **NumPy**
- 라이브러리가 import된 파일에서만 해당 팩 활성화
- 모듈 alias, 함수, 속성, ndarray 메서드 스타일 번역
- Python → KoPy 역변환에도 라이브러리 팩 적용
- `kopy packs`로 팩과 실제 Python 라이브러리 설치 상태 확인
- `kopy help np.어레이`처럼 외부 API 학습 도움말 제공
- Windows / Linux / macOS에서 실제 NumPy를 설치해 자동 실행 테스트

다음 공식 AI 팩 후보는 pandas → Matplotlib → scikit-learn → PyTorch → Hugging Face Transformers/Datasets 순입니다.

## NumPy 예시

KoPy:

```kopy
임포트 넘파이 애즈 np

x = np.어레이([1, 2, 3, 4], np.플로트32)
y = x.리셰이프(2, 2)
평균 = np.미인(y)
크기 = np.린알지.노름(y)

프린트(평균)
프린트(크기)
```

KoPy는 이를 다음 Python으로 변환합니다.

```python
import numpy as np

x = np.array([1, 2, 3, 4], np.float32)
y = x.reshape(2, 2)
평균 = np.mean(y)
크기 = np.linalg.norm(y)

print(평균)
print(크기)
```

NumPy 팩은 KoPy에 포함되지만 **실제 NumPy 라이브러리 자체를 대신 설치하지는 않습니다.** 실행하려면 일반 Python과 동일하게 NumPy가 설치되어 있어야 합니다.

```powershell
python -m pip install numpy
```

상태 확인:

```powershell
kopy packs
kopy packs numpy
```

## 라이브러리 팩의 충돌 방지 원칙

외부 라이브러리 API는 전역 단어로 등록하지 않습니다.

```kopy
임포트 넘파이 애즈 np
x = np.어레이([1, 2, 3])
```

처럼 NumPy를 import한 파일에서만 `어레이 → array`, `리셰이프 → reshape` 같은 NumPy 팩 규칙이 활성화됩니다.

앞으로 여러 팩이 동시에 활성화되고 같은 KoPy 철자가 서로 다른 Python API를 가리키면 KoPy는 임의로 추측하지 않습니다. 모호한 표현은 번역하지 않아 사용자가 명시적으로 구분하도록 합니다.

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

`pyproject.toml`의 설치 메타데이터나 console script가 바뀐 경우에는 다음을 다시 실행합니다.

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
kopy help print
kopy help np.어레이
kopy explain examples\hello.kpy
kopy learn examples\hello.kpy
kopy words
kopy packs
kopy packs numpy
kopy spelling on
kopy spelling off
kopy spelling status
kopy version
```

## 도움말

Core 단어:

```powershell
kopy help 프린트
kopy help print
```

라이브러리 API:

```powershell
kopy help np.어레이
kopy help numpy.array
```

NumPy 예:

```text
np.어레이 → Python numpy.array
팩: numpy
설명: Python 시퀀스에서 NumPy 배열을 만듭니다.
```

## Python → KoPy 변환

Core뿐 아니라 활성 라이브러리 팩도 역변환합니다.

Python:

```python
import numpy as np
x = np.arange(6).reshape(2, 3)
average = np.mean(x)
```

KoPy:

```kopy
임포트 넘파이 애즈 np
x = np.에이레인지(6).리셰이프(2, 3)
average = np.미인(x)
```

명령:

```powershell
kopy convert-python example.py
kopy to-kopy example.py -o example.kpy
```

문자열과 주석은 변환하지 않습니다.

## 교육형 오류와 코드 설명

```powershell
kopy explain examples\hello.kpy
```

KoPy는 코드를 실행하지 않고 AST를 읽어 변수 저장, 조건문, 반복문, 함수 정의, 호출 등의 흐름을 한국어로 설명합니다. LLM이 필요하지 않으며 오프라인입니다.

흔한 Python 문법 오류에는 콜론, 들여쓰기, 괄호 등을 중심으로 학습 힌트를 덧붙입니다.

## 편집기용 Core API

```powershell
kopy words --json
kopy info --json
kopy diagnose examples\hello.kpy --json
kopy packs --json
kopy packs numpy --json
```

VS Code 확장은 별도 Core 단어표나 오타 알고리즘을 유지하지 않고 KoPy Core를 사용합니다.

## 테스트 철학

KoPy는 Python 호환성을 가장 중요한 기준으로 둡니다.

```text
Python 소스 → CPython

Python 소스 → KoPy 변환 → 다시 Python 변환 → CPython
```

두 경로의 결과를 비교하는 Golden 테스트를 유지합니다.

v0.5부터 AI 라이브러리 팩은 별도의 GitHub Actions 매트릭스에서도 검증합니다.

```text
Windows ┐
Linux   ├→ KoPy 설치 → NumPy 2.5 설치 → 전체 테스트 → 실제 NumPy KoPy 코드 실행
macOS   ┘
```

## 구조

```text
src/kopy
   ├─ words.py       Python Core 단어·설명·예제
   ├─ packs/
   │   ├─ base.py    라이브러리 팩 규격
   │   ├─ registry.py 팩 등록부
   │   └─ numpy.py   첫 공식 AI 팩
   ├─ translator.py  KoPy ↔ Python + 활성 팩 변환
   ├─ spelling.py    오타 판정
   ├─ education.py   교육형 오류·코드 설명
   ├─ runtime.py     실행
   ├─ editor.py      IDE용 Core API
   └─ cli.py         사용자 CLI
```

## 버전 정책

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다.

현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License
