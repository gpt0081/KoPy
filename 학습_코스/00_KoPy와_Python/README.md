# 00. KoPy와 Python

## 학습 목표

- KoPy가 새 실행 엔진이 아니라 Python 호환 학습 레이어임을 설명합니다.
- 한글 음역과 표준 Python을 한 파일에서 함께 사용합니다.
- `run`, `learn`, `translate`의 차이를 체험합니다.

## 핵심 개념

KoPy는 괄호, 콜론, 들여쓰기, 연산자 같은 Python 문법을 그대로 사용합니다. 등록된 이름만 한글 음역으로도 쓸 수 있습니다.

```text
hello.kpy → KoPy 이름 변환 → 표준 Python → CPython 실행
```

`프린트`는 `print`, `포`는 `for`, `레인지`는 `range`로 변환됩니다. 반면 문자열 안의 `"프린트"`는 데이터이므로 그대로 남습니다. 표준 Python 표현을 직접 써도 KoPy는 수정하지 않습니다.

## 실행

```powershell
kopy run "학습_코스/00_KoPy와_Python/예제/hello.kpy"
python "학습_코스/00_KoPy와_Python/예제/hello.py"
kopy learn "학습_코스/00_KoPy와_Python/예제/hello.kpy"
kopy translate "학습_코스/00_KoPy와_Python/예제/hello.kpy"
```

두 예제의 출력이 같아야 합니다.

## 문제

[`문제/exercise.kpy`](문제/exercise.kpy)의 `환영문` 함수를 완성하세요. 이름을 받아 `"안녕하세요, 이름!"`을 반환해야 합니다.

```powershell
python -m unittest "학습_코스.00_KoPy와_Python.문제.test_exercise" -v
```

## 스스로 설명할 것

1. `.kpy`를 최종 실행하는 프로그램은 무엇인가?
2. KoPy와 Python 표현을 섞어 쓸 수 있는 이유는 무엇인가?
3. `learn`과 `translate`는 각각 무엇을 보여주는가?
