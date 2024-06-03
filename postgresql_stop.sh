#!/bin/sh

source ./utils.sh

TIMEOUT=5
POSTGRES_EXIST=$(podman ps -a -f "name=postgres_scheduler" | wc -l)
POSTGRES_RUNNING=$(podman ps -a -f "name=postgres_scheduler" -f "status=running" | wc -l)

if [ ${POSTGRES_EXIST} -eq 2 ]
then 

  if [ ${POSTGRES_RUNNING} -eq 2 ]
  then
    # Stop container
    print_log "Stop PostgreSQL container (docker) ..."
    podman-compose -f docker/docker_compose_postgres.yml stop
  
    cpt=0
    while { [ ${cpt} -le ${TIMEOUT} ] && [ ${POSTGRES_RUNNING} -eq 2 ] ;}
    do 
      sleep 5
      print_log "Check is PostgreSQL container is running ..."
      POSTGRES_RUNNING=$(podman ps -a -f "name=postgres_scheduler" -f "status=running" | wc -l)
      cpt=$((cpt + 1))
    done

    if [ ${POSTGRES_RUNNING} -ne 2 ]
    then
      print_log "PostgreSQL container (docker) stopped !"
    else
      print_log "ERROR : PostgreSQL container not stopped properly !"
      exit 1
    fi

  else 
    print_log "Nothing to do ! (PostgreSQL container is not running)"
  fi

else
  print_log "Nothing to do !"
fi



