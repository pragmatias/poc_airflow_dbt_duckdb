import streamlit as st
import pandas as pd 
import duckdb as dd 
import pathlib

file_dir  = pathlib.Path(__file__).parent.parent.resolve()
data_dir = f"{file_dir}/data"

# Path to database
path_db = f"{data_dir}/database"


con = dd.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = True)


df = con.sql("select * from prd_gold.ref_snap_random").df()

con.close()

st.write(f"Table : prd_gold.ref_snap_random")
st.table(df)




