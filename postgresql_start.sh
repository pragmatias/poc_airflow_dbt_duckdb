#!/bin/sh

source ./utils.sh

TIMEOUT=5
POSTGRES_EXIST=$(podman ps -a -f "name=postgres_scheduler" | wc -l)
POSTGRES_RUNNING=$(podman ps -a -f "name=postgres_scheduler" -f "status=running" | wc -l)

if [ ${POSTGRES_EXIST} -eq 2 ]
then 

  if [ ${POSTGRES_RUNNING} -ne 2 ]
  then
    # Start container
    print_log "Start PostgreSQL container (docker) ..."
    podman-compose -f docker/docker_compose_postgres.yml start

    cpt=0
    while { [ ${cpt} -le ${TIMEOUT} ] && [ ${POSTGRES_RUNNING} -ne 2 ] ;}
    do 
      print_log "Check is PostgreSQL container is running ..."
      sleep 5
      POSTGRES_RUNNING=$(podman ps -a -f "name=postgres_scheduler" -f "status=running" | wc -l)
      cpt=$((cpt + 1))
    done

    if [ ${POSTGRES_RUNNING} -eq 2 ]
    then
      print_log "PostgreSQL container (docker) started !"
    else
      print_log "ERROR : PostgreSQL container not started properly !"
      exit 1
    fi
  else 
    print_log "ERROR : PostgreSQL container exist but can't be started !"
    exit 1
  fi

else
  print_log "Nothing to do !"
fi

