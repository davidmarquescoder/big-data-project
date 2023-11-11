import streamlit as st
import pandas as pd

from utils import file_path
from settings import PageSettings


PageSettings('DashBoard', ':bar_chart:')

dataframe = pd.read_csv(file_path)
dataframe['AnoCalendario'] = dataframe['AnoCalendario'].astype('string')

st.dataframe(dataframe)