#!/usr/bin/env python

from dav_tools import requirements, commands, messages, files, argument_parser
import sys


if __name__ == '__main__':
    argument_parser.set_description('Configure home server')
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.args

    requirements.require(root=True, os=[requirements.OS.LINUX])

    # install requirements
    commands.execute('apt install samba fail2ban -y')

    # samba
    files.copy_file(f'{sys.path[0]}/.config/smb.conf', '/etc/samba/smb.conf',)
    commands.execute('service smbd restart')
    messages.success('Configured Samba')

    # ssh
    files.copy_file(f'{sys.path[0]}/.config/sshd_config', '/etc/ssh/sshd_config',)
    commands.execute('service ssh restart')
    messages.success('Configured SSH')

    # fail2ban
    files.copy_file(f'{sys.path[0]}/.config/jail.local', '/etc/fail2ban/jail.local',)
    commands.execute('service fail2ban restart')
    messages.success('Configured fail2ban')
