@echo off

:: Delete existing publish
del "Venv Manager.exe"
rmdir /s /q build
rmdir /s /q dist

:: Perform publish
call venv\Scripts\activate.bat
call py -m PyInstaller publish.spec

:: Move .exe to repo level
move dist\"Venv Manager.exe" "Venv Manager.exe"

:: Delete publishing dirs
rmdir /s /q build
rmdir /s /q dist
