import streamlit as st


st.write("Hi Student!")

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
st.header(f"This page has run {st.session_state.counter} times")
st.button("Run it again")

import pandas as pd
import numpy as np

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20,2),columns=["x","y"])

st.header("Choose a datapoint colour")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x",y="y",color=color)