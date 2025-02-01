# Markdown to PDF Converter

A robust Python-based tool for converting Markdown documents to PDF with advanced formatting options.

## Features

- Full Markdown syntax support
- GitHub-flavored Markdown extensions
- Code syntax highlighting
- Table support with auto-scaling
- Custom templates
- YAML frontmatter support
- Custom metadata fields
- Watermark support (coming soon)

## Installation

1. Install system dependencies (Fedora):
   ```bash
   sudo dnf install python3-pip python3-cffi python3-brotli pango harfbuzz pango-devel cairo-devel
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```python
from md_to_pdf import MarkdownToPDFConverter

# Initialize converter
converter = MarkdownToPDFConverter()

# Convert file
converter.convert('input.md', 'output.pdf')

# Convert string
markdown_content = '# Hello World\n\nThis is a test.'
converter.convert_string(markdown_content, 'output.pdf')
```

### Template Customization

The converter supports custom HTML templates. Place your templates in the `templates` directory and specify the template name when converting:

```python
converter.convert('input.md', 'output.pdf', template_name='custom.html')
```

### Document Metadata

Add YAML frontmatter to your Markdown files for custom metadata:

```markdown
---
title: My Document
author: John Doe
date: 2025-02-02
---

# Document Content
...
```

## Development

### Running Tests

```bash
./tests/run_tests.sh
```

### Project Structure

```
md_to_pdf/
├── __init__.py
├── converter.py
├── watermark.py
└── templates/
    └── default.html
tests/
├── inputs/
├── outputs/
└── run_tests.sh
```

## Known Issues

1. Watermark feature is currently in development and has been moved to the backlog
2. Performance optimization needed for large documents
3. Limited support for complex table layouts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- WeasyPrint for PDF generation
- Python-Markdown for Markdown parsing
- Jinja2 for templating
- BeautifulSoup4 for HTML processing
