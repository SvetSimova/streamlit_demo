import streamlit as st
import pandas as pd
import numpy as np


st.write("# My Cool Chart")
# x = st.text_input("Favourite Movie?")
# st.write(f"Your favourite movie is: {x}")

# data = pd.read_csv("movies.csv")
# st.write(data)

st.link_button("Profile", url="/profile?id=1234")
st.link_button("Dashboard", url="/dashboard?id=1234")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.bar_chart(chart_data)
st.line_chart(chart_data)