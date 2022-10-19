#!/bin/bash

declare -r poem_file_name="poem.txt"

echo "Set the file name for poem!"
read file_name

cat $poem_file_name | tee $file_name

echo "Task finished" > stderr

