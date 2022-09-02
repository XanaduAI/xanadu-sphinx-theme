"""This module implements the ``bio`` reST directive."""

from docutils.parsers.rst import Directive, directives
from docutils import nodes


class BioDirective(Directive):
    """Embed author bio in posts (ReST format).

    Based on the pelican_youtube plugin:
    https://github.com/kura/pelican_youtube

    Usage:

    .. bio:: Author name goes here
        :photo: ../_static/avatar.webp

        Write the author bio content here. It must be preceded by a blank line.
    """

    def boolean(argument):
        """Conversion function for yes/no True/False."""
        value = directives.choice(argument, ("yes", "True", "no", "False"))
        return value in ("yes", "True")

    required_arguments = 1
    optional_arguments = 8
    option_spec = {
        "photo": str,
    }
    final_argument_whitespace = False
    has_content = True

    def run(self):
        authorStringArray = self.arguments
        author = " ".join([str(item) for item in authorStringArray])
        photo = self.options.get("photo", None)
        bio = self.content[0].strip()
        bio_block = '<div class="bio" > <div class="photo" ><img class="photo__img" src="{}" alt="{}" ></div><div class="bio-text"><h4 class="bio-text__author-name">{}</h4><p class="bio-text__author-description">{}</p></div></div>'.format(
            photo, author, author, bio
        )
        return [
            nodes.raw("", bio_block, format="html"),
        ]
