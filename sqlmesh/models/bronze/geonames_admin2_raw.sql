MODEL (
  name bronze.geonames_admin2_raw,
  kind SEED (
    path '$root/../data/genere/geonames/admin2Codes.csv',
    csv_settings (delimiter = ';')
  ),
  columns ( 
    codes TEXT,
    name TEXT,
    name_ascii TEXT,
    geonameid TEXT
  ),
  grain (
    geonameid
  )
)