#!/bin/bash

base_ops=($(seq 10 5 100))
len=${#base_ops[@]}

function run {
	WORKLOAD=$1
	SANDBOX=$2

	for (( i=0; i<$len; i++ ));
	do
		start=`date +%s%N`
		./run.sh $SANDBOX $WORKLOAD ${base_ops[$i]} > /dev/null
		end=`date +%s%N`

		runtime=$(echo "scale=2;($end-$start)/1000000000" | bc)

		runtimes[$i]=$runtime
	done

	echo "====>>>>> $WORKLOAD on $SANDBOX <<<<<===="
	echo "base_ops=[${base_ops[@]}]" | sed 's/ /, /g'
	echo "runtimes=[${runtimes[@]}]" | sed 's/ /, /g'
	printf "\n\n\n"
}  

WORKLOADS="cpu memory-management process-management network file-io"
SANDBOXES="no-sandbox docker gvisor kata"

for WORKLOAD in $WORKLOADS
do
	for SANDBOX in $SANDBOXES
	do
		run $WORKLOAD $SANDBOX
		sleep 15
	done
done

