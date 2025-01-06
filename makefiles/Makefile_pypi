########## Makefile start ##########
# Type: PyPi
# Author: Davide Ponzini

NAME=dav-tools
VENV=./venv

ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV)/Scripts
else
	VENV_BIN=$(VENV)/bin
endif


venv:
	python -m venv --clear $(VENV)
	$(VENV_BIN)/python -m pip install --upgrade -r requirements.txt

prepare: test documentation
	:

install: uninstall build
	$(VENV_BIN)/python -m pip install ./dist/*.whl

build: venv
	sudo rm -rf dist/
	$(VENV_BIN)/python -m build

uninstall:
	$(VENV_BIN)/python -m pip uninstall -y $(NAME)

documentation:
	make html -C docs/

test: install
	$(VENV_BIN)/python -m pytest

upload: prepare
	$(VENV_BIN)/python -m pip install --upgrade twine
	$(VENV_BIN)/python -m twine upload --verbose dist/*

download: uninstall
	$(VENV_BIN)/python -m pip install $(NAME)

