"""This module implements the ``youtube-video`` reST directive."""

from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives

TEMPLATE = cleandoc(
    """
    <div class="col-lg-6 col-md-6 col-12">
        <a class="youtube-video-link" href="https://youtube.com/watch?v={id}" target="_blank" rel="noopener noreferrer">
            <div class="card video-card">
                <div class="video-card__media">
                    <img
                      class="card-img-top img-fluid"
                      src="https://img.youtube.com/vi/{id}/hqdefault.jpg"
                      alt="{title}"
                    />
                </div>
                <div class="card-body">
                    <h4 class="card-title">{title}</h4>
                    <p class="card-text video-card__author">{author}</p>
                    <p class="card-text video-card__description">
                        {description}
                    </p>
                </div>
                <div class="video-card__footer">
                    <span class="video-card__watch-label">Watch</span>
                    <i class="bx bx-chevron-right video-card__watch-icon"></i>
                </div>
            </div>
        </a>
    </div>
    """
)


class YouTubeVideoDirective(Directive):
    """Creates a YouTube card with the given video ID argument."""

    required_arguments = 1
    optional_arguments = 0
    option_spec = {
        "title": directives.unchanged_required,
        "author": directives.unchanged_required,
    }

    final_argument_whitespace = False
    has_content = True
    add_index = False

    def run(self):
        ytid = self.arguments[0]
        description = [i if i != "" else "<br><br>" for i in self.content]

        html = TEMPLATE.format(
            id=ytid,
            title=self.options["title"],
            author=self.options["author"],
            description=" ".join(description),
        )
        return [nodes.raw(text=html, format="html")]
