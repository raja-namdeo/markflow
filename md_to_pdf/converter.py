"""
Core module for converting Markdown to PDF.
"""
import markdown
from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import frontmatter
import os
from pathlib import Path
import tempfile
from typing import Optional, Union
import chardet

class MarkdownInput:
    """Handles different types of markdown input and validation."""
    
    @staticmethod
    def validate_content(content: str) -> bool:
        """
        Validate markdown content.
        
        Args:
            content: The markdown content to validate
            
        Returns:
            bool: True if content is valid
        """
        return bool(content and len(content.strip()) > 0)
    
    @staticmethod
    def sanitize_content(content: str) -> str:
        """
        Sanitize and normalize markdown content.
        
        Args:
            content: The markdown content to sanitize
            
        Returns:
            str: Sanitized content
        """
        # Normalize line endings
        content = content.replace('\r\n', '\n')
        # Remove null bytes
        content = content.replace('\0', '')
        return content
    
    @staticmethod
    def load_from_file(file_path: str) -> str:
        """
        Load markdown content from a file with encoding detection.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            str: The file contents
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is empty or invalid
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        # Read raw bytes first for encoding detection
        with open(file_path, 'rb') as f:
            raw_content = f.read()
            
        if not raw_content:
            raise ValueError("File is empty")
            
        # Detect encoding
        result = chardet.detect(raw_content)
        encoding = result['encoding'] or 'utf-8'
        
        # Decode content
        content = raw_content.decode(encoding)
        return MarkdownInput.sanitize_content(content)
    
    @staticmethod
    def load_from_string(content: str) -> str:
        """
        Load markdown content from a string.
        
        Args:
            content: The markdown content string
            
        Returns:
            str: Sanitized content
            
        Raises:
            ValueError: If content is empty or invalid
        """
        if not MarkdownInput.validate_content(content):
            raise ValueError("Content is empty or invalid")
        return MarkdownInput.sanitize_content(content)

class MarkdownToPDFConverter:
    """Main converter class that handles the conversion process."""
    
    def __init__(self, template_dir: Optional[str] = None):
        """
        Initialize the converter.
        
        Args:
            template_dir: Directory containing HTML templates
        """
        if template_dir is None:
            template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.markdown_input = MarkdownInput()
        
    def convert_string(self, content: str, output_file: str, template_name: str = 'default.html') -> bool:
        """
        Convert markdown string to PDF.
        
        Args:
            content: Markdown content string
            output_file: Path where to save the PDF
            template_name: Name of the HTML template to use
            
        Returns:
            bool: True if conversion was successful
        """
        try:
            content = self.markdown_input.load_from_string(content)
            return self._convert_to_pdf(content, output_file, template_name)
        except Exception as e:
            print(f"Error during conversion: {str(e)}")
            return False
            
    def convert(self, input_file: str, output_file: str, template_name: str = 'default.html') -> bool:
        """
        Convert markdown file to PDF.
        
        Args:
            input_file: Path to input Markdown file
            output_file: Path where to save the PDF
            template_name: Name of the HTML template to use
            
        Returns:
            bool: True if conversion was successful
        """
        try:
            content = self.markdown_input.load_from_file(input_file)
            return self._convert_to_pdf(content, output_file, template_name)
        except Exception as e:
            print(f"Error during conversion: {str(e)}")
            return False
    
    def _convert_to_pdf(self, content: str, output_file: str, template_name: str) -> bool:
        """
        Internal method to convert markdown to PDF.
        
        Args:
            content: Processed markdown content
            output_file: Output PDF path
            template_name: Template name
            
        Returns:
            bool: True if successful
        """
        # Convert markdown to HTML
        html_content = markdown.markdown(
            content,
            extensions=['tables', 'fenced_code', 'codehilite']
        )
        
        # Get the template
        template = self.env.get_template(template_name)
        
        # Render the template with our HTML content
        final_html = template.render(content=html_content)
        
        # Create a temporary file to store the HTML
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tmp:
            tmp.write(final_html)
            tmp_path = tmp.name
        
        try:
            # Ensure output directory exists
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Convert to PDF using the file-based approach
            HTML(filename=tmp_path).write_pdf(output_file)
            return True
        finally:
            # Clean up the temporary file
            os.unlink(tmp_path)
