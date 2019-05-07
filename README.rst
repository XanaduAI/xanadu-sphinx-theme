Xanadu Sphinx theme
###################

The Xanadu Sphinx theme is an open-source Sphinx theme used for Xanadu open-source
Python packages.


.. raw:: html

    <img src="https://i.imgur.com/tKwJWwe.png" width="400px"  align="left"> <img src="https://i.imgur.com/QnoTFzt.png" width="400px"  align="left">


A fork of the `Guzzle <https://github.com/guzzle/guzzle_sphinx_theme>`_
Sphinx theme, the theme has the following features:


- **Responsive**: fluid layout that automatically adjusts for phone, tablet,
  and computer screens

- **In-built LaTeX macros**: comes with in-built support for MathJAX and common
  predefined quantum optics LaTeX macros

- **Cohesive design**: supports the Xanadu color scheme


Installation
============

Xanadu Sphinx Theme requires Python 3. The latest version of the Xanadu Sphinx theme
can be installed directly from the GitHub repository using ``pip``:

.. code-block:: bash

    $ pip install git+https://github.com/XanaduAI/xanadu-sphinx-theme


For use on `Read the Docs <https://readthedocs.org>`_, add the following
to your ``doc/requirements.txt`` file:

.. code-block:: bash

    git+git://github.com/XanaduAI/xanadu-sphinx-theme#egg=xanadu-sphinx-theme


Getting started
===============

Once installed, simply modify the following variables of your Sphinx ``conf.py``
configuration file to start using the Xanadu Sphinx theme:

.. code-block:: python

    html_theme = 'xanadu'

    html_sidebars = {
        '**' : [
            'logo-text.html',
            'searchbox.html',
            'globaltoc.html',
        ]
    }

    html_theme_options = {
        "project_nav_name": "Project Name",
        "touch_icon": "_static/xanadu_logo.png",
        "touch_icon_small": "_static/xanadu_logo_small.png",
    }

The files ``xanadu_logo.png`` and ``xanadu_logo_small.png`` can be downloaded
from the ``doc/_static/`` folder of this repository.


Configuration
=============

The Xanadu Sphinx theme supports the following options. These should be added to
the ``html_theme_options`` dictionary in your ``conf.py`` file.

``project_nav_name``
    The name of the project to appear in the left navigation bar,
    under the Xanadu logo

``project_logo``
    If the project has a logo, set this to the path of the logo
    image file to appear in the left navigation bar,
    under the Xanadu logo. If defined, the project logo
    *replaces* ``project_nav_name``.

``touch_icon``
    Path to the main navigation sidebar Xanadu logo.
    You may find one to use here: ``doc/_static/xanadu_logo.png``

``touch_icon_small``
    Path to the main navigation sidebar small Xanadu logo.
    This is used if the table of contents is large, to save space.
    You may find one to use here: ``doc/_static/xanadu_logo_small.png``

``large_toc``
    If the table of contents is large enough to be scrollable, set
    this option to ``True``

``disqus_comments_shortname``
    Disqus comment account shortname. If provided, the right hand
    sidebar of each page will contain a scrollable disqus comment box.

``google_analytics_account``:
    Google analytics universal account ID to enable tracking
    and analytics

``homepage``
    Allow a separate homepage from the standard ``index.html`` Sphinx
    landing page

``latex_macros``
    Define custom :math:`\LaTeX{}` macros. This is a multiline raw string
    of the form

    .. code-block:: python

        latex_macros = r"""
        macroname: ['\\text{\#1}', 1],
        anothermacroname: ['\\hat{b}', 0],
        """

    where the second argument in the list is the number of arguments
    the macro takes.

    Note that both the backslash and the # symbol must be escaped.


Support
=======

- **Source Code:** https://github.com/XanaduAI/xanadu-sphinx-theme
- **Issue Tracker:** https://github.com/XanaduAI/xanadu-sphinx-theme/issues

If you are having issues, please let us know by posting the issue on our Github issue tracker.


License
=======

The Xanadu Sphinx theme is **free** and **open source**, released under the Apache License, Version 2.0.
