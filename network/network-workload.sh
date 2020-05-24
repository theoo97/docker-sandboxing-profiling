#!/bin/bash

ops_float=$(echo "$1*37" | bc)
ops=${ops_float%.*}
stress-ng --sock 1 --sock-ops $ops
