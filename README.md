# Project

POC with [Airflow](https://airflow.apache.org/), [DBT](https://www.getdbt.com/) and [Streamlit](https://streamlit.io/).

Adding POC with [Prefect](https://www.prefect.io/) and [Dagster](https://dagster.io/).

Adding work with [Polars](https://pola.rs/) and [Jupyter-notebooks/VsCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

# Folders

```
├── .github/workflows           <--- Config for Github Actions (CI/CD)
├── dags                        <--- Dags file for Airflow
├── dagster_jobs                <--- Jobs/Assets project for Dagster
├── data
|   ├── database                <--- Storage for DuckDB
|   ├── source                  <--- Storage for Source files
|   ├── genere                  <--- Storage for generated files (by scripts_api)
├── dbt/DuckyWH                 <--- DBT Project
├── docker                      <--- Config for docker-compose (PostgreSQL)
├── flows                       <--- Flows file for Prefect
├── import                      <--- Scripts to import raw data into DuckDB
├── scripts_api                 <--- Scripts to retrieve information from multiple API
├── scripts_polars              <--- Scripts to work with polars (python) library
├── streamlit                   <--- Streamlit application
```

# Tools

## PostgreSQL (Docker)

Command to manage the PostgreSQL (Docker) server :
- To create the docker container : `./postgresql_init.sh` 
- To start the docker container : `./postgresql_start.sh` 
- To stop the docker container : `./postgresql_stop.sh` 
- To clean all elements created by the docker container : `./postgresql_clean.sh` 

## Airflow

_prerequisite : PostgreSQL (Docker) need to be in running state to use Airflow_

Command to manage the Airflow environment :
- To load the Python Airflow environment : `source airflow_activate.sh`
- To init the Airflow services : `./airflow_init.sh`
- To start the Airflow services : `./airflow_start.sh`
- To stop the Airflow services : `./airflow_stop.sh`
- To clean all elements created with the Airflow services : `./postgresql_clean.sh` 
- To unload the Python Airflow environment : `deactivate`

Webserver : http://localhost:8080/home

_Connexion with username/password : admin/admin_

## Prefect

_prerequisite : PostgreSQL (Docker) need to be in running state to use Prefect_

Command to manage the Prefect environment :
- To load the Python Prefect environment : `source prefect_activate.sh`
- To init the Prefect services : `./prefect_init.sh`
- To start the Prefect services : `./prefect_start.sh`
- To stop the Prefect services : `./prefect_stop.sh`
- To clean all elements created with the Prefect services : `./prefect_clean.sh` 
- To unload the Python Prefect environment : `deactivate`

Command to deploy :
- Load deployment : `python3 flows/prefect_deployment.py &`
- Run deployment : `prefect deployment run dbt-init-environment/dbt_init_environment`

Webserver : http://localhost:4200/dashboard


## Dagster

- To load the Python Dagster environment : `source dagster_activate.sh`
- To start the Dagster services : `./dagster_start.sh`
- To stop the Dagster services : `./dagster_stop.sh`
- To clean all elements created with the Dagster services : `./dagster_clean.sh` 

Webserver : http://localhost:3000

## DBT & Streamlit

Command to manage the DBT environment : 
- To load the Python DBT environment : `source dbt_activate.sh`
- To unload the Python DBT environment : `deactivate`


## Streamlit

_prerequisite : You need to load the Python DBT Environment to use Streamlit_

Command to activate the Streamlit Application : `streamlit run streamlit/home.py`

Webserver : http://localhost:8501


## Polars with Jupiter Notebooks

Command to manage the DBT environment : 
- To load the Python Polars environment : `source polars_activate.sh`
- To unload the Python Polars environment : `deactivate`

_Note : `write_delta` function doesn't work with WSL_
