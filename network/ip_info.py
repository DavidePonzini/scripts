#!/usr/bin/env python

from dav_tools import messages, argument_parser

import socket
import requests
import json

def get_local_ip_address():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]

def get_external_ip_info(ip=None):
    if ip is None:
        ip = requests.get('http://ipinfo.io/ip').content.decode()

    result = requests.get(f'http://ipinfo.io/{ip}').content
    result = json.loads(result)

    return result


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Get information about an IP address')
    argument_parser.add_argument('ip', help='IP address to get info about. If None, use the current machine IP address', nargs='?')

    if argument_parser.args.ip is None:
        messages.info('Local IP:', get_local_ip_address(),
                  text_options=[[messages.TextFormat.Style.BOLD], []])
        print()

    messages.progress('Getting info about external IP...')
    external_ip_info = get_external_ip_info(argument_parser.args.ip)
    messages.info('External IP:', external_ip_info['ip'],
                  text_options=[[messages.TextFormat.Style.BOLD], []])
    messages.info('Location:', f'{external_ip_info["city"]}, {external_ip_info["region"]} ({external_ip_info["postal"]}) - {external_ip_info["country"]}',
                  text_options=[[messages.TextFormat.Style.BOLD], []])
    messages.info('Coordinates:', external_ip_info['loc'], f'(https://www.google.com/maps/@{external_ip_info["loc"]})',
                  text_options=[[messages.TextFormat.Style.BOLD], [], [messages.TextFormat.Style.ITALIC, messages.TextFormat.Style.DIM]])
    messages.info('Timezone:', external_ip_info['timezone'],
                  text_options=[[messages.TextFormat.Style.BOLD], []])
    messages.info('Provider:', external_ip_info['org'],
                  text_options=[[messages.TextFormat.Style.BOLD], []])
