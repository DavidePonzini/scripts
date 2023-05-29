#!/usr/bin/env python3

from dav_tools import commands, messages, requirements, argument_parser, ArgumentAction

if __name__ == '__main__':
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.set_description('Performs a full pc update')
    argument_parser.add_argument('--update', help='check for updates', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)
    argument_parser.add_argument('--download-only', help='download updates but skip installation', action=ArgumentAction.STORE_TRUE)
    argument_parser.add_argument('--cleanup', help='removed unnecessary packages', action=ArgumentAction.BOOLEAN_OPTIONAL, default=True)

    requirements.require_os('Linux')
    requirements.require_root()

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