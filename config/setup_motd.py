#!/usr/bin/env python

from dav_tools import requirements, commands, files
import sys


requirements.require(
   root=True,
   os=[requirements.OS.LINUX],
)

commands.execute('apt install -y landscape-common')                           # system info in motd
files.copy_file(f'{sys.path[0]}/.motd/motd-news', '/etc/default/motd-news')   # disable motd news
