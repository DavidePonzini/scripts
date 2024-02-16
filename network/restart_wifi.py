#!/usr/bin/env python3

import platform

from dav_tools import commands, messages, requirements, argument_parser


def restart_linux():
    try:
            messages.progress('Restarting...')
            commands.execute('service network-manager restart')
            messages.success('Restarted')
    except commands.CalledProcessError as e:
        messages.error(e)
    except KeyboardInterrupt:
        messages.warning('Interrupted')

def restart_windows():
    try:
            messages.progress('Restarting...')
            commands.execute(f'powershell -command "Restart-NetAdapter \\"{argument_parser.args.interface}\\""')
            messages.success('Restarted')
    except commands.CalledProcessError as e:
        messages.error(e)
    except KeyboardInterrupt:
        messages.warning('Interrupted')


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Restart Network interface')
    argument_parser.add_argument('interface', help='interface name to restart')
    argument_parser.args

    requirements.require(root=True, os=['Linux', 'Windows'])

    if platform.system() == 'Linux':
        restart_linux()
    elif platform.system() == 'Windows':
        restart_windows()