#!/bin/sh


if [ ! -d ".venv_dbt/" ]
then 
  python3 -m venv --prompt venv_dbt .venv_dbt
fi

source .venv_dbt/bin/activate





