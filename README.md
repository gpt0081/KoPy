# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 내장 함수를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.4.0**  
개발 기준 Python: **3.12.10**

## KoPy v0.4 핵심

- KoPy와 Python 코드를 한 파일에서 자유롭게 혼용
- `이프`, `포`, `프린트`, `인트` 같은 한글 음역 표현
- 단어 등록부를 Core의 단일 원본으로 관리
- `kopy help <단어>` 학습 도움말
- Python → KoPy 역변환
- 교육형 문법 오류 설명
- `kopy explain` 정적 코드 설명
- Python과 KoPy 실행 결과를 비교하는 Golden 호환성 테스트
- VS Code가 KoPy Core의 공식 단어/진단 API 사용

## 예시

```kopy
이름 = 인풋("이름: ")
나이 = 인트(인풋("나이: "))

이프 나이 >= 20:
    프린트(이름, "성인입니다.")
엘스:
    프린트(이름, "미성년자입니다.")
```

KoPy는 이를 표준 Python으로 변환한 뒤 CPython에서 실행합니다.

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

`pyproject.toml`의 설치 메타데이터나 console script가 바뀐 경우에만 다음을 다시 실행합니다.

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
kopy explain examples\hello.kpy
kopy learn examples\hello.kpy
kopy words
kopy spelling on
kopy spelling off
kopy spelling status
kopy version
```

## 단어 도움말

```powershell
kopy help 프린트
```

예:

```text
프린트 → Python print
분류: builtin
설명: 값을 화면에 출력합니다.

KoPy 예제:
프린트("안녕하세요")

Python 예제:
print("안녕하세요")
```

Python 이름으로도 찾을 수 있습니다.

```powershell
kopy help print
```

## Python → KoPy 변환

```powershell
kopy convert-python hello.py
```

Python:

```python
for i in range(3):
    print(i)
```

KoPy:

```kopy
포 i 인 레인지(3):
    프린트(i)
```

문자열과 주석은 변환하지 않습니다. 파일로 저장하려면:

```powershell
kopy to-kopy hello.py -o hello.kpy
```

## 교육형 오류

KoPy는 Python 문법을 바꾸지 않습니다. 대신 흔한 오류를 학습용 설명으로 보강합니다.

```kopy
이프 트루
    프린트("안녕")
```

예상 안내:

```text
학습 힌트: 콜론(:)이 필요합니다.
if, elif, else, for, while, def, class, try, except 같은 블록 문장은 끝에 ':'를 붙입니다.
수정 제안: 해당 줄의 끝에 : 를 추가해 보세요.
```

## 코드 설명

```powershell
kopy explain examples\hello.kpy
```

KoPy는 코드를 실행하지 않고 AST를 읽어 변수 저장, 조건문, 반복문, 함수 정의, 호출 등의 흐름을 한국어로 설명합니다. LLM이 필요하지 않으며 완전히 오프라인입니다.

## 편집기용 Core API

```powershell
kopy words --json
kopy info --json
kopy diagnose examples\hello.kpy --json
```

미저장 편집 내용도 표준 입력으로 검사할 수 있습니다.

```powershell
Get-Content examples\hello.kpy | kopy diagnose --stdin --json
```

- `words --json`: 단어, Python 대응, 분류, 설명, 예제
- `diagnose --json`: Core의 실제 스펠링 및 문법 진단
- `info --json`: KoPy/Python 런타임 정보

VS Code 확장은 별도 언어 규칙을 유지하지 않고 이 API를 사용합니다. Core를 `git pull`로 갱신하면 실행, 자동완성, Hover, 진단도 같은 최신 Core를 사용합니다.

## 테스트 철학

KoPy는 Python 호환성을 가장 중요한 기준으로 둡니다.

Golden 테스트는 다음 두 경로의 출력 결과를 비교합니다.

```text
Python 소스 → CPython

Python 소스 → KoPy 변환 → 다시 Python 변환 → CPython
```

동일한 프로그램이 동일한 결과를 내는지 자동 검사합니다. 새 기능을 추가할 때 기존 Python 호환성이 깨지는 것을 조기에 잡는 목적입니다.

## Windows EXE

`dist\kopy.exe`는 개발 본체가 아니라 Python 설치 없이 사용할 수 있는 독립 배포판을 위한 결과물입니다.

```powershell
build.bat
```

## 구조

```text
src/kopy
   ├─ words.py       단어·설명·예제의 단일 원본
   ├─ translator.py  KoPy ↔ Python 변환
   ├─ spelling.py    오타 판정
   ├─ education.py   교육형 오류·코드 설명
   ├─ runtime.py     실행
   ├─ editor.py      IDE용 Core API
   └─ cli.py         사용자 CLI
        │
        ├─ Terminal
        ├─ VS Code
        └─ 미래의 IDE / 웹 IDE / AI Tutor
```

## 버전 정책

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다.

현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License
