# KoPy 배포 구조

KoPy는 개발용 소스와 사용자 배포를 분리한다.

## 1. 개발자 모드

```text
GitHub checkout
  -> python -m pip install -e .
  -> kopy 명령
  -> VS Code 확장
```

일반 Core 수정은 `git pull` 직후 반영된다.

## 2. PyPI / pipx

패키지 이름은 `kopy-lang`, CLI 명령은 `kopy`를 사용한다.

저장소의 `.github/workflows/release.yml`은 GitHub Release가 발행되면 wheel/sdist를 만들고 PyPI Trusted Publishing(OIDC)으로 배포하도록 준비되어 있다.

필요한 외부 설정:

1. PyPI 계정에서 `kopy-lang` 프로젝트 또는 pending trusted publisher를 준비한다.
2. GitHub repository: `gpt0081/KoPy`
3. workflow filename: `release.yml`
4. GitHub environment를 사용할 경우 이름: `pypi`
5. 이후 GitHub Release를 발행한다.

일반 사용자 목표:

```powershell
pipx install kopy-lang
kopy version
```

업데이트:

```powershell
pipx upgrade kopy-lang
```

## 3. VS Code Marketplace

현재 VSIX 패키징은 자동화되어 있다. Marketplace 공개에는 Microsoft/Visual Studio Marketplace publisher ID가 필요하다.

외부 설정 후 목표:

```text
VS Code Extensions
  -> KoPy 검색
  -> Install
```

Marketplace에 공개하기 전 `vscode-extension/package.json`의 `publisher`를 실제 생성한 publisher ID로 변경해야 한다.

## 4. Language Server Protocol

현재 v0.4 구조:

```text
VS Code extension
  -> kopy words --json
  -> kopy diagnose --stdin --json
  -> kopy run
```

다음 단계에서는 이를 표준 LSP로 감쌀 수 있다.

```text
VS Code / 다른 LSP 편집기
        |
        v
KoPy Language Server (Python)
        |
        +-- words.py
        +-- spelling.py
        +-- translator.py
        +-- education.py
```

우선 지원 후보:

- textDocument/completion
- textDocument/hover
- textDocument/publishDiagnostics
- textDocument/documentSymbol
- textDocument/definition (사용자 심볼 분석 도입 후)

Core 규칙은 계속 `src/kopy`가 단일 원본이어야 한다.

## 5. 독립 Windows 배포판

현재 GitHub Actions의 Windows Build는 `dist/kopy.exe`를 만든다.

장기 목표:

```text
KoPy Installer
  -> KoPy runtime
  -> 필요한 Python runtime 또는 독립 frozen runtime
  -> PATH의 kopy 명령
  -> 선택적 VS Code extension 설치 안내
```

설치 프로그램 후보는 Inno Setup 또는 WiX이며, 릴리스 단계에서 GitHub Release asset으로 제공한다.
