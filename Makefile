GIT_USER_EMAIL="davide.ponzini95@gmail.com"
GIT_USER_NAME="Davide Ponzini"
PYTHON=python3
VENV=./.venv

ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV)/Scripts
else
	VENV_BIN=$(VENV)/bin
endif


venv:
	python -m venv $(VENV)
	$(VENV_BIN)/python -m pip install --upgrade -r requirements.txt

python:
	sudo apt install $(PYTHON)-full $(PYTHON)-pip ipython3 -y
	sudo rm -f /usr/bin/python
	sudo ln -s /usr/bin/$(PYTHON) /usr/bin/python				# link generic `python` to latest version

postgresql:
	sudo apt install postgresql libpq-dev -y
	$(VENV_BIN)/python -m pip install --upgrade psycopg2

git_config:
	git config --global user.email $(GIT_USER_EMAIL)
	git config --global user.name $(GIT_USER_NAME)
	git config --global pull.rebase false
	git config --global alias.history "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)' --all"

common_apps:
	sudo apt install ubuntu-restricted-extras vlc
