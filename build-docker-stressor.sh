#!/bin/bash
cd $1
sudo docker build -t docker-sandboxing-profiling:$1-workload .
cd ..
