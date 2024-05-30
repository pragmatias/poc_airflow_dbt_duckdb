#!/bin/sh

print_log()
{
  message=$1
  echo "`date +"%Y-%m-%d %H-%M-%S - "`${message}"
}

# check if python env exist
if [ ! -d ".venv_airflow/" ]
then 
  print_log "Creating the folder .venv_airflow ..."
  python3 -m venv --prompt venv_airflow .venv_airflow
  print_log "Folder .venv_airflow OK !"
fi


print_log "Source the environment ..."
source .venv_airflow/bin/activate
print_log "Environment OK !"

PWD_HOME=`pwd`
export AIRFLOW_HOME=${PWD_HOME}/airflow

# Install Airflow if needed (local)
AIRFLOW_INSTALLED=$(pip list | grep "apache-airflow" | grep "2.9.1" | wc -l)
if [ ${AIRFLOW_INSTALLED} -ne 1 ]
then
  print_log "Install requirements ..."
  pip install "apache-airflow==2.9.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-3.8.txt"
  pip install psycopg2-binary
  print_log "Requirements OK !"
fi




