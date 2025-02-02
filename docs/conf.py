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
release = '2.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_title = "MarkFlow Documentation"
html_short_title = "MarkFlow"

html_theme_options = {
    'analytics_id': '',  # TODO: Add your Google Analytics ID
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2196F3',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Convert markdown files to rst
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
