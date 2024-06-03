import pathlib
from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.decorators import task_group
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sensors.external_task import ExternalTaskSensor

env = "prod"

dir_root  = pathlib.Path(__file__).parent.parent.resolve()

dir_dbt = f"{dir_root}/dbt/DuckyWH"
dir_db = f"{dir_root}/data/database"

def exec_dbt(cmd,tag):
    return BashOperator(
        task_id=".".join(["run_dbt",cmd,tag,env]),
        bash_command = f"cd {dir_root} "
            + '&& source dbt_activate.sh '
            + f"&& cd {dir_dbt} "
            + f"&& dbt {cmd} --selector {tag} --target {env} ",
    )


def clean_dbt():
    return BashOperator(
        task_id="clean_dbt",
        bash_command = f"cd {dir_root} "
            + '&& source dbt_activate.sh '
            + f"&& cd {dir_dbt} "
            + "&& dbt clean",
    )


def seed_dbt():
    return BashOperator(
        task_id="seed_dbt",
        bash_command = f"cd {dir_root} "
            + '&& source dbt_activate.sh '
            + f"&& cd {dir_dbt} "
            + "&& dbt seed",
    )

def run_import(script):
    return BashOperator(
        task_id=".".join(["run_import",script.split(".")[0]]),
        bash_command = f"cd {dir_root}"
            + ' && source dbt_activate.sh '
            + f" && python3 import/{script}",
    )

def run_get_api(script):
    return BashOperator(
        task_id=".".join(["run_get_api",script.split(".")[0]]),
        bash_command = f"cd {dir_root}"
            + ' && source dbt_activate.sh '
            + f" && python3 scripts_api/{script}",
    )

def remove_db():
    return BashOperator(
        task_id="remove_db",
        bash_command = f"rm -f {dir_db}/*.duckdb",
    )


def run_dag(dag_id):
    return TriggerDagRunOperator(
        task_id=".".join(["dag_trigger",dag_id]),
        trigger_dag_id=dag_id,
        wait_for_completion=True,
        poke_interval=15,
    )
