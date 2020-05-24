#!/bin/bash
cd $1
sudo docker run -ti docker-sandboxing-profiling:$1-workload $2
cd ..
