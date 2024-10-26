#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Set the FLASK_APP environment variable
export FLASK_APP=app.py 

# Run the Flask application
flask run
