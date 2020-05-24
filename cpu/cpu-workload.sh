#!/bin/bash

ops_float=$(echo "$1*1358" | bc)
ops=${ops_float%.*}
stress-ng --cpu 1 --cpu-ops $ops
