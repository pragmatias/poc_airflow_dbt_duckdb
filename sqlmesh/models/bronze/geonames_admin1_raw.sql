MODEL (
  name bronze.geonames_admin1_raw,
  kind SEED (
    path '$root/../data/genere/geonames/admin1CodesASCII.csv',
    csv_settings (delimiter = ';')
  ),
  columns (
    code TEXT,
    name TEXT,
    name_ascii TEXT,
    geonameid TEXT
  ),
  grain (
    geonameid
  )
)