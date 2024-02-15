"""
Streamlit makes it easy to organize widgets in a left panel sidebar with 
st.sidebar()
"""

import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Where do you stay?',
    ('India', 'USA', 'Nigeria','China')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'What is your score range?',
    0, 100, (25, 75)
)

"""
- st.columns() lets you place widgets side by side
- st.expander() lets you conserve space by hiding away large content
"""

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Submit')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Superhero',
        ("Superman", "Batman", "Iron Man", "Black Panther"))
    st.write(f"{chosen} is my favourite super hero")

