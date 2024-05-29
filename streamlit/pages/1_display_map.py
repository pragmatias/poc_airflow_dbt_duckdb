import streamlit as st
import pydeck as pdk
from utils import db

con = db.connect_db()


df = con.sql("""
        select *
             ,cast((population/100) as int) as size
        from prd_gold.ref_geonames_cities 
        where population >= 0
             and  longitude > -7.480942
             and  longitude < 15
             and  latitude < 53
             and  latitude > 37
        """).df()
con.close()

list_department = df['dept_code'].unique()
pop_min = df['population'].min()
pop_max = df['population'].max()
sample_frac = 0.01


st.title(""" Population by cities """)

st.divider()

st.header("User Selection")
# filtre on population and department ?

col1_1, col1_2, col1_3 = st.columns(3)

input_radius = col1_1.number_input("Change radius :", value=5000, placeholder="Type a number...")
input_elevation_scale = col1_2.number_input("Change elevation scale :", value=10, placeholder="Type a number...")
input_elevation_range_max = col1_3.number_input("Change elevation range :", value=5000, placeholder="Type a number...")
input_pop_min = st.slider("Select population min :", value=int(pop_min), min_value=int(pop_min),max_value=int(pop_max),step=1000)
input_dept = st.multiselect("Select department :",list_department)

df_filter = df
if input_dept :
    df_filter = df[(df["population"] > input_pop_min) & (df["dept_code"].isin(input_dept))]
else :
    df_filter = df[(df["population"] > input_pop_min)]

df_slim = df_filter[["population","longitude","latitude","size"]]

st.divider()

st.header("Map (with PyDeck)")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=48.7533,
        longitude=2.2967,
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df_slim,
           get_position='[longitude, latitude]',
           radius=input_radius,
           elevation_scale=input_elevation_scale,
           elevation_range=[0, input_elevation_range_max],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df_slim,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=500,
        ),
    ],
    tooltip={
        'html': '<b>Elevation :</b> {elevationValue}',
        'style': {
            'color': 'white'
        }
    }
))

st.divider()

st.header("Map (basics)")

st.map(data=df_slim
       , latitude="latitude"
       , longitude="longitude"
       , color=None
       , size="size"
       , zoom=4
       , use_container_width=True)


st.divider()

st.header("Sample Data")
st.table(df_filter.sample(frac=sample_frac))
