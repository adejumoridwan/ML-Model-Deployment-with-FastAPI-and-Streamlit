"""
Caching allows you to save the output of a function without streamlit running
it over again
- st.cache_data - return data, allows you to cache dataframes, numpy array, csv, querying an api and serializable data objects
- st.cache_resource - return unserializable objects, such as models and data connections
"""

import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Simulating loading data from a remote source or time-consuming process
    data = {
        'Names': ["Henry", "Jamal", "William", "Dave"],
        'Weight': [40, 50, 70, 40]
    }
    return pd.DataFrame(data)

df = load_data()
df