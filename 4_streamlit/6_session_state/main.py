"""
- A session is the single instance of viewing an app e.g browser tab example
- refreshing resets the session state and starts a new session
- A session state is a dictionary like interface that you can use to save information preserved between various script reruns.
"""

import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

"""
Differences between session state and caching
- caching associates sttored values to specific functions or inputs
- cached values are available to all users across all sessions
- session state associates stored values to keys(strings.)
- session state are only available in the single session it was saved
"""

import pandas as pd
import numpy as np

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)