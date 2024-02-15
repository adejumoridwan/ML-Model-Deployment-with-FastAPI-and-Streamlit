import streamlit as st

y = st.slider("y", value=5)
st.write(y, "addition is", y + y)

st.text_input("Your name",key="name")

st.session_state.name

import numpy as np
import pandas as pd

if st.checkbox("Show Data"):
    chart = pd.DataFrame(
        np.random.randn(20,3),
        columns=["Weight","Height","BMI"]
    )
    chart

df = pd.DataFrame({
    "Names": ["Henry","Jamal","William","Dave"],
    "Weight": [40,50,70,40]
})

option = st.selectbox(
    "Select a name",
    df["Names"]
)

f"{option}'s weight is {df.loc[df["Names"] == option, "Weight"].values[0]}"