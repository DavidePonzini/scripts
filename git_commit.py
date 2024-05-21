#!/usr/bin/env python

from datetime import date
import sys

from dav_tools import argument_parser, commands, messages

if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Quickly commits and uploads all changes performed on the current directory')
    argument_parser.add_argument('-m', '--message', help='commit message', default=None)


    if commands.get_output('git status --porcelain') == b'': 
        messages.success('Nothing to commit')
        sys.exit(0)

    commands.execute('git add .')
    messages.success('Staged changes')

    commands.execute('git status')

    if argument_parser.args.message is not None:
        commit_message = argument_parser.args.message
    else:
        try:
            commit_message = messages.ask('Reason')
            if len(commit_message) == 0:
                commit_message = f'Quick commit ({date.today()})'
                messages.warning(f'Using default commit message: "{commit_message}"')
        except KeyboardInterrupt:
            messages.warning('Aborted')
            sys.exit(1)

    commands.execute(f'git commit --quiet -m "{commit_message}"')
    messages.success('Committed changes')

    messages.progress('Uploading commit...')
    commands.execute(f'git push --quiet')
    messages.success('Uploaded commit')
