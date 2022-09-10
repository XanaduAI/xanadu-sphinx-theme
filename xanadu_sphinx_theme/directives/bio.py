"""This module implements the ``bio`` reST directive."""

from inspect import cleandoc

from docutils import nodes
from docutils.parsers.rst import Directive, directives

TEMPLATE = cleandoc(
    """
    <div class="bio" >
        <div class="photo" >
            <img class="photo__img" src="{photo}" alt="{author}" >
        </div>
        <div class="bio-text">
            <h4 class="bio-text__author-name">{author}</h4>
            <p class="bio-text__author-description">{bio}</p>
        </div>
    </div>
    """
)


class BioDirective(Directive):
    """Embed author bio in posts (ReST format).

    Based on the pelican_youtube plugin:
    https://github.com/kura/pelican_youtube

    Usage:

    .. bio:: Author name goes here
        :photo: ../_static/avatar.webp

        Write the author bio content here. It must be preceded by a blank line.
    """

    required_arguments = 1
    optional_arguments = 8
    option_spec = {
        "photo": str,
    }
    final_argument_whitespace = False
    has_content = True

    def boolean(self):
        """Conversion function for yes/no True/False."""
        value = directives.choice(self, ("yes", "True", "no", "False"))
        return value in ("yes", "True")

    def run(self):
        author_string = self.arguments
        author = " ".join(map(str, author_string))

        photo = self.options.get("photo", None)
        bio = self.content[0].strip()
        bio_block = TEMPLATE.format(photo=photo, author=author, bio=bio)
        return [
            nodes.raw("", bio_block, format="html"),
        ]
