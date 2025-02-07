import streamlit as st
import pandas as pd

st.write("Tabela 118 - IPCA dessazonalizado:")
try:

    st.write(pd.read_csv(r'/home/deezinn/Documentos/Python/Meus Projetos Pessoais/IPCA-Streamlit/data/Tabela 118 - IPCA dessazonalizado.csv', sep=',', encoding='utf-8', skiprows=1))

except Exception as e:
    print('erro')
