#!/bin/bash

ops1=$(echo "$1*6200" | bc)
ops2=$(echo "$1*650" | bc)
ops3=$(echo "$1*53000" | bc)
ops4=$(echo "$1*210000" | bc)
ops5=$(echo "$1*16800" | bc)


stress-ng --fork 1 --fork-ops $ops1
stress-ng --exec 1 --exec-ops $ops2
stress-ng --vfork 1 --vfork-ops $ops3
stress-ng --kill 1 --kill-ops $ops4
stress-ng --pthread 1 --pthread-ops $ops5
