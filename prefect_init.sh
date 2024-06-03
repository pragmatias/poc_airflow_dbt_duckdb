#!/bin/sh

source ./utils.sh

PWD_HOME=`pwd`
export PREFECT_HOME=${PWD_HOME}/prefect


# if db config not exist
if [ ! -e ${PREFECT_HOME}/airflow.db ]
then 
  # Create needed subfolder for airflow execution
  mkdir ${PREFECT_HOME}

  print_log "Initialize the prefect configuration ..."
  prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
  prefect config set PREFECT_API_DATABASE_CONNECTION_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/prefect_db"
  prefect server database reset -y
  print_log "Prefect configuration OK !"

else
  print_log "Nothing to do !"
fi
