#!/usr/bin/env bash

answer="you"

if (( $# >= 1 )); then
    answer="$1"
fi

echo "One for $answer, one for me."
