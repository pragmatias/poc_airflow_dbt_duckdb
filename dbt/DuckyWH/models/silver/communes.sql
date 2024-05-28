{{ config(
  materialized="table",
  schema="silver",
  tags=["sel_cities"],
)}}


with newdata as (
  select nom
        ,code
        ,codeDepartement
        ,siren
        ,cast(codeEpci as integer) as codeEpci
        ,cast(codeRegion as integer) as codeRegion
        ,codesPostaux
        ,cast(coalesce(population,'0') as integer) as population
  from {{ source('raw','communes') }}
)

select *
from newdata

