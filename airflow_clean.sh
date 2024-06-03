#!/bin/sh

source ./utils.sh

if [ ${AIRFLOW_HOME} != "" ]
then 
  rm -rf ${AIRFLOW_HOME}
  print_log "AIRFLOW_HOME folder deleted !"
fi



