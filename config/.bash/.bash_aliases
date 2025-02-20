alias cdtmp='cd `mktemp -d`'
alias chmod='chmod -v'
alias chown='chown -v'
alias cls='clear'
#alias cp='cp -v'
alias cp='rsync -aP'
alias df='df -hT --sync'
alias du='du -hd 0'
alias egrep='egrep --color=auto'
alias free='free -h | head -n 2'
alias grep='grep --color=auto'
alias la='ls -AvhF'
alias ll='ls -alvhF'
alias ln='ln -v'
alias ls='ls -vhF --color=auto --group-directories-first'
alias ls1='ls -1vhF'
alias mkdir='mkdir -v'
alias mv='mv -v'
alias nano='nano -ixAUl'
alias psql='sudo -u postgres psql'
alias rm='rm -vf'
alias rmdir='rmdir -v'
alias rsync='rsync -aP'
alias shred='shred -vuzn 1'
alias sudo='sudo '
alias chgrp='chgrp -v'
alias dd='dd status=progress conv=fdatasync'
alias mysql='mysql --table'
alias motd='for i in /etc/update-motd.d/*; do if [ -x "$i" ] && [ "$i" != "/etc/update-motd.d/98-fsck-at-reboot" ]; then $i; fi; done'
alias lsblk='lsblk -o NAME,PATH,SIZE,STATE,TYPE,MODE,MODEL,FSTYPE,FSVER,MOUNTPOINT,LABEL,PARTLABEL,UUID'
alias mkfs.fat32='mkfs.fat -F 32'
alias ffmpeg='ffmpeg -hide_banner'
alias pipreqs='pipreqs --mode gt --force'
alias aws-ssh='ssh ubuntu@15.237.153.101 -i /home/dav/.ssh/davide_ponzini_key_240610.pem'
alias v='source /scripts/venv/bin/activate'
alias commit='/scripts/venv/bin/python /scripts/git_commit.py'
