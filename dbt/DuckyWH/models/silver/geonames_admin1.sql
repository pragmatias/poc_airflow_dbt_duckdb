{{ config(
  materialized="table",
  schema="silver",
  tags=["sel_geonames"],
)}}



with newdata as (
  select code
        ,name
        ,geonameid
  from {{ source('raw','geonames_admin1') }}
)

select *
from newdata