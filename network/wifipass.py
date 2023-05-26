#!/usr/bin/env python3

from dav_tools import requirements, messages, argument_parser, ArgumentAction, commands

import platform
import glob
import re
import sys


def get_wifipass_linux() -> dict[str, str]:
    requirements.require_root()

    DIRECTORY = '/etc/NetworkManager/system-connections/'
    pattern = re.compile(r'psk=')
    result = {}

    for file_path in glob.glob(f'{DIRECTORY}/*'):
        network = file_path.replace(DIRECTORY, '').replace('.nmconnection', '')

        with open(file_path, 'r') as f:
            for line in f:
                if pattern.search(line):
                    password = line.rstrip().replace('psk=', '')

                    result[network] = password
    return result

def get_wifipass_windows() -> dict[str, str]:
    result = {}
    
    profiles = commands.get_output('netsh wlan show profiles', return_type= bytes.decode)
    profiles = re.findall(r'\s{2,}:\s(.*?)\r', profiles)
    
    for profile in profiles:
        password = commands.get_output(f'netsh wlan show profile "{profile}" key=clear', return_type=bytes.decode)
        if re.search(r'Security key\s+:\sAbsent', password):
            password = None
        else:
            password = re.findall(r'Key Content\s*: (.*?)\r', password)[0]
        result[profile] = password
    return result


if __name__ == '__main__':
    argument_parser.set_description('Retrieves locally stored passwords for each network this computer has connected to')
    argument_parser.add_argument('-o', '--output', help='file to store the passwords on, in .csv format')
    argument_parser.add_argument('--show-password', help='show the password in cleartext (only applies if printing to screen)', action=ArgumentAction.BOOLEAN_OPTIONAL, default=False)
    argument_parser.args

    requirements.require_os('Linux', 'Windows')

    if platform.system() == 'Linux':
        passwords = get_wifipass_linux()
    elif platform.system() == 'Windows':
        passwords = get_wifipass_windows()
    else:
        messages.critical_error('OS not supported')

    if len(passwords) == 0:
        messages.error('No passwords detected')
        sys.exit(0)

    if argument_parser.args.output is None:
        longest_network = max(passwords, key=len)
        text_min_len=[len(longest_network)]
        
        messages.info('Network', 'Password', text_min_len=text_min_len,
                         text_options=[[messages.TextFormat.Style.BOLD], [messages.TextFormat.Style.BOLD]],
        )

        for network,passwd in passwords.items():
            if passwd is None:
                messages.success(network, 'None', text_min_len=text_min_len,
                                 text_options=[[], [messages.TextFormat.Style.ITALIC]])
            else:
                messages.success(network, passwd, text_min_len=text_min_len,
                                 text_options=[[], [messages.TextFormat.Style.INVISIBLE, messages.TextFormat.Style.REVERSE]] if not argument_parser.args.show_password else []
            )
    else:
        with open(argument_parser.args.output, 'w') as f:
            print('network,password', file=f)
            for network,passwd in passwords.items():
                print(f'{network},{passwd}', file=f)