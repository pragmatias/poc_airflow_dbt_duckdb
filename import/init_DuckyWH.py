import duckdb
import pathlib
import os

file_dir  = pathlib.Path(__file__).parent.parent.resolve()
data_dir = f"{file_dir}/data"


# Default schema to store imported data
import_schema = "raw"
# Path to database
path_db = f"{data_dir}/database"
# Path to source data
path_src = f"{data_dir}/source"
# Path to generated data
path_gen = f"{data_dir}/genere"

os.makedirs(name=path_db,exist_ok=True)

# Connection
con = duckdb.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = False)

# init Schema
sql_init_schema = f"CREATE SCHEMA IF NOT EXISTS {import_schema};"

con.execute(sql_init_schema)

# Import data cities
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

# Import data communes
sql_init_communes = f"drop table if exists {import_schema}.communes ;"
sql_load_communes = f"""
    create table if not exists {import_schema}.communes as 
    select distinct * 
    from read_json('{path_gen}/cities/communes.json'
                    ,format="array"
                    ,auto_detect="true") ;
    """

con.execute(sql_init_communes)
con.execute(sql_load_communes)


con.close()
