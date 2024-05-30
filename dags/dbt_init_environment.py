from local_dags_tools import *
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


with DAG(
    "dbt_init_environment",
    default_args={
        "depends_on_past": False,
        "email" : ["contact@pragmatias.fr"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description = "Init DBT environment",
    schedule=None,
    start_date=datetime(2024,5,14),
    catchup=False,
    tags=["dbt","init", "clean","environment"],
) as dag:

    t_clean = clean_dbt()

    t_remove_db = remove_db()

    t_api_communes = run_get_api("get_api_gouv_communes.py")

    t_init_db = run_import("init_DuckyWH.py")

    t_init_db_geo = run_import("init_geonames.py")

    t_init_snap = run_import("gen_snapshot_data.py")

    t_load_seed = seed_dbt()

    t_dag_test = run_dag("dbt_build_selectors")

    # relation
    [t_api_communes,t_remove_db] >> t_init_db >> t_init_db_geo >> t_init_snap
    [t_init_snap, t_clean] >> t_load_seed >> t_dag_test
