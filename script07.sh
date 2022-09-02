#!/bin/bash

echo "checks if 1st and 2nd string arguments are equal and outputs the exit code of this operation"
[[ $1 == $2 ]]
echo $?
echo "checks if 1st string argument is longer than 2nd string argument and outputs the exit code of this opera$"
[[ ${#1} -gt ${#2} ]]
echo $?
echo "checks if variable TEST is present in the environment (has non-zero length) and outputs the exit code of $"
[[ ${#TEST} -gt 0 ]]
echo $?
echo "checks if 3rd and 4th integer arguments are not equal and outputs the exit code of this operation"
[[ $3 -ne $4 ]]
echo $?
echo "checks if 3rd integer argument is greater or equal to 4th integer argument and outputs the exit code of $"
[[ $3 -ge $4 ]]
echo $?
