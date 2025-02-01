#!/bin/bash

echo "Running Markdown to PDF Converter Tests..."

# Test 0: Basic conversion (no watermark)
echo "Test 0: Basic conversion..."
python3 -m md_to_pdf.cli convert-file tests/inputs/complete_test.md tests/outputs/test_0_basic.pdf

# Test 1: Table handling
echo "Test 1: Table handling..."
python3 -m md_to_pdf.cli convert-file tests/inputs/table_test.md tests/outputs/test_1_tables.pdf

# Test 2: String input
echo "Test 2: String input..."
echo "# Test Document\n\nThis is a test." | python3 -m md_to_pdf.cli convert-string tests/outputs/test_2_string.pdf

echo "Cleaning up old test files..."
find tests/outputs -type f -name "*.pdf" -mtime +1 -delete

echo "All tests completed. Check the outputs in tests/outputs/ directory."
echo ""
echo "Generated test files:"
ls -l tests/outputs/*.pdf
