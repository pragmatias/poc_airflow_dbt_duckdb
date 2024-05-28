{{ config(
  materialized="view",
  schema="gold",
  tags=["sel_snap"],
)}}

with ref_snap as (
  select id
        ,name
        ,value
        ,strftime(dbt_valid_from,'%Y-%m-%d') as valid_from
        ,strftime(coalesce(dbt_valid_to,current_date),'%Y-%m-%d') as valid_to 
  FROM {{ ref("snap_random") }}
)

select * from ref_snap
order by id, valid_from
