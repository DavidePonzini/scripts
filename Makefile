
update:
	apt update
	apt dist-upgrade -y
	apt autoremove -y
	apt autoclean
git_config:
	git config --global user.email "davide.ponzini95@gmail.com"
	git config --global user.name "Davide Ponzini"
lid_close:
	sed -i 's/#HandleLidSwitch=.*/HandleLidSwitch=ignore/' /etc/systemd/logind.conf
	systemctl restart systemd-logind.service
bash_conf:
	rm -f ~/.bash_aliases ~/.bashrc
	ln /scripts/config/.bash_aliases ~/.bash_aliases
	ln /scripts/config/.bashrc ~/.bashrc
npm:
	apt install npm -y
ipython3:
	apt install ipython3 -y
ssh:
	apt install openssh-client openssh-server -y
	service ssh start
	ssh-keygen -t rsa
vftpd:
	apt install vsftpd -y
	#replace '\^root\$' '# root' -- /etc/ftpusers	# Allow root login
transmission-cli:
	apt install transmission-cli -y
