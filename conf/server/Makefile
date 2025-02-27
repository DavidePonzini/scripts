SHELL=/bin/bash

VENV=../../venv

ifeq ($(OS),Windows_NT)
        VENV_BIN=$(VENV)/Scripts
else
        VENV_BIN=$(VENV)/bin
endif


.PHONY:
        echo "Please specify a target to run."

apache:
        sudo apt install apache2 mysql-server php libapache2-mod-php php-mysql phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
        $(VENV_BIN)/python -m dav_tools.messages success "Apache configured successfully."

samba:
        sudo apt install -y samba
        sudo cp .files/smb.conf /etc/samba/smb.conf
        sudo service smbd restart
        $(VENV_BIN)/python -m dav_tools.messages success "Samba configured successfully."

ssh:
        sudo apt install -y openssh-server
        sudo cp .files/sshd_config /etc/ssh/sshd_config
        sudo service ssh restart
        $(VENV_BIN)/python -m dav_tools.messages success "SSH configured successfully."

fail2ban:
        sudo apt install -y fail2ban
        sudo cp .files/jail.local /etc/fail2ban/jail.local
        sudo service fail2ban restart
        $(VENV_BIN)/python -m dav_tools.messages success "Fail2Ban configured successfully."