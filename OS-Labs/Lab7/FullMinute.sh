#!/bin/bash

while true; do
if [[ `date +%S` = "00" ]]; then
	echo "Tochno e `date +%-M`-ta minuta";
	exit 1;
else 
	echo `date`
	sleep 1
fi
done

