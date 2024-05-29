{{ config(
  materialized="table",
  schema="silver",
  tags=["sel_geonames"],
)}}



with newdata as (
  select codes
        ,name
        ,geonameid
  from {{ source('raw','geonames_admin2') }}
)

select *
from newdata