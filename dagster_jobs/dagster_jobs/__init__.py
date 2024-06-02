from dagster import Definitions

from . import dbt_jobs


defs = Definitions(jobs=[dbt_jobs.dbt_init_environment
                         ,dbt_jobs.dbt_build_selectors
                         ,dbt_jobs.dbt_run_cities
                         ,dbt_jobs.dbt_run_geonames
                         ,dbt_jobs.dbt_run_snap_random],
                    sensors=[dbt_jobs.start_dbt_build_selectors_job],
                    schedules=[dbt_jobs.schedule_daily_dbt_run_cities
                               ,dbt_jobs.schedule_daily_dbt_run_geonames
                               ,dbt_jobs.schedule_daily_dbt_run_snap_random])
