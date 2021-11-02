import streamlit as st

st.write("Hello world")
number_input = st.numeric_input("pick a value for x")

result = number_input + 100
st.write("The result is:")
st.write(result)
st.balloons()

