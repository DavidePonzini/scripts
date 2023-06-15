#!/usr/bin/env python3

from dav_tools import requirements, argument_parser, commands, messages
import platform


def set_mac_linux(device, mac):
    commands.execute(f'ifconfig {device} down')
    messages.info(f'Device {device} brought down')

    commands.execute(f'ifconfig {device} hw ether {mac}')
    messages.success(f'MAC address set to "{mac}"')
    
    commands.execute(f'ifconfig {device} up')
    messages.info(f'Device {device} brought up')


if __name__ == '__main__':
    argument_parser.add_argument('device', help='device to change MAC address')
    argument_parser.add_argument('mac', help='new MAC address')
    argument_parser.args

    if platform.system() == 'Linux':
        requirements.require_root()
        set_mac_linux(argument_parser.args.device, argument_parser.args.mac)
    elif platform.system() == 'Windows':
        pass
    else:
        messages.critical_error('OS not supported')
