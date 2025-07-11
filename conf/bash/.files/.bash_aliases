alias cdtmp='cd `mktemp -d`'
alias chgrp='chgrp -v'
alias chmod='chmod -v'
alias chown='chown -v'
alias cls='clear'
alias commit='/scripts/venv/bin/python /scripts/git_commit.py'
alias update='/scripts/venv/bin/python /scripts/update.py'
alias cp='rsync -aP'
alias dd='dd status=progress conv=fdatasync'
alias df='df -hT --sync'
alias du='du -hd 0'
alias egrep='egrep --color=auto'
alias ffmpeg='ffmpeg -hide_banner'
alias free='free -h'
alias grep='grep --color=auto'
alias la='ls -AvhF'
alias ll='ls -alvhF'
alias ln='ln -v'
alias ls='ls -vhF --color=auto --group-directories-first'
alias ls1='ls -1vhF'
alias lsblk='lsblk -o NAME,PATH,SIZE,STATE,TYPE,MODE,MODEL,FSTYPE,FSVER,MOUNTPOINT,LABEL,PARTLABEL,UUID'
alias mkdir='mkdir -v'
alias mkfs.fat32='mkfs.fat -F 32'
alias motd='for i in /etc/update-motd.d/*; do if [ -x "$i" ] && [ "$i" != "/etc/update-motd.d/98-fsck-at-reboot" ]; then $i; fi; done'
alias mv='mv -v'
alias mysql='mysql --table'
alias nano='nano -ixAUl'
alias pipreqs='python -m pipreqs --mode gt --force'
alias pg_dump='sudo -u postgres pg_dump'
alias pg_dumpall='sudo -u postgres pg_dumpall'
alias psql='sudo -u postgres psql'
alias rm='rm -vf'
alias rmdir='rmdir -v'
alias shred='shred -vuzn 1'
alias sudo='sudo '
alias svg_to_pdf='rsvg-convert -f pdf'
alias v='source /scripts/venv/bin/activate'
