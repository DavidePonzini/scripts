GIT_USER_EMAIL="davide.ponzini95@gmail.com"
GIT_USER_NAME="Davide Ponzini"


install-all: git_config python

python:
	sudo apt install python3 python-is-python3 ipython3 -y
	python -m pip install --upgrade pip pipreqs dav-tools
	python ./py-install-packages.py

git_config:
	git config --global user.email $(GIT_USER_EMAIL)
	git config --global user.name $(GIT_USER_NAME)
	git config --global pull.rebase false

