#!/bin/bash -e

if [ -z "$1" -o -z "$2" ]; then
	echo "Creates a file of (<size>*<count>) null bytes" >&2
	echo "Usage" >&2
	echo -e "\t"	"$0 <file> <size> [<count>]" >&2
	exit 200
fi

OF="$1"
BS="$2"
if [ -z "$3" ]; then
	COUNT=1
else
	COUNT="$3"
fi



dd if=/dev/zero of="$OF" bs="$BS" count="$COUNT"

exit 0
