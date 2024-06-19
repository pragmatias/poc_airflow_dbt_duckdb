MODEL (
    name silver.geonames_admin1,
    kind FULL,
    column_descriptions (
        geonameid = 'General ID',
        name = "Name of the location ADM1"
    ),
    description "Administration Level 1 Referential",
    tags "sel_geonames",
    audits (
      assert_positive_geonameid,
      assert_notnull_codes(column := code)
    )
);


with newdata as (
  select code,
    name,
    name_ascii,
    geonameid::int
  from bronze.geonames_admin1_raw
)

select *
from newdata