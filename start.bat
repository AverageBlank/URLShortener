@echo off
rem Activate the virtual environment
call .venv\Scripts\activate.bat

rem Set the FLASK_APP environment variable
set FLASK_APP=app.py

rem Run the Flask application
flask run
