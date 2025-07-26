SHELL=/bin/bash
VENV=../../venv
USER=DavidePonzini

ifeq ($(OS),Windows_NT)
        VENV_BIN=$(VENV)/Scripts
else
        VENV_BIN=$(VENV)/bin
endif

MESSAGE=$(VENV_BIN)/python -m dav_tools.messages


.PHONY: apache apache-certbot samba ssh fail2ban postgresql common



nginx:
	sudo apt install nginx -y
	@$(MESSAGE) success 'Installed Nginx'
	sudo cp .files/nginx/ponzidav.conf /etc/nginx/sites-available/ponzidav.conf
	sudo ln -sf /etc/nginx/sites-available/ponzidav.conf /etc/nginx/sites-enabled/ponzidav.conf
	sudo nginx -t
	sudo systemctl reload nginx
	@$(MESSAGE) success 'Configured reverse proxy'

nginx-certbot:
	sudo apt install certbot python3-certbot-nginx -y
	sudo certbot --nginx -d ponzidav.com -d www.ponzidav.com -d lensql.ponzidav.com -d dev.lensql.ponzidav.com -d gpt4ct.ponzidav.com
	@$(MESSAGE) success 'Certbot configured successfully'
	sudo certbot renew --dry-run
	@$(MESSAGE) success 'Certbot renewal tested successfully'

apache:
	sudo apt install apache2 mysql-server php libapache2-mod-php php-mysql phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
	@$(MESSAGE) success 'Installed Apache'
	sudo a2enmod headers
	sudo a2enmod proxy
	sudo a2enmod proxy_http
	sudo cp .files/apache2/sites-available/* /etc/apache2/sites-available/
	sudo service apache2 restart
	@$(MESSAGE) success 'Configured reverse proxy service'

apache-certbot:
	sudo apt install apache2 certbot python3-certbot-apache -y
	sudo a2enmod ssl
	sudo systemctl restart apache2
	sudo certbot --apache
	@$(MESSAGE) success 'Certbot configured successfully'
	sudo certbot renew --dry-run
	@$(MESSAGE) success 'Certbot renewal tested successfully'

samba:
	sudo apt install -y samba
	sudo cp .files/samba/smb.conf /etc/samba/smb.conf
	sudo service smbd restart
	@$(MESSAGE) success 'Samba configured successfully'

ssh:
	sudo apt install -y openssh-server
	sudo cp .files/ssh/sshd_config /etc/ssh/sshd_config
	sudo service ssh restart
	@$(MESSAGE) success 'SSH configured successfully'
	ssh-import-id gh:$(USER)
	@$(MESSAGE) success "Imported SSH keys from GitHub user $(USER)"

fail2ban:
	sudo apt install -y fail2ban
	sudo cp .files/fail2ban/jail.local /etc/fail2ban/jail.local
	sudo service fail2ban restart
	@$(MESSAGE) success 'Fail2Ban configured successfully.'

postgresql:
	sudo apt install postgresql libpq-dev -y
	$(VENV_BIN)/python -m pip install --upgrade psycopg2
	@$(MESSAGE) success 'Installed PostgreSQL'

common:
	sudo apt install ubuntu-restricted-extras vlc

qbittorrent:
	sudo apt install qbittorrent-nox
	sudo cp .files/qbittorrent-nox/qbittorrent-nox.service /etc/systemd/system/qbittorrent-nox.service
	sudo systemctl enable qbittorrent-nox
	@$(MESSAGE) success 'qBitTorrent daemon configured successfully'
