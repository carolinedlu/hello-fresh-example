import streamlit as st

st.write("Hello world")
number = st.number_input("pick a value for x")

result = number + 100
st.write("The result is:")
st.write(result)
st.balloons()

