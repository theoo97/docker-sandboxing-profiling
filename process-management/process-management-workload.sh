#!/bin/bash

ops1_float=$(echo "$1*124" | bc)
ops1=${ops1_float%.*}

ops2_float=$(echo "$1*13" | bc)
ops2=${ops2_float%.*}

ops3_float=$(echo "$1*1060" | bc)
ops3=${ops3_float%.*}

ops4_float=$(echo "$1*4200" | bc)
ops=${ops4_float%.*}

ops5_float=$(echo "$1*336" | bc)
ops5=${ops5_float%.*}


stress-ng --fork 1 --fork-ops $ops1
stress-ng --exec 1 --exec-ops $ops2
stress-ng --vfork 1 --vfork-ops $ops3
stress-ng --kill 1 --kill-ops $ops4
stress-ng --pthread 1 --pthread-ops $ops5
