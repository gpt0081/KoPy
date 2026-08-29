# KoPy 공식 학습 코스

이 과정은 특정 업무나 산업이 아니라 **범용 Python 개발 능력**을 기르는 순수 학습 과정입니다. KoPy 음역으로 개념을 처음 만나고, 대응하는 표준 Python을 읽고, 마지막에는 KoPy 내부 구현과 테스트까지 확인합니다.

KoPy는 Python을 대체하지 않습니다. 현재 실행 구조는 `KoPy 소스 → 토큰 안전 변환 → 표준 Python → CPython`입니다.

## 학습 규칙

1. 설명을 읽고 예제를 직접 타이핑합니다.
2. `.kpy` 예제를 실행한 뒤 대응 `.py` 파일을 읽습니다.
3. `kopy learn`과 `kopy translate`로 두 표현을 연결합니다.
4. 문제를 최소 15분 직접 풉니다.
5. 학습자용 테스트를 실행하고 실패 원인을 읽습니다.
6. 테스트가 통과한 뒤에만 정답과 비교합니다.

## 과정 지도

### A. KoPy로 배우는 범용 Python

| 강 | 주제 |
| --- | --- |
| [00](00_KoPy와_Python/README.md) | KoPy의 목적, 설치, 실행, 한·영 혼용 |
| [01](01_값과_자료형/README.md) | 값, 변수, 자료형, 연산자 |
| [02](02_조건문과_반복문/README.md) | 분기, 반복, 들여쓰기 |
| [03](03_함수와_스코프/README.md) | 함수, 인자, 반환값, 스코프 |
| [04](04_자료구조와_컴프리헨션/README.md) | 리스트, 튜플, 딕셔너리, 집합, 컴프리헨션 |
| [05](05_문자열과_파일/README.md) | 문자열, `pathlib`, UTF-8, JSON |
| [06](06_예외와_클래스/README.md) | 예외, 클래스, 객체, 합성 |
| [07](07_모듈과_테스트/README.md) | 모듈, 패키지, 타입 힌트, `unittest` |

### B. KoPy 내부를 배우는 개발 과정

| 강 | 주제 |
| --- | --- |
| [08](08_토큰_번역기/README.md) | `tokenize`, NAME 토큰, 문자열·주석 보호 |
| [09](09_역변환과_왕복_변환/README.md) | `translate`, `to_kopy`, 교체 기록, 왕복 변환 |
| [10](10_CLI와_학습도구/README.md) | 전체 CLI 명령과 종료 코드 |
| [11](11_진단과_편집기_API/README.md) | 스펠링, 문법 설명, Editor JSON API |
| [12](12_라이브러리_팩/README.md) | 팩 등록부, API 음역, 동적 전체 색인 |
| [13](13_스코프와_충돌_방지/README.md) | namespace, call keyword, shadowing, 원문 예외 |
| [14](14_VSCode_CI_배포/README.md) | VS Code, CI, Windows 빌드, 버전·배포 |

### C. 종합 연습

[15강](15_종합_연습/README.md)은 두 개의 범용 프로젝트를 제공합니다.

- 텍스트 분석 CLI: 일반 Python 개발 종합 연습
- KoPy 소스 검사기: Core API 활용 종합 연습

## 설치

저장소 루트에서 다음을 실행합니다.

```powershell
python -m pip install -e .
kopy version
kopy run "학습_코스/00_KoPy와_Python/예제/hello.kpy"
```

## 테스트

저장소 전체 회귀 테스트:

```powershell
python -m unittest discover -s tests -v
```

학습 코스의 정답·예제·문서 무결성 테스트:

```powershell
python -m unittest "학습_코스.테스트.test_course" -v
```

각 문제의 `test_exercise.py`는 처음에는 실패하는 것이 정상입니다. 문제 파일을 완성한 뒤 해당 디렉터리에서 실행하세요. 문제 테스트는 저장소 기본 CI에 포함하지 않습니다.

## 권장 경로

- Python 입문자: `00 → 01 → … → 07 → 15A → 08 → … → 14 → 15B`
- Python 경험자: `00 → 08 → … → 14 → 15B`, 필요한 기초 강의만 복습

## 완료 기준

- KoPy 예제를 표준 Python으로 직접 다시 쓸 수 있다.
- 실행, 변환, 검사, 진단을 구분한다.
- 문자열·주석 보호와 namespace-scoped 팩의 이유를 설명한다.
- 실패하는 `unittest`에서 원인을 찾는다.
- 종합 연습 중 하나를 정답 없이 완성한다.

이 과정은 KoPy Core의 현재 구현을 기준으로 합니다. [`COURSE_MANIFEST.json`](COURSE_MANIFEST.json)과 자동 테스트가 버전·Python 기준·팩 수의 변화를 감지합니다.

현재 저장소의 각 구현이 어느 강의와 테스트에서 다뤄지는지는 [`구현_대응표.md`](구현_대응표.md)에서 확인할 수 있습니다.
