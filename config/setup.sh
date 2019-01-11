#!/bin/bash
if [ `whoami` != root ]; then
	echo "Need to be root." >&2
	exit 250
fi

cd ~
pwd

exit 0

rm -r ~/.bashrc ~/.bash_aliases

ln /scripts/config/.bashrc ~/.bashrc
ln /scripts/config/.bash_aliases ~/.bash_aliases

exit 0
