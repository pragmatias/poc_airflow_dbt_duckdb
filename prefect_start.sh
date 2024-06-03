#!/bin/sh

source ./utils.sh

TIMEOUT=10

print_log "Start Prefect server ..."
prefect server start &> ${PREFECT_HOME}/logs_server.log &

CHECK_STATUS=0
cpt=0

while { [ ${cpt} -le ${TIMEOUT} ] && [ ${CHECK_STATUS} -ne 1 ] ;}
do
  print_log "Check the Prefect server status ..."
  sleep 5
  CHECK_STATUS=$(curl --silent http://localhost:4200/dashboard | grep "title" | grep "Prefect Server" | wc -l)
  cpt=$((cpt + 1))
done

if [ ${CHECK_STATUS} -eq 1 ]
then
  print_log "Prefect server started !"
else 
  print_log "ERROR : Prefect server not started properly"
  exit 1
fi



