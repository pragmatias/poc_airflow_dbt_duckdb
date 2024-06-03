#!/bin/sh

source ./utils.sh

POSTGRES_EXIST=$(podman ps -a -f "name=postgres_scheduler" | wc -l)
if [ ${POSTGRES_EXIST} -eq 2 ]
then 
  # Create container
  print_log "Delete PostgreSQL container (docker) ..."
  podman-compose -f docker/docker_compose_postgres.yml down
  print_log "PostgreSQL container (docker) deleted !"
  
  print_log "Delete PostgreSQL volume ..."
  podman volume rm docker_postgresql_data --force
  print_log "PostgreSQL volume deleted !"
else
  print_log "Nothing to do !"
fi



