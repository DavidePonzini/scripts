#!/usr/bin/env python

from dav_tools import messages, commands, requirements, argument_parser


if __name__ == '__main__':
    requirements.require(root=True, os=[requirements.OS.LINUX])

    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Enables or disables gdm auto startup')
    argument_parser.add_argument('action', choices=['enable', 'disable'], help='action to perform')

    if argument_parser.args.action == 'enable':
        commands.execute('systemctl set-default graphical')
        messages.success('GDM enabled at startup')
    else:
        commands.execute('systemctl set-default multi-user')
        messages.success('GDM disabled at startup')
