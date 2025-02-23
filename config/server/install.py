from dav_tools import requirements, commands, messages, files, argument_parser
import sys


if __name__ == '__main__':
    argument_parser.set_description('Configure home server')
    argument_parser.set_developer_info('Davide Ponzini', 'davide.ponzini95@gmail.com')
    argument_parser.add_argument('--ssh_port', help='Port to use for SSH connection', default='2222', type=int)
    argument_parser.args

    requirements.require(root=True, os=[requirements.OS.LINUX])

    # Install requirements
    commands.execute('apt install samba fail2ban -y')

    # Samba
    files.copy_file(f'{sys.path[0]}/.config/smb.conf', '/etc/samba/smb.conf',)
    commands.execute('service smbd restart')
    messages.success('Configured Samba')

    # SSH
    files.copy_file(f'{sys.path[0]}/.config/ssh/sshd_config', '/etc/ssh/sshd_config',)
    commands.execute('service ssh restart')
    messages.success('Configured SSH')

    # 