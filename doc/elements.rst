Elements
========


Code
----

.. code-block:: python

	import pennylane as qml

	dev = qml.device("default.qubit", wires=2)

	@qml.qnode(dev)
	def circuit(x):
	    qml.RX(x, wires=0)
	    return qml.expval(qml.PauliZ(0))

	circuit(0.5)

Admonitions
-----------

.. admonition:: Definition
    :class: defn

    A **cat** is cat and that is that.


.. important::

   Quantum mechanics is objectively the coolest theory.

.. note::

   Classical mechanics is no longer cool.

.. warning::

   Is relativity cool?



Tables
------


.. rst-class:: docstable

    +---------------------+-------------------+--------------------------+
    | **Element**         |  **Type**         | **Description**          |
    +=====================+===================+==========================+
    | Cat 1               | A comfortable cat | This is an okay cat.     |
    +---------------------+-------------------+--------------------------+
    | Cat 2               | A fluffy cat      | This is the best cat.    |
    +---------------------+-------------------+--------------------------+
    | Cat 3               | A cat with a hat  | This cat is happy.       |
    +---------------------+-------------------+--------------------------+
