#!/bin/sh

source ./utils.sh


getFloNbr=`ps -ef | grep prefect | grep "flows/" | grep -v "grep" | wc -l`
if [ ${getFloNbr} -ge 1 ]
then
  print_log "Stop flows services ..."
  ps -ef | ps -ef | grep prefect | grep "flows/" | grep -v "grep" | awk '{print $2}' | xargs kill -9
fi 

getSrvNbr=`ps -ef | grep prefect | grep "prefect server start"| grep -v "grep" | wc -l`
if [ ${getSrvNbr} -ge 1 ]
then
  print_log "Stop prefect server ..."
  ps -ef | grep prefect | grep "prefect server start" | grep -v "grep" | awk '{print $2}' | xargs kill -9
fi 

getSrvAPINbr=`ps -ef | grep prefect | grep "prefect.server.api"| grep -v "grep" | wc -l`
if [ ${getSrvAPINbr} -ge 1 ]
then
  print_log "Stop prefect server API ..."
  ps -ef | grep prefect | grep "prefect.server.api"| grep -v "grep" | awk '{print $2}' | xargs kill -9
fi 

getDBNbr=`ps -ef | grep "prefect_db" | grep -v "grep" | wc -l`
if [ ${getDBNbr} -ge 1 ]
then
  print_log "Kill prefect_db process ..."
  ps -ef | grep "prefect_db" | grep -v "grep" | awk '{print $2}' | xargs kill -9
fi 
