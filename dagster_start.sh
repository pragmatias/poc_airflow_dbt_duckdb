#!/bin/sh

source ./utils.sh

mkdir -p ${DAGSTER_HOME}

print_log "Start Dagster server ..."
cd dagster_jobs && dagster dev &> ${DAGSTER_HOME}/logs_server.log &
sleep 60
print_log "Dagster server started !"



