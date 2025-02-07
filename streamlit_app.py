import streamlit as st
import pandas as pd
import os

st.write("Tabela 118 - IPCA dessazonalizado:")

file_path = 'data/Tabela 118 - IPCA dessazonalizado.csv'

if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path, sep=',', encoding='utf-8', skiprows=1)
        st.write(df)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
else:
    st.error("Arquivo não encontrado! Verifique o caminho e tente novamente.")
