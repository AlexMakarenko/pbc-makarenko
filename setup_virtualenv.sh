#!/usr/bin/env bash

# Create a virtual environment
virtualenv venv
# Activate virtual environment
source venv/bin/activate
# Install packages from requirements.txt
pip install -r requirements.txt