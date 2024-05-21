import streamlit as st
import pandas as pd 
import duckdb as dd 


path_db = "data/database"

con = dd.connect(database = f"{path_db}/DuckyWH.duckdb", read_only = False)


df = con.sql("select * from poc_silver.cities").df()


st.write(""" hello dude """)
#st.table(df)

st.map(data=df, latitude="latitude", longitude="longitude", color=None, size=None, zoom=5, use_container_width=True)




