"""This module implements the ``title-card`` reST directive."""
from inspect import cleandoc

from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList
from docutils import nodes

TEMPLATE = cleandoc(
    """
    .. raw:: html

        <div class="card" style="width: 15rem; float:left; margin: 10px;">
            <a href={link}>
                <div class="card-header">
                    <b>{name}</b>
                </div>
                <div class="card-body">
                    <p class="card-text"> {desc} </p>
                </div>
            </a>
        </div>
    """
)


class TitleCardDirective(Directive):
    """Creates a title card."""

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "name": directives.unchanged_required,
        "description": directives.unchanged_required,
        "link": directives.unchanged_required,
    }

    has_content = False
    add_index = False

    def run(self):
        name = self.options["name"]
        desc = self.options['description']
        link = self.options["link"]

        thumbnail_rst = TEMPLATE.format(name=name, desc=desc, link=link)
        thumbnail = StringList(thumbnail_rst.split('\n'))

        thumb = nodes.paragraph()
        self.state.nested_parse(thumbnail, self.content_offset, thumb)
        return [thumb]
