.. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/xst_title.svg
    :alt: Xanadu Sphinx Theme
    :height: 65
    :width: 100%

.. header-start-inclusion-marker-do-not-remove

The **Xanadu Sphinx Theme** (XST) is a Sphinx theme used for open-source Xanadu
software projects.

A fork of the `Guzzle <https://github.com/guzzle/guzzle_sphinx_theme>`_
Sphinx theme, the theme has the following features:

* *Responsive*. Fluid layout that automatically adjusts for phone, tablet,
  and computer screens.

* *LaTeX Macros*. Comes with built-in support for MathJAX and common predefined
  quantum optics LaTeX macros.

* *Cohesive Design*. Unifies the appearance of all Xanadu Sphinx documentation.

.. header-end-inclusion-marker-do-not-remove


Installation
============

.. installation-start-inclusion-marker-do-not-remove

The Xanadu Sphinx Theme requires Python 3.7 or later. The latest version of the
XST can be installed directly from the GitHub repository using ``pip``:

.. code-block:: bash

    pip install xanadu-sphinx-theme


.. installation-end-inclusion-marker-do-not-remove


Getting Started
===============

.. getting-started-start-inclusion-marker-do-not-remove

Once installed, simply add or modify the following variables of your Sphinx
``conf.py`` configuration file to start using the Xanadu Sphinx Theme:

.. code-block:: python

    from xanadu_sphinx_theme import templates_dir

    # Add Xanadu Sphinx Theme autosummary templates
    templates_path = [templates_dir()]

    html_theme = "xanadu"

    html_theme_options = {
        "navbar_name": "Example Project",
        "navbar_logo_colour": "#123456",

        "navbar_home_link": "https://example.com",

        "github_repo": "",
        "navbar_left_links": [
            {
                "name": "Tutorials",
                "href": "https://example.com/tutorials",
                "img": "_static/tutorial.png",
                "img_width": "30px",
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

.. getting-started-end-inclusion-marker-do-not-remove

Configuration
=============

.. configuration-start-inclusion-marker-do-not-remove

The Xanadu Sphinx Theme supports the following options. These should be added to
the ``html_theme_options`` dictionary in your ``conf.py`` file.

``google_analytics_tracking_id``
    Google Analytics tracking ID to enable website analytics.
    
``github_repo``
    The GitHub organization and repository associated with the documentation. E.g.,
    for a GitHub repository https://github.com/Organization/repo, this should be
    ``"github_repo": "Organization/repo"``.

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
    with the ``"name"``, ``"href"``, and optionally, ``"active"`` keys. In addition,
    the ``"img"`` key can be used to specify an image for the navbar link,
    alongside ``"img_width"`` to specify the width of the image.

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

``toc_global``
    Whether to show the global table of contents by default via the left sidebar.
    If ``False``, then the left sidebar will be disabled.

``toc_hover``
    Whether hovering over the active navbar link (or navbar logo if there is
    no active navbar link) will show the global table of contents as a dropdown.
    Only applies if ``toc_global=False``.

``toc_subset``
    If set to ``True``, and the current page has no local table of contents,
    the right-hand table of contents will instead display the current subset
    of the document tree. That is, the right-hand ToC will display the location
    in the document of the current page. If ``False``, and the current page
    has no local table of contents, no right-hand ToC will be shown.

``relations``
    If ``True``, then Next and Previous buttons are included at the bottom of
    every page, allowing navigation according to the table of contents.

Footer
------

``footer_about``
    A dictionary of the form ``{"title": ..., "description": ...}`` that specifies
    the 'About' section of the footer. Set to an empty dictionary to remove.

``footer_links``
    A list of dictionaries of the form

    .. code-block:: python

        "footer_links": [
            {
                "title": "Column1",
                "links": [
                    {
                        "name": "Home",
                        "href": "https://pennylane.ai/",
                    },
                    {
                        "name": "Learn",
                        "href": "https://pennylane.ai/qml",
                    }
                ]
            },
            {
                "title": "Column2",
                "links": [...]
            }
        ]

    that specifies footer links. Each top-level dictionary in the list is a
    separate titled column. Set to an empty list to remove.


``footer_socials``
    A list of dictionaries of the form

    .. code-block:: python

        "footer_socials": [
            {
                "icon": "fab fa-twitter",
                "href": "https://twitter.com/xanaduai"
            },
            {
                "icon": "fab fa-github",
                "href": "https://github.com/XanaduAI"
            },
            ...
        ]

    specifying social media icons. ``icon`` should correspond to a FontAwesome5 icon.
    Set to an empty list to remove.

``footer_tagline``
    A dictionary of the form ``{"text": "Some text", "href": "https://..."}`` specifying
    a tagline hyperlink that appears underneath the social media icons. Set to an
    empty dictionary to remove.

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

.. configuration-end-inclusion-marker-do-not-remove

Directives
==========

.. directives-start-inclusion-marker-do-not-remove

The Xanadu Sphinx Theme implements the custom Sphinx directives listed below.
For more information, consult the relevant Python module in the
`directives <xanadu_sphinx_theme/directives>`_ package.

Community Card
--------------

<No example is available yet.>

**Details**

.. code-block:: rest

    .. details::
        :title: Usage Details

        In general, the block takes :math:`D` parameters and **must** have the following signature:

        .. code-block:: python

            unitary(parameter1, parameter2, ... parameterD, wires)

        For a block with multiple parameters, ``n_params_block`` is equal to the number of parameters in ``block``.
        For a block with a single parameter, ``n_params_block`` is equal to the length of the parameter array.

.. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/details.png
    :alt: Details
    :height: 253

Gallery Item
------------

.. code-block:: rest

    .. gallery-item::
        :description: :doc:`AmplitudeEmbedding <../code/api/pennylane.AmplitudeEmbedding>`
        :figure: _static/templates/embeddings/amplitude.png

.. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/gallery_item.png
    :alt: Gallery Item
    :height: 232

Index Card
----------

.. code-block:: rest

    .. index-card::
        :name: Using PennyLane
        :link: introduction/pennylane.html
        :description: A guided tour of the core features of PennyLane

.. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/index_card.png
    :alt: Index Card
    :height: 159

Related Demo
------------

<No example is available yet.>

Title Card
----------

.. code-block:: rest

    .. title-card::
        :name: 'lightning.qubit'
        :description: A fast state-vector qubit simulator written in C++
        :link: devices.html

.. image:: https://raw.githubusercontent.com/XanaduAI/xanadu-sphinx-theme/master/doc/_static/directives/title_card.png
    :alt: Title Card
    :height: 161

YouTube Video
-------------

<No example is available yet.>


.. directives-end-inclusion-marker-do-not-remove

Support
=======

.. support-start-inclusion-marker-do-not-remove

- **Source Code:** https://github.com/XanaduAI/xanadu-sphinx-theme
- **Issue Tracker:** https://github.com/XanaduAI/xanadu-sphinx-theme/issues

If you are having issues, please let us know by posting the issue on our Github
issue tracker.

.. support-end-inclusion-marker-do-not-remove

License
=======

.. license-start-inclusion-marker-do-not-remove

The Xanadu Sphinx Theme is **free** and **open source**, released under the
`Apache License, Version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_.

.. license-end-inclusion-marker-do-not-remove
