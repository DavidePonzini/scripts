alias alias-edit='nano ~/.bash_aliases'
alias cdtmp='cd `mktemp -d`'
alias chkconfig='sysv-rc-conf'
alias chmod='chmod -v'
alias chown='chown -v'
alias cls='clear'
alias cmatrix='cmatrix -bC red -u 9'
alias cmd='cmd.exe'
#alias cp='cp -v'
alias cp='rsync -aP'
alias df='df -hT --sync'
alias dmy='date +%d%m%y'
alias du='du -hd 0'
alias egrep='egrep --color=auto'
alias firefox='firefox 2> /dev/null 1>&2'
alias free='free -h | head -n 2'
alias grep='grep --color=auto'
alias hddtemp='hddtemp /dev/sd?'
alias la='ls -AvhF'
alias ll='ls -alvhF'
alias ln='ln -v'
alias ls='ls -vhF --color=auto --group-directories-first'
alias ls1='ls -1vhF'
alias mkdir='mkdir -v'
alias mon='watch -n 0,5'
alias mv='mv -v'
alias nano='nano -ixAUl'
alias nautilus='nautilus 2> /dev/null'
alias open='gnome-open 2> /dev/null'
alias psql='sudo -u postgres psql'
alias q='exit'
alias reconnect='sudo service network-manager restart'
alias rm='rm -vf'
alias rmdir='rmdir -v'
alias rsync='rsync -aP'
alias shred='shred -vuzn 1'
alias split='split -d'
alias sudo='sudo '
alias ymd='date +%y%m%d'
alias youtube-dl='youtube-dl -o "%(title)s.%(ext)s"'
alias chgrp='chgrp -v'
alias battery='/scripts/util/battery-status'
alias dd='dd status=progress conv=fdatasync'
alias trasmission-cli='transmission-cli -w ./'
alias bc='bc -l'
alias dirs='dirs -v'
alias lw='/scripts/util/list-writable'
alias repquota='repquota -ast'
alias mysql='mysql -t'
alias motd='for i in /etc/update-motd.d/*; do if [ -x "$i" ] && [ "$i" != "/etc/update-motd.d/98-fsck-at-reboot" ]; then $i; fi; done'
alias lsblk='lsblk -o NAME,PATH,SIZE,STATE,TYPE,MODE,MODEL,FSTYPE,FSVER,MOUNTPOINT,LABEL,PARTLABEL,UUID'
alias mktempdir='mktemp -d'
alias mkfs.fat32='mkfs.fat -F 32'
alias DM='sudo service gdm3 start'
alias speedtest='speedtest --bytes --simple'
alias sudo='sudo --preserve-env=SCRIPTS'
alias ffmpeg='ffmpeg -hide_banner'
alias pipreqs='pipreqs --mode no-pin --force'
alias aws-ssh='ssh ubuntu@15.237.153.101 -i /home/dav/.ssh/davide_ponzini_key_240610.pem'

