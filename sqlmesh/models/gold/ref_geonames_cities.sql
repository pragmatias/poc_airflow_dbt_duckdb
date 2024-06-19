MODEL (
    name gold.ref_geonames_cities,
    kind VIEW,
    description "Geonames Cities Referential",
    tags "sel_geonames"
);

with ref_cities as (
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
  FROM silver.geonames_country
  where feature_code = 'ADM4'
    and country_code = 'FR'
),
ref_region as (
    select code
        ,name
    from silver.geonames_admin1
    where code like '%FR%'
),
ref_dept as (
    select codes
        ,name
    from silver.geonames_admin2
    where codes like '%FR%'
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
    from ref_cities rc
    left outer join ref_region rg
    on (rc.admin_code1 = rg.code)
    left outer join ref_dept rd
    on (rc.admin_code2 = rd.codes)
)

select *
from newdata
