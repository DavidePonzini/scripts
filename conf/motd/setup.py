#!/usr/bin/env python

from dav_tools import requirements, commands, files, messages
import sys


if __name__ == '__main__':
   requirements.require(
      root=True,
      os=[requirements.OS.LINUX],
   )

   # system info
   commands.execute('apt install -y landscape-common')
   messages.info('Enabled system info')

   # motd news
   files.copy_file(f'{sys.path[0]}/.files/motd-news', '/etc/default/motd-news')
   messages.info('Disabled news')

   # services running
   files.copy_file(f'{sys.path[0]}/.files/60-services-running', '/etc/update-motd.d/60-services-running')
   messages.info('Enabled services running')
