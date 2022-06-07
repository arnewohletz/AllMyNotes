# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Fix Sphinx 4.0+ deprecation of sphinx.util.osutil.ENOENT ----------------
# from: https://github.com/mgaitan/sphinxcontrib-mermaid/issues/72#issuecomment-835822975
import errno
import sphinx.util.osutil
sphinx.util.osutil.ENOENT = errno.ENOENT

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
copyright = '2021, Arne Wohletz'
author = 'Arne Wohletz'
version = 'stable'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.mermaid',
    'sphinxcontrib.images',
    'sphinx_git',
    'sphinx-prompt',
    'sphinxemoji.sphinxemoji',
    'sphinx_copybutton',
    'sphinxcontrib.bibtex',
    # 'jupyter_sphinx', # conflicts with sphinxcontrib.mermaid & sphinxcontrib.images
    'unicode_guilabel',
    'sphinx_gitstamp'
]

# Bibtex Bibfiles
bibtex_bibfiles = ['refs.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

jupyter_sphinx_thebelab_config = {
    'requestKernel': True,
    'binderOptions': {
        'repo': "binder-examples/requirements",
    },
}

linkcheck_ignore = [
    "https://mkyong.com",
]

pygments_style = "default"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5,
    'logo_only': True,
    'display_version': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static',
                    'reference/python/cheat_sheets/_file',
                    'reference/others/_file',
                    ]
html_css_files = [
    'css/custom.css',
]
html_favicon = "_static/img/favicon.png"
html_logo = "_static/img/logo.png"

# Date format for git timestamps
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
gitstamp_fmt = "%b %d, %Y"

# Add custom role directives globally
rst_prolog = """
.. role:: python(code)
    :language: python
    :class: highlight

.. role:: java(code)
    :language: java
    :class: highlight

.. role:: rst(code)
    :language: rst
    :class: highlight
    
.. role:: raw-html(raw)
   :format: html

.. role:: rbg
.. role:: gfg
.. role:: ulined
"""
