#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage $0 load"
	exit 0
fi

ops1_float=$(echo "$1*2750" | bc)
ops1=${ops1_float%.*}

ops2_float=$(echo "$1*32800" | bc)
ops2=${ops2_float%.*}

stress-ng --hdd 1 --hdd-ops $ops1_float --io 1 --io-ops $ops2_float
