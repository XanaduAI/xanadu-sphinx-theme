"""This module implements the ``community-card`` reST directive."""

import re
from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives

COMMUNITY_CARD_TEMPLATE = cleandoc(
    """
    <div class="card community-card plugin-card" id={id}>
        <div class="card-header {colour}">
            <h4 class="card-header__text">{title}</h4>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-lg-8 d-flex flex-column">
                    <div>
                        <h6>{author}</h6>
                        <p class="plugin-card__meta">
                            <i class="far fa-clock pe-1"></i> {date}
                        </p>
                    </div>
                    <p class="plugin-card__description">
                        {description}
                    </p>
                    <div class="mt-auto plugin-card__read-more-wrapper">
                        <a
                          class="plugin-card__read-more text-primary d-none"
                          data-bs-toggle="modal"
                          data-bs-target="#{id}-modal"
                        >
                            Read More
                        </a>
                    </div>
                </div>
                <div class="col-lg-4 d-flex">
                    <div class="plugin-card__buttons">
                        {paper_footer}
                        {blog_footer}
                        {code_footer}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div
      class="modal fade" id="{id}-modal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="{id}-modal"
      aria-hidden="true"
    >
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title mt-0">{title}</h5>
                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                    ></button>
                </div>
                <div class="modal-body">
                    {description}
                </div>
                <div class="modal-footer">
                    {paper_footer}
                    {blog_footer}
                    {code_footer}
                </div>
            </div>
        </div>
    </div>
    """
)

PAPER_FOOTER_TEMPLATE = cleandoc(
    """
    <a href="{paper}" class="btn btn-info plugin-card__paper-btn" style="width: 100%;"><i class="fas fa-book"></i> Paper</a>
    """
)

BLOG_FOOTER_TEMPLATE = cleandoc(
    """
    <a href="{blog}" class="btn btn-info plugin-card__blog-btn" style="width: 100%;"><i class="fas fa-newspaper"></i> Blog</a>
    """
)

CODE_FOOTER_TEMPLATE = cleandoc(
    """
    <a href="{code}" class="btn btn-info plugin-card__code-btn" style="width: 100%;"><i class="fas fa-code-branch"></i></i> Code</a>
    """
)


class CommunityCardDirective(Directive):
    """Creates a community card."""

    required_arguments = 0
    optional_arguments = 4
    option_spec = {
        "title": directives.unchanged_required,
        "author": directives.unchanged_required,
        "paper": directives.unchanged,
        "blog": directives.unchanged,
        "code": directives.unchanged,
        "date": directives.unchanged_required,
        "colour": directives.unchanged,
    }

    final_argument_whitespace = False
    has_content = True
    add_index = False

    def run(self):
        description = [i if i != "" else "<br><br>" for i in self.content]
        colour = self.options.get("colour", "weird-blue-gradient")

        if "paper" in self.options:
            paper_footer = PAPER_FOOTER_TEMPLATE.format(paper=self.options["paper"])
        else:
            paper_footer = ""

        if "code" in self.options:
            code_footer = CODE_FOOTER_TEMPLATE.format(code=self.options["code"])
        else:
            code_footer = ""

        if "blog" in self.options:
            blog_footer = BLOG_FOOTER_TEMPLATE.format(blog=self.options["blog"])
        else:
            blog_footer = ""

        def remove_accents(raw_text):
            """Removes common accent characters."""
            raw_text = re.sub("[àáâãäå]", "a", raw_text)
            raw_text = re.sub("[èéêë]", "e", raw_text)
            raw_text = re.sub("[ìíîï]", "i", raw_text)
            raw_text = re.sub("[òóôõö]", "o", raw_text)
            raw_text = re.sub("[ùúûü]", "u", raw_text)
            raw_text = re.sub("[ýÿ]", "y", raw_text)
            raw_text = re.sub("[ß]", "ss", raw_text)
            raw_text = re.sub("[ñ]", "n", raw_text)
            return raw_text

        id_ = remove_accents(self.options["author"].split(" ")[-1].lower())
        id_ += self.options["date"].split("/")[-1]
        id_ += self.options["title"].split(" ")[0].lower()

        html = COMMUNITY_CARD_TEMPLATE.format(
            title=self.options["title"],
            author=self.options["author"],
            description=" ".join(description),
            date=self.options["date"],
            paper_footer=paper_footer,
            code_footer=code_footer,
            blog_footer=blog_footer,
            colour=colour,
            id=id_,
        )
        return [nodes.raw(text=html, format="html")]
