#!/usr/bin/env python

from dav_tools import requirements, commands, files, messages
import sys


requirements.require(
   root=True,
   os=[requirements.OS.LINUX],
)

# system info
commands.execute('apt install -y landscape-common')
messages.success('Enabled system info')

# motd news
files.copy_file(f'{sys.path[0]}/.motd-news', '/etc/default/motd-news')
messages.success('Disabled news')

# fail2ban
files.copy_file(f'{sys.path[0]}/.fail2ban', '/etc/update-motd.d/86-fail2ban')
messages.success('Enabled fail2ban')
