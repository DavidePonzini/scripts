#!/usr/bin/env python

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
        exit(1)


def update_linux():
    # upgrade
    messages.info('Downloading package information...')
    commands.execute('apt update')
    messages.success('Downloaded package information')

    # update
    messages.info('Installing package upgrades...')
    commands.execute('apt dist-upgrade -y')
    messages.success('Installed package upgrades')

    # autoremove
    messages.info('Removing unused packages...')
    commands.execute('apt autoremove -y')
    messages.success('Removed unused packages')

    # autoclean
    messages.info('Cleaning up...')
    commands.execute('apt autoclean')
    messages.success('Cleaned up')
    
def update_windows():
    messages.info('Installing prerequisites...')
    commands.execute('powershell -command "Install-Module PSWindowsUpdate"')
    commands.execute('powershell -command "Import-Module PSWindowsUpdate"')
    messages.info('Installed prerequisites')
    
    messages.info('Checking for updates...')
    commands.execute('powershell -command "Get-WindowsUpdate -Install -AcceptAll -IgnoreReboot -Verbose"')
    messages.success('Installed updates')

def update_python():
    messages.info('Updating pip...')
    commands.execute('python -m pip install --upgrade pip --root-user-action=ignore')
    messages.success('Updated pip to latest version')


if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Performs a full pc update')
    argument_parser.add_argument('--python', help='update python package manager', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)

    requirements.require(root=True, os=['Linux', 'Windows'])

    if(argument_parser.args.python):
        run_update(update_python)

    if platform.system() == 'Linux':
        run_update(update_linux)
    elif platform.system() == 'Windows':
        run_update(update_windows)
    