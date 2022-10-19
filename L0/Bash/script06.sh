#!/bin/sh

#print name of running script
echo $0

#print all arguments in line
echo $@
for val in "$@"; do
  echo $val
done

#print number of arg
echo $#

#prints 2nd and 4th argument
echo "${2} and $4"

#print the exit code of -eq operation on 1st and 2nd arguments (use [[]])
[[ $1 == $3 ]]  
echo $?