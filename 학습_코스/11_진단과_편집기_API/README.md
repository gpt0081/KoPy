# 11. 진단과 편집기 API

## 학습 목표

- 스펠링 힌트와 문법 진단을 구분합니다.
- 규칙 기반 코드 설명이 실행과 다른 점을 이해합니다.
- VS Code 확장이 사용하는 JSON 계약을 검사합니다.
- Core 등록부를 편집기에서 중복하지 않는 이유를 설명합니다.

## 핵심 구현

- `spelling.py`: 고신뢰 영문 오타 후보만 제안
- `education.py`: AST 흐름 설명과 문법 오류 학습 메시지
- `editor.py`: 단어·정보·진단 JSON payload
- `config.py`: 사용자별 스펠링 설정

KoPy는 오타를 자동 수정하지 않습니다. `pritn()`이 `print()`일 가능성이 높더라도 사용자 정의 함수일 가능성을 완전히 배제할 수 없기 때문입니다.

`explain_source`는 코드를 실행하지 않고 AST의 최상위 문장을 설명합니다. 실행 결과나 모든 내부 흐름을 예측하는 도구가 아닙니다.

Editor JSON API는 VS Code 확장과 Core 사이의 계약입니다. 확장이 자체 단어표를 복사하면 Core가 갱신될 때 서로 어긋납니다.

## 실행

```powershell
python "학습_코스/11_진단과_편집기_API/예제/diagnostics.py"
kopy run "학습_코스/11_진단과_편집기_API/예제/sample.kpy"
python "학습_코스/11_진단과_편집기_API/예제/sample.py"
```

의도적인 오류 예시는 [`예제/syntax_error.txt`](예제/syntax_error.txt)에 있습니다.

## 문제

`diagnose_source` 결과를 성공 여부, 오류·경고 수, 코드 목록으로 요약하세요.

```powershell
python -m unittest "학습_코스.11_진단과_편집기_API.문제.test_exercise" -v
```

## 스스로 설명할 것

1. 스펠링 힌트가 자동 수정보다 안전한 이유는 무엇인가?
2. JSON 스키마 변경이 VS Code 확장에 어떤 영향을 주는가?
3. AST 설명과 실제 실행 추적은 무엇이 다른가?
