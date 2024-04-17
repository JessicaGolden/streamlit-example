import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime
import scripts
import hmac

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

"""
# Welcome to the analytics dashboard!
"""
people = st.multiselect(
    'Who would you like displayed?',
    ['Antonio', 'Alejandra', 'Nima', 'Luca'],
    ['Antonio', 'Alejandra'])

st.write('You selected:', people)


timestamps = st.slider(
    "Schedule your appointment:",
    value=(datetime(2024, 3, 29, 0, 0), scripts.get_date()),
    format="MM/DD/YY"), #scripts.get_date())
st.write("You selected the dates:", timestamps)

st.write(scripts.analysis_streamlit(timestamps[0][0], timestamps[0][1], people))

'''
Examples of what can be done, I need this to be migrated to the awear-data repository before being able to create the plots and give figures
'''


num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
