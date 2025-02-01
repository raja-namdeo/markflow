# Testing Documentation

## Overview
This document describes the testing approach for the Markdown to PDF converter project.

## Test Structure
The tests are organized into two main categories:

1. **Core Functionality Tests**
   - Located in `tests/test_core.py`
   - Tests the basic markdown to PDF conversion functionality
   - No GUI dependencies required
   - Fast and reliable for CI/CD pipelines

2. **GUI Tests** (Optional)
   - Located in `tests/test_gui.py`
   - Tests the graphical user interface components
   - Requires PyQt6 and additional GUI dependencies
   - Best run manually during development
   - Note: Some GUI tests may be flaky due to event timing issues in PyQt6

## Running Tests

### Core Tests Only
```bash
python3 -m unittest tests/test_core.py
```

### All Tests (including GUI)
```bash
./tests/run_tests.sh
```

## Manual Testing Guidelines

### Core Functionality
1. Test basic markdown to PDF conversion
2. Verify PDF output quality
3. Check error handling for invalid input

### GUI Testing
1. **Editor Component**
   - Verify text input and display
   - Check syntax highlighting
   - Test undo/redo functionality

2. **Preview Panel**
   - Verify real-time markdown preview
   - Check HTML rendering
   - Test scrolling synchronization

3. **File Operations**
   - Test new file creation
   - Verify file open/save operations
   - Check PDF export functionality

## Known Issues
1. GUI tests may occasionally fail due to Qt event loop timing issues
2. These failures don't affect actual functionality
3. Manual testing is recommended for GUI components

## Best Practices
1. Always run core tests before committing changes
2. Manually test GUI features after significant changes
3. Document any new test cases added
4. Keep GUI and core functionality tests separate

## Future Improvements
1. Improve GUI test reliability
2. Add more comprehensive core functionality tests
3. Implement integration tests for complex workflows
