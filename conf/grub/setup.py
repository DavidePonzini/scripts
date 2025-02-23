#!/usr/bin/env python

from dav_tools import requirements, commands, messages, files, argument_parser, ArgumentAction
import sys


if __name__ == '__main__':
    argument_parser.set_description('Configure grub')
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.add_argument('--custom', help='Add custom entries to grub', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)
    argument_parser.args

    requirements.require(root=True, os=[requirements.OS.LINUX])

    files.copy_file(f'{sys.path[0]}/.files/grub', '/etc/default/grub')
    messages.info('Copied grub configuration')

    if argument_parser.args.custom:
        files.copy_file(f'{sys.path[0]}/.files/grub_40_custom', '/etc/grub.d/40_custom')
        messages.info('Copied custom entries')

    commands.execute('update-grub')
    messages.success('Configured complete')


