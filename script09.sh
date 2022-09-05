#!/bin/bash

MYSPID="/tmp/MYSPIDFILE"

case $1 in
  start )
    echo "$$" >> $MYSPID # write all PID processes to file
    echo "Service started"
    sleep 9999;;

  stop )
    # pkill my_service.sh
    # MYSPID=$(ps | grep my_ | cut -d ' ' -f 1)

    for mpid in $(cat $MYSPID)
    do
      kill -9 $mpid
    done
    echo "" > $MYSPID
    echo "Service stopped" ;;

  restart )
    # pkill my_service.sh
    # MYSPID=$(ps | grep my_ | cut -d ' ' -f 1)
    for mpid in $(cat $MYSPID)
      do
        kill -9 $mpid
      done
    echo "" > $MYSPID
    echo "Stop service"
    echo "$$" >> $MYSPID
    echo "Start service"
    sleep 9999;;

  * )
    echo " Usage: my_service.sh [start & | stop | restart & ]"
esac