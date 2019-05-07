PYTHON3 := $(shell which python3 2>/dev/null)
PYTHON := python3

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  install            to install Xanadu Sphinx Theme"
	@echo "  docs               to build the documentation"
	@echo "  wheel              to build the Xanadu Sphinx Theme wheel"
	@echo "  dist               to package the source distribution"
	@echo "  clean              to delete all temporary, cache, and build files"

.PHONY: install
install:
ifndef PYTHON3
	@echo "To install Xanadu Sphinx Theme you need to have Python 3 installed"
endif
	$(PYTHON) setup.py install

.PHONY: wheel
wheel:
	$(PYTHON) setup.py bdist_wheel

.PHONY: dist
dist:
	$(PYTHON) setup.py sdist

docs:
	make -C doc html

.PHONY : clean
clean:
	make -C doc clean
