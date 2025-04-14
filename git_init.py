#!/usr/bin/env python

from datetime import date
import sys

from dav_tools import argument_parser, commands, messages

if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Quickly initializes and uploads the current directory to a remote repository')
    argument_parser.add_argument('remote_url')
    
    # check args before running the program
    argument_parser.args

    commands.execute('git add .')
    messages.success('Staged changes')

    commands.execute('git status')

    commands.execute(f'git commit --quiet -m "Initial commit"')
    messages.success('Committed changes')

    commands.execute('git branch -M main')
    messages.success('Created "main" branch')

    commands.execute(f'git remote add origin {argument_parser.args.remote_url}')
    messages.success('Added remote url')

    messages.progress('Uploading commit...')
    commands.execute(f'git push -u origin main --quiet')
    messages.success('Uploaded commit')
