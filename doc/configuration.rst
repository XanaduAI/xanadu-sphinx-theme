.. _configuration:

Configuration
=============


The Xanadu Sphinx Theme supports the following options. These should be added to
the ``html_theme_options`` dictionary in your ``conf.py`` file.

``project_nav_name``
    The name of the project to appear in the left navigation bar,
    under the Xanadu logo.

``project_logo``
    If the project has a logo, set this to the path of the logo
    image file to appear in the left navigation bar,
    under the Xanadu logo. If defined, the project logo
    *replaces* ``project_nav_name``.

``touch_icon``
    Path to the main navigation sidebar Xanadu logo.
    You may find one to use here: :download:`_static/xanadu_logo.png`.

``touch_icon_small``
    Path to the main navigation sidebar small Xanadu logo.
    This is used if the table of contents is large, to save space.
    You may find one to use here: :download:`_static/xanadu_logo_small.png`.

``large_toc``
    If the table of contents is large enough to be scrollable, set
    this option to ``True``.

``disqus_comments_shortname``
    Disqus comment account shortname. If provided, the right hand
    sidebar of each page will contain a scrollable disqus comment box.

``google_analytics_account``:
    Google analytics universal account ID to enable tracking
    and analytics.

``homepage``
    Allow a separate homepage from the standard ``index.html`` Sphinx
    landing page.

``latex_macros``
    Define custom :math:`\LaTeX{}` macros. This is a multiline raw string
    of the form:

    .. code-block:: python

        latex_macros = r"""
        macroname: ['\\text{\#1}', 1],
        anothermacroname: ['\\hat{b}', 0],
        """

    where the second argument in the list is the number of arguments
    the macro takes.

    Note that both the backslash and the # symbol must be escaped.
