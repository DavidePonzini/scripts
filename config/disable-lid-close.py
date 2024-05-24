#!/usr/bin/env python

from dav_tools import messages, commands, requirements


requirements.require(root=True, os=[requirements.OS.LINUX])

commands.execute("sed -i 's/#HandleLidSwitch=.*/HandleLidSwitch=ignore/' /etc/systemd/logind.conf")
commands.execute('systemctl restart systemd-logind.service')

messages.success('Closing the lid will now do nothing')
