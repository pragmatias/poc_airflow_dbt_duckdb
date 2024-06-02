#!/bin/sh

source ./utils.sh

print_log "Start Prefect server ..."
prefect server start &> ${PREFECT_HOME}/logs_server.log &
sleep 30
print_log "Prefect server started !"



