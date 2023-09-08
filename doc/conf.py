# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import re

# -- Project information -----------------------------------------------------

project = 'Xanadu Sphinx Theme'
copyright = '2023 | Xanadu | All rights reserved'
author = 'Xanadu Inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

import xanadu_sphinx_theme

# The full version, including alpha/beta/rc tags.
release = xanadu_sphinx_theme.__version__

# The short X.Y version.
version = re.match(r"^(\d+\.\d+)", release).expand(r"\1")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
    "m2r2"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [xanadu_sphinx_theme.templates_dir()]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = "index"

autosummary_generate = True
autosummary_imported_members = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'xanadu'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"


# Xanadu theme options (see theme.conf for more information).
html_theme_options = {
    "navbar_name": "Xanadu Sphinx Theme",
    "navbar_logo_colour": "#f48fb1",
    # "navbar_home_link": "https://pennylane.ai",
    "navbar_left_links": [
        {
            "name": "Blog",
            "href": "javascript:void(0);",
        },
        {
            "name": "Search",
            "href": "search.html",
        },
        {
            "name": "Documentation",
            "href": "index.html",
            "active": True,
        }
    ],
    "navbar_right_links": [
        {
            "name": "GitHub",
            "href": "https://github.com/XanaduAI/xanadu-sphinx-theme",
            "icon": "fab fa-github",
        },
    ],
    "extra_copyrights": [
        "Any extra copyrights can be added here."
    ],
    "border_colour": "#f48fb1",
    "prev_next_button_colour": "#f48fb1",
    "prev_next_button_hover_colour": "#ec407a",
    "table_header_background_colour": "#f8bbd0",
    "social_icon_colour": "#ec407a",
    "text_accent_colour": "#f48fb1",
    "toc_marker_colour": "#f48fb1",
    "toc_overview": True,
    "toc_global": True,
    "toc_hover": False,
    "relations": True
}


# -- Options for Sphinx Gallery --------------------------------------------

sphinx_gallery_conf = {
    # path to your example scripts
    "examples_dirs": ["tutorials"],
    # path where to save gallery generated examples
    "gallery_dirs": ["gallery"],
    # execute files that match the following filename pattern,
    # and skip those that don't. If the following option is not provided,
    # all example scripts in the 'examples_dirs' folder will be skiped.
    "filename_pattern": r"tutorial",
    "pypandoc": True,
    # first notebook cell in generated Jupyter notebooks
    "first_notebook_cell": (
        "# This cell is added by sphinx-gallery\n"
        "# It can be customized to whatever you like\n"
        "%matplotlib inline"
    ),
    # thumbnail size
    "thumbnail_size": (400, 400),
}
