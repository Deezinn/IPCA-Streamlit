import streamlit as st
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('/home/deezinn/Documentos/Python/Meus Projetos Pessoais/IPCA-Streamlit/data/Tabela 118 - IPCA dessazonalizado.csv', sep= ',')

# Exibindo o DataFrame no Streamlit
st.write("### Tabela 118 - IPCA dessazonalizado:")
st.dataframe(df)  # Exibe o dataframe corretamente

# Testando a saída no terminal (apenas para debug)

