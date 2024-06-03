#!/bin/sh

source ./utils.sh

# check if python env exist
if [ ! -d ".venv_prefect/" ]
then 
  print_log "Creating the folder .venv_prefect ..."
  python3 -m venv --prompt venv_prefect .venv_prefect
  print_log "Folder .venv_prefect OK !"
fi


print_log "Source the environment ..."
source .venv_prefect/bin/activate
print_log "Environment OK !"

PWD_HOME=`pwd`
export PREFECT_HOME=${PWD_HOME}/prefect
export PREFECT_LOCAL_STORAGE_PATH=${PREFECT_HOME}/storage

# Install Airflow if needed (local)
PREFECT_INSTALLED=$(pip list | grep -E "prefect|prefect-shell" | wc -l)
if [ ${PREFECT_INSTALLED} -le 2 ]
then
  print_log "Install requirements ..."
  pip install -U prefect prefect-shell
  print_log "Requirements OK !"
fi




