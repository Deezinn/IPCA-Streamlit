import streamlit as st
import pandas as pd
import os

st.write("Tabela 118 - IPCA dessazonalizado:")

# Caminho do arquivo
file_path = r'data/Tabela 118 - IPCA dessazonalizado.csv'

# Verificar se o arquivo existe antes de carregar
if os.path.exists(file_path):
    st.write(f"Carregando arquivo de: {file_path}")  # Mostra o caminho
    try:
        df = pd.read_csv(file_path, sep=',', encoding='utf-8', skiprows=1)
        st.write("### DataFrame carregado:")
        st.dataframe(df)  # Exibe o DataFrame corretamente
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
else:
    st.error(f"Arquivo não encontrado no caminho: {file_path}")

st.write('teste')
