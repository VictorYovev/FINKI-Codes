#!/bin/bash

if [ $# -lt 3 ]; then
	echo "USAGE: ./zad2.txt <filename1> <filename2> <filename3>"
	exit 1;
fi

if [ ! -f $1 ] || [ ! -f $2 ] || [ ! -f $3 ]; then
	echo "Dude, that file doesn't exist or exists but as directory"
	exit 1;
fi
c=0
wc -c "$@" | sort -nk1 | awk '{if (NR<4) printf("%d. %s (%s bytes)\n",++c,$2,$1); }'

