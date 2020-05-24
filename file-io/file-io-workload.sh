#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage $0 load"
	exit 0
fi

ops1_float=$(echo "$1*55" | bc)
ops1=${ops1_float%.*}

ops2_float=$(echo "$1*656" | bc)
ops2=${ops2_float%.*}



stress-ng --hdd 1 --hdd-ops $ops1 --io 1 --io-ops $ops2
