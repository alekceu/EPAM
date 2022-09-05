#!/bin/bash
declare -r max_size=1024000

echo "Enter filename"
read user_filename

head -c 4KB /dev/urandom > $user_filename
file_size=$(stat --format=%s $user_filename)
echo $file_size
until [ $file_size -gt $max_size ]
do
  cp $user_filename temp.file
  cat temp.file >> $user_filename
  rm -f temp.file
  file_size=$(stat --format=%s $user_filename)
  echo $file_size
done