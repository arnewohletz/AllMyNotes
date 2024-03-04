"""
Fixes 'Uncaught TypeError: docsearch is not a function' error reported after
adding Algolia Docsearch configuration.

It is caused by the JS asset to be loaded after the page is loaded. This script
causes the asset to be loaded before a page is rendered, by adding a script
line to the HTMLs <head> section.

See:
https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-html-page-context


"""

from sphinx.application import Sphinx


def add_docsearch_js(app: Sphinx, pagename: str, templatename: str, context: dict, doctree):
    docsearch_script = r"""
    <script src="https://cdn.jsdelivr.net/npm/@docsearch/js@3"></script>
    """
    if "metatags" in context:
        context["metatags"] += docsearch_script
    else:
        context["metatags"] = docsearch_script


def setup(app: Sphinx):
    app.connect("html-page-context", add_docsearch_js)
