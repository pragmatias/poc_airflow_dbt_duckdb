#!/bin/sh

source ./utils.sh

POSTGRES_EXIST=$(podman ps -a -f "name=postgres_scheduler" | wc -l)
POSTGRES_RUNNING=$(podman ps -a -f "name=postgres_scheduler" -f "status=running" | wc -l)
if [ "${POSTGRES_EXIST}" -eq "2" ]
then 

  if [ ! "${POSTGRES_RUNNING}" -eq "2" ]
  then
    # Start container
    print_log "Start postgreSQL container (docker) ..."
    podman-compose -f docker/docker_compose_postgres.yml start
    print_log "postgreSQL container (docker) started !"
  
  else 
    print_log "ERROR : Container exist but can't be started !"
    exit 1
  fi

else
  print_log "Nothing to do !"
fi

