#!/usr/bin/env python3

import platform

from dav_tools import commands, messages, requirements, argument_parser, ArgumentAction


def update_linux():
    try:
        if argument_parser.args.update:
            commands.execute('apt update')
            messages.success('Downloaded package information')
        else:
            messages.info('Skipping update')

        if argument_parser.args.download_only:
            commands.execute('apt dist-upgrade -y --download-only')
            messages.success('Downloaded package upgrades')
        else:
            commands.execute('apt dist-upgrade -y')
            messages.success('Installed package upgrades')

        if argument_parser.args.cleanup:
            commands.execute('apt autoremove -y')
            messages.success('Removed unused packages')

            commands.execute('apt autoclean')
            messages.success('Cleaned up')
        else:
            messages.info('Skipping cleanup')
    except commands.CalledProcessError as e:
        messages.error(e)
    except KeyboardInterrupt:
        messages.warning('Interrupted')

def update_windows():
    try:
        messages.progress('Installing prerequisites...')
        commands.execute('powershell -command "Install-Module PSWindowsUpdate"')
        commands.execute('powershell -command "Import-Module PSWindowsUpdate"')
        messages.info('Installed prerequisites')
        
        messages.progress('Checking for updates...')
        commands.execute('powershell -command "Get-WindowsUpdate -Install -AcceptAll -IgnoreReboot -Verbose"')
        messages.success('Installed updates')
    except commands.CalledProcessError as e:
        messages.error(e)
    except KeyboardInterrupt:
        messages.warning('Interrupted')


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Performs a full pc update')
    argument_parser.add_argument('--update', help='check for updates', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)
    argument_parser.add_argument('--download-only', help='download updates but skip installation', action=ArgumentAction.STORE_TRUE)
    argument_parser.add_argument('--cleanup', help='removed unnecessary packages', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)

    requirements.require(root=True, os=['Linux', 'Windows'])

    if platform.system() == 'Linux':
        update_linux()
    elif platform.system() == 'Windows':
        update_windows()