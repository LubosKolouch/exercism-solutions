#!/usr/bin/env bash

answer=""


modules=(0 1 2 "Pling" 4 "Plang" 6 "Plong")

for m in 3 5 7 
do 
    if (( $1 % $m == 0 )); then
        answer+=${modules[$m]}
    fi
done

if [[ -z $answer ]]; then
    answer="$1"
fi

echo "$answer"
