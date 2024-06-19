#!/bin/sh

source ./utils.sh

export VENV_NAME="venv_dbt"

if [ ! -d "${VENV_NAME}/" ]
then 
  print_log "Creating the folder .${VENV_NAME} ..."
  python3 -m venv --prompt ${VENV_NAME} .${VENV_NAME}
  print_log "Folder .${VENV_NAME} OK !"
fi

print_log "Source the environment ..."
source .${VENV_NAME}/bin/activate
print_log "Environment OK !"

# Check if we need to install requirements
check_install=$(pip list | grep -E "dbt-core|dbt-duckdb|duckdb|streamlit" | wc -l)

if [ ${check_install} -lt 4 ]
then
  print_log "Install requirements ..."
  #pip install -r requirements_venv_dbt.txt
  pip install dbt-core dbt-duckdb duckdb 
  pip install streamlit
  print_log "Requirements OK !"
fi




