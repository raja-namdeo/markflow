"""
Watermark handling module for PDF generation.
"""
from typing import Dict, Optional, Tuple
import math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from PyPDF2 import PdfReader, PdfWriter
import io
import os

class WatermarkConfig:
    """Configuration for watermark rendering."""
    
    POSITIONS = {
        'center': (0.5, 0.5),
        'top-left': (0.25, 0.75),
        'top-right': (0.75, 0.75),
        'bottom-left': (0.25, 0.25),
        'bottom-right': (0.75, 0.25)
    }
    
    def __init__(
        self,
        text: str,
        position: str = 'center',
        rotation: int = -45,
        opacity: float = 0.3,
        color: str = '#000000',
        font_size: Optional[int] = None
    ):
        """
        Initialize watermark configuration.
        
        Args:
            text: Watermark text
            position: One of 'center', 'top-left', 'top-right', 'bottom-left', 'bottom-right'
            rotation: Rotation angle in degrees
            opacity: Opacity value between 0 and 1
            color: Color in hex format
            font_size: Optional font size in points
        """
        self.text = text
        self.position = position
        self.rotation = rotation
        self.opacity = max(0.15, min(1.0, opacity))
        self.color = self._hex_to_rgb(color)
        self.font_size = font_size or 100  # Default large font size
        
    def _hex_to_rgb(self, hex_color: str) -> Color:
        """Convert hex color to RGB."""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16) / 255.0
        g = int(hex_color[2:4], 16) / 255.0
        b = int(hex_color[4:6], 16) / 255.0
        return Color(r, g, b, alpha=self.opacity)
    
    def get_position(self) -> Tuple[float, float]:
        """Get position coordinates as fractions."""
        return self.POSITIONS.get(self.position, self.POSITIONS['center'])

def create_watermark(config: WatermarkConfig, page_size: Tuple[float, float]) -> io.BytesIO:
    """
    Create watermark PDF page.
    
    Args:
        config: WatermarkConfig instance
        page_size: Tuple of (width, height) in points
        
    Returns:
        BytesIO: PDF content with watermark
    """
    # Create PDF buffer
    buffer = io.BytesIO()
    
    # Create PDF canvas
    c = canvas.Canvas(buffer, pagesize=page_size)
    
    # Set font and color
    c.setFont("Helvetica-Bold", config.font_size)
    c.setFillColor(config.color)
    
    # Get position
    x_ratio, y_ratio = config.get_position()
    x = page_size[0] * x_ratio
    y = page_size[1] * y_ratio
    
    # Save state and apply transformations
    c.saveState()
    c.translate(x, y)
    c.rotate(config.rotation)
    
    # Draw watermark multiple times for better coverage
    text_width = c.stringWidth(config.text, "Helvetica-Bold", config.font_size)
    text_height = config.font_size
    
    # Main watermark
    c.drawString(-text_width/2, -text_height/2, config.text)
    
    # Additional watermarks
    scale = 0.7
    offset = config.font_size * 2
    c.setFontSize(config.font_size * scale)
    c.drawString(-text_width/2, -text_height/2 + offset, config.text)
    c.drawString(-text_width/2, -text_height/2 - offset, config.text)
    
    # Restore state
    c.restoreState()
    
    # Save PDF
    c.save()
    buffer.seek(0)
    return buffer

def apply_watermark_to_pdf(input_pdf: str, output_pdf: str, config: WatermarkConfig):
    """
    Apply watermark to existing PDF.
    
    Args:
        input_pdf: Path to input PDF
        output_pdf: Path to output PDF
        config: WatermarkConfig instance
    """
    # Read input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Get page size from first page
    page = reader.pages[0]
    page_size = (float(page.mediabox.width), float(page.mediabox.height))
    
    # Create watermark PDF
    watermark_pdf = create_watermark(config, page_size)
    watermark_reader = PdfReader(watermark_pdf)
    watermark_page = watermark_reader.pages[0]
    
    # Apply watermark to each page
    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)
    
    # Write output PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
