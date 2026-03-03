#!/bin/bash

# GACP Protocol MVP One-Click Run Script (Mac/Linux version)

# Set working directory
cd "$(dirname "$0")"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3.10+ not found, please install Python first"
    exit 1
fi

# Check if dependencies are installed
if ! pip3 list | grep -q "pydantic"; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Dependency installation failed"
        exit 1
    fi
fi

# Run MVP main program
echo "Running GACP Protocol MVP..."
python3 02-Core-Code/gacp_mvp.py

# Wait for user input
echo "Press any key to continue..."
read -n 1 -s