"""
MarkFlow documentation build configuration file.

Author: Raja Namdeo
Email: cse.rajanamdeo@gmail.com
"""

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'MarkFlow'
copyright = '2025, Raja Namdeo'
author = 'Raja Namdeo'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_static_path = ['_static']

html_title = "MarkFlow Documentation"
html_favicon = '_static/favicon.ico'
html_logo = '_static/logo.png'

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2196F3",
        "color-brand-content": "#2196F3",
    },
    "dark_css_variables": {
        "color-brand-primary": "#90CAF9",
        "color-brand-content": "#90CAF9",
    },
}
