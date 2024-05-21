#!/usr/bin/env python3

from dav_tools import messages, argument_parser, commands
from pathlib import Path
import sys
import os


def copy(filename):
    source = sys.path[0]
    destination = argument_parser.args.home_path

    target = Path(f'{destination}/{filename}')

    if target.exists():
        target.unlink()

    target.symlink_to(Path(source))


argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
argument_parser.set_description('Initialize bash profile with custom parameters')
argument_parser.add_argument('home_path', nargs='?', help='Path to home directory to setup', default=os.environ['HOME'])

messages.ask_continue(f'Target directory is: {argument_parser.args.home_path}')

copy('.bashrc')
messages.info('Copied bash configuration')

copy('.bash_aliases')
messages.info('Copied bash aliases')

copy('.bashrc')
messages.info('Copied directory colors for command `ls`')

messages.success('Setup complete')
