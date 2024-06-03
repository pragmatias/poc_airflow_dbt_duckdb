#!/bin/sh

source ./utils.sh
TIMEOUT=10

print_log "Start Airflow scheduler ..."
airflow scheduler &> ${AIRFLOW_HOME}/logs/scheduler.log &

print_log "Start Airflow webserver ..."
airflow webserver &> ${AIRFLOW_HOME}/logs/webserver.log &

CHECK_STATUS=""
cpt=0

while { [ ${cpt} -le ${TIMEOUT} ] && [ "${CHECK_STATUS}" != "healthy" ] ;}
do
  print_log "Check the Airflow scheduler & webserver status ..."
  sleep 10
  CHECK_STATUS=$(curl --silent http://localhost:8080/health | jq .scheduler.status | sed 's/"//g')
  cpt=$((cpt + 1))
done

if [ "${CHECK_STATUS}" = "healthy" ]
then
  print_log "Airflow scheduler and webserver started !"
else 
  print_log "ERROR : Airflow scheduler and webserver not started properly"
  exit 1
fi



