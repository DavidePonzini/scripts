SCRIPTS = /scripts


full_update:
	git pull
	./update

git_config:
	git config --global user.email "davide.ponzini95@gmail.com"
	git config --global user.name "Davide Ponzini"

bash:
	sed -i "s|^export SCRIPTS=.*$|export SCRIPTS=$(SCRIPTS)|" ./config/.bashrc
	./config/setup_bash

grub:
	rm -f /etc/default/grub /etc/grub.d/40_custom
	cp ./config/.grub /etc/default/grub			# grub config
	cp ./config/.grub_40_custom /etc/grub.d/40_custom	# custom entries
	sudo update-grub

disable_gdm:
	sudo systemctl set-default multi-user

enable_gdm:
	sudo systemctl set-default graphical

export_terminal_profile:
	dconf dump /org/gnome/terminal/legacy/profiles:/ > ./config/.gnome-terminal-profiles.dconf

import_terminal_profile:
	dconf load /org/gnome/terminal/legacy/profiles:/ < ./config/.gnome-terminal-profiles.dconf
