#!/bin/sh

source ./utils.sh

# if db config not exist
if [ ! -e ${AIRFLOW_HOME}/airflow.db ]
then 
  # Create needed subfolder for airflow execution
  print_log "Create subfolder (config & logs) for Airflow execution in ${AIRFLOW_HOME}"
  mkdir -p {${AIRFLOW_HOME}/config,${AIRFLOW_HOME}/logs}

  print_log "Initialize the airflow configuration ..."
  airflow db migrate 

  # Maj config file
  sed -i 's/^\(load_examples =\).*/\1 False/g' ${AIRFLOW_HOME}/airflow.cfg
  # Change the dags folder ()
  sed -i "s#^\(dags_folder =\).*#\1 ${AIRFLOW_DAGS_HOME}#g" ${AIRFLOW_HOME}/airflow.cfg
  # Change the airflow executor
  sed -i "s#^\(executor =\).*#\1 LocalExecutor#g" ${AIRFLOW_HOME}/airflow.cfg
  # Change connexion to postgresql
  sed -i "s#^\(sql_alchemy_conn =\).*#\1 postgresql+psycopg2://postgres:postgres@localhost:5432/airflow_db#g" ${AIRFLOW_HOME}/airflow.cfg
  
  airflow db migrate 
  airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@admin --password admin

  print_log "Airflow configuration OK !"

else
  print_log "Nothing to do !"
fi



