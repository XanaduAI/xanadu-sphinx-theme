.. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/xst_title.svg
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
        "navbar_logo_colour": "#123456",

        "navbar_home_link": "https://example.com",

        "navbar_left_links": [
            {
                "name": "Tutorials",
                "href": "https://example.com/tutorials",
            },
            {
                "name": "Install",
                "href": "install.html",
            },
            {
                "name": "Documentation",
                "href": "index.html",
                "active": True,
            }
        ],

        "navbar_right_links": [
            {
                "name": "FAQ",
                "href": "https://example.com/faq.html",
                "icon": "fas fa-question",
            },
            {
                "name": "GitHub",
                "href": "https://github.com/XanaduAI/example",
                "icon": "fab fa-github",
            }
        ],

        "extra_copyrights": [
            "TensorFlow, the TensorFlow logo, and any related marks are "
            "trademarks of Google Inc."
        ],

        "google_analytics_tracking_id": "UA-116279123-2",

        "prev_next_button_colour": "#b13a59",
        "prev_next_button_hover_colour": "#712b3d",
        "toc_marker_colour": "#b13a59",
        "table_header_background_colour": "#ffdce5",
        "border_colour": "#b13a59",
        "text_accent_colour": "#b13a59",
    }


Configuration
=============

The Xanadu Sphinx Theme supports the following options. These should be added to
the ``html_theme_options`` dictionary in your ``conf.py`` file.

``google_analytics_tracking_id``
    Google Analytics tracking ID to enable website analytics.

Navigation Bar
--------------

The following options customize the appearance of the navigation bar.

``navbar_name``
    Name of the project to appear in the navigation bar.

``navbar_wordmark_path``
    Path to the project wordmark to appear in the navigation bar. Specifying
    this option will replace the project name in the navigation bar. Eventually,
    this option will be removed in favour of ``navbar_name`` for the sake of
    consistency.

``navbar_logo_path``
    Path to the project logo that appears in the navigation bar. Defaults to
    ``_static/xanadu_logo.svg`` which points to the generated Xanadu (X) logo
    logo (see ``navbar_logo_colour``).

``navbar_logo_colour``
    Colour of the auto-generated Xanadu (X) logo (available at
    ``_static/xanadu_logo.svg``). Defaults to ``#000000`` (i.e., black).

``navbar_home_link``
    Link that is opened when the name or logo on the navigation bar is clicked.
    Defaults to ``index.html``.

``navbar_left_links``
    Links on the LHS of the navigation bar in the form of a list of dictionaries
    with the ``"name"``, ``"href"``, and optionally, ``"active"`` keys.

``navbar_right_links``
    Links on the RHS of the navigation bar in the form of a list of dictionaries
    with the ``"name"`` and ``"href"`` keys.

Footer
------

The following options customize the appearance of the footer.

``extra_copyrights``
    List of extra copyright notices to place in the footer.
    
Table of contents
-----------------

The following options customize the table of contents.

``toc_overview``
    If ``True``, the project name, and a link to the homepage ``index.rst``, is included
    in the left-hand table of contents.

Style Colours
-------------

The following options allow the colours of various theme elements to be altered.
These should be fully qualified CSS color specifiers such as ``#004B6B`` or
``#444``.

``border_colour``
    Border colour of accent rules and table headers.

``code_colour``
    Colour of code blocks and teletype text. Defaults to ``#8D1A38``.

``prev_next_button_colour`` and ``prev_next_button_hover_colour``
    Colours of the "Next" and "Previous" navigation buttons located at the
    bottom of most pages.

``table_header_background_colour``
    Background colour of table headers.

``text_accent_colour``
    Accent colour for text such as download links.

``toc_marker_colour``
    Colour of the marker beside the current ToC entry.


Directives
==========

The Xanadu Sphinx Theme implements the custom Sphinx directives listed below.
For more information, consult the relevant Python module in the
`directives <xanadu_sphinx_theme/directives>`_ package.

**Community Card**

    <No example is available yet.>

**Details**

    .. code-block:: rest
    
        .. details::
            :title: Usage Details

            In general, the block takes D parameters and **must** have the following signature:

            .. code-block:: python

                unitary(parameter1, parameter2, ... parameterD, wires)

            For a block with multiple parameters, ``n_params_block`` is equal to the number of parameters in ``block``.
            For a block with a single parameter, ``n_params_block`` is equal to the length of the parameter array.
            
    .. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/details.png
        :alt: Details
        :height: 253

**Gallery Item**

    .. code-block:: rest

        .. gallery-item::
            :description: :doc:`AmplitudeEmbedding <../code/api/pennylane.AmplitudeEmbedding>`
            :figure: _static/templates/embeddings/amplitude.png

    .. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/gallery_item.png
        :alt: Gallery Item
        :height: 232

**Index Card**

    .. code-block:: rest

        .. index-card::
            :name: Using PennyLane
            :link: introduction/pennylane.html
            :description: A guided tour of the core features of PennyLane
        
    .. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/index_card.png
        :alt: Index Card
        :height: 159
           
**Related Demo**

    <No example is available yet.>

**Title Card**

    .. code-block:: rest

        .. title-card::
            :name: 'lightning.qubit'
            :description: A fast state-vector qubit simulator written in C++
            :link: devices.html

    .. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/title_card.png
        :alt: Title Card
        :height: 161

**YouTube Video**

    <No example is available yet.>


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
