#!/bin/bash

usage="Usage: $0 sandbox stressor load"
usage_example="Example: $0 gvisor cpu 1"

if [ "$#" -ne 3 ]; then
	echo $usage
	echo $usage_example	
fi

cd $2

if [ "$1" == "no-sandbox" ]; then
	./$2-workload.sh $3
elif [ "$1" == "docker" ]; then
	sudo docker run -ti docker-sandboxing-profiling:$2-workload $3
elif [ "$1" == "gvisor" ]; then
	sudo docker run --runtime=runc -ti docker-sandboxing-profiling:$2-workload $3
fi

cd ..
