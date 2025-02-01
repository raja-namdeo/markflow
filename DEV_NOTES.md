# Development Notes

## Project Setup (Phase 1)

### Technology Choices
1. **Python**: Chosen for its rich ecosystem of text processing libraries
2. **WeasyPrint**: A powerful HTML/CSS to PDF converter
   - Advantages: Supports modern CSS features
   - Can handle complex layouts
3. **Jinja2**: Template engine for generating HTML
   - Allows for customizable PDF styling
   - Separates content from presentation

### Project Structure
```
md_to_pdf/
├── __init__.py         # Package initialization
├── converter.py        # Core conversion logic
├── templates/          # HTML templates
│   └── default.html    # Default template
└── cli.py             # Command-line interface
```

### Development Best Practices
1. **Documentation First**: Writing documentation before code helps in:
   - Clear understanding of functionality
   - Better API design
   - Future maintainability

2. **Modular Design**: 
   - Separate concerns (conversion, templating, CLI)
   - Easy to test and maintain
   - Extensible for future features

3. **Error Handling**:
   - Proper error messages
   - Graceful failure handling
   - User-friendly feedback

### Learning Resources
1. WeasyPrint Documentation: https://doc.courtbouillon.org/weasyprint/
2. Markdown in Python: https://python-markdown.github.io/
3. Jinja2 Templates: https://jinja.palletsprojects.com/

## Installation Requirements

### System Dependencies
Before running the application, you need to install these system dependencies:

1. Python 3.7 or higher
2. pip (Python package manager)
3. WeasyPrint system dependencies:
   ```bash
   # For Ubuntu/Debian
   sudo apt-get install python3-pip python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
   
   # For Fedora
   sudo dnf install python3-pip python3-cffi python3-brotli pango harfbuzz
   
   # For macOS
   brew install python3 pango harfbuzz
   ```

### Python Dependencies
After installing system dependencies, install Python packages:
```bash
python3 -m pip install -r requirements.txt
```

## Next Steps
- [ ] Implement basic conversion functionality
- [ ] Add template support
- [ ] Create CLI interface
- [ ] Add styling options
