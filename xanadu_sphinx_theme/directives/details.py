"""This module implements the ``details`` reST directive."""
from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList

TEMPLATE = cleandoc(
    """
    .. raw:: html

        <a
          class="details-header collapse-header"
          data-toggle="collapse"
          href="#details"
          aria-expanded="false"
          aria-controls="details"
        >
            <h2 style="font-size: 24px;">
                <i class="fas fa-angle-down rotate" style="float: right;"></i> {title}
            </h2>
        </a>
        <div class="collapse" id="details">

    {content}

    .. raw:: html

        </div>
    """
)


class DetailsDirective(Directive):
    """Creates a collapsable Details section."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {"title": directives.unchanged}
    has_content = True
    add_index = False

    def run(self):
        title = self.options.get("title", "Details and Conventions")
        rst = TEMPLATE.format(title=title, content="\n".join(self.content))
        string_list = StringList(rst.split("\n"))
        node = nodes.tbody()
        self.state.nested_parse(string_list, self.content_offset, node)
        return [node]
