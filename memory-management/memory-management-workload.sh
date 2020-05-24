#!/bin/bash

ops1_float=$(echo "$1*333000" | bc)
ops1=${ops1_float%.*}

ops2_float=$(echo "$1*2490" | bc)
ops2=${ops2_float%.*}

ops3_float=$(echo "$1*22900" | bc)
ops3=${ops3_float%.*}

ops4_float=$(echo "$1*45000" | bc)
ops4=${ops4_float%.*}

ops5_float=$(echo "$1*1095000" | bc)
ops5=${ops5_float%.*}

ops6_float=$(echo "$1*1000" | bc)
ops6=${ops6_float%.*}





stress-ng --brk 1 --brk-ops $ops1
stress-ng --stack 1 --stack-ops $ops2
stress-ng --bigheap 1 --bigheap-ops $ops3
stress-ng --vm 1 --vm-ops $ops4
stress-ng --malloc 1 --malloc-ops $ops5
stress-ng --shm 1 --shm-ops $ops6
