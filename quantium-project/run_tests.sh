#!/bin/bash

# Activate virtual environment (if exists)
if [ -d "venv" ]; then
    source venv/Scripts/activate
fi

# Run tests
pytest

# Check result
if [ $? -eq 0 ]; then
    echo "All tests passed ✅"
    exit 0
else
    echo "Tests failed ❌"
    exit 1
fi