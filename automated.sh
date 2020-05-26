#!/bin/bash

base_ops=(5 10 15 20 25 30 35 40 45 50)
len=${#base_ops[@]}

for (( i=0; i<$len; i++ ));
do
	start=`date +%s%N`
	./run.sh no-sandbox process-management ${base_ops[$i]}
	end=`date +%s%N`

	runtime=$(echo "scale=2;($end-$start)/1000000000" | bc)
	echo $runtime

	runtimes[$i]=$runtime
done

echo "runtimes=[${runtimes[@]}]" | sed 's/ /, /g'


