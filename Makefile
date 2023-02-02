SCRIPTS = /scripts


update:
	apt update
	apt dist-upgrade -y
	apt autoremove -y
	apt autoclean

git_config:
	git config --global user.email "davide.ponzini95@gmail.com"
	git config --global user.name "Davide Ponzini"

bash:
	sed -i "s|^export SCRIPTS=.*|export SCRIPTS=$(SCRIPTS)|" ./config/.bashrc
	./config/setup_bash

grub:
	rm -fv /etc/default/grub /etc/grub.d/40_custom
	ln -v ./config/.grub /etc/default/grub			# grub config
	ln -v ./config/.grub_40_custom /etc/grub.d/40_custom	# clonezilla entry
	sudo update-grub

disable_gdm:
	sudo systemctl set-default multi-user

enable_gdm:
	sudo systemctl set-default graphical

export_terminal_profile:
	dconf dump /org/gnome/terminal/legacy/profiles:/ > ./config/.gnome-terminal-profiles.dconf

import_terminal_profile:
	dconf load /org/gnome/terminal/legacy/profiles:/ < ./config/.gnome-terminal-profiles.dconf

disable_lid_close:
	sed -i 's/#HandleLidSwitch=.*/HandleLidSwitch=ignore/' /etc/systemd/logind.conf
	systemctl restart systemd-logind.service

bios_local_time:
	timedatectl set-local-rtc 1 --adjust-system-clock
	systemctl restart systemd-logind.service

ipython3:
	apt install ipython3 -y
	apt install python3-pip -y
