import pathlib
from prefect import task
from prefect_shell import ShellOperation

env = "prod"

dir_root  = pathlib.Path(__file__).parent.parent.resolve()

dir_dbt = f"{dir_root}/dbt/DuckyWH"
dir_db = f"{dir_root}/data/database"

@task(task_run_name="exec_dbt-{cmd}-{tag}")
def exec_dbt(cmd,tag):
    return ShellOperation(
        commands=[
            f"cd {dir_root} ",
            "source dbt_activate.sh",
            f"cd {dir_dbt}",
            f"dbt {cmd} --selector {tag} --target {env}",
        ]
    ).run()


@task(task_run_name="clean_dbt")
def clean_dbt():
    return ShellOperation(
        commands=[
            f"cd {dir_root} ",
            "source dbt_activate.sh",
            f"cd {dir_dbt}",
            f"dbt clean",
        ]
    ).run()


@task(task_run_name="seed_dbt")
def seed_dbt():
    return ShellOperation(
        commands=[
            f"cd {dir_root} ",
            "source dbt_activate.sh",
            f"cd {dir_dbt}",
            f"dbt seed",
        ]
    ).run()

@task(task_run_name="run_import-{script}")
def run_import(script):
    return ShellOperation(
        commands=[
            f"cd {dir_root} ",
            "source dbt_activate.sh",
            f"python3 import/{script}",
        ]
    ).run()


@task(task_run_name="run_get_api-{script}")
def run_get_api(script):
    return ShellOperation(
        commands=[
            f"cd {dir_root} ",
            "source dbt_activate.sh",
            f"python3 scripts_api/{script}",
        ]
    ).run()


@task(task_run_name="remove_db")
def remove_db():
    return ShellOperation(
        commands=[
            f"cd {dir_db} ",
            "rm -f *.duckdb",
        ]
    ).run()
