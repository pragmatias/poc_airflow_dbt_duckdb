{{ config(
  materialized="view",
  schema="gold",
  tags=["sel_cities"],
)}}

with ref_com as (
  select nom
        ,code
        ,population 
  FROM {{ ref("communes") }}
)
, ref_cit as (
  select insee_code 
        ,city_code
        ,label
        ,zip_code
        ,department_number
        ,department_name
        ,latitude
        ,longitude
  FROM {{ ref("cities") }}
)

select r2.insee_code
  ,r1.nom
  ,r2.zip_code
  ,r2.department_number
  ,r2.department_name
  ,r2.latitude
  ,r2.longitude
  ,r1.population
from ref_com r1
inner join ref_cit r2
on (r1.code == r2.insee_code)
