import streamlit as st
import pandas as pd

from utils import file_path_3
from settings import PageSettings
from settings import Component


PageSettings('DashBoard', ':bar_chart:')

dataframe = pd.read_csv(file_path_3())

# dataframe['AnoCalendario'] = dataframe['AnoCalendario'].astype('string')
# dataframe['DataArquivamento'] = pd.to_datetime(dataframe['DataArquivamento'])
# dataframe['DataAbertura'] = pd.to_datetime(dataframe['DataAbertura'])

# component = Component()
# component.CreateFilter(1, 'UF', dataframe,'UF')
# # component.CreateFilter(2, 'Empresa', dataframe,'strNomeFantasia')
# dataframe = component.ReturnDataframe()

st.dataframe(dataframe)