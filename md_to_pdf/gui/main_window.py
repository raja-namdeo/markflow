"""
Main window for the Markdown to PDF converter GUI.
"""
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QFileDialog, QMessageBox, QSplitter,
    QMenuBar, QMenu, QStatusBar
)
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QAction, QIcon
from .editor import MarkdownEditor
from .preview import PreviewPanel
from ..converter import MarkdownToPDFConverter
import os

class MainWindow(QMainWindow):
    """Main window of the application."""
    
    def __init__(self):
        super().__init__()
        self.converter = MarkdownToPDFConverter()
        self.editor = None
        self.preview = None
        self.preview_timer = QTimer()
        self.preview_timer.setSingleShot(True)
        self.preview_timer.setInterval(500)  # 500ms delay
        self.setup_ui()
        
    def setup_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Markdown to PDF Converter")
        self.setMinimumSize(QSize(800, 600))
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create main content area
        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)
        
        # Add editor
        self.editor = MarkdownEditor()
        splitter.addWidget(self.editor)
        
        # Add preview panel
        self.preview = PreviewPanel()
        splitter.addWidget(self.preview)
        
        # Set splitter sizes
        splitter.setSizes([400, 400])
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")
        
        # Connect editor to preview with debouncing
        self.editor.contentChanged.connect(self._schedule_preview_update)
        self.preview_timer.timeout.connect(self._update_preview)
        
        # Set initial content
        welcome_text = """# Welcome to Markdown to PDF Converter

Start typing your Markdown content here. The preview will update automatically.

## Features
- Real-time preview
- File operations (New, Open, Save)
- PDF export
- Syntax highlighting

## Keyboard Shortcuts
- **Ctrl+N**: New file
- **Ctrl+O**: Open file
- **Ctrl+S**: Save file
- **Ctrl+E**: Export PDF
- **Ctrl+Q**: Quit
"""
        self.editor.setPlainText(welcome_text)
        
    def _schedule_preview_update(self, content):
        """Schedule a preview update with debouncing."""
        self.preview_timer.start()
        
    def _update_preview(self):
        """Update the preview content."""
        content = self.editor.toPlainText()
        self.preview.update_preview(content)
        
    def create_menu_bar(self):
        """Create the application menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        new_action = QAction("&New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        export_action = QAction("&Export PDF", self)
        export_action.setShortcut("Ctrl+E")
        export_action.triggered.connect(self.export_pdf)
        file_menu.addAction(export_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("&Edit")
        
        undo_action = QAction("&Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(lambda: self.editor.undo() if self.editor else None)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction("&Redo", self)
        redo_action.setShortcut("Ctrl+Shift+Z")
        redo_action.triggered.connect(lambda: self.editor.redo() if self.editor else None)
        edit_menu.addAction(redo_action)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        toggle_preview_action = QAction("Toggle Preview", self)
        toggle_preview_action.setShortcut("Ctrl+P")
        toggle_preview_action.triggered.connect(self.toggle_preview)
        view_menu.addAction(toggle_preview_action)
        
    def create_toolbar(self):
        """Create the main toolbar."""
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        
        # Add toolbar actions
        new_action = toolbar.addAction("New")
        new_action.triggered.connect(self.new_file)
        
        open_action = toolbar.addAction("Open")
        open_action.triggered.connect(self.open_file)
        
        save_action = toolbar.addAction("Save")
        save_action.triggered.connect(self.save_file)
        
        toolbar.addSeparator()
        
        export_action = toolbar.addAction("Export PDF")
        export_action.triggered.connect(self.export_pdf)
        
    def new_file(self):
        """Create a new file."""
        if self.editor:
            self.editor.setPlainText("")
            self.statusBar.showMessage("New file created")
        
    def open_file(self):
        """Open a markdown file."""
        if not self.editor:
            return
            
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Markdown File",
            "",
            "Markdown Files (*.md);;All Files (*)"
        )
        
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.editor.setText(content)
                self.statusBar.showMessage(f"Opened {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")
        
    def save_file(self):
        """Save the current file."""
        if not self.editor:
            return
            
        # Get first line as title or use default
        content = self.editor.toPlainText()
        first_line = content.split('\n')[0].strip('# ') if content else 'Untitled'
        
        # Create suggested filename
        suggested_name = first_line.lower().replace(' ', '_')
        suggested_name = ''.join(c for c in suggested_name if c.isalnum() or c in '_-')
        suggested_name = f"{suggested_name}_{self.get_next_index()}.md"
        
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Markdown File",
            suggested_name,
            "Markdown Files (*.md);;All Files (*)"
        )
        
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.editor.toPlainText())
                self.statusBar.showMessage(f"Saved to {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")
    
    def get_next_index(self):
        """Get next available index for file naming."""
        try:
            save_dir = os.path.expanduser("~/Documents")
            existing_files = [f for f in os.listdir(save_dir) if f.endswith('.md')]
            indices = []
            
            for file in existing_files:
                try:
                    index = int(file.split('_')[-1].split('.')[0])
                    indices.append(index)
                except (ValueError, IndexError):
                    continue
            
            return max(indices, default=0) + 1
        except Exception:
            return 1

    def export_pdf(self):
        """Export the current document as PDF."""
        if not self.editor:
            return
            
        # Get first line as title or use default
        content = self.editor.toPlainText()
        first_line = content.split('\n')[0].strip('# ') if content else 'Untitled'
        
        # Create suggested filename
        suggested_name = first_line.lower().replace(' ', '_')
        suggested_name = ''.join(c for c in suggested_name if c.isalnum() or c in '_-')
        suggested_name = f"{suggested_name}_{self.get_next_index()}.pdf"
        
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Export PDF",
            suggested_name,
            "PDF Files (*.pdf);;All Files (*)"
        )
        
        if file_name:
            try:
                content = self.editor.toPlainText()
                self.converter.convert_string(content, file_name)
                self.statusBar.showMessage(f"Exported to {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not export PDF: {str(e)}")
        
    def toggle_preview(self):
        """Toggle the preview panel visibility."""
        if self.preview and self.preview.isVisible():
            self.preview.hide()
        elif self.preview:
            self.preview.show()
            self.preview.update_preview(self.editor.toPlainText())
