PYTHON3 := $(shell which python3 2>/dev/null)
PYTHON := python3

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  install            to install the Xanadu Sphinx Theme"
	@echo "  wheel              to build the Xanadu Sphinx Theme wheel"
	@echo "  dist               to build the Xanadu Sphinx Theme source distribution"
	@echo "  docs               to generate the Sphinx documentation"
	@echo "  lint               to lint the Python source files"
	@echo "  format             to format the Python source files"
	@echo "  clean              to delete all temporary, cache, and build files"
	@echo "  clean-docs         to delete all generated documentation"

.PHONY: install
install:
ifndef PYTHON3
	@echo "You need to install Python 3 before installing the Xanadu Sphinx Theme"
endif
	$(PYTHON) -m pip install -e .

.PHONY: wheel
wheel:
	$(PYTHON) -m build --no-isolation --wheel

.PHONY: dist
dist:
	$(PYTHON) -m build --no-isolation --sdist

.PHONY : docs
docs:
	make -C docs html

.PHONY: lint
lint:
	$(PYTHON) -m pylint xanadu_sphinx_theme

.PHONY: format
format:
	$(PYTHON) -m black --check --diff --color -l 100 xanadu_sphinx_theme
	$(PYTHON) -m isort --check --diff --color --profile black xanadu_sphinx_theme

.PHONY : clean
clean:
	rm -rf build
	rm -rf dist
	rm -rf xanadu_sphinx_theme/__pycache__

.PHONY : clean-docs
clean-docs:
	rm -rf docs/api
	make -C docs clean
