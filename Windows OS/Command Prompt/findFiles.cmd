@echo off
cd /d %1

set "Desktop=%USERPROFILE%\Desktop"
set "OutputFile=%Desktop%\Test\videos.txt"

echo Searching for .MTS, .mov, and .mp4 files in %CD%...

(
    echo Files with .MTS extension:
    dir /b /s *.MTS
    echo.
    echo Files with .mov extension:
    dir /b /s *.mov
    echo.
    echo Files with .mp4 extension:
    dir /b /s *.mp4
) > "%OutputFile%"

echo Search complete. Results written to %OutputFile%.

pause