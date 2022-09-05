#!/bin/sh

for (( i=1; i<=$#; i++));
do
  echo "Arg$i:${@:$i:1}"
done

for (( i=1; i<=$#; i++));
do
  if [[ $i == ${#} ]];
  then
    echo $((${@:$i:1}+$1))
  else
    echo -n $((${@:$i:1}+${@:$i+1:1}))"  "
  fi
done