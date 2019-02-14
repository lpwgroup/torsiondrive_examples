#!/bin/bash

# set -e

for d in */; do
  echo $d
  cd $d
  for dd in */; do
    echo $dd
    cd $dd
    for ddd in */; do
      echo $ddd
      cd $ddd  
      bash run_command > scan.log
      cd ..
    done
    cd ..
  done
  cd ..
done
