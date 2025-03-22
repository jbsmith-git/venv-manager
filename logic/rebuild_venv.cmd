@echo off

:: Compute filepaths
set "repo_filepath=%~1"
set "venv_filepath=%~1\venv"
set "reqs_filepath=%~1\requirements.txt"

:: Check repo exists
if not exist "%repo_filepath%" (
    echo Error: Repo does not exist >&2
    exit /b 1
)

:: Change directory to repo
call cd "%repo_filepath%"

:: Rebuild the venv
if exist "%venv_filepath%" (
    echo Deleting %venv_filepath%
    rmdir /s /q "%venv_filepath%"
) else (
    echo Existing venv not found
)
call py -m venv venv

:: Activate the venv
call venv\Scripts\activate.bat

:: Upgrade pip and purge the cache
call python.exe -m pip install --upgrade pip
call pip cache purge

:: Install required packages
if exist "%reqs_filepath%" (
    echo Installing requirements.txt
    call pip install -r requirements.txt
) else (
    echo requirements.txt not found
)

echo Venv rebuild complete
