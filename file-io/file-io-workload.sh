#!/bin/bash

ops_float=$(echo "$1*2500" | bc)
ops=${ops_float%.*}
stress-ng --iomix 1 --iomix-ops $ops
