"""This module implements the ``index-card`` reST directive."""
from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList

TEMPLATE = cleandoc(
    """
    .. raw:: html

        <div class="col-lg-4 mb-2 align-items-stretch">
            <a href="{link}">
                <div class="card rounded-lg" style="height:100%;">
                    <div class="d-flex">
                        <div>
                            <h3 class="card-title pl-3 mt-4">
                                {name}
                            </h3>
                            <p class="mb-3 grey-text px-3">
                                {description}
                                <i class="fas fa-angle-double-right"></i>
                            </p>
                        </div>
                    </div>
                </div>
            </a>
        </div>
    """
)


class IndexCardDirective(Directive):
    """Creates an index card."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "name": directives.unchanged_required,
        "link": directives.unchanged_required,
        "description": directives.unchanged_required,
    }

    has_content = False
    add_index = False

    def run(self):
        name = self.options["name"]
        link = self.options["link"]
        desc = self.options["description"]

        thumbnail_rst = TEMPLATE.format(name=name, link=link, description=desc)
        thumbnail = StringList(thumbnail_rst.split("\n"))

        thumb = nodes.paragraph()
        self.state.nested_parse(thumbnail, self.content_offset, thumb)
        return [thumb]
