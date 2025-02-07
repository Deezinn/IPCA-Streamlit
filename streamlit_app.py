import streamlit as st
import pandas as pd

st.write("Tabela 118 - IPCA dessazonalizado:")
st.write(pd.read_csv(r'/home/deezinn/Documentos/Python/Meus Projetos Pessoais/IPCA-Streamlit/data/Tabela 118 - IPCA dessazonalizado.csv',sep=','))
