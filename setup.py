from setuptools import setup, find_packages

with open("xanadu_sphinx_theme/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")


requirements = [
    "sphinx",
    "importlib_resources",
    # The packages below are used to generate thumbnail images.
    "pillow",
    "sphinx-gallery",
]

info = {
    "description": "Sphinx theme for Xanadu open-source Python packages",
    "entry_points": {"sphinx.html_themes": ["xanadu = xanadu_sphinx_theme"]},
    "maintainer": "Xanadu Inc.",
    "maintainer_email": "software@xanadu.ai",
    "install_requires": requirements,
    "license": "Apache License 2.0",
    "license_files": ["LICENSE"],
    "long_description": open("README.rst").read(),
    "long_description_content_type": "text/x-rst",
    "include_package_data": True,
    "name": "xanadu-sphinx-theme",
    "packages": find_packages(where="."),
    "package_data": {
        "xanadu_sphinx_theme": ["static/*", "*.html", "theme.conf", "templates/*/*.rst"],
    },
    "provides": ["xanadu_sphinx_theme"],
    "url": "https://github.com/XanaduAI/xanadu-sphinx-theme",
    "version": version,
}

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Documentation",
    "Topic :: Documentation :: Sphinx",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
]


setup(classifiers=classifiers, **info)
