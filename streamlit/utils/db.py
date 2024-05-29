import duckdb as dd 
import pathlib

file_dir  = pathlib.Path(__file__).parent.parent.parent.resolve()
data_dir = f"{file_dir}/data"

# Path to database
path_db = f"{data_dir}/database"

def connect_db() :
    return dd.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = True)