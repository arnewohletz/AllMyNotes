"""
https://github.com/mgaitan/sphinxcontrib-mermaid/issues/74#issuecomment-1937184257

Cludge solution by Zlatko to issue

This extension injects the Mermaid.js code verbatim into the <head> section of each HTML page.
This approach involves using Sphinx's extension mechanism to programmatically modify the HTML output.

This is a custom Sphinx extension that uses the app object to add custom HTML to the <head> section.
We use the `html-page-context` event to modify the context of each HTML page before it is rendered,
allowing for the injection of custom scripts. The function `add_mermaid_js` adds the Mermaid.js
script tags to the HTML context.
"""
from sphinx.application import Sphinx


def add_mermaid_js(app: Sphinx, pagename: str, templatename: str, context: dict, doctree):
    mermaid_script = r"""
    <script src="https://unpkg.com/mermaid@10.9.0/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true});</script>
    """
    if "metatags" in context:
        context["metatags"] += mermaid_script
    else:
        context["metatags"] = mermaid_script


def setup(app: Sphinx):
    app.connect("html-page-context", add_mermaid_js)
