#!/bin/sh

print_log()
{
  message=$1
  echo "`date +"%Y-%m-%d %H-%M-%S - "`${message}"
}

if [ ! -d ".venv_dbt/" ]
then 
  print_log "Creating the folder .venv_dbt ..."
  python3 -m venv --prompt venv_dbt .venv_dbt
  print_log "Folder .venv_dbt OK !"
fi

print_log "Source the environment ..."
source .venv_dbt/bin/activate
print_log "Environment OK !"

# Check if we need to install requirements
check_install=$(pip list | grep -E "dbt-core|dbt-duckdb|duckdb|streamlit" | wc -l)

if [ ${check_install} -lt 4 ]
then
  print_log "Install requirements ..."
  pip install -r requirements_venv_dbt.txt
  print_log "Requirements OK !"
fi




