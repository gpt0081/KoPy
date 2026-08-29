# 14. VS Code, CI, 빌드와 배포

## 학습 목표

- VS Code 확장이 KoPy Core와 통신하는 구조를 설명합니다.
- 로컬 테스트와 CI의 역할을 구분합니다.
- Windows 실행 파일과 Python 패키지 배포 경로를 이해합니다.
- 여러 파일의 버전 정보를 동기화해야 하는 이유를 검증합니다.

## VS Code 확장

`vscode-extension/`에는 다음 요소가 있습니다.

- `extension.js`: Core CLI의 JSON 출력을 호출해 완성·진단·실행 제공
- `language-configuration.json`: 괄호, 주석, 들여쓰기 설정
- `syntaxes/kopy.tmLanguage.json`: 문법 강조
- `snippets/kopy.json`: 코드 조각
- `package.json`: 확장 메타데이터와 명령 등록

확장이 Core 단어표를 별도로 복제하지 않는 것이 중요합니다. `kopy words --json`, `kopy diagnose --json`, `kopy info --json`이 연결 계약입니다.

## 테스트와 CI

`.github/workflows/`는 목적별로 분리되어 있습니다.

- Windows Core 테스트와 PyInstaller 빌드
- VS Code VSIX 패키징
- Library Pack별 실제 라이브러리 런타임
- 여러 운영체제·의존성 버전 조합
- 릴리스 시 wheel과 source distribution 생성

번역 테스트가 통과해도 외부 라이브러리의 실제 API가 바뀌면 실행은 실패할 수 있습니다. 반대로 외부 의존성 설치 실패가 Core 번역 버그를 뜻하지는 않습니다. 실패 층위를 구분해야 합니다.

## 버전과 기준 Python

최소한 다음 정보가 서로 일치해야 합니다.

- `pyproject.toml`의 프로젝트 버전
- `src/kopy/__init__.py`의 `__version__`
- README의 현재 Core 버전
- `PYTHON_BASELINE`과 CI의 Python 설정

학습 코스의 `COURSE_MANIFEST.json`도 버전 변경 시 검토 대상입니다.

## 실행

```powershell
python "학습_코스/14_VSCode_CI_배포/예제/editor_contract.py"
kopy run "학습_코스/14_VSCode_CI_배포/예제/sample.kpy"
python "학습_코스/14_VSCode_CI_배포/예제/sample.py"
python -m unittest tests.test_version_metadata -v
```

## 문제

저장소 루트를 받아 패키지 버전, 런타임 버전, README 표기, Python 기준을 비교하는 함수를 완성하세요.

```powershell
python -m unittest "학습_코스.14_VSCode_CI_배포.문제.test_exercise" -v
```

## 스스로 설명할 것

1. Core 단어표를 VS Code 확장에 복사하면 어떤 드리프트가 생기는가?
2. 번역 테스트와 실제 라이브러리 smoke test는 무엇이 다른가?
3. 버전 문자열 하나가 어긋나도 배포 문제로 보는 이유는 무엇인가?
