#!/bin/sh

#set variable NAME
NAME="alekceu_shved"

#import variable from source file
source ./vars

#create folder and file
mkdir ./$NAME
touch ./$NAME/$FILE

# get directory content
ls -l ./
ls -l ./$NAME