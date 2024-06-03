#!/bin/sh

source ./utils.sh

POSTGRES_EXIST=$(podman ps -a -f "name=postgres_scheduler" | wc -l)
if [ ${POSTGRES_EXIST} -ne 2 ]
then 
  # Create container
  print_log "Create PostgreSQL container (docker) ..."
  podman-compose -f docker/docker_compose_postgres.yml up &

  POSTGRES_RUNNING=0
  while [ ${POSTGRES_RUNNING} -ne 2 ]
  do
     print_log "Check if PostgreSQL container is running ..."
     sleep 5
     POSTGRES_RUNNING=$(podman ps -f "name=postgres_scheduler" -f "status=running" | wc -l)
  done

  print_log "PostgreSQL container (docker) created !"

  # Stop container
  print_log "Stop PostgreSQL container (docker) ..."
  podman-compose -f docker/docker_compose_postgres.yml stop
  print_log "PostgreSQL container (docker) stopped !"
else
  print_log "Nothing to do !"
fi



