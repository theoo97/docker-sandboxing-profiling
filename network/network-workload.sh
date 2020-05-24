#!/bin/bash

ops_float=$(echo "$1*2380" | bc)
ops=${ops_float%.*}
stress-ng --sock 1 --sock-ops $ops
