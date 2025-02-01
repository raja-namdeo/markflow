# MarkFlow API Reference

> **Author**: Raja Namdeo  
> **Email**: cse.rajanamdeo@gmail.com  
> **Role**: Software Developer  

## Core Module

### `convert_to_pdf`

Convert a Markdown file to PDF.

```python
from markflow.core import convert_to_pdf

def convert_to_pdf(
    input_file: str,
    output_file: str,
    style_file: Optional[str] = None
) -> bool:
    """
    Convert a Markdown file to PDF.
    
    Args:
        input_file: Path to input markdown file
        output_file: Path for output PDF file
        style_file: Optional CSS style file path
    
    Returns:
        bool: True if conversion successful, False otherwise
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        PermissionError: If output location is not writable
    """
```

Example usage:
```python
# Basic conversion
convert_to_pdf('input.md', 'output.pdf')

# With custom styling
convert_to_pdf('input.md', 'output.pdf', 'style.css')
```

## GUI Module

### `MarkdownEditor`

Interactive Markdown editor component.

```python
from markflow.gui import MarkdownEditor

class MarkdownEditor(QPlainTextEdit):
    """
    Markdown editor with syntax highlighting and real-time preview.
    
    Signals:
        contentChanged(str): Emitted when content changes
    """
    
    def setPlainText(self, text: str) -> None:
        """Set the editor content."""
        
    def toPlainText(self) -> str:
        """Get the current editor content."""
```

### `PreviewPanel`

Real-time Markdown preview component.

```python
from markflow.gui import PreviewPanel

class PreviewPanel(QWidget):
    """
    Preview panel showing rendered Markdown.
    """
    
    def update_preview(self, content: str) -> None:
        """Update the preview with new content."""
```

### `MainWindow`

Main application window.

```python
from markflow.gui import MainWindow

class MainWindow(QMainWindow):
    """
    Main window containing editor and preview.
    """
    
    def new_file(self) -> None:
        """Create a new file."""
        
    def open_file(self) -> None:
        """Open an existing file."""
        
    def save_file(self) -> None:
        """Save current file."""
        
    def export_pdf(self) -> None:
        """Export current content as PDF."""
```

## CLI Module

### Command Line Interface

```python
from markflow.cli import cli

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--style', '-s', help='CSS style file')
def cli(input_file, output_file, style=None):
    """Convert Markdown files to PDF."""
```

## Constants

### Version Information
```python
from markflow import __version__

VERSION = '1.0.0'
```

### Default Styles
```python
DEFAULT_STYLE = """
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    padding: 2em;
}
"""
```

## Error Handling

### Custom Exceptions
```python
class MarkFlowError(Exception):
    """Base exception for MarkFlow errors."""
    pass

class ConversionError(MarkFlowError):
    """Raised when PDF conversion fails."""
    pass

class StyleError(MarkFlowError):
    """Raised when style processing fails."""
    pass
```

## Type Hints

```python
from typing import Optional, Dict, List

PathLike = Union[str, Path]
StyleDict = Dict[str, str]
```

## Event System

### Signals
```python
from PyQt6.QtCore import pyqtSignal

contentChanged = pyqtSignal(str)
conversionComplete = pyqtSignal(bool)
```

## Configuration

### Default Settings
```python
DEFAULT_CONFIG = {
    'theme': 'light',
    'font_size': 12,
    'line_numbers': True,
    'auto_preview': True,
    'preview_delay': 500,  # ms
}
```

## Utility Functions

### File Operations
```python
def get_safe_filename(title: str) -> str:
    """Convert a title to a safe filename."""
    
def ensure_extension(filename: str, ext: str) -> str:
    """Ensure filename has the correct extension."""
```

## Examples

### Basic Usage
```python
from markflow.core import convert_to_pdf

# Convert a file
convert_to_pdf('input.md', 'output.pdf')

# With custom style
convert_to_pdf(
    input_file='input.md',
    output_file='output.pdf',
    style_file='custom.css'
)
```

### GUI Integration
```python
from markflow.gui import MainWindow
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
