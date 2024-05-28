#!/bin/sh

print_log()
{
  message=$1
  echo "`date +"%Y-%m-%d %H-%M-%S - "`${message}"
}

PWD_HOME=`pwd`
export AIRFLOW_HOME=${PWD_HOME}/airflow
export PODMAN_IGNORE_CGROUPSV1_WARNING=""

# Execution Docker
print_log "Create postgreSQL container (docker) ..."
podman-compose -f docker/docker_compose.yml up &
print_log "postgreSQL container (docker) created !"

# if db config not exist
if [ ! -e ${AIRFLOW_HOME}/airflow.db ]
then 
  print_log "Initialize the airflow configuration ..."
  airflow db migrate 

  # Maj config file
  sed -i 's/^\(load_examples =\).*/\1 False/g' ${AIRFLOW_HOME}/airflow.cfg
  # Change the dags folder ()
  sed -i "s#^\(dags_folder =\).*#\1 ${PWD_HOME}/dags#g" ${AIRFLOW_HOME}/airflow.cfg
  # Change the airflow executor
  sed -i "s#^\(executor =\).*#\1 LocalExecutor#g" ${AIRFLOW_HOME}/airflow.cfg
  # Change connexion to postgresql
  sed -i "s#^\(sql_alchemy_conn =\).*#\1 postgresql+psycopg2://airflow:airflow@localhost:5432/airflow_db#g" ${AIRFLOW_HOME}/airflow.cfg
  
  airflow db migrate 
  airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@admin --password admin

  print_log "Airflow configuration OK !"
fi



