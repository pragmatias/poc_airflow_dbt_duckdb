from local_dags_tools import *
from datetime import datetime, timedelta
from airflow.models.dag import DAG


with DAG(
    "dbt_run_snap_random",
    default_args={
        "depends_on_past": False,
        "email" : ["contact@pragmatias.fr"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description = "Run the snapshot random with DBT",
    schedule="@hourly",
    start_date=datetime(2024,5,14),
    catchup=False,
    tags=["dbt","snapshot", "import"],
) as dag:

    t_import = run_import("gen_snapshot_data.py")

    t_snapshot = exec_dbt("snapshot","sel_snap")

    t_run = exec_dbt("run","sel_snap")
    
    # Relation
    t_import >> t_snapshot >> t_run
