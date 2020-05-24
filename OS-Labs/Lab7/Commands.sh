#!/bin/bash

if [ $# -ne 1 ]; then
	echo "USAGE: ./zad3.sh <command>";
	exit 1;
fi

case "$1" in
	print|p) ls -l "../Lab[1-6]/" | awk '{ if( $1 = '/^-/' )printf("%s\n",$10) }' ;;
	top3|t) ls -lS "../Lab[1-6]/" | grep "^-" | head -3 | awk '{printf("%s (%s bytes)\n",$10,$6);}' ;;
	exec|exe|x) ls -l "../Lab[1-6]/"   | grep "^-..x" | awk '{print $10}' ;;
	*) echo "That command doesn't exist" ;;
esac

