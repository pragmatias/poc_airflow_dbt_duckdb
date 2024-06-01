#!/bin/sh

source ./utils.sh

print_log "Start airflow scheduler ..."
airflow scheduler &> ${AIRFLOW_HOME}/logs/scheduler.log &

print_log "Start airflow webserver ..."
airflow webserver &> ${AIRFLOW_HOME}/logs/webserver.log &


