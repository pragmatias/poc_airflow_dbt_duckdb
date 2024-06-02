#!/bin/sh

source ./utils.sh

if [ ${DAGSTER_HOME} != "" ]
then 
  rm -rf ${DAGSTER_HOME}
  print_log "DAGSTER_HOME deleted !"
fi



