#!/bin/sh

if [ ${AIRFLOW_HOME} != "" ]
then 
  rm -rf ${AIRFLOW_HOME}
fi

deactivate

unset AIRFLOW_HOME

