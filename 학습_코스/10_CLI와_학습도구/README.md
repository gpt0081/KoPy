# 10. CLI와 학습도구

## 학습 목표

- KoPy CLI 명령을 실행·검사·학습·정보 조회로 분류합니다.
- 명령의 표준 출력, 표준 오류, 종료 코드를 구분합니다.
- 파일을 직접 실행하는 축약형이 어떻게 정규화되는지 이해합니다.

## 전체 명령

| 명령 | 코드 실행 | 역할 |
| --- | --- | --- |
| `run FILE` | 예 | KoPy/Python 파일 실행 |
| `check FILE` | 아니오 | 변환 후 문법 검사 |
| `translate FILE` | 아니오 | KoPy → Python 출력 |
| `to-kopy FILE` | 아니오 | Python → KoPy 출력 |
| `learn FILE` | 아니오 | 사용된 음역과 Python 결과 표시 |
| `explain FILE` | 아니오 | AST 기반 상위 흐름 설명 |
| `help WORD` | 아니오 | Core 단어·팩 API 설명 |
| `diagnose FILE` | 아니오 | 스펠링·문법 진단 |
| `words` | 아니오 | Core 등록부 출력 |
| `packs [NAME]` | 아니오 | 팩 목록·상세 출력 |
| `spelling` | 아니오 | 기본 힌트 설정 |
| `info`, `version` | 아니오 | 런타임·버전 정보 |

`kopy file.kpy`는 내부에서 `kopy run file.kpy`로 정규화됩니다. 성공은 보통 종료 코드 0, 사용자 코드·문법 실패는 1, 파일·권한·인자 문제는 2를 사용합니다.

## 실행

```powershell
kopy check "학습_코스/10_CLI와_학습도구/예제/cli_sample.kpy"
kopy learn "학습_코스/10_CLI와_학습도구/예제/cli_sample.kpy"
kopy explain "학습_코스/10_CLI와_학습도구/예제/cli_sample.kpy"
kopy run "학습_코스/10_CLI와_학습도구/예제/cli_sample.kpy"
python "학습_코스/10_CLI와_학습도구/예제/cli_sample.py"
```

## 문제

`kopy.cli.main`을 호출해 종료 코드와 stdout/stderr를 함께 반환하는 함수를 완성하세요.

```powershell
python -m unittest "학습_코스.10_CLI와_학습도구.문제.test_exercise" -v
```

## 스스로 설명할 것

1. `check`가 코드를 실행하지 않아야 하는 이유는 무엇인가?
2. 정상 출력과 오류 출력을 분리하면 자동화에 어떤 이점이 있는가?
3. 종료 코드 0과 화면에 오류 문구가 없는 것은 같은 조건인가?
