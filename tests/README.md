# Testing Documentation

## Overview

This directory contains the test suite for the Markdown to PDF converter. The tests verify core functionality including Markdown parsing, PDF generation, table handling, and metadata processing.

## Test Structure

```
tests/
├── inputs/
│   ├── complete_test.md       # Tests all Markdown features
│   └── table_test.md         # Tests table formatting
├── outputs/                   # Generated PDFs
└── run_tests.sh              # Test runner script
```

## Test Cases

### Core Functionality Tests
1. `test_0_no_watermark.pdf`
   - Basic Markdown to PDF conversion
   - All Markdown syntax elements
   - Code blocks with syntax highlighting
   - Lists and nested lists
   - Links and images

### Table Tests
1. Simple tables
2. Complex tables with headers
3. Wide tables with auto-scaling
4. Tables with special characters

### Metadata Tests
1. YAML frontmatter parsing
2. Custom metadata fields
3. PDF properties

## Running Tests

```bash
./tests/run_tests.sh
```

## Expected Output

The test script will:
1. Clean previous test outputs
2. Run conversion tests
3. Generate PDFs in `outputs/` directory
4. Display test results

## Test Results

A successful test run will:
- Generate PDFs for each test case
- Show "Successfully converted" messages
- Create files with proper formatting

## Known Limitations

1. No watermark support in current version
2. Large tables may require horizontal scrolling
3. Some complex Markdown extensions not supported

## Adding New Tests

1. Add test Markdown files to `inputs/`
2. Update `run_tests.sh` with new test cases
3. Add expected outputs to this documentation
