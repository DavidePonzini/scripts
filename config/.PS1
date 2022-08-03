#!/bin/bash

### IP ###
#static_ip=`cat /config/IP`

local_ip()
{
	ip_addr=`hostname -I | cut -d ' ' -f 2`
	echo -n $ip_addr
}


### COLOR ###
color_prompt=yes

colour()
{
    if [ "$color_prompt" = yes ]; then
        echo -ne "\033[$1";
    else
        echo -n "";
    fi;
}


# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi


# Set prompt colour based on user privileges
if [ $EUID -eq 0  ]; then
    priv='01;31m'    # Red
elif [ ! -z "$(id | grep 'sudo')" ]; then
    priv='01;33m'    # Yellow
else
    priv='01;32m'    # Green
fi

# Set PS1
PS1='\
\[$(colour "01;30m")\]($SHLVL) \
\[$(colour "00;00m")\]${debian_chroot:+($debian_chroot)}\
\[$(colour "$priv" )\]\u@\h\
\[$(colour "00;00m")\]:\
\[$(colour "01;36m")\]\w\
\[$(colour "00;00m")\]\$ '

# \[$(colour "01;35m")\] (`local_ip`)\

