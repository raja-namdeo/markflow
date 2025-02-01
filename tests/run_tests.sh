#!/bin/bash

# Run all tests
echo "Running core functionality tests..."
python3 -m unittest discover -s tests -p "test_*.py" -v

# Check if tests passed
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
