import streamlit as st
import pandas as pd
import os


file_path = "data/tabela_118_ipca.csv"

df = pd.read_csv(file_path, sep=",", encoding="utf-8")

st.title("Tabela 118 - IPCA Dessazonalizado")
st.dataframe(df)

st.write('andre luiz souza nascimento')
