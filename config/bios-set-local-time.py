#!/usr/bin/env python

from dav_tools import messages, commands, requirements


requirements.require(
    os=[requirements.OS.LINUX]
)


commands.execute('timedatectl set-local-rtc 1 --adjust-system-clock')
commands.execute('systemctl restart systemd-logind.service')

messages.success('BIOS will now use local time')
