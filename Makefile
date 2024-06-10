GIT_USER_EMAIL="davide.ponzini95@gmail.com"
GIT_USER_NAME="Davide Ponzini"
PYTHON_INTERPRETER=python3.12

# install-all: git_config python

python:
	sudo apt install $(PYTHON_INTERPRETER)-full ipython3 -y
	sudo rm -f /usr/bin/python
	sudo ln -s /usr/bin/$(PYTHON_INTERPRETER) /usr/bin/python		# link generic `python` to latest version
	python -m pip install --upgrade pip pipreqs dav-tools
	python ./py-install-packages.py

postgresql:
	sudo apt install postgresql libpq-dev -y
	python -m pip install --upgrade psycopg2

git_config:
	git config --global user.email $(GIT_USER_EMAIL)
	git config --global user.name $(GIT_USER_NAME)
	git config --global pull.rebase false

