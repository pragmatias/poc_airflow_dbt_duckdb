#!/bin/sh

source ./utils.sh

export VENV_NAME="venv_polars"

if [ ! -d ".venv_polars/" ]
then 
  print_log "Creating the folder .${VENV_NAME} ..."
  python3 -m venv --prompt ${VENV_NAME} .${VENV_NAME}
  print_log "Folder .${VENV_NAME} OK !"
fi

print_log "Source the environment ..."
source .${VENV_NAME}/bin/activate
print_log "Environment OK !"

# Check if we need to install requirements
check_install=$(pip list | grep -E "polars|deltalake|requests" | wc -l)

if [ ${check_install} -lt 3 ]
then
  print_log "Install requirements ..."
  pip install polars deltalake requests
  print_log "Requirements OK !"
fi




