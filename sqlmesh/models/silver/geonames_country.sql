MODEL (
    name silver.geonames_country,
    kind FULL,
    column_descriptions (
        geonameid = 'General ID',
        name = "Name of the location",
        modification_date = "last modification"
    ),
    description "Information about the entity location in a country",
    tags "sel_geonames",
    audits (assert_positive_geonameid)
);


with newdata as (
  select geonameid::int
        ,name
        ,latitude
        ,longitude
        ,feature_code
        ,country_code
        ,admin1_code
        ,admin2_code
        ,admin3_code
        ,admin4_code
        ,population::int
        ,elevation
        ,dem
        ,timezone
        ,modification_date ::date
  from bronze.geonames_country_raw
)

select *
from newdata