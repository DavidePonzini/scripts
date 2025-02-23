#!/usr/bin/env python

from dav_tools import requirements, commands, files, messages
import sys


def install_fail2ban(result):
      files.copy_file(f'{sys.path[0]}/.files/88-fail2ban', '/etc/update-motd.d/88-fail2ban')
      messages.info('Enabled fail2ban')

def skip_fail2ban():
      messages.info('fail2ban is not installed, skipping')


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

   # fail2ban
   commands.get_output('which fail2ban-client', on_success=install_fail2ban, on_error=skip_fail2ban)
