#!/bin/bash
total=0
menu=("Hamburger (150 den)" "Pica (200 den)" "Kafe (70 den)" "Kolach (90 den)" "Narachaj")

select item in "${menu[@]}"; do
	case $item in
		"${menu[0]}") ((total+=150));;
		"${menu[1]}") ((total+=200));;
		"${menu[2]}") ((total+=70));;
		"${menu[3]}") ((total+=90));;
		"${menu[4]}") echo "Vkupno: $total den"; exit 1;;
	esac
	echo "Momentalno: $total den"
done

