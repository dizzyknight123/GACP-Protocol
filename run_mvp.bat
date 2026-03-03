@echo off

REM GACP Protocol MVP One-Click Run Script (Windows version)

REM Set working directory
cd "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python 3.10+ not found, please install Python first
    pause
    exit /b 1
)

REM Check if dependencies are installed
pip list | findstr "pydantic" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Error: Dependency installation failed
        pause
        exit /b 1
    )
)

REM Run MVP main program
echo Running GACP Protocol MVP...
python 02-Core-Code\gacp_mvp.py

REM Wait for user input
pause