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

    echo -ne "$(colour "01;34m")(git:"

    # Check for uncommitted changes
    if [[ ! -z $(git status --porcelain) ]]; then
        echo -ne "$(colour "00;1;3m")edits"
    else
        echo -ne "$(colour "00;37;2;3m")edits"
    fi

    echo -ne "$(colour "01;34;3m")|"

    # git fetch origin --quiet
    # Check for commits to push
    if [[ ! -z $(git log origin/main..HEAD) ]]; then
        echo -ne "$(colour "01;32;3m")push"
    else
        echo -ne "$(colour "00;32;2;3m")push"
    fi

    echo -ne "$(colour "01;34;3m")|"

    # Check for commits to pull
    if [[ ! -z $(git log HEAD..origin/main --oneline) ]]; then
        echo -ne "$(colour "01;36;3m")pull"
    else
        echo -ne "$(colour "00;36;2;3m")pull"
    fi

    echo -ne "$(colour "m")$(colour "01;34m")) "
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
