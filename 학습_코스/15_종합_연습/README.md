# 15. 종합 연습

두 프로젝트 중 A를 먼저 완성하면 범용 Python 기초를 확인할 수 있고, B를 완성하면 KoPy Core API 이해를 확인할 수 있습니다. 어느 프로젝트도 특정 산업이나 서비스에 종속되지 않습니다.

## A. 텍스트 분석 CLI

입력 텍스트 파일을 읽어 다음 정보를 JSON으로 출력합니다.

- 전체 단어 수
- 고유 단어 수
- 단어별 빈도
- 빈도순 상위 단어

사용 개념:

- 함수 분리
- 문자열 정규화
- 리스트와 딕셔너리
- 정렬
- UTF-8 파일
- `argparse`
- JSON
- 예외와 테스트

문제: [`A_텍스트_분석_CLI/문제/exercise.kpy`](A_텍스트_분석_CLI/문제/exercise.kpy)

```powershell
python -m unittest "학습_코스.15_종합_연습.A_텍스트_분석_CLI.문제.test_exercise" -v
kopy run "학습_코스/15_종합_연습/A_텍스트_분석_CLI/정답/solution.kpy" -- "학습_코스/15_종합_연습/A_텍스트_분석_CLI/sample.txt"
```

## B. KoPy 소스 검사기

문자열로 받은 KoPy 소스를 실행하지 않고 검사해 다음 정보를 반환합니다.

- 표준 Python 변환 결과
- 전체 교체 횟수
- 중복 없는 음역 대응
- 문법·스펠링 진단
- 정상 여부

사용 개념:

- `translate`
- `diagnose_source`
- 교체 위치 기록
- JSON으로 만들 수 있는 결과 구조
- 회귀 테스트

문제: [`B_KoPy_소스_검사기/문제/exercise.py`](B_KoPy_소스_검사기/문제/exercise.py)

```powershell
python -m unittest "학습_코스.15_종합_연습.B_KoPy_소스_검사기.문제.test_exercise" -v
python "학습_코스/15_종합_연습/B_KoPy_소스_검사기/정답/solution.py" "학습_코스/15_종합_연습/B_KoPy_소스_검사기/sample.kpy"
```

## 완료 기준

- 정답을 보지 않고 모든 테스트를 통과시킨다.
- 빈 입력, 중복, 한글, 잘못된 경로 또는 잘못된 문법을 추가로 테스트한다.
- 한 함수에 모든 코드를 넣지 않고 계산·I/O·CLI 책임을 나눈다.
- 실패 메시지를 숨기지 않고 사용자에게 의미 있게 전달한다.
