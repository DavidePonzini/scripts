#!/usr/bin/env python

from dav_tools import requirements, messages, argument_parser, ArgumentAction, commands

import platform
import subprocess
import re
import sys


def get_wifipass_linux() -> dict[str, str]:
    # Ask NetworkManager rather than depending on where profiles are stored.
    # Run as the desktop user first so user-owned secrets can be available.
    def nmcli(*args: str) -> str:
        try:
            return subprocess.run(
                ['nmcli', '--terse', '--escape', 'no', *args],
                check=True, capture_output=True, text=True,
            ).stdout
        except FileNotFoundError as exc:
            raise RuntimeError('nmcli is required; install the network-manager package') from exc
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(f'NetworkManager query failed: {exc.stderr.strip()}') from exc

    result = {}
    uuids = nmcli('--get-values', 'UUID', 'connection', 'show').splitlines()
    for uuid in uuids:
        profile = nmcli(
            '--show-secrets', '--fields',
            'connection.id,connection.type,802-11-wireless-security.psk',
            'connection', 'show', 'uuid', uuid,
        )
        # Split only the first colon: names and passwords may contain colons.
        properties = dict(line.split(':', 1) for line in profile.splitlines() if ':' in line)
        if properties.get('connection.type') != '802-11-wireless':
            continue
        password = properties.get('802-11-wireless-security.psk', '')
        if password:
            result[properties['connection.id']] = password
    return result

def get_wifipass_windows() -> dict[str, str]:
    result = {}
    
    profiles = commands.get_output('netsh wlan show profiles', on_success=bytes.decode)
    profiles = re.findall(r'\s{2,}:\s(.*?)\r', profiles)
    
    for profile in profiles:
        password = commands.get_output(f'netsh wlan show profile "{profile}" key=clear', on_success=bytes.decode)

        if re.search(r'(Security key\s+:\sAbsent|Chiave di sicurezza\s+:\sAssente)', password):
            password = None
        else:
            password = re.findall(r'(Key Content\s*: (.*?)\r|Contenuto chiave\s*: (.*?)\r)', password)[0]
            password = password[1] if password[1] else password[2]

        result[profile] = password
    return result


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Retrieves locally stored passwords for each network this computer has connected to')
    argument_parser.add_argument('-o', '--output', help='file to store the passwords on, in .csv format')
    argument_parser.add_argument('--show-password', help='show the password in cleartext (only applies if printing to screen)', action=ArgumentAction.BOOLEAN_OPTIONAL, default=False)
    argument_parser.args

    requirements.require(os=['Linux', 'Windows'])

    if platform.system() == 'Linux':
        try:
            passwords = get_wifipass_linux()
        except RuntimeError as exc:
            messages.error(str(exc))
            sys.exit(1)
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
        
        messages.message('', 'Network', 'Password', text_min_len=[3] + text_min_len,
                         additional_text_options=[[], [messages.TextFormat.Style.BOLD], [messages.TextFormat.Style.BOLD]],
        )

        for network,passwd in passwords.items():
            if passwd is None:
                messages.info(network, 'None', text_min_len=text_min_len,
                                 text_options=[[], [messages.TextFormat.Style.ITALIC, messages.TextFormat.Style.DIM]])
            else:
                messages.info(network, passwd, text_min_len=text_min_len,
                                 text_options=[[], [messages.TextFormat.Style.INVISIBLE, messages.TextFormat.Style.REVERSE]] if not argument_parser.args.show_password else [[], []]
            )
    else:
        with open(argument_parser.args.output, 'w') as f:
            print('network,password', file=f)
            for network,passwd in passwords.items():
                print(f'{network},{passwd}', file=f)