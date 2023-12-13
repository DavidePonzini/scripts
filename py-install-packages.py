#!/usr/bin/env python3

from dav_tools import messages, commands

commands.execute('python3 -m pip install --upgrade pip')
messages.success('Updated pip to latest version')

commands.execute('pipreqs --mode no-pin --force')
messages.info('Generated requirements file')

commands.execute('pip3 install -r requirements.txt --upgrade')
messages.success('Installed requirements')

commands.execute('rm -f requirements.txt')
messages.info('Removed requirements file')
