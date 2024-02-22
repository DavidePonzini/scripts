#!/usr/bin/env python3

import platform

from dav_tools import commands, messages, requirements, argument_parser, ArgumentAction

def run_update(func, *args, **kwargs) -> None:
    '''
    Helper function to run an update and handle exceptions
    
    :param func: Function to run.

    :returns: None
    '''
    try:
        func(*args, **kwargs)
    except commands.CalledProcessError as e:
        messages.error(e)
    except KeyboardInterrupt:
        messages.warning('Interrupted')


def update_linux(check_for_updates=True, download_only=False, cleanup=True):
    if check_for_updates:
        commands.execute('apt update')
        messages.success('Downloaded package information')
    else:
        messages.info('Skipping check for updates')

    if download_only:
        commands.execute('apt dist-upgrade -y --download-only')
        messages.success('Downloaded package upgrades')
    else:
        commands.execute('apt dist-upgrade -y')
        messages.success('Installed package upgrades')

    if cleanup:
        commands.execute('apt autoremove -y')
        messages.success('Removed unused packages')

        commands.execute('apt autoclean')
        messages.success('Cleaned up')
    else:
        messages.info('Skipping cleanup')
    
def update_windows():
    messages.progress('Installing prerequisites...')
    commands.execute('powershell -command "Install-Module PSWindowsUpdate"')
    commands.execute('powershell -command "Import-Module PSWindowsUpdate"')
    messages.info('Installed prerequisites')
    
    messages.progress('Checking for updates...')
    commands.execute('powershell -command "Get-WindowsUpdate -Install -AcceptAll -IgnoreReboot -Verbose"')
    messages.success('Installed updates')

def update_python():
    commands.execute('python -m pip install --upgrade pip')
    messages.success('Updated pip to latest version')


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Performs a full pc update')
    argument_parser.add_argument('--check-for-updates', help='check for updates', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)
    argument_parser.add_argument('--download-only', help='download updates but skip installation', action=ArgumentAction.STORE_TRUE)
    argument_parser.add_argument('--cleanup', help='removed unnecessary packages', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)
    argument_parser.add_argument('--python', help='update python package manager', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)

    requirements.require(root=True, os=['Linux', 'Windows'])

    if(argument_parser.args.python):
        run_update(update_python)

    if platform.system() == 'Linux':
        run_update(update_linux,
                   check_for_updates=argument_parser.args.check_for_updates,
                   download_only=argument_parser.args.download_only,
                   cleanup=argument_parser.args.cleanup)
    elif platform.system() == 'Windows':
        run_update(update_windows)