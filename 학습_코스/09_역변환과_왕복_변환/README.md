# 09. 역변환과 왕복 변환

## 학습 목표

- KoPy → Python과 Python → KoPy를 구분합니다.
- 왕복 변환으로 등록된 표현의 보존을 검사합니다.
- 역변환의 모호성과 스코프 분석 필요성을 이해합니다.

## 핵심 개념

| 함수 | 방향 | 결과 |
| --- | --- | --- |
| `translate` | KoPy → Python | `Translation.python` |
| `to_kopy` | Python → KoPy | `ReverseTranslation.kopy` |

왕복 변환은 다음 과정입니다.

```text
Python 원문 → KoPy → 복원 Python
```

등록된 단어가 일대일이고 문맥이 명확하다면 복원 결과가 원문과 같아야 합니다. 하지만 왕복 문자열 일치만으로 모든 프로그램 의미가 같다고 완전히 증명되지는 않습니다. 실행 테스트와 충돌 회귀 테스트가 함께 필요합니다.

직접 import된 클래스 이름과 같은 철자의 지역 변수가 있을 수 있습니다. KoPy는 Python의 실제 바인딩 규칙을 따라 어느 이름을 복원할지 판단합니다.

## 실행

```powershell
python "학습_코스/09_역변환과_왕복_변환/예제/round_trip.py"
kopy run "학습_코스/09_역변환과_왕복_변환/예제/sample.kpy"
python "학습_코스/09_역변환과_왕복_변환/예제/sample.py"
```

## 문제

Python 소스를 KoPy로 바꾸고 다시 Python으로 복원해 `(kopy, restored, stable)`을 반환하세요.

```powershell
python -m unittest "학습_코스.09_역변환과_왕복_변환.문제.test_exercise" -v
```

## 스스로 설명할 것

1. 역변환은 실행 기능보다 학습 기능에 가까운 이유가 무엇인가?
2. 왕복 변환과 실제 런타임 테스트는 각각 무엇을 잡는가?
3. 지역 변수 shadowing이 역변환을 어렵게 만드는 이유는 무엇인가?
