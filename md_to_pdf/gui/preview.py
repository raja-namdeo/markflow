"""
Preview panel for rendered Markdown content.
"""
import os
import tempfile
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import markdown
import logging

logger = logging.getLogger(__name__)

class PreviewPanel(QWidget):
    """Preview panel that renders Markdown as HTML."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.web_view = None
        self.temp_dir = tempfile.mkdtemp(prefix='md_preview_')
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the preview panel UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        
        # Set default content
        self.update_preview("")
        
    def update_preview(self, content):
        """Update the preview with new Markdown content."""
        try:
            # Convert Markdown to HTML
            html_content = markdown.markdown(
                content,
                extensions=['tables', 'fenced_code', 'codehilite']
            )
            
            # Add styling
            styled_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>{content.split('\n')[0] if content else 'Preview'}</title>
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, 
                                   "Segoe UI", Roboto, "Helvetica Neue", 
                                   Arial, sans-serif;
                        line-height: 1.6;
                        padding: 20px;
                        max-width: 800px;
                        margin: 0 auto;
                    }}
                    h1, h2, h3, h4, h5, h6 {{
                        color: #2c3e50;
                        margin-top: 24px;
                        margin-bottom: 16px;
                    }}
                    code {{
                        background-color: #f6f8fa;
                        padding: 2px 4px;
                        border-radius: 3px;
                        font-family: "SFMono-Regular", Consolas, 
                                   "Liberation Mono", Menlo, Courier, 
                                   monospace;
                    }}
                    pre code {{
                        display: block;
                        padding: 16px;
                        overflow-x: auto;
                    }}
                    blockquote {{
                        border-left: 4px solid #dfe2e5;
                        padding-left: 16px;
                        color: #6a737d;
                        margin: 0;
                    }}
                    table {{
                        border-collapse: collapse;
                        width: 100%;
                        margin: 16px 0;
                    }}
                    th, td {{
                        border: 1px solid #dfe2e5;
                        padding: 8px;
                    }}
                    th {{
                        background-color: #f6f8fa;
                    }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
            
            # Write to temporary file
            temp_path = os.path.join(self.temp_dir, 'preview.html')
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.write(styled_html)
            
            # Load in web view
            self.web_view.setUrl(QUrl.fromLocalFile(temp_path))
            logger.debug("Preview updated successfully")
            
        except Exception as e:
            logger.error("Error updating preview: %s", str(e))
            self.web_view.setHtml(f"<h1>Error</h1><p>{str(e)}</p>")
    
    def cleanup(self):
        """Clean up temporary files."""
        try:
            if os.path.exists(self.temp_dir):
                for file in os.listdir(self.temp_dir):
                    os.remove(os.path.join(self.temp_dir, file))
                os.rmdir(self.temp_dir)
        except Exception as e:
            logger.error("Error cleaning up preview files: %s", str(e))
    
    def closeEvent(self, event):
        """Handle cleanup when closing."""
        self.cleanup()
        super().closeEvent(event)
