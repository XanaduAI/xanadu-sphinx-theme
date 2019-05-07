# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python3
import sys
import os
from setuptools import setup


with open("xanadu_sphinx_theme/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")


requirements = ["sphinx"]


info = {
    "name": "xanadu-sphinx-theme",
    "version": version,
    "maintainer": "Xanadu Inc.",
    "maintainer_email": "josh@xanadu.ai",
    "url": "http://xanadu.ai",
    "license": "Apache License 2.0",
    "packages": ["xanadu_sphinx_theme"],
    "include_package_data": True,
    "entry_points": {"sphinx.html_themes": ["xanadu = xanadu_sphinx_theme"]},
    "description": "Sphinx theme for Xanadu open-source Python packages",
    "long_description": open("README.rst").read(),
    "provides": ["xanadu_sphinx_theme"],
    "install_requires": requirements,
}


classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Documentation",
    "Topic :: Software Development :: Documentation",
]


setup(classifiers=classifiers, **(info))
