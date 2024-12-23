#!/usr/bin/env python

from dav_tools import messages, commands
import os

messages.info('Generating requirements file')
commands.execute('python -m pipreqs.pipreqs --mode gt --force')
messages.success('Generated requirements file')

messages.info('Installing requirements')
commands.execute('python -m pip install -r requirements.txt --upgrade')
messages.success('Installed requirements')

os.remove('requirements.txt')
messages.success('Removed requirements file')
