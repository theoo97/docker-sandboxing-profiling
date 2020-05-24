#!/bin/bash

ops=$(echo "$1*2380" | bc)
stress-ng --sock 1 --sock-ops $ops
