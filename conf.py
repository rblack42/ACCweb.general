# -*- coding: utf-8 -*-
#
import sys
import os
import shlex
import cloud_sptheme as csp

sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.graphviz',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.spelling',
]
templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'General'
copyright = u'2015, Roie R. Black'
author = u'Roie R. Black'

version = 'Spring.17.1'
release = '1.0'

language = None

today_fmt = '%B %d, %Y'
exclude_patterns = ['_venv', '_build', '_unpublished']
pygments_style = 'sphinx'

todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'cloud'
html_sidebars = {
    'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']
}

html_title = "General"
#html_short_title = None
#html_logo = None
#html_favicon = '_static/images/favicon.ico'

html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
#html_sidebars = {}
#html_use_index = True
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
'papersize': 'letterpaper',
'pointsize': '11pt',
#'preamble': '',
}

latex_documents = [
  (master_doc, 'General.tex', u'General Notes',
   u'Roie R. Black', 'manual'),
]

#latex_logo = None
#latex_show_urls = False
#latex_appendices = []
#latex_domain_indices = True

