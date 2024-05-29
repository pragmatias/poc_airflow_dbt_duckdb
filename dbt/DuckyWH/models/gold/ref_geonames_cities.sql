{{ config(
  materialized="view",
  schema="gold",
  tags=["sel_geonames"],
)}}

with ref_cit as (
  select geonameid
        ,name
        ,latitude
        ,longitude
        ,country_code
        ,country_code||'.'||admin1_code as admin_code1
        ,country_code||'.'||admin1_code||'.'||admin2_code as admin_code2
        ,admin2_code as  dept_code
        ,admin3_code
        ,admin4_code as postal_code
        ,population
        ,timezone
        ,modification_date 
  FROM {{ ref("geonames_country") }}
  where admin4_code is not null
    and country_code = 'FR'
),
ref_region as (
    select code
        ,name
    from {{ ref("geonames_admin1") }}
),
ref_dept as (
    select codes
        ,name
    from {{ ref("geonames_admin2") }}
),
newdata as (
    select rc.geonameid
        ,rc.name
        ,rc.latitude
        ,rc.longitude
        ,rc.country_code
        ,rg.name as region_name
        ,rd.name as dept_name
        ,rc.dept_code
        ,rc.postal_code
        ,rc.population
        ,rc.timezone
        ,rc.modification_date
    from ref_cit rc
    left outer join ref_region rg
    on (rc.admin_code1 = rg.code)
    left outer join ref_dept rd
    on (rc.admin_code2 = rd.codes)
)

select *
from newdata
