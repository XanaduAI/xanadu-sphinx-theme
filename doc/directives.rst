Directives
==========


The Xanadu Sphinx Theme implements the custom Sphinx directives listed below.
For more information, consult the relevant Python module in the
`directives <xanadu_sphinx_theme/directives>`_ package.

Community Card
--------------

.. code-block:: rst

    .. community-card::
        :title: Weighted SubSpace QAOA to find maximum graph cliques
        :date: 03/07/2022
        :author: John Smith, Jane Doe
        :paper: https://example.com
        :code: https://code.com

        An explanation of the work.


.. community-card::
    :title: Weighted SubSpace QAOA to find maximum graph cliques
    :date: 03/07/2022
    :author: John Smith, Jane Doe
    :paper: https://example.com
    :code: https://code.com

    An explanation of the work.



Details Dropdown
----------------

.. code-block:: rest

    .. details::
        :title: Usage Details

        In general, the block takes D parameters and **must** have the following signature:

        .. code-block:: python

            unitary(parameter1, parameter2, ... parameterD, wires)

        For a block with multiple parameters, ``n_params_block`` is equal to the number of parameters in ``block``.
        For a block with a single parameter, ``n_params_block`` is equal to the length of the parameter array.

.. admonition:: Example:

    .. details::
        :title: Usage Details

        In general, the block takes D parameters and **must** have the following signature:

        .. code-block:: python

            unitary(parameter1, parameter2, ... parameterD, wires)

        For a block with multiple parameters, ``n_params_block`` is equal to the number of parameters in ``block``.
        For a block with a single parameter, ``n_params_block`` is equal to the length of the parameter array.


Gallery Item
------------

.. code-block:: rest

    .. gallery-item::
        :description: :doc:`Getting Started <started>`
        :figure: :figure: _static/teleport.png

    .. raw:: html

        <div style='clear:both'>

.. gallery-item::
    :description: :doc:`Getting Started <started>`
    :figure: _static/teleport.png

.. raw:: html

    <div style='clear:both'>

Index Card
----------

.. code-block:: rest

    .. index-card::
        :name: Using the theme
        :link: started.html
        :description: Get started using the Xanadu Sphinx theme

.. index-card::
    :name: Using the theme
    :link: started.html
    :description: Get started using the Xanadu Sphinx theme


Related
-------

.. code-block:: rest


    .. related::

       elements View elements
       configuration View configuration options

This adds a 'Related' section, with links to content, to the local table
of contents on the right.

.. related::

   elements View elements
   configuration View configuration options

Title Card
----------

.. code-block:: rest

    .. title-card::
        :name: 'lightning.qubit'
        :description: A fast state-vector qubit simulator written in C++
        :link: https://docs.pennylane.ai/projects/lightning

    .. raw:: html

        <div style='clear:both'>

.. title-card::
    :name: 'lightning.qubit'
    :description: A fast state-vector qubit simulator written in C++
    :link: https://docs.pennylane.ai/projects/lightning

.. raw:: html

    <div style='clear:both'>

YouTube Video
-------------

.. code-block:: rest

    .. youtube-video:: WOLzqeuXVT8
        :title: PennyLane, a framework for quantum programming
        :author: Xanadu, a Toronto-based quantum computing company

.. raw:: html

    <div class="row">

.. youtube-video:: WOLzqeuXVT8
    :title: PennyLane, a framework for quantum programming
    :author: Xanadu, a Toronto-based quantum computing company

.. youtube-video:: bnX57EjvFVQ
    :title: Quantum Computational Advantage with Borealis
    :author: Xanadu, a Toronto-based quantum computing company

.. raw:: html

    </div>


Author bio
----------

.. code-block:: rest

    .. bio:: John Smith
        :photo: _static/teleport.png

        Write the author bio content here. It must be preceded by a blank line.

.. bio:: John Smith
    :photo: _static/teleport.png

    Write the author bio content here. It must be preceded by a blank line.
