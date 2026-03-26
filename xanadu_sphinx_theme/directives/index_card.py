"""This module implements the ``index-card`` reST directive."""

from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives

TEMPLATE = cleandoc(
    """
    .. raw:: html

        <div class="col-lg-4 mb-2 d-flex align-items-stretch">
            <a class="index-card-link d-flex w-100" href="{link}">
                <div class="card rounded-3 h-100 w-100">
                    <div class="d-flex">
                        <div>
                            <h3 class="card-title ps-3 mt-4">
                                {name}
                            </h3>
                            <p class="mb-3 text-muted px-3">
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

        html = TEMPLATE.format(name=name, link=link, description=desc)
        return [nodes.raw(text=html, format="html")]
