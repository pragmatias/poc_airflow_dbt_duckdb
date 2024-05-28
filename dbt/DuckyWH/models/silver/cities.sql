{{ config(
  materialized="table",
  schema="silver",
  tags=["sel_cities"],
)}}


with newdata as (
  select insee_code 
        ,city_code
        ,zip_code
        ,label
        ,cast((case when latitude = '' then '0.0' else latitude end) as float) as latitude
        ,cast((case when longitude = '' then '0.0' else longitude end) as float) as longitude
        ,department_name
        ,department_number
        ,region_name
        ,region_geojson_name 
  from {{ source('raw','cities') }}
)

select *
from newdata


