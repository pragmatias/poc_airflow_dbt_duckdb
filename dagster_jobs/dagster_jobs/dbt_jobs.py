# Manage Ops & Jobs
from dagster import get_dagster_logger, op, job, In, Out,Nothing, Definitions
# Manage sensor
from dagster import run_status_sensor, RunRequest, DagsterRunStatus,SkipReason
# Manage schedule
from dagster import schedule, ScheduleEvaluationContext
# Manage Shell command execution (ops)
from dagster_shell import execute_shell_command
import pathlib


env = "prod"

dir_root  = pathlib.Path(__file__).parent.parent.parent.resolve()

dir_dbt = f"{dir_root}/dbt/DuckyWH"
dir_db = f"{dir_root}/data/database"


# Define Ops (task)

@op(ins={"start": In(Nothing)})
def dbt_clean():
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt clean"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def dbt_seed():
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt seed"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def remove_db():
    cmds = f"rm -f {dir_db}/*.duckdb" 
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def run_get_api_gouv_communes() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && python3 scripts_api/get_api_gouv_communes.py"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())

@op(ins={"start": In(Nothing)})
def run_get_api_geonames() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && python3 scripts_api/get_api_geonames.py"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def run_import_init_DuckyWH() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && python3 import/init_DuckyWH.py"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def run_import_init_geonames() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && python3 import/init_geonames.py"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def run_import_gen_snapshot_data() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && python3 import/gen_snapshot_data.py"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def dbt_build_select_cities() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt build --selector sel_cities --target {env}"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())

@op(ins={"start": In(Nothing)})
def dbt_build_select_snap() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt build --selector sel_snap --target {env}"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def dbt_build_select_geonames() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt build --selector sel_geonames --target {env}"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def dbt_run_select_cities() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt run --selector sel_cities --target {env}"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())

@op(ins={"start": In(Nothing)})
def dbt_run_select_snap() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt snapshot --selectors sel_snap --target {env}" \
            + f" && dbt run --selector sel_snap --target {env}"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


@op(ins={"start": In(Nothing)})
def dbt_run_select_geonames() :
    cmds =  f"cd {dir_root} " \
            + " && source dbt_activate.sh" \
            + f" && cd {dir_dbt}" \
            + f" && dbt run --selector sel_geonames --target {env}"
    execute_shell_command(cmds, output_logging="STREAM", log=get_dagster_logger())


## Define Jobs (Workflow)



@job
def dbt_init_environment():
    t1 = dbt_clean()
    t2 = remove_db()
    t3 = run_get_api_geonames(
            start=run_get_api_gouv_communes(
                start=[t2,t1] ))
    t4 = run_import_gen_snapshot_data(
            start=run_import_init_geonames(
                start=run_import_init_DuckyWH(
                    start=t3)
                )
            )
    dbt_seed(start=t4)



@job
def dbt_build_selectors() :
    dbt_build_select_geonames(
        start=dbt_build_select_snap(
            start=dbt_build_select_cities()
            )
        )


@job
def dbt_run_cities() :
    dbt_run_select_cities(
        start=run_get_api_gouv_communes()
    )


@job
def dbt_run_geonames() :
    dbt_run_select_geonames(
        start=run_get_api_geonames()
    )


@job
def dbt_run_snap_random() :
    dbt_run_select_snap(
        start=run_import_gen_snapshot_data()
    )


# Sensor to manage the job dependence
@run_status_sensor(
    run_status=DagsterRunStatus.SUCCESS,
    monitored_jobs=[dbt_init_environment],
    request_job=dbt_build_selectors,
)
def start_dbt_build_selectors_job(context):
    if context.dagster_run.job_name in [dbt_init_environment.name]:
        # Trigger the next job
        return RunRequest(run_key=None, job_name="dbt_build_selectors") 
    else:
        # Skip if the sensor is triggered by other jobs
        return SkipReason(f"Waiting for {dbt_init_environment.name} to finish successfully.")



# Schedule
@schedule(job=dbt_run_cities, cron_schedule="0 10 * * *")
def schedule_daily_dbt_run_cities(context: ScheduleEvaluationContext):
    scheduled_date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return RunRequest(
        run_key=None,
        tags={"date": scheduled_date},
    )


@schedule(job=dbt_run_geonames, cron_schedule="15 10 * * *")
def schedule_daily_dbt_run_geonames(context: ScheduleEvaluationContext):
    scheduled_date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return RunRequest(
        run_key=None,
        tags={"date": scheduled_date},
    )


@schedule(job=dbt_run_snap_random, cron_schedule="30 10 * * *")
def schedule_daily_dbt_run_snap_random(context: ScheduleEvaluationContext):
    scheduled_date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return RunRequest(
        run_key=None,
        tags={"date": scheduled_date},
    )
