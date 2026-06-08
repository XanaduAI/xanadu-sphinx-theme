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

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.


.. community-card::
    :title: Weighted SubSpace QAOA to find maximum graph cliques
    :date: 03/07/2022
    :author: John Smith, Jane Doe
    :paper: https://example.com
    :code: https://code.com

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.


.. code-block:: rst

    .. raw:: html

        <div class="row g-3">
            <div class="col-lg-6 col-md-6 col-12">

    .. community-card::
        :title: Weighted SubSpace QAOA to find maximum graph cliques
        :date: 03/07/2022
        :author: John Smith, Jane Doe
        :paper: https://example.com
        :code: https://code.com

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

    .. raw:: html

            </div>
            <div class="col-lg-6 col-md-6 col-12">

    .. community-card::
        :title: Quantum-Train Long Short-Term Memory (QT-LSTM) for Wave Prediction
        :date: 09/04/2024
        :author: John Smith, Jane Doe
        :paper: https://example.com
        :code: https://example.com

        In this demo we introduce our new Momentum-QNG optimization algorithm and benchmark it with Momentum and QNG.

    .. raw:: html

            </div>
        </div>

.. raw:: html

    <div class="row g-3">
        <div class="col-lg-6 col-md-6 col-12">

.. community-card::
    :title: Weighted SubSpace QAOA to find maximum graph cliques
    :date: 03/07/2022
    :author: John Smith, Jane Doe
    :paper: https://example.com
    :code: https://code.com

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. raw:: html

        </div>
        <div class="col-lg-6 col-md-6 col-12">

.. community-card::
    :title: Quantum-Train Long Short-Term Memory (QT-LSTM) for Wave Prediction
    :date: 09/04/2024
    :author: Lakshay Goel, Kovid Tandon
    :paper: https://example.com
    :code: https://example.com

    In this demo we introduce our new Momentum-QNG optimization algorithm and benchmark it with Momentum and QNG.

.. raw:: html

        </div>
    </div>



Details Dropdown
----------------

.. code-block:: rest

    .. details::
        :title: Important Details
        :href: important-details

        In general, the block takes D parameters and **must** have the following signature:

        .. code-block:: python

            unitary(parameter1, parameter2, ... parameterD, wires)

        For a block with multiple parameters, ``n_params_block`` is equal to the number of parameters in ``block``.
        For a block with a single parameter, ``n_params_block`` is equal to the length of the parameter array.

    .. details::
        :title: Usage Details

        This function can be used with any of the supported autodifferentiation frameworks. It also supports
        just-in-time compilation with JAX:

        .. code-block:: python

            jax.jit(unitary)(parameter1, parameter2, ... parameterD, wires)


.. admonition:: Example:

    .. details::
        :title: Important Details
        :href: important-details

        In general, the block takes D parameters and **must** have the following signature:

        .. code-block:: python

            unitary(parameter1, parameter2, ... parameterD, wires)

        For a block with multiple parameters, ``n_params_block`` is equal to the number of parameters in ``block``.
        For a block with a single parameter, ``n_params_block`` is equal to the length of the parameter array.

    .. details::
        :title: Usage Details

        This function can be used with any of the supported autodifferentiation frameworks. It also supports
        just-in-time compilation with JAX:

        .. code-block:: python

            jax.jit(unitary)(parameter1, parameter2, ... parameterD, wires)


Gallery Item
------------

.. code-block:: rest

    .. raw:: html

        <div class="gallery-grid">

    .. gallery-item::
        :description: :doc:`Getting Started <started>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Installation <started>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Configuration <configuration>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`API Reference <code>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Development Guide <directives>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Plugin Tutorials <gallery>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Device Docs <elements>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Optimization <elements>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Templates <directives>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Demos <gallery>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Machine Learning <elements>`
        :figure: _static/teleport.png

    .. gallery-item::
        :description: :doc:`Quantum Chemistry <elements>`
        :figure: _static/teleport.png

    .. raw:: html

        </div>

.. raw:: html

    <div class="gallery-grid">

.. gallery-item::
    :description: :doc:`Getting Started <started>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Installation <started>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Configuration <configuration>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`API Reference <code>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Development Guide <directives>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Plugin Tutorials <gallery>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Device Docs <elements>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Optimization <elements>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Templates <directives>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Demos <gallery>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Machine Learning <elements>`
    :figure: _static/teleport.png

.. gallery-item::
    :description: :doc:`Quantum Chemistry <elements>`
    :figure: _static/teleport.png

.. raw:: html

    </div>

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

.. code-block:: rst

    .. raw:: html

        <div class="row g-3">

    .. title-card::
        :name: Installation
        :description: Install and configure PennyLane in development mode.
        :link: guide/installation.html

    .. title-card::
        :name: Contribution guide
        :description: How to get involved in the PennyLane community and start contributing through issues, discussions, and pull requests.
        :link: guide/contributing.html

    .. title-card::
        :name: Software tests
        :description: Running tests.
        :link: guide/tests.html

    .. raw:: html

        </div>
        <div class="row g-3 mt-1">

    .. title-card::
        :name: Documentation
        :description: Building and contributing modules and packages to the PennyLane documentation.
        :link: guide/documentation.html

    .. title-card::
        :name: Architecture Design Records
        :description: Proposing important architectural decisions and tracking design rationale over time.
        :link: guide/adr.html

    .. title-card::
        :name: Deprecations and Removals
        :description: Ensuring safe migration paths when introducing breaking changes.
        :link: guide/deprecations_removals.html

    .. raw:: html

        </div>

.. raw:: html

    <div class="row g-3">

.. title-card::
    :name: Installation
    :description: Install and configure PennyLane in development mode.
    :link: guide/installation.html

.. title-card::
    :name: Contribution guide
    :description: How to get involved in the PennyLane community and start contributing through issues, discussions, and pull requests.
    :link: guide/contributing.html

.. title-card::
    :name: Software tests
    :description: Running tests.
    :link: guide/tests.html

.. raw:: html

    </div>
    <div class="row g-3 mt-1">

.. title-card::
    :name: Documentation
    :description: Building and contributing modules and packages to the PennyLane documentation.
    :link: guide/documentation.html

.. title-card::
    :name: Architecture Design Records
    :description: Proposing important architectural decisions and tracking design rationale over time.
    :link: guide/adr.html

.. title-card::
    :name: Deprecations and Removals
    :description: Ensuring safe migration paths when introducing breaking changes.
    :link: guide/deprecations_removals.html

.. raw:: html

    </div>

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
