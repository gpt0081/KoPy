@echo off
setlocal

python -c "import sys; raise SystemExit(0 if sys.version_info[:2] == (3, 12) else 1)"
if errorlevel 1 (
  echo [KoPy] Python 3.12.x가 필요합니다. 개발 기준은 Python 3.12.10입니다.
  python --version
  exit /b 1
)

python -m pip install --upgrade pip
if errorlevel 1 exit /b 1

python -m pip install -e . "pyinstaller>=6.20,<7"
if errorlevel 1 exit /b 1

python -m unittest discover -s tests -v
if errorlevel 1 exit /b 1

python -m PyInstaller --clean --onefile --name kopy --paths src src\kopy\__main__.py
if errorlevel 1 exit /b 1

echo.
echo [KoPy] 빌드 완료: dist\kopy.exe
