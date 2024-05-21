{{ config(
  materialized="view",
  schema="gold"
)}}


with data as (
  select insee_code 
        ,city_code
        ,zip_code
        ,label
  FROM {{ ref("cities") }}
)

select * from data
