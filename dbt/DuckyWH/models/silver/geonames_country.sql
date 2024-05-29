{{ config(
  materialized="table",
  schema="silver",
  tags=["sel_geonames"],
)}}



with newdata as (
  select geonameid
        ,name
        ,latitude
        ,longitude
        ,country_code
        ,admin1_code
        ,admin2_code
        ,admin3_code
        ,admin4_code
        ,population
        ,elevation
        ,dem
        ,timezone
        ,modification_date 
  from {{ source('raw','geonames_country') }}
)

select *
from newdata