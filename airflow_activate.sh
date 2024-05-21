#!/bin/sh

# check if python env exist
if [ ! -d ".venv_airflow/"]
then 
  python3 -m venv --prompt venv_airflow .venv_airflow
fi

source .venv_airflow/bin/activate

PWD_HOME=`pwd`
export AIRFLOW_HOME=${PWD_HOME}/airflow

# Create needed subfolder for airflow execution
mkdir -p {${AIRFLOW_HOME}/config,${AIRFLOW_HOME}/logs}

# Install Airflow if needed (local)
AIRFLOW_INSTALLED=`pip list | grep "apache-airflow" | grep "2.9.1" | wc -l`
if [ ${AIRFLOW_INSTALLED} -ne 1 ]
then
  pip install "apache-airflow==2.9.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-3.8.txt"
fi


# if db config not exist
if [ ! -e ${AIRFLOW_HOME}/airflow.db ]
then 
  airflow db migrate 
  airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@admin --password admin


  # Maj config file
  sed -i 's/^\(load_examples =\).*/\1 False/g' ${AIRFLOW_HOME}/airflow.cfg
  # Change the dags folder ()
  sed -i "s#^\(dags_folder =\).*#\1 ${PWD_HOME}/dags#g" ${AIRFLOW_HOME}/airflow.cfg

fi




