"""This module implements the ``youtube-video`` reST directive."""
from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList

TEMPLATE = cleandoc(
    """
    .. raw:: html

        <a href="https://youtube.com/watch?v={id}" target="_blank">
            <div class="card video-card">
                <img
                  class="card-img-top img-fluid"
                  src="https://img.youtube.com/vi/{id}/hqdefault.jpg"
                />
                <div class="card-body">
                    <h4 class="card-title">{title}</h4>
                    <p class="card-text grey-text">{author}</p>
                    <p class="card-text">
                        {description}
                    </p>
                </div>
                <div class="white-text watch">
                    <hr>
                    <h5>Watch <i class="fas fa-angle-double-right"></i></h5>
                </div>
            </div>
        </a>
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

        thumbnail_rst = TEMPLATE.format(
            id=ytid,
            title=self.options["title"],
            author=self.options["author"],
            description=" ".join(description),
        )
        thumbnail = StringList(thumbnail_rst.split("\n"))
        thumb = nodes.paragraph()
        self.state.nested_parse(thumbnail, self.content_offset, thumb)
        return [thumb]
