"""
Example Sphinx-Gallery demo
===========================

This tutorial is an example demo generated using Sphinx Gallery.

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
# Author
# ------
#
# .. bio:: John Smith
#     :photo: ../_static/teleport.png
#
#     Write the author bio content here. It must be preceded by a blank line.
