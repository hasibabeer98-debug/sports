import streamlit as st
import pandas as pd

st.title("People intrested in sports")
file = st.file_uploader("upload your csv file", type=["csv"])

if file:
   df= pd.read_csv(file)
   st.subheader("data preview")
   st.dataframe(df)
   
