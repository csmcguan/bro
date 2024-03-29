#!/bin/bash

DEFENDED=./defended
B=$(seq -f "b%g" 1 2)
TB=$(seq -f "tb%g" 1 5)
TP=$(seq -f "tp%g" 1 12)

if [ $# -ne 0 ]; then
  for ARG in "$@"; do
    case $ARG in
      "b")
        for CONFIG in $B; do
          python3 ./util/bwoh.py $CONFIG
        done
        ;;
      "tb")
        for CONFIG in $TB; do
          python3 ./util/bwoh.py $CONFIG
        done
        ;;
      "tp")
        for CONFIG in $TP; do
          python3 ./util/bwoh.py $CONFIG
        done
        ;;
      *)
        python3 ./util/bwoh.py $ARG
        ;;
    esac
  done
else
  for CONFIG in $B $TB $TP; do
    if [ -d $DEFENDED/$CONFIG ]; then
      python3 ./util/bwoh.py $CONFIG >> bwoh.txt
    fi
  done
fi
