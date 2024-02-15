import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "Where do you stay?",
    ("India","USA","Nigeria","China")
)

add_slider = st.sidebar.slider(
    "What is your score range?",
    0,100,(25,75)
)

left_column, right_column = st.columns(2)

left_column.button("Submit")

with right_column:
    chosen = st.radio(
        "Superhero",
        ("Superman","Batman","Iron Man","Black Panther")
    )
    st.write(f"{chosen} is my favourite super hero")