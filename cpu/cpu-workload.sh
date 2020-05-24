#!/bin/bash

ops_float=$(echo "$1*27" | bc)
ops=${ops_float%.*}
stress-ng --cpu 1 --cpu-ops $ops
