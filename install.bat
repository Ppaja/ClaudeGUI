@echo off

python --version
if %errorlevel% neq 0 (
    echo Python not found. Please install Python.
    start https://www.python.org/downloads/
    exit /b
) else (
    echo Python found.
)

pip install -r requirements.txt
@echo requirements installed

start https://console.anthropic.com/
@echo get your api key

pause
