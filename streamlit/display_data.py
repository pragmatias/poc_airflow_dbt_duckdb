import streamlit as st
import pandas as pd 
import duckdb as dd 


path_db = "data/database"

con = dd.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = True)


df = con.sql("select * from poc_gold.ref_cities where zip_code = '91440' ").df()

con.close()

st.write(""" Map """)
#st.table(df)

st.map(data=df, latitude="latitude", longitude="longitude", color=None, size=None, zoom=5, use_container_width=True)




