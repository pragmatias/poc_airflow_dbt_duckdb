#!/bin/sh

airflow scheduler &> ${AIRFLOW_HOME}/logs/scheduler.log &
airflow webserver &> ${AIRFLOW_HOME}/logs/webserver.log &

