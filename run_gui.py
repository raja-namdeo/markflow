#!/usr/bin/env python3
"""
Launch script for the Markdown to PDF Converter GUI.
"""
import sys
import os
import logging
import argparse
from PyQt6.QtWidgets import QApplication
from md_to_pdf.gui import MainWindow

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('md_to_pdf_gui.log')
    ]
)
logger = logging.getLogger(__name__)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Markdown to PDF Converter GUI'
    )
    parser.add_argument(
        '--file', '-f',
        help='Open specified markdown file on startup'
    )
    parser.add_argument(
        '--debug', '-d',
        action='store_true',
        help='Enable debug mode'
    )
    return parser.parse_args()

def main():
    """Main entry point for the GUI application."""
    try:
        # Parse arguments
        args = parse_args()
        
        # Set log level
        if not args.debug:
            logging.getLogger().setLevel(logging.INFO)
        
        logger.debug("Starting application...")
        app = QApplication(sys.argv)
        logger.debug("Created QApplication")
        
        # Create and show main window
        window = MainWindow()
        logger.debug("Created MainWindow")
        
        # Open file if specified
        if args.file:
            if os.path.exists(args.file):
                logger.info(f"Opening file: {args.file}")
                with open(args.file, 'r', encoding='utf-8') as f:
                    content = f.read()
                window.editor.setPlainText(content)
                window.statusBar.showMessage(f"Opened {args.file}")
            else:
                logger.warning(f"File not found: {args.file}")
        
        window.show()
        logger.debug("Called show() on window")
        
        # Set up exception handling
        sys._excepthook = sys.excepthook
        def exception_hook(exctype, value, traceback):
            """Handle uncaught exceptions."""
            logger.error("Uncaught exception:", exc_info=(exctype, value, traceback))
            sys._excepthook(exctype, value, traceback)
        sys.excepthook = exception_hook
        
        logger.debug("Entering main event loop")
        return app.exec()
    
    except Exception as e:
        logger.exception("Error in main: %s", str(e))
        return 1

if __name__ == "__main__":
    sys.exit(main())
