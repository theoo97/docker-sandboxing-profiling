#!/bin/bash

ops=$(echo "$1*1358" | bc)
stress-ng --cpu 1 --cpu-ops $ops
