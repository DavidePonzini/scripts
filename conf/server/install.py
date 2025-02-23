#!/usr/bin/env python

from dav_tools import requirements, commands, messages, files, argument_parser
import sys


if __name__ == '__main__':
    argument_parser.set_description('Configure home server')
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.add_argument('--samba', help='Install and configure Samba', action='store_true', default=False)
    argument_parser.add_argument('--ssh', help='Install and configure SSH', action='store_true', default=False)
    argument_parser.add_argument('--fail2ban', help='Install and configure fail2ban', action='store_true', default=False)
    argument_parser.args

    requirements.require(root=True, os=[requirements.OS.LINUX])

    # install requirements
    packages = []
    if argument_parser.args.samba:
        packages.append('samba')
    if argument_parser.args.ssh:
        packages.append('openssh-server')
    if argument_parser.args.fail2ban:
        packages.append('fail2ban')
    
    if packages:
        commands.execute(f'apt install {" ".join(packages)} -y')

    # samba
    files.copy_file(f'{sys.path[0]}/.files/smb.conf', '/etc/samba/smb.conf',)
    commands.execute('service smbd restart')
    messages.success('Configured Samba')

    # ssh
    files.copy_file(f'{sys.path[0]}/.files/sshd_config', '/etc/ssh/sshd_config',)
    commands.execute('service ssh restart')
    messages.success('Configured SSH')

    # fail2ban
    files.copy_file(f'{sys.path[0]}/.files/jail.local', '/etc/fail2ban/jail.local',)
    commands.execute('service fail2ban restart')
    messages.success('Configured fail2ban')
