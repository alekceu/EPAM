#!/bin/sh

function f_multiply(){
  return $(($i*$i));
}

function f2_add1(){
  f_multiply $i
  return $(($?+1))
}

for i in "${@}";
do
  f2_add1 $i
  echo $?
don