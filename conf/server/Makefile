VENV="../../venv"

ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV)/Scripts
else
	VENV_BIN=$(VENV)/bin
endif


samba:
	apt install -y samba
	cp .files/smb.conf /etc/samba/smb.conf
	service smbd restart
	$(VENV_BIN)/python -m dav_tools.messages success "Samba configured successfully."

ssh:
	apt install -y openssh-server
	cp .files/sshd_config /etc/ssh/sshd_config
	service ssh restart
	$(VENV_BIN)/python -m dav_tools.messages success "SSH configured successfully."

fail2ban:
	apt install -y fail2ban
	cp .files/jail.local /etc/fail2ban/jail.local
	service fail2ban restart
	$(VENV_BIN)/python -m dav_tools.messages success "Fail2Ban configured successfully."

apache:
	apt install apache2 mysql-server php libapache2-mod-php php-mysql phpmyadmin php-mbstring php-zip php-gd php-json php-curl -y
	mysql <<< "DROP USER IF EXISTS 'dba'@'localhost';"
	mysql <<< "CREATE USER 'dba'@'localhost' IDENTIFIED BY 'dav';"
	$(VENV_BIN)/python -m dav_tools.messages info "Created admin account: 'dba'@'localhost', password: 'dav'"
	$(VENV_BIN)/python -m dav_tools.messages success "Apache configured successfully."