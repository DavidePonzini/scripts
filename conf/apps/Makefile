SHELL=/bin/bash
VENV=../../venv

ifeq ($(OS),Windows_NT)
        VENV_BIN=$(VENV)/Scripts
else
        VENV_BIN=$(VENV)/bin
endif

MESSAGE=$(VENV_BIN)/python -m dav_tools.messages


.PHONY: apache apache-certbot samba ssh fail2ban postgresql common



apache:
	sudo apt install apache2 mysql-server php libapache2-mod-php php-mysql phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
	@$(MESSAGE) success 'Apache configured successfully.'

apache-certbot:
	sudo apt install apache2 certbot python3-certbot-apache -y
	sudo a2enmod ssl
	sudo systemctl restart apache2
	sudo certbot --apache
	@$(MESSAGE) success 'Certbot configured successfully.'
	sudo certbot renew --dry-run
	@$(MESSAGE) success 'Certbot renewal tested successfully.'

samba:
	sudo apt install -y samba
	sudo cp .files/smb.conf /etc/samba/smb.conf
	sudo service smbd restart
	@$(MESSAGE) success 'Samba configured successfully.'

ssh:
	sudo apt install -y openssh-server
	sudo cp .files/sshd_config /etc/ssh/sshd_config
	sudo service ssh restart
	@$(MESSAGE) success 'SSH configured successfully.'

fail2ban:
	sudo apt install -y fail2ban
	sudo cp .files/jail.local /etc/fail2ban/jail.local
	sudo service fail2ban restart
	@$(MESSAGE) success 'Fail2Ban configured successfully.'

postgresql:
	sudo apt install postgresql libpq-dev -y
	$(VENV_BIN)/python -m pip install --upgrade psycopg2

common:
	sudo apt install ubuntu-restricted-extras vlc

