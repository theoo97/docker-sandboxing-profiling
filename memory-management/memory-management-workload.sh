#!/bin/bash

ops1=$(echo "$1*333000" | bc)
ops2=$(echo "$1*2490" | bc)
ops3=$(echo "$1*22900" | bc)
ops4=$(echo "$1*45000" | bc)
ops5=$(echo "$1*1095000" | bc)
ops6=$(echo "$1*1000" | bc)





stress-ng --brk 1 --brk-ops $ops1
stress-ng --stack 1 --stack-ops $ops2
stress-ng --bigheap 1 --bigheap-ops $ops3
stress-ng --vm 1 --vm-ops $ops4
stress-ng --malloc 1 --malloc-ops $ops5
stress-ng --shm --shm-ops $ops6
