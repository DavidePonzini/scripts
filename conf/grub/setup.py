#!/usr/bin/env python

from dav_tools import requirements, commands, messages, files, argument_parser
import sys


if __name__ == '__main__':
    argument_parser.set_description('Configure grub')
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.args

    requirements.require(root=True, os=[requirements.OS.LINUX])

    files.copy_file(f'{sys.path[0]}/.files/grub', '/etc/default/grub')
    messages.info('Copied grub configuration')

    if messages.ask_yn ('Do you want to include custom entries?', default_yes=True):
        files.copy_file(f'{sys.path[0]}/.files/40_custom', '/etc/grub.d/40_custom')
        messages.info('Copied custom entries')
    else:
        files.delete_file('/etc/grub.d/40_custom')
        messages.info('Deleted custom entries')

    commands.execute('update-grub')
    messages.success('Updated grub configuration')


