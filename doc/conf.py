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
copyright = '2022, Xanadu, Inc.'
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
    "sphinx_automodapi.automodapi",
    "m2r2"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = "index"

autosummary_generate = True
autosummary_imported_members = False

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

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
html_sidebars = {
    "**": [
        "searchbox.html",
        "globaltoc.html",
    ]
}


# Xanadu theme options (see theme.conf for more information).
html_theme_options = {
    "navbar_name": "Xanadu Sphinx Theme",
    "navbar_logo_colour": "#2d7c7f",
    # "navbar_home_link": "https://pennylane.ai",
    "navbar_left_links": [
        {
            "name": "Example1",
            "href": "javascript:void(0);",
        },
        {
            "name": "Blog",
            "href": "javascript:void(0);",
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
        "Any extra copyrights can be added here"
    ],
    "border_colour": "#19b37b",
    "prev_next_button_colour": "#19b37b",
    "prev_next_button_hover_colour": "#0e714d",
    "table_header_background_colour": "#edf7f4",
    "text_accent_colour": "#19b37b",
    "toc_marker_colour": "#19b37b",
    "toc_overview": True
}