"""
Core functionality for MarkFlow - Markdown to PDF converter
"""
import markdown
import weasyprint
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def convert_to_pdf(input_file: str, output_file: str, style_file: str = None) -> bool:
    """Convert a Markdown file to PDF.
    
    Args:
        input_file: Path to input markdown file
        output_file: Path for output PDF file
        style_file: Optional CSS style file path
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Read markdown content
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = markdown.markdown(
            md_content,
            extensions=['tables', 'fenced_code', 'codehilite']
        )
        
        # Add basic styling
        base_css = """
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 2em; }
        h1, h2, h3 { color: #2c3e50; }
        code { background: #f8f9fa; padding: 0.2em 0.4em; border-radius: 3px; }
        pre { background: #f8f9fa; padding: 1em; border-radius: 5px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f8f9fa; }
        """
        
        # Combine with custom CSS if provided
        if style_file:
            with open(style_file, 'r') as f:
                base_css += f.read()
        
        # Create full HTML document
        html_doc = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{base_css}</style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Convert to PDF
        weasyprint.HTML(string=html_doc).write_pdf(output_file)
        logger.info(f"Successfully converted {input_file} to {output_file}")
        return True
        
    except Exception as e:
        logger.error(f"Error converting {input_file} to PDF: {str(e)}")
        return False
