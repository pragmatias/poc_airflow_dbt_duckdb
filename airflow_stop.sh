#!/bin/sh

# stop airflow process
getWebNbr=`ps -ef | grep airflow | grep webserver | wc -l`
getSchNbr=`ps -ef | grep airflow | grep scheduler | wc -l`

if [ ${getWebNbr} -ge 1 ]
then
  ps -ef | grep airflow | grep webserver | awk '{print $2}' | xargs kill -9
fi 


if [ ${getSchNbr} -ge 1 ]
then
  ps -ef | grep airflow | grep scheduler | awk '{print $2}' | xargs kill -9
fi 
