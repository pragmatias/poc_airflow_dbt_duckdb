from local_flows_tools import *
from prefect import flow, serve


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dbt_init_environment() :
    clean_dbt()
    run_import("init_DuckyWH.py")
    run_import("init_geonames.py")
    run_import("gen_snapshot_data.py")
    run_import("gen_snapshot_data.py")
    seed_dbt()
    dbt_build_selectors()

@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dbt_build_selectors() :
    exec_dbt("build","sel_cities")
    exec_dbt("build","sel_snap")
    exec_dbt("build","sel_geonames")


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dbt_run_cities():
    exec_dbt("run","sel_cities")


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dbt_run_geonames():
    exec_dbt("run","sel_geonames")

@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dbt_run_snap_random():
    run_import("gen_snapshot_data.py")
    exec_dbt("snapshot","sel_snap")
    exec_dbt("run","sel_snap")


if __name__ == "__main__":
    dbt_init_environment_slow_deploy = dbt_init_environment.to_deployment(name="dbt_init_environment")
    dbt_build_selectors_deploy = dbt_build_selectors.to_deployment(name="dbt_build_selectors")
    dbt_run_cities_deploy = dbt_run_cities.to_deployment(name="dbt_run_cities",cron="0 10 * * *")
    dbt_run_geonames_deploy = dbt_run_geonames.to_deployment(name="dbt_run_geonames",cron="10 10 * * *")
    dbt_run_snap_random_deploy = dbt_run_snap_random.to_deployment(name="dbt_run_snap_random",cron="20 10 * * *")
    serve(dbt_init_environment_slow_deploy
          , dbt_build_selectors_deploy
          ,dbt_run_cities_deploy
          ,dbt_run_geonames_deploy
          ,dbt_run_snap_random_deploy)