#!/bin/bash

if [ $# -lt 3 ]; then
	echo "USAGE: ./zad1.sh <number> <op> <number>";
	exit 1;
fi

case "$2" in
	"+") expr $(($1+$3)) ;;
	"-") expr $(($1-$3)) ;;
	*) echo "Dude, not that operator" ;;
esac

