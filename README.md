# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 내장 함수를 한글 음역으로도 사용할 수 있게 하는 학습용 호환 레이어입니다.

- 기준 Python: **3.14.7**
- KoPy와 Python 코드를 한 파일에서 자유롭게 혼용
- 올바른 영문 Python 코드는 그대로 실행
- `이프`, `포`, `프린트`, `인트` 같은 한글 음역 표현 지원
- 영문 오타가 의심되면 원본 코드를 자동 수정하지 않고 `# KoPy 힌트:` 형태로 후보 제시
- 스펠링 힌트 기능 ON/OFF 가능

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

## 다운로드

GitHub 저장소의 **Code → Download ZIP**으로 전체 소스를 받을 수 있습니다.

Git이 설치되어 있다면:

```powershell
git clone https://github.com/gpt0081/KoPy.git
cd KoPy
```

## 설치

KoPy v0.1.x는 Python 3.14.x를 대상으로 합니다.

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip
pip install -e .
```

설치 후에는 다음 두 방식이 모두 됩니다.

```powershell
kopy run examples\hello.kpy
kopy examples\hello.kpy
```

일반 Python 파일도 그대로 실행할 수 있습니다.

```powershell
kopy my_script.py
```

## 사용법

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

### 일시적으로 스펠링 힌트 끄기

```powershell
kopy run --no-spelling examples\hello.kpy
```

### 스펠링 힌트

예를 들어 다음과 같이 작성하면:

```python
pritn("Hello")
```

KoPy는 코드를 자동 수정하지 않고 실행 전에 다음과 같은 힌트를 출력합니다.

```text
1:1  # KoPy 힌트: 'pritn' → 'print' 를 입력하려고 했나요?
```

`kopy spelling off`로 기본 기능을 끌 수 있고, `kopy spelling on`으로 다시 켤 수 있습니다.

## Windows EXE 직접 빌드

저장소 루트에서:

```powershell
build.bat
```

테스트를 통과하면 다음 파일이 생성됩니다.

```text
dist\kopy.exe
```

그 다음에는:

```powershell
dist\kopy.exe version
dist\kopy.exe examples\hello.kpy
```

처럼 사용할 수 있습니다.

## GitHub Actions에서 EXE 받기

저장소의 **Actions → Windows Build**에서 성공한 실행을 열고, **Artifacts → KoPy-Windows**를 받으면 `kopy.exe`가 들어 있습니다.

## 설계 원칙

KoPy는 Python을 대체하려는 언어가 아닙니다. 사용자가 처음에는 한글 음역 표현을 사용하고, 익숙해질수록 실제 Python 영문 표현으로 자연스럽게 이동하도록 돕는 것이 목적입니다.

Python 새 버전이 발표되어도 KoPy가 자동으로 즉시 따라가지는 않습니다. 새 문법, 호환성, 보안, 교육적 가치 등을 검토해 필요할 때 기준 Python 버전을 올립니다. 각 KoPy 릴리스는 기준 Python 버전을 명시합니다.

## 현재 단계

KoPy v0.1.x는 다음을 목표로 합니다.

- 핵심 Python 예약어 음역 지원
- 주요 built-in 음역 지원
- 일반 Python 코드 무변환 실행
- 한글/영문 혼용
- 선택형 스펠링 힌트
- 번역 보기 및 학습 모드
- Windows 실행 파일 빌드

## 라이선스

MIT License
