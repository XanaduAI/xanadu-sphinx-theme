Installation and getting started
================================


Xanadu Sphinx Theme requires Python 3. The latest version of the Xanadu Sphinx Theme
can be installed directly from the GitHub repository using ``pip``:

.. code-block:: bash

    $ pip install git+https://github.com/XanaduAI/xanadu-sphinx-theme


For use on `Read the Docs <https://readthedocs.org>`_, add the following
to your ``doc/requirements.txt`` file:

.. code-block:: bash

    git+git://github.com/XanaduAI/xanadu-sphinx-theme#egg=xanadu-sphinx-theme


Once installed, simply add/modify the following variables of your Sphinx ``conf.py``
configuration file to start using the Xanadu Sphinx Theme:

.. code-block:: python

    html_theme = 'xanadu'

.. code-block:: python

    html_sidebars = {
        '**' : [
            'logo-text.html',
            'searchbox.html',
            'globaltoc.html',
        ]
    }

.. code-block:: python

    html_theme_options = {
        "project_nav_name": "Project Name",
        "touch_icon": "_static/xanadu_logo.png",
        "touch_icon_small": "_static/xanadu_logo_small.png",
    }

Additional configuration options are detailed in :ref:`configuration`.

Downloads
---------

To help get you started with your Sphinx documentation, here are some
useful downloads:

* An example :download:`conf.py` file. Simply replace the relevant
  fields.

* :download:`_static/xanadu_logo.png`: Xanadu logo for the sidebar

* :download:`_static/xanadu_logo_small.png`: Smaller Xanadu logo for the sidebar

* :download:`_static/favicon.ico`: Favicon for browser tabs. Simply
  specify the path to this file in the ``html_favicon`` variable in ``conf.py``.


LaTeX Support
-------------

The following :math:`\LaTeX{}` macros are defined by default. Additional
macros can be defined in the ``conf.py`` file; see :ref:`configuration`.

* ``\pr`` : ``|\#1\rangle\langle\#1|``,
* ``\ket``: ``\left| \#1\right\rangle``,
* ``\bra``: ``\left\langle \#1\right|``,
* ``\xket``: ``\left| \#1\right\rangle_x``,
* ``\xbra``: ``\left\langle \#1\right|_x``,
* ``\braket``: ``\langle \#1 \rangle``,
* ``\braketD``: ``\langle \#1 \mid \#2 \rangle``,
* ``\braketT``: ``\langle \#1 \mid \#2 \mid \#3 \rangle``,
* ``\ketbra``: ``| #1 \rangle \langle #2 |``,
* ``\hc``: ``\text{h.c.}``,
* ``\cc``: ``\text{c.c.}``,
* ``\h``: ``\hat``,
* ``\nn``: ``\nonumber``,
* ``\di``: ``\frac{d}{d \#1}``,
* ``\uu``: ``\mathcal{U}``,
* ``\inn``: ``\text{in}``,
* ``\out``: ``\text{out}``,
* ``\vac``: ``\text{vac}``,
* ``\I``: ``\hat{\mathbf{1}}``,
* ``\x``: ``\hat{x}``,
* ``\p``: ``\hat{p}``,
* ``\a``: ``\hat{a}``,
* ``\ad``: ``\hat{a}^\dagger``,
* ``\n``: ``\hat{n}``,
* ``\nbar``: ``\overline{n}``,
* ``\sech``: ``\mathrm{sech~}``,
* ``\tanh``: ``\mathrm{tanh~}``,
* ``\re``: ``\text{Re}``,
* ``\im``: ``\text{Im}``,
* ``\tr``: ``\mathrm{Tr} #1``,
* ``\sign``: ``\text{sign}``,
* ``\overlr``: ``\overset\leftrightarrow{\#1}``,
* ``\overl``: ``\overset\leftarrow{\#1}``,
* ``\overr``: ``\overset\rightarrow{\#1}``,
* ``\avg``: ``\left< \#1 \right>``,
* ``\slashed``: ``\cancel{\#1}``,
* ``\bold``: ``\boldsymbol{\#1}``,
* ``\d``: ``\mathrm d``,
* ``\expect``: ``\langle #1 \rangle``,
* ``\pde``: ``\frac{\partial}{\partial \#1}``,
* ``\R``: ``\mathbb{R}``,
* ``\C``: ``\mathbb{C}``,
* ``\Ad``: ``\text{Ad}``,
* ``\Var``: ``\text{Var}``,
* ``\bx``: ``\mathbf{x}``,
* ``\bm``: ``\boldsymbol{\#1}``
