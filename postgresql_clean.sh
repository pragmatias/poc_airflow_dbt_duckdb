#!/bin/sh

source ./utils.sh

POSTGRES_EXIST=$(podman ps -a -f "name=postgres_scheduler" | wc -l)
if [ "${POSTGRES_EXIST}" -eq "2" ]
then 
  # Create container
  print_log "Create postgreSQL container (docker) ..."
  podman-compose -f docker/docker_compose_postgres.yml down
  print_log "postgreSQL container (docker) created !"
  
  print_log "Delete postgreSQL volume ..."
  podman volume rm docker_postgresql_data --force
  print_log "volume postgreSQL deleted !"
else
  print_log "Nothing to do !"
fi



