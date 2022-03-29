.. image:: doc/_static/xst_title.svg
    :alt: Xanadu Sphinx Theme
    :height: 65
    :width: 100%

The **Xanadu Sphinx Theme** (XST) is a Sphinx theme used for open-source Xanadu
software projects.

A fork of the `Guzzle <https://github.com/guzzle/guzzle_sphinx_theme>`_
Sphinx theme, the theme has the following features:

* *Responsive*. Fluid layout that automatically adjusts for phone, tablet,
  and computer screens.

* *LaTeX Macros*. Comes with built-in support for MathJAX and common predefined
  quantum optics LaTeX macros.

* *Cohesive Design*. Unifies the appearance of all Xanadu Sphinx documentation.


Installation
============

The Xanadu Sphinx Theme requires Python 3.7 or later. The latest version of the
XST can be installed directly from the GitHub repository using ``pip``:

.. code-block:: bash

    pip install git+https://github.com/XanaduAI/xanadu-sphinx-theme


For use on `Read the Docs <https://readthedocs.org>`_, add the following to your
``doc/requirements.txt`` file:

.. code-block:: bash

    git+git://github.com/XanaduAI/xanadu-sphinx-theme#egg=xanadu-sphinx-theme


Getting Started
===============

Once installed, simply add or modify the following variables of your Sphinx
``conf.py`` configuration file to start using the Xanadu Sphinx Theme:

.. code-block:: python

    html_theme = "xanadu"

.. code-block:: python

    html_sidebars = {
        "**" : [
            "searchbox.html",
            "globaltoc.html",
        ]
    }

.. code-block:: python

    html_theme_options = {
        "navbar_name": "Example Project",
        "border_colour": "#444444",
        "prev_next_button_colour": "#666666",
        "prev_next_button_hover_colour": "#222222",
        "toc_marker_colour": "#444444",
        "table_header_background_colour": "#444444",
        "text_accent_colour": "#444444",
        "github_repository_url": "https://github.com/XanaduAI/Example",
    }


Configuration
=============

The Xanadu Sphinx Theme supports the following options. These should be added to
the ``html_theme_options`` dictionary in your ``conf.py`` file.

``google_analytics_tracking_id``
    Google Analytics tracking ID to enable website analytics.

``github_repository_url``
    URL to the project GitHub repository.

Navigation Bar
--------------

The following options customize the appearance of the navigation bar.

``navbar_name``
    Name of the project to appear in the navigation bar.

``navbar_logo_path``
    Path to the project logo that appears in the navigation bar. Defaults to
    ``_static/x.svg`` which points to the instantiated Xanadu (X) SVG logo
    (see ``navbar_logo_colour``).

``navbar_logo_colour``
    Colour to apply to the Xanadu (X) SVG logo template. Defaults to ``#000000``
    (i.e., black).

Style Colours
-------------

The following options allow the colours of various theme elements to be altered.
These should be fully qualified CSS color specifiers such as ``#004B6B`` or
``#444``.

``border_colour``
    Border colour of accent rules and table headers.

``prev_next_button_colour`` and ``prev_next_button_hover_colour``
    Colours of the "Next" and "Previous" navigation buttons located at the
    bottom of most pages.

``table_header_background_colour``
    Background colour of table headers.

``text_accent_colour``
    Accent colour for text such as download links.

``toc_marker_colour``
    Colour of the marker beside the current ToC entry.


Support
=======

- **Source Code:** https://github.com/XanaduAI/xanadu-sphinx-theme
- **Issue Tracker:** https://github.com/XanaduAI/xanadu-sphinx-theme/issues

If you are having issues, please let us know by posting the issue on our Github
issue tracker.


License
=======

The Xanadu Sphinx Theme is **free** and **open source**, released under the
`Apache License, Version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_.
