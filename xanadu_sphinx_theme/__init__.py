"""
This module registers the Xanadu Sphinx Theme. For more information, see
https://www.sphinx-doc.org/en/master/development/theming.html
"""
from os import path

def setup(app):
    app.add_html_theme("xanadu", path.abspath(path.dirname(__file__)))
