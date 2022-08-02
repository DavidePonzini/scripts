bash:
	./setup_bash

grub:
	rm -fv /etc/default/grub
	ln -v /scripts/config/.grub /etc/default/grub
	sudo update-grub2

disable-gdm:
	sudo systemctl set-default multi-user

enable-gdm:
	sudo systemctl set-default graphical

export-terminal-profile:
	dconf dump /org/gnome/terminal/legacy/profiles:/ > /scripts/config/.gnome-terminal-profiles.dconf

import-terminal-profile:
	dconf load /org/gnome/terminal/legacy/profiles:/ < /scripts/config/.gnome-terminal-profiles.dconf
