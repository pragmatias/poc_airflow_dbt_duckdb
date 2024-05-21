{{ config(
  materialized="table",
  schema="silver"
)}}


with newdata as (
  select nom
        ,code
        ,codeDepartement
        ,siren
        ,cast(codeEpci as integer) as codeEpci
        ,cast(codeRegion as integer) as codeRegion
        ,codesPostaux
        ,cast(population as integer) as population
  from {{ source('raw','communes') }}
)

select *
from newdata

