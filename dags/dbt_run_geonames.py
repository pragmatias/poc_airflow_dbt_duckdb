from local_dags_tools import *
from datetime import datetime, timedelta
from airflow.models.dag import DAG


with DAG(
    "dbt_run_geonames",
    default_args={
        "depends_on_past": False,
        "email" : [""],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description = "Run the DBT geonames models",
    schedule="@daily",
    start_date=datetime(2024,5,14),
    catchup=False,
    tags=["dbt","geonames"],
) as dag:

    t_api_geonames = run_get_api("get_api_geonames.py")

    t_run = exec_dbt("run","sel_geonames")
    
    # Relation
    t_api_geonames >> t_run
