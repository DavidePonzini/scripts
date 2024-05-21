# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines in the history. See bash(1) for more options
# ... or force ignoredups and ignorespace
HISTCONTROL=ignoredups:ignorespace

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

#if [ "$color_prompt" = yes ]; then
#    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
#else
#    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
#fi
#unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
fi

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi



###### SET PS1 #####
### COLOR ###
color_prompt=yes

PS1_color()
{
    if [ "$color_prompt" = yes ]; then
        echo -ne "\033[$1";
    else
        echo -n "";
    fi;
}

### GIT REPO ###
PS1_git_repo_status() {
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

    echo -ne "$(PS1_color "01;34m")[git:"

    # Get branch name, change color depending on edits
    branch="$(git rev-parse --abbrev-ref HEAD)"
    echo -ne "$(PS1_color "00;37m")$branch"

    # Check for uncommitted changes
    if [[ ! -z $(git status --porcelain) ]]; then
        echo -ne "$(PS1_color "01;37m"){$(git status --porcelain | wc -l)}"
    fi

    echo -ne "$(PS1_color "01;34m")] "
}

PS1_make_status() {
    if [ -f 'Makefile' ]; then
        echo -ne "$(PS1_color "01;31m")[make] "
    fi
}

PS1_shell_level() {
	if [ "$SHLVL" -gt 1 ]; then
		echo -ne "$(PS1_color "01;30m")($SHLVL) "
	fi
}

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi


# Set prompt PS1_color based on user privileges
if [ $EUID -eq 0  ]; then
    priv='01;31m'    # Red
elif [ ! -z "$(id | grep 'sudo')" ]; then
    priv='01;33m'    # Yellow
else
    priv='01;32m'    # Green
fi

# Set PS1
PS1='\
\[$(PS1_shell_level)\
\[$(PS1_git_repo_status)\]\
\[$(PS1_make_status)\]\
\[$(PS1_color "00;00m")\]${debian_chroot:+($debian_chroot)}\
\[$(PS1_color "$priv" )\]\u@\h\
\[$(PS1_color "00;00m")\]:\
\[$(PS1_color "01;36m")\]\w\
\[$(PS1_color "00;00m")\] > '
