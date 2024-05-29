# Project

Hands on with [Airflow](https://airflow.apache.org/), [DBT](https://www.getdbt.com/) and [Streamlit](https://streamlit.io/)


# Folders

```
├── .github/workflows           <--- Config for Github Actions (CI/CD)
├── dags                        <--- Dags file for Airflow
├── data
|   ├── database                <--- Storage for DuckDB
|   ├── source                  <--- Storage for Source files
|   ├── genere                  <--- Storage for generated files (by scripts_api)
├── dbt/DuckyWH                 <--- DBT Project
├── docker                      <--- Config for docker-compose (PostgreSQL)
├── import                      <--- Scripts to import raw data into DuckDB
├── scripts_api                 <--- Scripts to retrieve information from multiple API
├── streamlit                   <--- Streamlit application
```

# Tools

## Airflow

Command to manage the Airflow Environment :
- To charge the Python Airflow environment : `source airflow_activate.sh`
- To init the Docker (PostgreSQL) for Airflow environment : `./airflow_init.sh`
- To start Docker & Airflow services : `./airflow_start.sh`
- To stop Airflow & Docker services : `./airflow_stop.sh`
- To unload the Python Airflow environment : `source airflow_deactivate.sh`



## DBT

Command to manage the Airflow Environment : 
- To charge the Python DBT Enviroment : `source dbt_activate.sh`
- To unload the Python DBT Environment : `deactivate`


## Streamlit

Command to activate the Streamlit Application : `streamlit run streamlit/display_app.py`
