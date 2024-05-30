#!/bin/sh

print_log()
{
  message=$1
  echo "`date +"%Y-%m-%d %H-%M-%S - "`${message}"
}

export PODMAN_IGNORE_CGROUPSV1_WARNING=""

print_log "Stop postgreSQL container (docker) ..."
podman-compose -f docker/docker_compose.yml stop


# stop airflow process
getWebNbr=`ps -ef | grep airflow | grep webserver | wc -l`
getSchNbr=`ps -ef | grep airflow | grep scheduler | wc -l`

print_log "Stop airflow webserver ..."
if [ ${getWebNbr} -ge 1 ]
then
  ps -ef | grep airflow | grep webserver | awk '{print $2}' | xargs kill -9
fi 

print_log "Stop airflow scheduler ..."
if [ ${getSchNbr} -ge 1 ]
then
  ps -ef | grep airflow | grep scheduler | awk '{print $2}' | xargs kill -9
fi 
