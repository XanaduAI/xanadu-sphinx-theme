"""This module implements the ``index-card`` reST directive."""

from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives

TEMPLATE = cleandoc(
    """
    <div class="col-lg-4 mb-2 d-flex align-items-stretch">
        <div class="card index-card h-100 w-100">
            <div class="card-header index-card-header">
                <h3 class="index-card-title">{name}</h3>
            </div>
            <div class="card-body index-card-body">
                <p class="card-text index-card-description">
                    {description}
                    <i class="fas fa-angle-double-right"></i>
                </p>
            </div>
            <a class="index-card-link stretched-link" href="{link}" aria-label="{name}"></a>
        </div>
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

        html = TEMPLATE.format(name=name, link=link, description=desc)
        return [nodes.raw(text=html, format="html")]
