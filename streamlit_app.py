import streamlit as st
import pandas as pd
import os


file_path = "data/tabela_118_ipca.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path, sep=",", encoding="utf-8")

    st.title("Tabela 118 - IPCA Dessazonalizado")
    st.write("### DataFrame carregado com sucesso:")
    st.dataframe(df)  
else:
    st.error(f"❌ ERRO: Arquivo CSV não encontrado em {file_path}. Verifique o caminho do arquivo.")

st.write("✅ Aplicação Streamlit rodando corretamente!")
