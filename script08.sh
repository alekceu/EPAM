#!/bin/sh

# takes any number of arguments
# if there are less than 2 arguments, output the values of these arguments
# if there are more than 2 but less than 4 arguments, output only the last argument
# else output "Invalid number of arguments" message

if [[ $# -lt 2 ]];
then
  echo $0  $1
elif [[ ($# -ge 2) && ($# -lt 4) ]];
then
  echo ${@: -1}
else
  echo "Invalid number of arguments"
fi