import duckdb
import pathlib
import os

file_dir  = pathlib.Path(__file__).parent.parent.resolve()
data_dir = f"{file_dir}/data"


# Default schema to store imported data
import_schema = "raw"
# Path to database
path_db = f"{data_dir}/database"
# Path to generated data
path_gen = f"{data_dir}/genere/geonames"

os.makedirs(name=path_db,exist_ok=True)

# Connection
con = duckdb.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = False)

file_FR = "FR.csv"
file_admin1 = "admin1CodesASCII.csv"
file_admin2 = "admin2Codes.csv"
list_files = [("geonames_country",file_FR)
              ,("geonames_admin1",file_admin1)
              ,("geonames_admin2",file_admin2)]

# Import CSV files into DuckDB
for (tbl,file) in list_files:
    sql_clean = f"drop table if exists {import_schema}.{tbl} ;"
    sql_import = f"""
        create table if not exists {import_schema}.{tbl} as 
        select * 
        from read_csv('{path_gen}/{file}'
                        ,delim = ';'
                        ,header = true) ;
    """
    con.execute(sql_clean)
    con.execute(sql_import)

con.close()
