"""
- magic and st.write is used for displaying text and tables
- magic command allows you to display anthing without explicitly stating any command
- Just put in the object you want to show on its own line of code and it will display
- st.write renders anything from table, plots to interactive charts.
"""
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'Name': ["Julia", "Johnny", "Kate", "Omar"],
  'Scores': [10, 20, 30, 40]
})

df
st.table(df)
st.dataframe(df)

"""
When not to use magic and st.write()
- If you want to return an object that can be modified by adding data 
to it or replacing it
- If you want to pass additional arguments to customize it's behaviour
- st.table() - static table
- st.dataframe() - interactive table
"""
# Styling


st.dataframe(df.style.highlight_max(axis=0))

#Drawing Charts and Maps

# line charts
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(10, 2),
     columns=['x', 'y'])

st.line_chart(chart_data)
chart_data

#maps
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)