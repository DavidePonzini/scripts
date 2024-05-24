#!/usr/bin/env python

from dav_tools import messages, commands

messages.info('Generating requirements file')
commands.execute('pipreqs --mode no-pin --force')
messages.success('Generated requirements file')

messages.info('Installing requirements')
commands.execute('pip3 install -r requirements.txt --upgrade')
messages.success('Installed requirements')

commands.execute('rm -f requirements.txt')
messages.success('Removed requirements file')
