"""
MarkFlow - Modern Markdown to PDF Converter

Copyright (c) 2025 Raja Namdeo <cse.rajanamdeo@gmail.com>
All rights reserved.

This file is part of MarkFlow, a modern Markdown to PDF converter.
For more information, visit: [website coming soon]

Created by: Raja Namdeo
Email: cse.rajanamdeo@gmail.com
Role: Software Developer

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

"""
Markdown editor component with basic editing features.
"""
from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtGui import QFont, QTextCharFormat, QSyntaxHighlighter
from PyQt6.QtCore import Qt, pyqtSignal
import logging

logger = logging.getLogger(__name__)

class MarkdownHighlighter(QSyntaxHighlighter):
    """Basic Markdown syntax highlighter."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_formats()
        
    def setup_formats(self):
        """Set up text formats for different Markdown elements."""
        # Heading format
        self.heading_format = QTextCharFormat()
        self.heading_format.setFontWeight(700)
        self.heading_format.setForeground(Qt.GlobalColor.darkBlue)
        
        # Code format
        self.code_format = QTextCharFormat()
        self.code_format.setFontFamily('Courier')
        self.code_format.setBackground(Qt.GlobalColor.lightGray)
        
    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text."""
        # Highlight headings
        if text.startswith('#'):
            self.setFormat(0, len(text), self.heading_format)
            
        # Highlight inline code
        start = 0
        while True:
            start = text.find('`', start)
            if start >= 0:
                end = text.find('`', start + 1)
                if end >= 0:
                    self.setFormat(start, end - start + 1, self.code_format)
                    start = end + 1
                else:
                    break
            else:
                break

class MarkdownEditor(QPlainTextEdit):
    """Basic Markdown editor with syntax highlighting."""
    
    contentChanged = pyqtSignal(str)  # Signal for text changes with content
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._content = ""  # Store content internally
        self.setup_editor()
        
    def setup_editor(self):
        """Configure the editor."""
        # Set font
        font = QFont('Consolas', 12)
        self.setFont(font)
        
        # Enable line wrapping
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        
        # Set up tab stops
        self.setTabStopDistance(40)  # 4 spaces
        
        # Add syntax highlighter
        self.highlighter = MarkdownHighlighter(self.document())
        
        # Connect signals
        self.textChanged.connect(self._on_text_changed)
        
    def _on_text_changed(self):
        """Handle text changes."""
        self._content = super().toPlainText()
        logger.debug("Text changed: %s", self._content)
        self.contentChanged.emit(self._content)
        
    def setPlainText(self, text):
        """Set text content."""
        logger.debug("Setting text: %s", text)
        super().setPlainText(text)
        self._content = text
        self._on_text_changed()
        
    def toPlainText(self):
        """Get current text content."""
        return self._content
