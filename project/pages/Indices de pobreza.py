import pandas as pd
import streamlit as st
import plotly.express as px

from utils import file_path_4
from settings import PageSettings
from settings import Component

component = Component()

# Page config
PageSettings('DashBoard', '💰')

# Colunas
col_table_1, col_table_2 = st.columns(2)

dataframe_1 = pd.read_csv(file_path_4(1)) # Anual
dataframe_2 = pd.read_csv(file_path_4(2)) # Período

def formatar_periodo(valor):
    ano = str(valor)[:4]
    mes = str(valor)[4:]
    return f"{ano}-{mes}"

# Aplicar a função à coluna "periodo"
dataframe_1['periodo'] = dataframe_1['periodo'].apply(formatar_periodo)
dataframe_2['periodo'] = dataframe_2['periodo'].apply(formatar_periodo)

filter_1 = component.CreateFilter(1, 'Ano - Tab 1', dataframe_1,'referencia')
dataframe_1 = dataframe_1.query(f'referencia == {filter_1}')

filter_2 = component.CreateFilter(2, 'Período - Tab 2', dataframe_2,'referencia')
dataframe_2 = dataframe_2.query(f'referencia == {filter_2}')

dataframe_1['referencia'] = dataframe_1['referencia'].astype('string')
col_table_1.header(("Índices de pobreza consolidado anual").upper())
col_table_1.dataframe(dataframe_1)

col_table_2.header(("Índices de pobreza consolidado").upper())
col_table_2.dataframe(dataframe_2)


col_checks_1, col_checks_2, col_checks_3 = st.columns([0.1, 0.1, 0.21])
col_charts_1, col_charts_2 = st.columns(2)

check_1 = col_checks_1.checkbox('Exibir Gráficos Anuais',
                                help='Quando ativada, esta opção exibe os gráficos dos dados anuais na tela.')
check_2 = col_checks_2.checkbox('Exibir Marcadores',
                                help='Quando ativada, esta opção adiciona marcadores aos gráficos de linhas.')
check_3 = col_checks_3.checkbox('Mostrar Percentual',
                                help='Quando ativada, esta opção exibe os percentuais sobre as barras nos gráficos de barras.')

fig_1 = px.line(
    dataframe_1,
    x='referencia',
    y='pobreza',
    markers=check_2,
    title='Pessoas em Situação de Pobreza no Brasil (2012-2022)',
    labels={'referencia': 'Ano', 'pobreza': 'Nº de Pessoas em Situação de Pobreza'}
    )

fig_2 = px.line(
    dataframe_1,
    x='referencia',
    y='extrema_pobreza',
    markers=check_2,
    title='Pessoas em Situação de Extrema Pobreza no Brasil (2012-2022)',
    labels={'referencia': 'Ano', 'extrema_pobreza': 'Nº de Pessoas em Situação de Extrema Pobreza'}
    )

fig_3 = px.line(
    dataframe_1,
    x='referencia',
    y='total',
    markers=check_2,
    title='Pessoas em Situação de Vulnerabilidade (2012-2022)',
    labels={'referencia': 'Ano', 'total': 'Nº Total de Pessoas em Situação de Vulnerabilidade'}
    )

fig_4 = px.line(
    dataframe_1,
    x='referencia',
    y='populacao_estimada',
    markers=check_2,
    title='População Estimada (2012-2022)',
    labels={'referencia': 'Ano', 'populacao_estimada': 'Estimativa populacional'},
    )

fig_5 = px.bar(
    dataframe_1,
    x='referencia',
    y='porcentagem_pobreza',
    title='Percentual de Pessoas em Situação de Pobreza (2012-2022)',
    labels={'referencia': 'Ano', 'porcentagem_pobreza': 'Percentual'},
    color_discrete_sequence=['#3498db'],
    )

fig_6 = px.bar(
    dataframe_1,
    x='referencia',
    y='porcentagem_extrema_pobreza',
    title='Percentual de Pessoas em Extrema Pobreza (2012-2022)',
    labels={'referencia': 'Ano', 'porcentagem_extrema_pobreza': 'Percentual'},
    color_discrete_sequence=['#3498db'],
    )

if check_3 == True:
    fig_5.update_traces(texttemplate='%{y:.0%}', textposition='inside')
    fig_6.update_traces(texttemplate='%{y:.0%}', textposition='inside')
    
fig_5.update_layout(
        yaxis_tickformat='.0%',
        yaxis_title='Percentual',
        xaxis_title='',
        showlegend=False,
        )

fig_6.update_layout(
        yaxis_tickformat='.0%',
        yaxis_title='Percentual',
        xaxis_title='',
        showlegend=False,
        )

if check_1 == True:
    col_charts_1.plotly_chart(fig_1)
    col_charts_2.plotly_chart(fig_2)
    col_charts_1.plotly_chart(fig_3)
    col_charts_2.plotly_chart(fig_4)
    col_charts_1.plotly_chart(fig_5)
    col_charts_2.plotly_chart(fig_6)