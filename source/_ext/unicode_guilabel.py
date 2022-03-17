from docutils import nodes


def setup(app):
    app.add_role('unicode-guilabel', unicode_guilabel_role)


def unicode_guilabel_role(name, rawtext, text, lineno, inliner,
                          options={}, content=[]):
    """Returns a guilabel node including a single unicode html-code"""

    if not text.startswith("&#"):
        msg = inliner.reporter.error("Wrong Unicode! "
                                     "Must start with '&#'.", line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [msg], [prb]

    if not text.endswith(";"):
        msg = inliner.reporter.error("Wrong Unicode! "
                                     "Must end with ';'.", line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [msg], [prb]

    html = f"<span class=\"guilabel\">{text}</span>"
    node = nodes.raw("\n".join(content), html, format="html", **options)

    return [node], []
