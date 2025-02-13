# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import locale

sys.path.insert(0, os.path.abspath('.') + '/_ext')

# -- Project information -----------------------------------------------------

project = 'All-My-Notes'
copyright = '2021-2025, Arne Wohletz'
author = 'Arne Wohletz'
version = 'stable'

# -- General configuration ---------------------------------------------------

# if both 'jupyter_sphinx' and 'sphinxcontrib.mermaid' are listed also requires
# the 'fix_mermaid_jupyter_conflict' extension (found in source/_ext directory)
extensions = [
    'fix_docsearch_not_found_error',
    'fix_mermaid_jupyter_conflict',
    'jupyter_sphinx',
    'nbsphinx',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_docsearch',
    'sphinx_git',
    'sphinx_gitstamp',
    'sphinx_tabs.tabs',
    'sphinxcontrib.bibtex',
    #'sphinxcontrib.images', disable until https://github.com/sphinx-contrib/images/issues/40 resolved
    'sphinxcontrib.mermaid',
    'sphinxemoji.sphinxemoji',
    'unicode_guilabel',
    'waiting_admonition'
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# linkcheck config
linkcheck_anchors = False
linkcheck_ignore = [
    ".*/_static/",
    "http://www.javavideokurs.de/",
    "https://computingforgeeks.com",
    "https://dashboard.algolia.com/",
    "https://derickbailey.com",
    "https://developer.mozilla.org/en-US/docs/Tools/Browser_Toolbox",
    "https://github.com/shellspec/shellspec#installation",
    "https://linux.die.net/man/8/update-alternatives",
    "https://mkyong.com",
    "https://prosupport.logi.com/",
    "https://treyhunner.com/",
    "https://zdoom.org/",
]

pygments_style = "default"

# -- Extension configuration -------------------------------------------------

# sphinx-copybutton
# ----- remove this later ----
# copybutton_prompt_text = (r"span.prompt1:before \{|"
#                           r"  content: \".*\"\;|"
#                           r"\}|"
#                           r"\(.*\) \$ |"
#                           r"\(.*\) |"
#                           r"\$|"
#                           r"\>{3} "
#                           )
# -----------------------------
copybutton_line_continuation_character = "\\"
copybutton_prompt_text = (r"\(.*\) \$ |"
                          r"\(.*\) |"
                          r"\$ |"
                          r"\>{3} |"
                          r"P?S?\ ?C:\\> "
                          )
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True
copybutton_copy_empty_lines = False
copybutton_here_doc_delimiter = "EOT"

# sphinx-docsearch
docsearch_app_id = 'WOEM7FVORC'
docsearch_api_key = '6dbea932bf661e0b80a33bd99d184f75'
docsearch_index_name = 'arnewohletzio'

# jupyter_sphinx
jupyter_sphinx_thebelab_config = {
    'requestKernel': True,
    'binderOptions': {
        'repo': "binder-examples/requirements",
    },
}

# sphinxcontrib.bibtex
bibtex_bibfiles = ['refs.bib']

# nbsphinx
nbsphinx_epilog = r"""
.. footbibliography::
"""

# sphinx_gitstamp
try:
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')

gitstamp_fmt = "%b %d, %Y"   # Date format for git timestamps

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}
html_favicon = "_static/img/favicon.png"
html_logo = "_static/img/logo.png"

# Custom CSS files
html_css_files = [
    'css/custom.css',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static',
                    'howto/others/_file',
                    'tutorial/python/_file',
                    'reference/others/_file',
                    'reference/python/_file',
                    'reference/python/cheat_sheets/_file',
                    ]

# -- rst_prolog reStructuredText string --------------------------------------
#  included at the beginning of every source file
rst_prolog = """
.. role:: python(code)
    :language: python
    :class: highlight

.. role:: java(code)
    :language: java
    :class: highlight

.. role:: javascript(code)
    :language: javascript
    :class: highlight

.. role:: rst(code)
    :language: rst
    :class: highlight

.. role:: html(code)
    :language: html
    :class: highlight

.. role:: bash(code)
    :language: bash
    :class: highlight

.. role:: raw-html(raw)
   :format: html

.. role:: rbg
.. role:: rfg
.. role:: gfg
.. role:: gbg
.. role:: ulined
.. role:: strike

"""
