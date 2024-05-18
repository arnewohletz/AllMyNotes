from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.nodes import Admonition, Element
from sphinx.application import Sphinx

try:
    from sphinx.util.typing import ExtensionMetadata
except ImportError:
    ExtensionMetadata = 'ExtensionMetadataType'   # Sphinx <7.3


class waiting(Admonition, Element):
    pass


class WaitingAdmonition(BaseAdmonition):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    node_class = waiting

    def run(self):
        title = " ".join(self.arguments)
        waiting_node = waiting(title=title)
        self.state.nested_parse(self.content, self.content_offset,
                                waiting_node)
        return [waiting_node]


def visit_waiting_node(self, node):
    self.body.append("<div class=\"admonition waiting\">")
    self.body.append("<p class=\"admonition-title\">")
    self.body.append(f"{node.get('title')}")
    self.body.append("</p>")


def depart_waiting_node(self, node):
    self.body.append("</div>")


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_node(waiting, html=(visit_waiting_node, depart_waiting_node))
    app.add_directive('waiting', WaitingAdmonition)

    return {'version': '0.1'}
