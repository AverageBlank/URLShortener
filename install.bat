@echo off
setlocal enabledelayedexpansion

rem Create a .env file if it doesn't exist
if not exist ".env" (
    echo. > .env
)

rem Function to setup URI and key
call :get_input "Enter your MongoDB URI" "link"
call :get_input "Enter your secret key" "SECRET_KEY"

echo Setup complete. Installing dependencies...

rem Create a virtual environment if it doesn't exist
if not exist ".venv" (
    python -m venv .venv
)

rem Activate the virtual environment
call .venv\Scripts\activate.bat

rem Install required libraries
pip install -r requirements.txt

echo Installation complete. You can now run the application using 'start.bat'.
exit /b

:get_input
set prompt=%~1
set key=%~2

set valueExists=0
for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    if "%%A"=="%key%" (
        set valueExists=1
        set current_value=%%B
    )
)

if !valueExists! equ 1 (
    echo Value for '%key%' already exists in the .env file.
    set /p action="Would you like to view or edit it? (n to move to next) (v/e/n): "
    if /i "!action!"=="v" (
        echo %key% is currently set to: !current_value!
    ) else if /i "!action!"=="e" (
        set /p input_value="Enter new value for %key% (Press Enter to keep current value): "
        if "!input_value!"=="" (
            echo Keeping current value: !current_value!
        ) else (
            call :set_env_value "%key%" "!input_value!"
        )
    ) else if /i "!action!"=="n" (
        exit /b
    ) else (
        echo Invalid option. Please enter 'v' to view, 'e' to edit, or 'n' to go to the next variable.
        call :get_input "!prompt!" "!key!"
    )
) else (
    set /p input_value="%prompt%: "
    call :set_env_value "%key%" "!input_value!"
)

exit /b

:set_env_value
set key=%~1
set value=%~2
findstr /b /c:"%key%=" .env >nul
if %errorlevel%==0 (
    powershell -Command "(Get-Content .env) -replace '^%key%=.*', '%key%=%value%' | Set-Content .env"
) else (
    echo %key%=%value% >> .env
)
exit /b
