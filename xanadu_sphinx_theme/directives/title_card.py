"""This module implements the ``title-card`` reST directive."""

from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives

TEMPLATE = cleandoc(
    """
    <div class="title-card-col col-lg-4 mb-2">
        <a class="title-card-link d-flex w-100" href="{link}">
            <div class="card title-card h-100 w-100">
                <div class="card-header title-card-header">
                    <span class="title-card-title">{name}</span>
                </div>
                <div class="card-body title-card-body">
                    <p class="card-text title-card-description">{description}</p>
                </div>
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
        "link": directives.unchanged_required,
        "description": directives.unchanged_required,
    }

    has_content = False
    add_index = False

    def run(self):
        name = self.options["name"]
        link = self.options["link"]
        desc = self.options["description"]

        html = TEMPLATE.format(name=name, link=link, description=desc)
        return [nodes.raw(text=html, format="html")]
