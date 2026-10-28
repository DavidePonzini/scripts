#!/usr/bin/env python

from dav_tools import messages, argument_parser, commands
import sys


argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
argument_parser.set_description('Import/export terminal profile')
argument_parser.add_argument('action', choices=['export', 'import'],  help='Action to perform')
argument_parser.add_argument('file', nargs='?', help='Path to the terminal profile backup file')
argument_parser.add_argument('--gnome', action='store_true', help='Use GNOME Terminal instead of Ptyxis (the default)')

terminal = 'gnome-terminal' if argument_parser.args.gnome else 'ptyxis'
profile_path = '/org/gnome/terminal/legacy/profiles:/' if argument_parser.args.gnome else '/org/gnome/Ptyxis/'
profile_file = argument_parser.args.file or f'{sys.path[0]}/.{terminal}-profiles.dconf'

if argument_parser.args.action == 'import':
    with open(profile_file) as f:
        commands.execute(f'dconf load {profile_path}', stdin=f)
        messages.success('Configuration imported')
else:
    with open(profile_file, 'w') as f:
        commands.execute(f'dconf dump {profile_path}', stdout=f)
        messages.success(f'Configuration exported to {profile_file}')

