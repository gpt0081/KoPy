# 08. 토큰 번역기

## 학습 목표

- 단순 문자열 치환이 소스 코드를 망가뜨리는 이유를 설명합니다.
- Python `tokenize`가 만드는 토큰을 관찰합니다.
- KoPy가 등록된 `NAME` 토큰만 바꾸는 원리를 확인합니다.
- 일반 Python과 문자열·주석이 보존되는지 검증합니다.

## 핵심 구현

- `src/kopy/translator.py`: 변환 흐름
- `src/kopy/words.py`: Core 단어의 단일 등록부
- `tests/test_translator.py`: 핵심 회귀 계약

`str.replace("프린트", "print")`를 사용하면 문자열 데이터와 주석까지 바뀝니다. KoPy는 `tokenize.generate_tokens`로 소스를 나눈 뒤 토큰 종류가 `NAME`이고 등록부에 존재할 때만 교체합니다.

변환 결과는 문자열 하나가 아니라 다음 정보를 갖는 `Translation`입니다.

- `source`: 원본
- `python`: 변환된 표준 Python
- `replacements`: 원문, 변환문, 행, 열 기록

## 실행

```powershell
python "학습_코스/08_토큰_번역기/예제/inspect_tokens.py"
kopy run "학습_코스/08_토큰_번역기/예제/sample.kpy"
python "학습_코스/08_토큰_번역기/예제/sample.py"
```

## 문제

`변환된_이름들(source)`가 실제로 교체된 `(KoPy, Python)` 쌍만 순서대로 반환하도록 완성하세요.

```powershell
python -m unittest "학습_코스.08_토큰_번역기.문제.test_exercise" -v
```

## 스스로 설명할 것

1. 문자열과 주석이 `NAME` 토큰이 아닌 이유는 무엇인가?
2. 교체 위치 정보는 CLI와 편집기에 어떻게 사용될 수 있는가?
3. 일반 Python을 그대로 통과시키는 것이 호환성에 왜 필요한가?
