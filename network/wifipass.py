#!/usr/bin/env python

from dav_tools import requirements, messages, argument_parser, ArgumentAction, commands

import csv
import platform
from typing import NamedTuple
import subprocess
import re
import sys


class Credentials(NamedTuple):
    username: str | None
    password: str | None


def get_wifipass_linux() -> dict[str, Credentials]:
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
            'connection.id,connection.type,802-11-wireless-security.psk,'
            '802-1x.identity,802-1x.password,'
            '802-11-wireless-security.leap-username,802-11-wireless-security.leap-password',
            'connection', 'show', 'uuid', uuid,
        )
        # Split only the first colon: names and passwords may contain colons.
        properties = dict(line.split(':', 1) for line in profile.splitlines() if ':' in line)
        if properties.get('connection.type') != '802-11-wireless':
            continue
        username = (properties.get('802-1x.identity')
                    or properties.get('802-11-wireless-security.leap-username'))
        password = (properties.get('802-1x.password')
                    or properties.get('802-11-wireless-security.leap-password')
                    or properties.get('802-11-wireless-security.psk'))
        if username or password:
            result[properties['connection.id']] = Credentials(username, password)
    return result

def get_wifipass_windows() -> dict[str, Credentials]:
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

        result[profile] = Credentials(None, password)
    return result


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Retrieves locally stored Wi-Fi usernames and passwords')
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
        messages.error('No saved credentials detected')
        sys.exit(0)

    if argument_parser.args.output is None:
        text_min_len = [max(len('Network'), *(len(name) for name in passwords)),
                        max(len('Username'), *(len(c.username or '') for c in passwords.values()))]
        bold = [messages.TextFormat.Style.BOLD]
        messages.message('', 'Network', 'Username', 'Password',
                         text_min_len=[3] + text_min_len,
                         additional_text_options=[[], bold, bold, bold])

        for network, credentials in passwords.items():
            password_style = []
            if credentials.password is None:
                password_style = [messages.TextFormat.Style.ITALIC, messages.TextFormat.Style.DIM]
            elif not argument_parser.args.show_password:
                password_style = [messages.TextFormat.Style.INVISIBLE, messages.TextFormat.Style.REVERSE]
            messages.info(network, credentials.username or '',
                          credentials.password if credentials.password is not None else 'Unavailable',
                          text_min_len=text_min_len, text_options=[[], [], password_style])
    else:
        with open(argument_parser.args.output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['network', 'username', 'password'])
            for network, credentials in passwords.items():
                writer.writerow([network, credentials.username, credentials.password])
