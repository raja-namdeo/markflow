# Markdown to PDF Converter - Execution Documentation

<<<<<<< HEAD
<<<<<<< HEAD
## Project Status (as of 2025-02-02)

### Completed Features

#### Epic 1: Core Conversion ( Complete)
- Full Markdown syntax support
- Table handling with auto-scaling
- Code syntax highlighting
- YAML frontmatter support
- Custom template system
- String and file input support
- Comprehensive test coverage

#### Epic 2: User Interface ( In Progress)
- Basic GUI implementation complete:
  - Split-pane interface with editor and preview
  - Real-time Markdown preview
  - File operations (New, Open, Save)
  - PDF export integration
  - Basic syntax highlighting
  - Error handling and user feedback
  - Cross-platform compatibility (PyQt6-based)

### Upcoming Features

#### Epic 2: User Interface (Remaining Tasks)
1. Configuration Panel
   - Template selection
   - Style customization
   - Export settings
   - User preferences

2. Enhanced Editor Features
   - Advanced syntax highlighting
   - Auto-completion
   - Spell checking
   - Find and replace

3. Preview Enhancements
   - Custom style themes
   - Print preview
   - Zoom controls
   - Table of contents

#### Epic 3: Deployment & Non-Functional Requirements ( Planned)
1. Cross-Platform Packaging
   - Windows installer
   - macOS package
   - Linux package (deb, rpm)
   - PyPI distribution

2. Performance Optimization
   - Large document handling
   - Memory usage optimization
   - Startup time improvement
   - Preview rendering optimization

3. Advanced Features
   - Plugin system
   - Custom template management
   - Export format options
   - Batch processing

### Technical Implementation

#### Core Module
- Uses WeasyPrint for PDF generation
- Python-Markdown for parsing
- Jinja2 for templating
- BeautifulSoup4 for HTML processing

#### GUI Module
- Built with PyQt6 framework
- Components:
  - MainWindow: Application shell and menu system
  - MarkdownEditor: Text editing component
  - PreviewPanel: Live preview using QtWebEngine
  - Converter integration for PDF export

#### Testing
- Comprehensive test suite for core functionality
- GUI component tests with PyQt6 test framework
- Automated test runner (run_tests.sh)
- Integration tests for complete workflows

### Development Guidelines

#### Code Organization
```
md_to_pdf/
├── __init__.py
├── converter.py      # Core conversion logic
├── templates/        # HTML templates
└── gui/             # GUI components
    ├── __init__.py
    ├── main_window.py
    ├── editor.py
    └── preview.py
```

#### Testing Strategy
1. Unit Tests
   - Core conversion functions
   - GUI components
   - Template handling

2. Integration Tests
   - Complete conversion workflow
   - GUI interactions
   - File operations

3. Manual Testing Requirements
   - Cross-platform verification
   - Large document handling
   - User interface usability
   - Export quality verification

### Installation Requirements

#### System Dependencies (Fedora)
=======
## Project Overview
A Python-based tool to convert Markdown files to beautifully formatted PDFs with support for various Markdown features and customization options.
=======
## Project Status
Current Version: 1.0.0
Last Updated: 2025-02-02
>>>>>>> 8c87781 (feat(tables): enhance table handling and documentation)

## Features Implementation Status

### Core Features
- FR1: Input Handling (5 points) 
  - File upload with encoding detection
  - Text paste via stdin
  - Input validation and sanitization
  - Error handling for invalid inputs
  - Support for different file encodings

- FR2: Markdown Formatting (8 points) 
  - Headings (h1-h6) with proper styling
  - Ordered and unordered lists with nesting
  - Code blocks with syntax highlighting
  - Inline code formatting
  - Blockquotes
  - Links and images
  - Horizontal rules
  - Basic text formatting (bold, italic)

- FR3: Table Handling (8 points) 
  - Basic table support
  - Auto-scaling for wide tables
  - Responsive design for different content widths
  - Font size adjustments for better readability
  - Content-aware formatting
  - Header repetition on new pages

- FR4: A4 Page Configuration (5 points) 
  - Default A4 size configuration
  - Proper margin settings (2.5cm)
  - Page numbering
  - Content scaling for page size
  - Consistent page layouts

- FR5: Watermark Configuration ( points) 
  - Not yet implemented

## Project Structure
```
md_to_pdf/
├── __init__.py         # Package initialization
├── converter.py        # Core conversion logic
├── cli.py             # Command-line interface
└── templates/         
    └── default.html    # HTML/CSS template
```

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd python-md-to-pdf-converstor

# Install dependencies
python3 -m pip install -r requirements.txt

# For Fedora, install system dependencies
sudo dnf install python3-pip python3-cffi python3-brotli pango harfbuzz pango-devel cairo-devel
```

### Basic Usage
1. Convert a Markdown file to PDF:
```bash
python3 -m md_to_pdf.cli convert-file input.md output.pdf
```

2. Convert Markdown text from stdin:
```bash
echo "# Test" | python3 -m md_to_pdf.cli convert-string output.pdf
```

## Testing Instructions

<<<<<<< HEAD
### System Requirements
For Fedora:
>>>>>>> 5b55f65 (feat(core): implement markdown to pdf core conversion module)
```bash
sudo dnf install python3-pip python3-cffi python3-brotli pango harfbuzz pango-devel cairo-devel
```

<<<<<<< HEAD
#### Python Dependencies
```bash
pip install -r requirements.txt
```

### Usage

#### Command Line Interface
```python
from md_to_pdf import MarkdownToPDFConverter
converter = MarkdownToPDFConverter()
converter.convert('input.md', 'output.pdf')
```

#### Graphical Interface
```bash
python3 run_gui.py
```

### Known Issues and Limitations
1. Memory usage with large documents needs optimization
2. Template customization requires manual file editing
3. Limited support for complex table layouts
4. Watermark feature moved to backlog

### Future Roadmap

#### Version 2.0
- Complete GUI implementation
- Advanced editor features
- Template management system
- Performance optimizations

#### Version 2.1
- Plugin system
- Theme support
- Export format options
- Configuration management

#### Version 3.0
- Cloud integration
- Collaborative editing
- Version control
- Asset management

### Contributing Guidelines
1. Fork the repository
2. Create feature branch
3. Follow PEP 8 style guide
4. Include tests for new features
5. Update documentation
6. Submit pull request

### License
MIT License - See LICENSE file for details
=======
=======
### 1. Basic Features Test
Use `test_features.md`:
```markdown
# Heading 1
## Heading 2

- List item 1
- List item 2

1. Numbered item 1
2. Numbered item 2

\`\`\`python
def test():
    print("Hello")
\`\`\`
```

### 2. Table Features Test
Use `table_test.md` to test various table scenarios:
- Regular tables
- Wide tables
- Long content
- Many rows
- Numeric data

### 3. Page Configuration Test
Test A4 formatting and page breaks with `page_test.md`

## Known Issues and Limitations
1. Tables wider than page width may scale down for readability
2. Watermark feature not yet implemented
3. Some complex markdown extensions not supported

## Architecture
See `docs/architecture.svg` for the system flow diagram.

## Performance Metrics
- Average conversion time: < 2 seconds for standard documents
- Memory usage: ~100MB for typical operations
- Supported file size: Up to 10MB markdown files

>>>>>>> 8c87781 (feat(tables): enhance table handling and documentation)
## Development Notes
- Used WeasyPrint for PDF generation
- Implemented file-based approach for better resource handling
- Added comprehensive CSS styling for all markdown elements
- Included error handling and input validation
- Created modular code structure for maintainability
<<<<<<< HEAD
>>>>>>> 5b55f65 (feat(core): implement markdown to pdf core conversion module)
=======

## Dependencies
- Python 3.7+
- WeasyPrint 52.5
- Markdown 3.4.3
- Other dependencies in requirements.txt

## System Requirements
For Fedora:
```bash
sudo dnf install python3-pip python3-cffi python3-brotli pango harfbuzz pango-devel cairo-devel
```
>>>>>>> 8c87781 (feat(tables): enhance table handling and documentation)
