# MarkFlow User Guide

> **Author**: Raja Namdeo  
> **Email**: cse.rajanamdeo@gmail.com  
> **Role**: Software Developer  

## Getting Started

### Installation

#### Basic Installation (CLI Only)
```bash
pip install markflow
```

#### Full Installation (with GUI)
```bash
pip install markflow[gui]
```

### Quick Start

#### CLI Usage
```bash
# Basic conversion
markflow input.md output.pdf

# With custom styling
markflow input.md output.pdf --style custom.css
```

#### GUI Usage
1. Launch the application:
   ```bash
   markflow-gui
   ```
2. Start typing in the editor
3. See real-time preview
4. Save or export to PDF

## Features in Detail

### Markdown Support

#### Text Formatting
```markdown
# Heading 1
## Heading 2

**Bold text**
*Italic text*
~~Strikethrough~~

> Blockquote
```

#### Lists
```markdown
1. Ordered item
2. Another item
   - Subitem
   - Another subitem

- Unordered item
- Another item
  * Nested item
  * Another nested item
```

#### Code Blocks
```markdown
Inline `code` example

```python
def hello():
    print("Hello, World!")
```
```

#### Tables
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

### GUI Features

#### Editor
- Syntax highlighting
- Line numbers
- Auto-indentation
- Undo/redo support

#### Preview Panel
- Real-time updates
- Scroll synchronization
- Zoom controls

#### File Operations
- New file (Ctrl+N)
- Open file (Ctrl+O)
- Save file (Ctrl+S)
- Export PDF (Ctrl+E)

### Customization

#### Custom CSS
Create a CSS file for styling:
```css
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
    padding: 2em;
}

h1, h2, h3 {
    color: #2c3e50;
}

code {
    background: #f8f9fa;
    padding: 0.2em 0.4em;
    border-radius: 3px;
}
```

Apply the style:
```bash
markflow input.md output.pdf --style custom.css
```

## Tips and Tricks

### Performance
- Split large documents into sections
- Use appropriate image formats
- Optimize table layouts

### Best Practices
1. Use consistent heading structure
2. Include table of contents for long documents
3. Preview before final export
4. Use relative paths for images

### Common Issues

#### Problem: Images not showing
- Ensure correct path to images
- Use supported image formats
- Check file permissions

#### Problem: Table formatting issues
- Keep tables simple
- Use consistent column widths
- Avoid nested tables

#### Problem: PDF generation slow
- Optimize image sizes
- Split large documents
- Use simpler formatting

## Advanced Usage

### Python API
```python
from markflow.core import convert_to_pdf

# Basic conversion
convert_to_pdf('input.md', 'output.pdf')

# With custom style
convert_to_pdf(
    input_file='input.md',
    output_file='output.pdf',
    style_file='custom.css'
)
```

### Command Line Options
```bash
# Show help
markflow --help

# Version info
markflow --version

# Custom style
markflow input.md output.pdf --style custom.css
```

## Getting Help

### Support Channels
- GitHub Issues
- Documentation
- Community Forums

### Reporting Bugs
1. Check existing issues
2. Include reproduction steps
3. Attach example files
4. Describe expected behavior

## Contributing
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

See [Contributing Guidelines](../CONTRIBUTING.md) for details.
