#!/bin/sh

source ./utils.sh

getSrvNbr=`ps -ef | grep "dagster" | grep "/bin/dagster"| grep -v "grep" | wc -l`
if [ ${getSrvNbr} -ge 1 ]
then
  print_log "Stop Dagster server ..."
  ps -ef | grep "dagster" | grep "bin/dagster" | grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Dagster server stopped !"
fi 

getAPINbr=`ps -ef | grep "dagster" | grep "dagster api grpc"| grep -v "grep" | wc -l`
if [ ${getAPINbr} -ge 1 ]
then
  print_log "Stop Dagster API ..."
  ps -ef | grep "dagster" | grep "dagster api grpc"| grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Dagster API stopped !"
fi 

getWebNbr=`ps -ef | grep "dagster" | grep "dagster_webserver"| grep -v "grep" | wc -l`
if [ ${getWebNbr} -ge 1 ]
then
  print_log "Stop Dagster webserver ..."
  ps -ef | grep "dagster" | grep "dagster_webserver"| grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Dagster webserver stopped !"
fi 

getDaeNbr=`ps -ef | grep "dagster" | grep "dagster._daemon run"| grep -v "grep" | wc -l`
if [ ${getDaeNbr} -ge 1 ]
then
  print_log "Stop Dagster deamon ..."
  ps -ef | grep "dagster" | grep "dagster._daemon run"| grep -v "grep" | awk '{print $2}' | xargs kill -9
  print_log "Dagster deamon stopped !"
fi 
