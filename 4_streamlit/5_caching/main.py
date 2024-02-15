import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = {
        "Names":["Henry","Jamal","William","Dave"],
        "weight": [40, 50, 60, 70]
    }
    return pd.DataFrame(data)

df = load_data()
df