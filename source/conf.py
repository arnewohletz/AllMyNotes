# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Fix Sphinx 4.0+ deprecation of sphinx.util.osutil.ENOENT ----------------
# from: https://github.com/mgaitan/sphinxcontrib-mermaid/issues/72#issuecomment-835822975

# import errno
# import sphinx.util.osutil
# sphinx.util.osutil.ENOENT = errno.ENOENT

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import locale

sys.path.insert(0, os.path.abspath('.') + '/_ext')


# -- Project information -----------------------------------------------------

project = 'All-My-Notes'
copyright = '2021-2024, Arne Wohletz'
author = 'Arne Wohletz'
version = 'stable'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'fix_mermaid_jupyter_conflict',
    'jupyter_sphinx', # combined with sphinxcontrib.mermaid requires 'fix_mermaid_jupyter_conflict'
    'nbsphinx',
    'sphinx-prompt',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_docsearch',
    'sphinx_git',
    'sphinx_gitstamp',
    'sphinx_tabs.tabs',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.images',
    'sphinxcontrib.mermaid',
    'sphinxemoji.sphinxemoji',
    'unicode_guilabel',
]

# Bibtex Bibfiles
bibtex_bibfiles = ['refs.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = []

docsearch_app_id = 'WOEM7FVORC'
docsearch_api_key = '58572af7098fa34e5f17486c4c4b491f'
docsearch_index_name = 'arnewohletzio'

jupyter_sphinx_thebelab_config = {
    'requestKernel': True,
    'binderOptions': {
        'repo': "binder-examples/requirements",
    },
}

linkcheck_ignore = [
    ".*/_static/",
    "http://www.javavideokurs.de/",
    "https://computingforgeeks.com",
    "https://derickbailey.com",
    "https://developer.mozilla.org/en-US/docs/Tools/Browser_Toolbox",
    "https://github.com/shellspec/shellspec#installation",
    "https://linux.die.net/man/8/update-alternatives",
    "https://mkyong.com",
    "https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python",
    "https://zdoom.org/"
]

pygments_style = "default"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'display_version': False,
    'logo_only': True,
    'navigation_depth': 5,
}

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
html_css_files = [
    'css/custom.css',
]
html_favicon = "_static/img/favicon.png"
html_logo = "_static/img/logo.png"

# Date format for git timestamps
try:
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')

gitstamp_fmt = "%b %d, %Y"

# nbsphinx
nbsphinx_epilog = r"""
.. footbibliography::
"""

# Add custom role directives globally
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

.. |br| raw:: html

    <br />
"""
