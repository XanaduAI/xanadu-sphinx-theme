"""This module implements the ``related-demo`` reST directive."""
from inspect import cleandoc

from docutils.parsers.rst import Directive
from docutils.statemachine import StringList
from docutils import nodes

TEMPLATE = cleandoc(
    """
    .. raw:: html

        <script type="text/javascript">
            var related_tutorials = [{urls}];
            var related_tutorials_titles = {linkText};
        </script>
    """
)

class RelatedDemoDirective(Directive):
    """Creates a related demo and adds it to the sidebar."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    add_index = False

    def run(self):
        urls = [f'"{u.split(" ")[0]}.html"' for u in list(self.content)]
        linkText = [" ".join(u.split(" ")[1:]) for u in list(self.content)]
        urls = ", ".join(urls)
        html = TEMPLATE.format(urls=urls, linkText=linkText)
        str_list = StringList(html.split("\n"))
        related_variables = nodes.paragraph()
        self.state.nested_parse(str_list, self.content_offset, related_variables)
        return [related_variables]
