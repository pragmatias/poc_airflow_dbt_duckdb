#!/bin/sh

source ./utils.sh

TIMEOUT=10

mkdir -p ${DAGSTER_HOME}

print_log "Start Dagster server ..."
cd dagster_jobs && dagster dev &> ${DAGSTER_HOME}/logs_server.log &

CHECK_STATUS=0
cpt=0

while { [ ${cpt} -le ${TIMEOUT} ] && [ ${CHECK_STATUS} -ne 1 ] ;}
do
  print_log "Check the Dagster server status ..."
  sleep 10
  CHECK_STATUS=$(curl --silent http://localhost:3000/server_info | jq . | grep "dagster_version" | wc -l)
  cpt=$((cpt + 1))
done

if [ ${CHECK_STATUS} -eq 1 ]
then
  print_log "Dagster server started !"
else 
  print_log "ERROR : Dagster server not started properly"
  exit 1
fi





