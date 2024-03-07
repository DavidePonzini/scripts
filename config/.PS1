#!/bin/bash

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

### GIT REPO ###
git_repo_status() {
    local is_repo=false
    local dir="$PWD"
    while [[ "$dir" != "/" ]]; do
        if [[ -d "$dir/.git" ]]; then
            is_repo=true
            break
        fi
        dir="$(dirname "$dir")"
    done

    if ! "$is_repo"; then
        return
    fi

    echo -ne "$(colour "01;34m")[git:"

    # Get branch name, change color depending on edits
    branch="$(git rev-parse --abbrev-ref HEAD)"
    echo -ne "$(colour "00;37m")$branch"

    # Check for uncommitted changes
    if [[ ! -z $(git status --porcelain) ]]; then
        echo -ne "$(colour "01;37m"){$(git status --porcelain | wc -l)}"
    fi

    echo -ne "$(colour "01;34m")] "
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
\[$(git_repo_status)\]\
\[$(colour "00;00m")\]${debian_chroot:+($debian_chroot)}\
\[$(colour "$priv" )\]\u@\h\
\[$(colour "00;00m")\]:\
\[$(colour "01;36m")\]\w\
\[$(colour "00;00m")\]\$ '
