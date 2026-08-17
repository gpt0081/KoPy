# KoPy Language Support for VS Code

KoPy(`.kpy`)를 VS Code에서 하나의 프로그래밍 언어처럼 작성하고 실행하기 위한 확장입니다.

## 현재 지원

- `.kpy` 언어 인식
- Python 기반 문법 강조 + KoPy 한글 토큰 강조
- 편집기 우측 상단 ▶ 실행 버튼
- `Ctrl+F5`로 현재 KoPy 파일 실행
- 통합 터미널에서 실행하므로 `input()` 사용 가능
- 영문 Python 고확률 오타를 실시간 진단
- 오타 오른쪽에 `# → print?` 형태의 인라인 힌트 표시
- 한글 KoPy 토큰 자동완성
- 한글 토큰 Hover 시 실제 Python 표현 표시
- KoPy 스펠링 힌트 ON/OFF 설정

## 실행기 찾는 순서

확장은 다음 순서로 KoPy 실행기를 찾습니다.

1. VS Code 설정 `kopy.executablePath`
2. 현재 워크스페이스의 `dist/kopy.exe` (Windows)
3. PATH에 등록된 `kopy`

KoPy 저장소 자체를 VS Code로 열었다면 보통 `dist/kopy.exe`를 자동으로 찾습니다.

## 설치

GitHub Actions에서 생성된 `kopy-language-0.2.0.vsix`를 받은 뒤 VS Code에서:

1. `Ctrl+Shift+X`
2. 확장 화면 우측 상단 `...`
3. `Install from VSIX...`
4. 받은 `.vsix` 선택
5. VS Code 다시 로드

명령줄 설치도 가능합니다.

```powershell
code --install-extension kopy-language-0.2.0.vsix
```

## 첫 테스트

KoPy 저장소를 VS Code로 열고 `examples/hello.kpy`를 여세요.

오른쪽 위 ▶ 버튼을 누르거나 `Ctrl+F5`를 누르면 KoPy 통합 터미널에서 실행됩니다.

## 현재 한계

이 버전은 편집/실행 경험을 먼저 완성한 단계입니다. 아직 Python Pylance와 같은 프로젝트 전체 타입 추론, 정의로 이동, 참조 찾기, F5 디버깅은 제공하지 않습니다. 이 기능들은 KoPy Language Server 및 Debug Adapter 단계에서 추가할 예정입니다.
