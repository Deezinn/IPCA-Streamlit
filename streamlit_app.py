import streamlit as st
import pandas as pd
import os

# Caminho do arquivo CSV
file_path = "/home/deezinn/Documentos/Python/Meus Projetos Pessoais/IPCA-Streamlit/data/tabela_118_ipca.csv"

# Verifica se o arquivo existe antes de tentar carregar
if os.path.exists(file_path):
    df = pd.read_csv(file_path, sep=",", encoding="utf-8")

    st.title("Tabela 118 - IPCA Dessazonalizado")
    st.write("### DataFrame carregado com sucesso:")
    st.dataframe(df)  # Exibe o DataFrame no Streamlit
else:
    st.error("❌ ERRO: Arquivo CSV não encontrado. Verifique o caminho do arquivo.")

st.write("✅ Aplicação Streamlit rodando corretamente!")
