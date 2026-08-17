# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 내장 함수를 한글 음역으로도 사용할 수 있게 하는 학습용 호환 레이어입니다.

- 개발 기준 Python: **3.12.10**
- 호환 대상: **Python 3.12.x**
- KoPy와 Python 코드를 한 파일에서 자유롭게 혼용
- 올바른 영문 Python 코드는 그대로 실행
- `이프`, `포`, `프린트`, `인트` 같은 한글 음역 표현 지원
- 영문 오타가 의심되면 원본 코드를 자동 수정하지 않고 후보 제시
- VS Code 확장은 KoPy Core의 공식 단어/진단 API를 사용

## 예시

```kopy
이름 = input("이름: ")
나이 = 인트(input("나이: "))

if 나이 >= 20:
    프린트(이름, "성인입니다.")
엘스:
    print(이름, "미성년자입니다.")
```

위 코드는 KoPy에서 정상 실행되며 내부적으로 표준 Python으로 변환됩니다.

## 개발용 설치

Git 저장소를 clone한 뒤 editable install을 사용하면 KoPy 소스를 다시 빌드하지 않고 바로 실행할 수 있습니다.

```powershell
git clone https://github.com/gpt0081/KoPy.git
cd KoPy
python -m pip install -e .
```

설치 후 어느 폴더에서든:

```powershell
kopy version
kopy examples\hello.kpy
```

를 실행할 수 있습니다.

일반적인 `src/kopy/*.py` 변경은 editable install이 현재 소스를 직접 가리키므로 다음 개발 주기가 가능합니다.

```powershell
git pull
kopy version
```

`pyproject.toml`의 설치 메타데이터, 의존성, console script 구성이 바뀐 경우에만 `python -m pip install -e .`를 다시 실행합니다.

## CLI 사용법

```powershell
kopy run examples\hello.kpy
kopy check examples\hello.kpy
kopy translate examples\hello.kpy
kopy learn examples\hello.kpy
kopy spelling on
kopy spelling off
kopy spelling status
kopy version
```

### 편집기용 Core API

KoPy Core가 IDE의 단일 진실 원본이 되도록 편집기용 JSON 인터페이스를 제공합니다.

```powershell
kopy words --json
kopy info --json
kopy diagnose examples\hello.kpy --json
```

미저장 편집 내용은 표준 입력으로 직접 검사할 수 있습니다.

```powershell
Get-Content examples\hello.kpy | kopy diagnose --stdin --json
```

- `words --json`: `src/kopy/words.py`에서 파생된 공식 KoPy 단어 등록부
- `diagnose --json`: 실제 KoPy 스펠링/번역 로직을 사용한 진단
- `info --json`: KoPy와 Python 런타임 정보

VS Code 확장은 별도의 KoPy 단어표나 오타 알고리즘을 유지하지 않고 이 API를 호출합니다. 따라서 Core 규칙을 변경한 뒤 `git pull`하면 실행, 자동완성, Hover, 진단이 같은 KoPy 본체를 사용합니다.

## VS Code 개발 확장

`vscode-extension`은 `.kpy` 파일 인식, 실행 버튼, 자동완성, Hover, 진단 UI를 제공합니다.

기본 실행 대상은 PATH의:

```text
kopy
```

명령입니다. 따라서 개발 PC에서 `python -m pip install -e .`를 한 번 수행하면 VS Code 역시 현재 Git checkout의 KoPy Core를 사용합니다.

확장 자체의 JavaScript/UI/명령 구성이 바뀐 경우에만 새 VSIX가 필요합니다. `words.py`, `spelling.py`, `translator.py`, `runtime.py` 등 Core 변경에는 VSIX 재설치가 필요하지 않습니다.

## 스펠링 힌트

예를 들어:

```python
pritn("Hello")
```

를 작성하면 KoPy Core는 `print` 후보를 진단으로 반환합니다. CLI에서는:

```text
1:1  # KoPy 힌트: 'pritn' → 'print' 를 입력하려고 했나요?
```

형태로 표시하고, VS Code에서는 같은 Core 결과를 경고 밑줄과 인라인 힌트로 표시합니다.

## Windows EXE 배포판 빌드

`dist\kopy.exe`는 개발 본체가 아니라 Python 설치 없이 사용할 수 있는 독립 배포판을 만들기 위한 결과물입니다.

```powershell
build.bat
```

성공하면:

```text
dist\kopy.exe
```

가 생성됩니다.

## GitHub Actions

- **Windows Build**: Python 3.12.10 테스트, PyInstaller EXE 빌드, smoke test
- **VS Code Extension**: 확장 JavaScript 검사, VSIX 패키징

## 구조 원칙

KoPy의 언어 규칙은 `src/kopy`가 단일 원본입니다.

```text
src/kopy
   │
   ├─ words.py       공식 단어 등록부
   ├─ spelling.py    공식 오타 판정
   ├─ translator.py  공식 변환
   ├─ runtime.py     공식 실행
   └─ editor.py      IDE용 Core API
          │
          ├─ CLI
          ├─ VS Code
          └─ 미래의 다른 IDE / 웹 IDE
```

VS Code는 KoPy 언어 자체가 아니라 KoPy Core를 사용하는 첫 번째 공식 편집기 클라이언트입니다.

## 버전 정책

KoPy는 각 릴리스마다 기준 Python 버전을 명시합니다. Python 새 버전이 발표되어도 자동 추종하지 않고 새 문법, 호환성, 보안, 교육적 가치를 검토해 필요할 때 기준 버전을 올립니다.

현재 개발 기준은 Python 3.12.10입니다.

## 라이선스

MIT License
