#!/bin/sh

deactivate

if [ ${AIRFLOW_HOME} != "" ]
then 
  rm -rf ${AIRFLOW_HOME}
fi

unset AIRFLOW_HOME
