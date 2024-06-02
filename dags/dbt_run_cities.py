from local_dags_tools import *
from datetime import datetime, timedelta
from airflow.models.dag import DAG


with DAG(
    "dbt_run_cities",
    default_args={
        "depends_on_past": False,
        "email" : [""],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description = "Run the DBT cities models",
    schedule="@daily",
    start_date=datetime(2024,5,14),
    catchup=False,
    tags=["dbt","cities"],
) as dag:

    t_api_communes = run_get_api("get_api_gouv_communes.py")

    t_run = exec_dbt("run","sel_cities")
    
    # Relation
    t_api_communes >> t_run
