
update:
	apt update
	apt dist-upgrade -y
	apt autoremove -y
	apt autoclean

npm:
	apt install npm -y
ipython3:
	apt intall ipython3 -y
ssh:
	apt install openssh-client openssh-server -y
	service ssh start
	ssh-keygen -t rsa

svftpd:
	apt install vsftpd -y
	replace '\^root\$' '# root' -- /etc/ftpusers	# Allow root login

