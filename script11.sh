#!/bin/bash

digit='^[0-9]$'

for i in ${*};
do
  if [[ $i =~ $digit ]];
  then
    echo "$i is gigit"
  else
    echo "$i is not digit"
    echo "all parameters need to be digits"
    exit 0
  fi
done

for i in ${*};
do
  sum=$((sum+i))
done

echo "Sum: $sum"
echo "Args number: ${#}"
echo "Result: $((sum/${#}))"