MODEL (
  name bronze.geonames_country_raw,
  kind SEED (
    path '$root/../data/genere/geonames/FR.csv',
    csv_settings (delimiter = ';')
  ),
  columns (
    geonameid TEXT,
    name TEXT,
    ascii_name TEXT,
    alternate_names TEXT,
    latitude TEXT,
    longitude TEXT,
    feature_class TEXT,
    feature_code TEXT,
    country_code TEXT,
    cc2 TEXT,
    admin1_code TEXT,
    admin2_code TEXT,
    admin3_code TEXT,
    admin4_code TEXT,
    population TEXT,
    elevation TEXT,
    dem TEXT,
    timezone TEXT,
    modification_date DATE
  ),
  grain (
    geonameid
  )
)