import duckdb
import pathlib
import random

file_dir  = pathlib.Path(__file__).parent.parent.resolve()
data_dir = f"{file_dir}/data"



data_template = [
    {"id" : 1,"name": "Bob","value": 0,"date" : "2021-01-01"},
    {"id" : 2,"name": "Geolie","value": 0,"date" : "2021-01-01"},
    {"id" : 3,"name": "Marly","value": 0,"date" : "2021-01-01"},
    {"id" : 4,"name": "Charle","value": 0,"date" : "2021-01-01"},
    {"id" : 5,"name": "Ickey","value": 0,"date" : "2021-01-01"},
]


# Default schema to store imported data
import_schema = "raw"
# Path to database
path_db = f"{data_dir}/database"

# Connection
con = duckdb.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = False)

# init Schema
sql_init_schema = f"CREATE SCHEMA IF NOT EXISTS {import_schema};"

con.execute(sql_init_schema)

# CREATE TABLE IF NOT EXISTS
sql_init_table = f"create table if not exists {import_schema}.snap_random (id INTEGER, name VARCHAR, value INTEGER, date Date) ;"
con.execute(sql_init_table)

## check if the table is empty
count, = con.sql(f"SELECT count(*) as nbr from {import_schema}.snap_random").fetchall()[0]

if (count < 1) :
    # init the tbl
    for row in data_template:
        con.sql(f"INSERT INTO {import_schema}.snap_random VALUES ({row['id']},'{row['name']}',{row['value']},'{row['date']}')")
else:
    choice = random.randint(1,200)
    if (choice > 20) :
        # modif the table
        index = random.randint(1,count)
        newVal = random.randint(1,99999)
        newInterval = random.randint(1,3)
        con.sql(f"UPDATE {import_schema}.snap_random SET value = {newVal}, date = date_add(date,interval {newInterval} month) WHERE id = {index}")
    else:
        # clean the table
        con.execute(f"TRUNCATE TABLE {import_schema}.snap_random")

    con.table(f"{import_schema}.snap_random").show()


con.close()
