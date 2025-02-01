"""
Tests for the GUI components of the Markdown to PDF converter.
"""
import sys
import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineCore import QWebEnginePage
from md_to_pdf.gui import MainWindow, MarkdownEditor, PreviewPanel
import logging

logger = logging.getLogger(__name__)

class TestGUI(unittest.TestCase):
    """Test cases for GUI components."""
    
    @classmethod
    def setUpClass(cls):
        """Create the application once for all tests."""
        cls.app = QApplication(sys.argv)
    
    def setUp(self):
        """Set up test cases."""
        self.window = MainWindow()
        # Clear any welcome text
        self.window.editor.setPlainText("")
        QTest.qWait(100)
    
    def test_window_creation(self):
        """Test that the main window is created properly."""
        self.assertIsNotNone(self.window)
        self.assertEqual(self.window.windowTitle(), "Markdown to PDF Converter")
        self.assertTrue(self.window.editor is not None)
        self.assertTrue(self.window.preview is not None)
    
    def test_editor(self):
        """Test the Markdown editor component."""
        editor = self.window.editor
        test_text = "# Test Heading\nThis is a test."
        
        # Test text input
        editor.setFocus()
        QTest.qWait(100)
        
        # Set text and wait for update
        editor.setPlainText(test_text)
        QTest.qWait(500)  # Wait longer for update
        
        # Process events to ensure update
        for _ in range(10):  # Process multiple times
            QApplication.processEvents()
            QTest.qWait(50)
        
        # Get text directly from document
        actual_text = editor.document().toPlainText()
        logger.debug("Expected text: %r", test_text)
        logger.debug("Actual text: %r", actual_text)
        self.assertEqual(actual_text, test_text)
        
        # Test undo/redo
        editor.setPlainText("")
        QTest.qWait(100)
        self.assertEqual(editor.toPlainText(), "")
        
        editor.document().undo()
        QTest.qWait(100)
        self.assertEqual(editor.toPlainText(), test_text)
    
    def test_preview(self):
        """Test the preview panel."""
        preview = self.window.preview
        self.assertIsNotNone(preview)
        
        # Test preview update
        test_md = "# Test Preview\nThis is a *test*."
        self.window.editor.setPlainText(test_md)
        
        # Wait for preview to update (500ms debounce + buffer)
        QTest.qWait(1000)
        
        # Get HTML content directly
        html_content = ""
        def handle_html(content):
            nonlocal html_content
            html_content = content
            self.assertIn("Test Preview", content)
        
        preview.web_view.page().toHtml(handle_html)
        QTest.qWait(500)  # Wait for HTML callback
    
    def test_file_operations(self):
        """Test file menu operations."""
        # Test new file
        self.window.editor.setPlainText("Old content")
        QTest.qWait(100)
        self.window.new_file()
        QTest.qWait(100)
        self.assertEqual(self.window.editor.toPlainText(), "")
    
    def tearDown(self):
        """Clean up after each test."""
        self.window.close()
        QTest.qWait(100)  # Wait for cleanup
    
    @classmethod
    def tearDownClass(cls):
        """Clean up the application."""
        cls.app.quit()

if __name__ == '__main__':
    unittest.main()
