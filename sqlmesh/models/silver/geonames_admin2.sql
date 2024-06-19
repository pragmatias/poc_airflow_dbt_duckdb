MODEL (
    name silver.geonames_admin2,
    kind FULL,
    column_descriptions (
        geonameid = 'General ID',
        name = "Name of the location ADM2"
    ),
    description "Administration Level 2 Referential",
    tags "sel_geonames",
    audits (
      assert_positive_geonameid,
      assert_notnull_codes(column := codes)
    )
);


with newdata as (
  select codes,
    name,
    name_ascii,
    geonameid::int
  from bronze.geonames_admin2_raw
)

select *
from newdata