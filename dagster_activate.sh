#!/bin/sh

source ./utils.sh

# check if python env exist
if [ ! -d ".venv_dagster/" ]
then 
  print_log "Creating the folder .venv_dagster ..."
  python3 -m venv --prompt venv_dagster .venv_dagster
  print_log "Folder .venv_dagster OK !"
fi

print_log "Source the environment ..."
source .venv_dagster/bin/activate
print_log "Environment OK !"

PWD_HOME=`pwd`
export DAGSTER_HOME=${PWD_HOME}/dagster

# Install Airflow if needed (local)
DAGSTER_INSTALLED=$(pip list | grep -E "dagster|dagster-webserver|dagster-shell" | wc -l)
if [ ${DAGSTER_INSTALLED} -le 7 ]
then
  print_log "Install requirements ..."
  pip install -U dagster dagster-webserver dagster-shell
  print_log "Requirements OK !"
fi




