#!/usr/bin/env python

from dav_tools import messages, argument_parser, files, requirements
import sys
import os


def copy(filename):
    dest = f'{argument_parser.args.home_path}/{filename}'
    
    if files.delete_file(dest):
        messages.info(f'Removed existing {filename} file')

    files.copy_file(
        f'{sys.path[0]}/.files/{filename}', dest,
        symlink=True
    )


requirements.require(
    os=[requirements.OS.LINUX],
)


argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
argument_parser.set_description('Initialize bash profile with custom parameters')
argument_parser.add_argument('home_path', nargs='?', help='Path to home directory to setup', default=os.environ['HOME'])

messages.ask_continue(f'Target directory is: {argument_parser.args.home_path}')

copy('.bashrc')
messages.info('Copied bash configuration')

copy('.bash_aliases')
messages.info('Copied bash aliases')

copy('.dircolors')
messages.info('Copied directory colors for command `ls`')

messages.success('Setup complete')
