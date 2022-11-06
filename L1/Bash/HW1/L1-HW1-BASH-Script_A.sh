#!/bin/bash

#########################################################################################################
#
#A. Create a script that uses the following keys:
#1. When starting without parameters, it will display a list of possible keys and their description.
#2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet
#3. The --target key displays a list of open system TCP ports.
#The code that performs the functionality of each of the subtasks must be placed in a separate function
#
########################################################################################################

f_showhelp(){
  echo "";
  echo "########################################################################################";
  echo "List of possible keys and their description";
  echo "--all , --target";
  echo "-all key displays the IP addresses and symbolic names of all hosts in the current subnet. For fast scan type --all fast";
  echo "--target key displays a list of open system TCP ports. Use --target IP";
  echo "======================";
  echo "Author Aleksey Shved";
  echo "======================";
  echo "#########################################################################################";
}

f_showallhost(){
  net_mask=$(ip a | grep "global" | cut -d ' ' -f 6 | cut -d '/' -f 2)
  host_ip=$(ip a | grep "global" | cut -d ' ' -f 6 | cut -d '/' -f 1 | cut -d '.' -f 4)
  host_network=$(ip a | grep "global" | cut -d ' ' -f 6 | cut -d '/' -f 1 | cut -d '.' -f 1,2,3)
  if [[ $net_mask -ge 24 && $net_mask -le 26 ]]; then
    if [[ $net_mask -eq 24 ]]; then
      start_ip="1"
      end_ip="254";
    elif [[ $net_mask -eq 25 ]]; then
      if [[ $host_ip -le 127 ]]; then
        start_ip="1";
        end_ip="126";
      else
        start_ip="128";
        end_ip="254";
      fi
    else
      if [[$host_ip -le 63]]; then
        start_ip="1";
        end_ip="62";
      elif [[ $host_ip -le 127 ]]; then
        start_ip="65";
        end_ip="126";
      elif [[ $host_ip -le 191 ]]; then
        start_ip="129";
        end_ip="190";
      else
        start_ip="193";
        end_ip="254";
      fi
    fi
  else
    echo "Network is too big or too small. Script allow to scan network with mask 24-26"
    exit 0
  fi
  echo $1
  case $1 in
    "fast" )
      for (( i=$start_ip; i<=$end_ip; i++))
      do
        ping "$host_network.$i"  -c 1 | grep ttl | cut -d " " -f 4 | cut -d ":" -f 1 &
      done;;

    * )
      for (( i=$start_ip; i<=$end_ip; i++))
      do
        if [[ $(ping "$host_network.$i" -c 1 | grep ttl ) ]];then
          echo "$host_network.$i"
        fi
      done;;
  esac
}

case $1 in
  "--all" )
    if [[ $2 ]]; then
      f_showallhost $2
    else
      f_showallhost
    fi;;

  "--target" )
    echo "show open port on target system";;

  * )
    f_showhelp;;
esac
