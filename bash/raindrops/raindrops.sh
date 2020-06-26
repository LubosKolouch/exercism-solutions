#!/usr/bin/env bash

answer=""

declare -A modules

modules=( ["3"]="Pling" ["5"]="Plang" ["7"]="Plong" )

for m in 3 5 7 
do 
    if (( $1 % m == 0 )); then
        answer="${answer}${modules[$m]}"
    fi
done

if [[ $answer == "" ]]; then
    answer=$1
fi

echo $answer
