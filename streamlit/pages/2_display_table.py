import streamlit as st
import datetime as dt
import pandas as pd
from utils import db


con = db.connect_db()


df = con.sql("select id,name,value,valid_from,valid_to from prd_gold.ref_snap_random").df()
df['valid_from'] = pd.to_datetime(df['valid_from'],format="%Y-%m-%d")
df['valid_to'] = pd.to_datetime(df['valid_to'],format="%Y-%m-%d")
con.close()


max_period = df["valid_to"].max()
min_period = df["valid_from"].min()
current_date = dt.datetime.strptime(dt.date.strftime(dt.date.today(),"%Y-%m-%d"),"%Y-%m-%d")
list_name = df["name"].unique()


st.title(f"Table : ref_snap_random")
st.divider()

st.header("User Selection")
filter_date = st.date_input("Select a date :", max_period
                            ,min_value=df["valid_from"].min()
                            ,max_value=df["valid_to"].max()
                            ,format="YYYY-MM-DD")

selects_name = st.multiselect("Select names :"
                               ,options=list_name
                               ,default=list_name
                               ,placeholder= "Select a name"
)
filter_datetime = dt.datetime.strptime(dt.datetime.strftime(filter_date,"%Y-%m-%d"),"%Y-%m-%d")

st.text("Result : ")
st.table(df[(df["valid_to"] >= filter_datetime) 
            & (df["valid_from"] <= filter_datetime) 
            & (df["name"].isin(selects_name))])


st.divider()

st.header("Current valid version")
st.table(df[df["valid_to"] == max_period])

st.divider()

st.header("Historical version")
st.table(df)



