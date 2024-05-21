import duckdb

# Default schema to store imported data
import_schema = "raw"
# Path to database
path_db = "data/database"
# Path to source data
path_src = "data/source"

# Connection
con = duckdb.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = False)

# Default schema to store imported data
import_schema = "raw"

# init Schema
sql_init_schema = f"CREATE SCHEMA IF NOT EXISTS {import_schema};"

con.execute(sql_init_schema)

# Impotr data
sql_init_cities = f"drop table if exists {import_schema}.cities ;"
sql_load_cities = f"""
    create table if not exists {import_schema}.cities as 
    select distinct cities.* 
    from (
        select unnest(cities) as cities 
        from read_json('{path_src}/cities.json'
                        ,format="auto"
                        ,auto_detect="true"
                        ,maximum_object_size="180000000")) ;
    """

con.execute(sql_init_cities)
con.execute(sql_load_cities)

con.commit
