#!/bin/sh

source ./utils.sh

getWebNbr=`ps -ef | grep airflow | grep webserver | grep -v "grep" | wc -l`
if [ ${getWebNbr} -ge 1 ]
then
  print_log "Stop airflow webserver ..."
  ps -ef | grep airflow | grep webserver | grep -v "grep" | awk '{print $2}' | xargs kill -9
fi 

getSchNbr=`ps -ef | grep airflow | grep scheduler | grep -v "grep" | wc -l`
if [ ${getSchNbr} -ge 1 ]
then
  print_log "Stop airflow scheduler ..."
  ps -ef | grep airflow | grep scheduler | grep -v "grep" |  awk '{print $2}' | xargs kill -9
fi 

getWrkNbr=`ps -ef | grep airflow | grep worker | grep -v "grep" | wc -l`
if [ ${getWrkNbr} -ge 1 ]
then
  print_log "Stop airflow workers ..."
  ps -ef | grep airflow | grep worker | grep -v "grep" | awk '{print $2}' | xargs kill -9
fi 

getExeNbr=`ps -ef | grep airflow | grep executor | grep -v "grep" | wc -l`
if [ ${getExeNbr} -ge 1 ]
then
  print_log "Stop airflow executor ..."
  ps -ef | grep airflow | grep executor | grep -v "grep" | awk '{print $2}' | xargs kill -9
fi 