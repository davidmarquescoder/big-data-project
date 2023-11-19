import pandas as pd
import streamlit as st

from utils import file_path_4
from settings import Component

component = Component()


dataframe_2 = pd.read_csv(file_path_4(2)) # Período

def formatar_periodo(valor):
    ano = str(valor)[:4]
    mes = str(valor)[4:]
    return f"{ano}-{mes}"

dataframe_2['periodo'] = dataframe_2['periodo'].apply(formatar_periodo)

filter_2 = component.CreateFilter(2, 'Período - Tab 2', dataframe_2,'referencia')
dataframe_2 = dataframe_2.query(f'referencia == {filter_2}')

st.header(("Índices de pobreza consolidado").upper())
st.dataframe(dataframe_2)