"""
.. _example_gallery:

Example gallery item
====================

An example gallery item to highlight Sphinx gallery integration.
The module docstring will appear at the top of the page, and can
include arbitrary ReST markup.
"""

# Comments without a line of hashes will render
# as a Python comment cell.

##############################################################################
# .. note::
#
#    Comments beginning with 79 hashes will render as ReST markup
#    within the documentation: :math:`\int_0^1 x^2 ~dx`.

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x = np.linspace(0, 10)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x) + x + np.random.randn(50))
ax.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
ax.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
ax.plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
ax.plot(x, np.sin(x) - 2 * x + np.random.randn(50))
ax.plot(x, np.sin(x) + np.random.randn(50))

plt.show()


##############################################################################
# Images and plots generated within the script, as well as all output,
# will be automatically executed and inserted as an output cell.

y = np.random.random([4])
x = np.log(y)
print(y)


##############################################################################
# For scripts with large dependencies, or that might take too long to run,
# you can configure Sphinx gallery to skip the script execution, and instead
# place an output cell within a ReST comment block via the following
# syntax:
#
# .. code-block:: rest
#
#     .. rst-class:: sphx-glr-script-out
#
#      Out:
#
#      .. code-block:: none
#
#         -9.999666671111085e-05
#
# This renders like so:
#
# .. rst-class:: sphx-glr-script-out
#
#  Out:
#
#  .. code-block:: none
#
#     -9.999666671111085e-05
