import streamlit as st
import pandas as pd

df = pd.DataFrame(
    {"Name": ["Julia", "Johnny", "Kate", "Omar"], 
     "Scores": [10, 20, 30, 40]}
)

df
st.table(df)
st.dataframe(df.style.highlight_max(axis=0))

import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(10,2),
    columns=["x","y"]
)

st.bar_chart(chart_data)
chart_data

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns = ["lat","lon"]
)
st.map(map_data)
