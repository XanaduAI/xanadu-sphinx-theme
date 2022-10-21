"""
Example Sphinx-Gallery demo
===========================

This tutorial is an example demo generated using Sphinx Gallery. Here are a few
references to see what they look like [#stokes2019]_ [#sweke2019]_.

System Info
-----------
"""

import platform
uname = platform.uname()

###############################################################
# Let's print out the system information.

print("="*20, "System Information", "="*20)
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

###############################################################
# References
# ----------
#
# .. [#stokes2019]
#
#     James Stokes, Josh Izaac, Nathan Killoran, and Giuseppe Carleo. "Quantum Natural Gradient."
#     `arXiv:1909.02108 <https://arxiv.org/abs/1909.02108>`__ (2019).
#
# .. [#sweke2019]
#
#     Ryan Sweke, Frederik Wilde, Johannes Jakob Meyer, Maria Schuld, Paul K. Fährmann, Barthélémy
#     Meynard-Piganeau, and Jens Eisert. "Stochastic gradient descent for hybrid quantum-classical
#     optimization." `arXiv:1910.01155 <https://arxiv.org/abs/1910.01155>`__ (2019).
#
# Author
# ------
#
# .. bio:: John Smith
#     :photo: ../_static/teleport.png
#
#     Write the author bio content here. It must be preceded by a blank line.
