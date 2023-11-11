import streamlit as st
import pandas as pd

from utils import file_path_3
from settings import PageSettings
from settings import Component
from settings import FormatingTable


PageSettings('DashBoard', ':bar_chart:')

formating_table = FormatingTable()
component = Component()

dataframe_fixo = pd.read_csv(file_path_3())
formating_table.RemoveSpacesColumn(dataframe_fixo)

dataframe = pd.read_csv(file_path_3())
formating_table.RemoveSpacesColumn(dataframe)
dataframe = formating_table.SortingBy(dataframe, 'Country','Year')

filter_1 = component.CreateFilter(1, 'Ano', dataframe,'Year')
filter_2 = component.CreateFilter(2, 'País', dataframe,'Country')
dataframe = dataframe.query(f'Year == {filter_1} and Country == {filter_2}')


pais_selecionado = st.selectbox('Selecione um país', dataframe_fixo['Country'].unique())
col1, col2 = st.columns(2)

dados_pais = dataframe_fixo[dataframe_fixo['Country'] == pais_selecionado]

populacao_1970 = dados_pais[dados_pais['Year'] == 1970]['Population'].values[0]
populacao_2021 = dados_pais[dados_pais['Year'] == 2021]['Population'].values[0]

aumento_populacional = populacao_2021 - populacao_1970
percentual_aumento = ((populacao_2021 - populacao_1970) / populacao_1970) * 100

col2.metric(f'Aumento populacional - {pais_selecionado}', f'{aumento_populacional:,}',delta=f'{percentual_aumento:.2f} %', help=f'Aumento populacional de 1970 a 2021 - {pais_selecionado}')

num_linhas = dataframe.shape[0]
col1.metric('Resultados', num_linhas)

formating_table.YearToString(dataframe, 'Year')

st.dataframe(dataframe)