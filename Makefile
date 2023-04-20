SCRIPTS = /scripts

GIT_USER_EMAIL="davide.ponzini95@gmail.com"
GIT_USER_NAME="Davide Ponzini"


install: bash git_config update

update:
	git pull
	./update-packages

git_config:
	git config --global user.email $(GIT_USER_EMAIL)
	git config --global user.name $(GIT_USER_NAME)

bash:
	sed -i "s/^export SCRIPTS=.*$/export SCRIPTS=$(SCRIPTS)/" ./config/.bash/.bashrc
	./config/bash-setup

grub:
	rm -f /etc/default/grub /etc/grub.d/40_custom
	cp ./config/.grub /etc/default/grub			# grub config
	cp ./config/.grub_40_custom /etc/grub.d/40_custom	# custom entries
	sudo update-grub

