@echo off
setlocal enabledelayedexpansion

REM Loop through all subfolders
for /r %%i in (*) do (
    REM Check if the current item is a file
    if exist "%%i" (
        REM Check if the parent directory is C:\Path\To\Directory
        set parent=%%~pi
        if "!parent:%cd%\=!"=="!parent!" (
            REM Attempt to move the file to the current folder
            move "%%i" "%cd%" > nul 2>&1
        )
    )
)

echo All files moved to the current folder.
pause
