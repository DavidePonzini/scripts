bash:
	./setup_bash
grub:
	rm -fv /etc/default/grub
	ln -v /scripts/config/.grub /etc/default/grub
	sudo update-grub2
disable_gdm:
	sudo systemctl set-default multi-user
enable_gdm:
	sudo systemctl set-default graphical
export_terminal_profile:
	dconf dump /org/gnome/terminal/legacy/profiles:/ > /scripts/config/.gnome-terminal-profiles.dconf
import_terminal_profile:
	dconf load /org/gnome/terminal/legacy/profiles:/ < /scripts/config/.gnome-terminal-profiles.dconf
disable_lid_close:
	sed -i 's/#HandleLidSwitch=.*/HandleLidSwitch=ignore/' /etc/systemd/logind.conf
	systemctl restart systemd-logind.service
bios_local_time:
	timedatectl set-local-rtc 1 --adjust-system-clock
