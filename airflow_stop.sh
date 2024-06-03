#!/bin/sh

source ./utils.sh

getWebNbr=`ps -ef | grep airflow | grep webserver | grep -v "grep" | wc -l`
if [ ${getWebNbr} -ge 1 ]
then
  print_log "Stop Airflow webserver ..."
  ps -ef | grep airflow | grep webserver | grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Airflow webserver stopped !"
fi 

getSchNbr=`ps -ef | grep airflow | grep scheduler | grep -v "grep" | wc -l`
if [ ${getSchNbr} -ge 1 ]
then
  print_log "Stop Airflow scheduler ..."
  ps -ef | grep airflow | grep scheduler | grep -v "grep" |  awk '{print $2}' | xargs kill -9
  print_log "Airflow scheduler stopped !"
fi 

getWrkNbr=`ps -ef | grep airflow | grep worker | grep -v "grep" | wc -l`
if [ ${getWrkNbr} -ge 1 ]
then
  print_log "Stop airflow workers ..."
  ps -ef | grep airflow | grep worker | grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Airflow workers stopped !"
fi 

getExeNbr=`ps -ef | grep airflow | grep executor | grep -v "grep" | wc -l`
if [ ${getExeNbr} -ge 1 ]
then
  print_log "Stop airflow executors ..."
  ps -ef | grep airflow | grep executor | grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Airflow executors stopped !"
fi 

