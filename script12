#!/bin/bash

while :
do
  echo "Enter command"
  read user_input
  clear
  case $user_input in
    ls* )
      echo "Show directory content"
      echo "Enter dir name full path"
      read user_dir
      ls $user_dir 2> /dev/null
      if [[ $? -eq 0 ]];
      then
        ls $user_dir
      else
        echo "Bad directory"
      fi;;
    pwd* )
      pwd;;
    hi* )
      echo "Hello $USER";;
    exit* )
      exit 0;;
    * )
       echo "Use the following commands: ls | pwd | hi | exit"
   esac
done