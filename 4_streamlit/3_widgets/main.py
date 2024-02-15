"""
These are items you can use to manipulate your data
"""

import streamlit as st
y = st.slider('y')  # 👈 this is a widget
st.write(y, 'addition is', y + y)

# widget can also be accessed by key
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

## Using Checkboxes

import numpy as np
import pandas as pd

if st.checkbox('Show Data'):
    chart = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['Weight', 'Height', 'BMI'])

    chart

df = pd.DataFrame({
    'Names': ["Henry", "Jamal", "William", "Dave"],
    'Weight': [40, 50, 70, 40]
    })

option = st.selectbox(
    'Select a name',
     df['Names'])

f"{option}'s weight is {df.loc[df['Names'] == 'Henry', 'Weight'].values[0]}"