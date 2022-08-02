
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
ipython3:
	apt install ipython3 -y
	apt install python3-pip -y
vftpd:
	apt install vsftpd -y
	#replace '\^root\$' '# root' -- /etc/ftpusers	# Allow root login
