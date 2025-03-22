@echo off

rmdir /s /q build
rmdir /s /q dist

call venv\Scripts\activate.bat
call py -m PyInstaller publish.spec
