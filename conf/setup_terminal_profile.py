#!/usr/bin/env python

from dav_tools import messages, argument_parser, commands
import sys


argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
argument_parser.set_description('Import/export terminal profile')
argument_parser.add_argument('action', choices=['export', 'import'],  help='Action to perform')
argument_parser.add_argument('file', nargs='?', help='Path to home directory to setup', default=f'{sys.path[0]}/.gnome-terminal-profiles.dconf')

if argument_parser.args.action == 'import':
    with open(argument_parser.args.file) as f:
        commands.execute('dconf load /org/gnome/terminal/legacy/profiles:/', stdin=f)
        messages.success('Configuration imported')
else:
    with open(argument_parser.args.file, 'w') as f:
        commands.execute('dconf dump /org/gnome/terminal/legacy/profiles:/', stdout=f)
        messages.success(f'Configuration exported to {argument_parser.args.file}')

