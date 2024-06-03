#!/bin/sh

source ./utils.sh


getFloNbr=`ps -ef | grep prefect | grep "flows/" | grep -v "grep" | wc -l`
if [ ${getFloNbr} -ge 1 ]
then
  print_log "Stop flows services ..."
  ps -ef | grep prefect | grep "flows/" | grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Flows services stopped !"
fi 

getSrvNbr=`ps -ef | grep prefect | grep "prefect server start"| grep -v "grep" | wc -l`
if [ ${getSrvNbr} -ge 1 ]
then
  print_log "Stop prefect server ..."
  ps -ef | grep prefect | grep "prefect server start" | grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Prefect server stopped !"
fi 

getSrvAPINbr=`ps -ef | grep prefect | grep "prefect.server.api"| grep -v "grep" | wc -l`
if [ ${getSrvAPINbr} -ge 1 ]
then
  print_log "Stop prefect server API ..."
  ps -ef | grep prefect | grep "prefect.server.api"| grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Prefect server API stopped !"
fi 

getDBNbr=`ps -ef | grep "prefect_db" | grep -v "grep" | wc -l`
if [ ${getDBNbr} -ge 1 ]
then
  print_log "Stop prefect process ..."
  ps -ef | grep "prefect_db" | grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Prefect process stopped !"
fi 
