#!/bin/sh

source ./utils.sh

POSTGRES_EXIST=$(podman ps -a -f "name=postgres_scheduler" | wc -l)
if [ ! "${POSTGRES_EXIST}" -eq "2" ]
then 
  # Create container
  print_log "Create postgreSQL container (docker) ..."
  podman-compose -f docker/docker_compose_postgres.yml up &
  print_log "postgreSQL container (docker) created !"
  
  sleep 15

  # Stop container
  print_log "Stop postgreSQL container (docker) ..."
  podman-compose -f docker/docker_compose_postgres.yml stop
  print_log "postgreSQL container (docker) stopped !"
else
  print_log "Nothing to do !"
fi



