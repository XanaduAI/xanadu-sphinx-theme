"""
This module registers the Xanadu Sphinx Theme. For more information, see
https://www.sphinx-doc.org/en/master/development/theming.html
"""
from pathlib import Path

from .directives import (
    CommunityCardDirective,
    DetailsDirective,
    GalleryItemDirective,
    IndexCardDirective,
    RelatedDemoDirective,
    TitleCardDirective,
    YouTubeVideoDirective,
)


def setup(app):
    """See https://www.sphinx-doc.org/en/master/extdev/appapi.html."""
    cwd = Path(__file__).resolve().parent
    app.add_html_theme("xanadu", str(cwd))

    directives = {
        "community-card": CommunityCardDirective,
        "details": DetailsDirective,
        "gallery-item": GalleryItemDirective,
        "index-card": IndexCardDirective,
        "related-demo": RelatedDemoDirective,
        "title-card": TitleCardDirective,
        "youtube-video": YouTubeVideoDirective,
    }
    for name, cls in directives.items():
        app.add_directive(name, cls)
