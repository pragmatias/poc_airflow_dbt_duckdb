#!/bin/sh

source ./utils.sh

if [ ${PREFECT_HOME} != "" ]
then 
  rm -rf ${PREFECT_HOME}
  print_log "PREFECT_HOME deleted !"
fi



