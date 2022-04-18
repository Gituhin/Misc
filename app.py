import streamlit as st
import pandas as pd

st.header("This is a test app deployed using streamlit-io.")
st.subheader("To display the contents of uploaded files.")
if st.button("Click me"):
    st.success("Thanks for clicking")

st.text("That's all, © Tuhin 2022")