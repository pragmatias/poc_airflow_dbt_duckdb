#!/bin/sh

print_log()
{
  message=$1
  echo "`date +"%Y-%m-%d %H-%M-%S - "`${message}"
}

export PODMAN_IGNORE_CGROUPSV1_WARNING=""

# Execution Docker
print_log "Start postgreSQL container (docker) ..."
podman-compose -f docker/docker_compose.yml start

print_log "Start airflow scheduler ..."
airflow scheduler &> ${AIRFLOW_HOME}/logs/scheduler.log &

print_log "Start airflow webserver ..."
airflow webserver &> ${AIRFLOW_HOME}/logs/webserver.log &


