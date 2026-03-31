"""This module implements the ``community-card`` reST directive."""

import re
from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives

COMMUNITY_CARD_TEMPLATE = cleandoc(
    """
    <div class="card community-card plugin-card" id={id}>
        <div class="card-header">
            <h4 class="card-header__text">{title}</h4>
            <h6 class="plugin-card__author">{author}</h6>
            <p class="plugin-card__meta">Added: {date}</p>
        </div>
        <div class="card-body">
            <div class="plugin-card__description-section">
                <div class="collapse plugin-card__description-collapse" id="{id}-description">
                    <p class="plugin-card__description plugin-card__description--expanded">
                        {description}
                    </p>
                </div>
                <p class="plugin-card__description plugin-card__description--preview">
                    {description}
                </p>
                <a
                  class="plugin-card__read-more collapsed"
                  data-bs-toggle="collapse"
                  href="#{id}-description"
                  role="button"
                  aria-expanded="false"
                  aria-controls="{id}-description"
                >
                    <span class="plugin-card__read-more-label-collapsed">Read more</span>
                    <span class="plugin-card__read-more-label-expanded">Collapse</span>
                </a>
            </div>
        </div>
        <div class="plugin-card__footer">
            {paper_footer}
            {blog_footer}
            {code_footer}
        </div>
    </div>
    """
)

PAPER_FOOTER_TEMPLATE = cleandoc(
    """
    <a href="{paper}" class="btn plugin-card__action-btn plugin-card__paper-btn"><i class="bx bx-book"></i> View paper</a>
    """
)

BLOG_FOOTER_TEMPLATE = cleandoc(
    """
    <a href="{blog}" class="btn plugin-card__action-btn plugin-card__blog-btn"><i class="bx bx-news"></i> Blog</a>
    """
)

CODE_FOOTER_TEMPLATE = cleandoc(
    """
    <a href="{code}" class="btn plugin-card__action-btn plugin-card__action-btn--outlined plugin-card__code-btn"><i class="bx bx-git-branch"></i> Code</a>
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
            id=id_,
        )
        return [nodes.raw(text=html, format="html")]
