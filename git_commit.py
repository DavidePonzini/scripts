#!/usr/bin/env python

from datetime import date
import sys

from dav_tools import argument_parser, commands, messages


def git_add(*paths: str):
    commands.execute(f'git add {" ".join(paths)}')
    messages.success('Staged changes')

def git_commit(amend: bool = False, message: str | None = None):
    command = 'git commit --quiet'
    if amend:
        command += ' --amend'
    if message:
        command += f' -m "{message}"'
    
    try:
        commands.execute(command)
    except (KeyboardInterrupt, EOFError):
        messages.warning('Aborted')
        sys.exit(1)

    messages.success('Committed changes')

def git_push():
    messages.progress('Uploading commit...')
    commands.execute(f'git push --quiet')
    messages.success('Uploaded commit')


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Quickly commits and uploads all changes performed on the current directory')
    argument_parser.add_argument('path', help='files (or folders) to commit', nargs='*', default=[])
    argument_parser.add_argument('-m', '--message', help='commit message', default=None)
    argument_parser.add_argument('-a', '--amend', help='amend', action='store_true')
    argument_parser.add_argument('-p', '--push', help='push changes to remote', action='store_true')
    argument_parser.add_argument('-v', '--verbose', help='show diff', action='store_true')
    argument_parser.parse_args()

    if commands.get_output('git status --porcelain') == b'': 
        messages.success('Nothing to commit')

        if argument_parser.args.push:
            git_push()

        sys.exit(0)

    if len(argument_parser.args.path) > 0:
        git_add(*argument_parser.args.path)

    # display changes for the user
    if argument_parser.args.verbose:
        commands.execute('git status -v')
    else:
        commands.execute('git status')

    if commands.get_output('git diff --cached ') == b'':
        messages.warning('No changes staged for commit')

        if argument_parser.args.push:
            git_push()

        sys.exit(0)

    git_commit(amend=argument_parser.args.amend, message=argument_parser.args.message)

    if argument_parser.args.push:
        git_push()
