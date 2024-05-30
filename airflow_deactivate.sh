#!/bin/sh

if [ ${AIRFLOW_HOME} != "" ]
then 
  rm -rf ${AIRFLOW_HOME}
fi

unset AIRFLOW_HOME
unset PODMAN_IGNORE_CGROUPSV1_WARNING

deactivate
