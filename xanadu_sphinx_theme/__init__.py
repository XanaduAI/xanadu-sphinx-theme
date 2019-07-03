# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Xanadu Sphinx Theme"""
import os

from .custom_directives import IncludeDirective, GalleryItemDirective, CustomGalleryItemDirective
from ._version import __version__


def get_path():
    """Shortcut for users whose theme is next to their conf.py"""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context["xanadu_version"] = __version__


def setup(app):
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("xanadu", theme_path)

    app.connect("html-page-context", update_context)
    app.add_directive("includenodoc", IncludeDirective)
    app.add_directive("galleryitem", GalleryItemDirective)
    app.add_directive("customgalleryitem", CustomGalleryItemDirective)
    app.add_stylesheet(os.path.join(theme_path, "static/gallery.css"))

    return {"version": __version__, "parallel_read_safe": True}
