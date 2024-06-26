from local_dags_tools import *
from datetime import datetime, timedelta
from airflow.models.dag import DAG



with DAG(
    "dbt_build_selectors",
    default_args={
        "depends_on_past": False,
        "email" : [""],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description = "Builds the DBT models",
    schedule=None,
    start_date=datetime(2024,5,14),
    catchup=False,
    tags=["dbt","build","selectors"],
) as dag:

    t_build_cities = exec_dbt("build","sel_cities")

    t_build_snap = exec_dbt("build","sel_snap")

    t_build_geo = exec_dbt("build","sel_geonames")
    
    # Relations
    t_build_cities >> t_build_geo >> t_build_snap
