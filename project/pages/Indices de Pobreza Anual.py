import pandas as pd
import streamlit as st
import plotly.express as px

from utils import file_path_4
from settings import PageSettings
from settings import Component

component = Component()

# Page config
PageSettings('DashBoard', '💰')

dataframe_1 = pd.read_csv(file_path_4(1)) # Anual


def formatar_periodo(valor):
    ano = str(valor)[:4]
    mes = str(valor)[4:]
    return f"{ano}-{mes}"

# Aplicar a função à coluna "periodo"
dataframe_1['periodo'] = dataframe_1['periodo'].apply(formatar_periodo)

filter_1 = component.CreateFilter(1, 'Ano - Tab 1', dataframe_1,'referencia')
dataframe_1 = dataframe_1.query(f'referencia == {filter_1}')

dataframe_1['referencia'] = dataframe_1['referencia'].astype('string')
st.header(("Índices de pobreza consolidado anual").upper())
st.dataframe(dataframe_1)

# Colunas
col_checks_1, col_checks_2, col_checks_3 = st.columns([0.1, 0.1, 0.21])
col_charts_1, col_charts_2 = st.columns(2)
col_select_1, col_select_2 = st.columns(2)
col_charts_pizza_1, col_charts_pizza_2, col_charts_pizza_3 = st.columns([1, 1, 1])


check_1 = col_checks_1.checkbox('Exibir Gráficos Anuais',
                                help='Quando ativada, esta opção exibe os gráficos dos dados anuais na tela.')
check_2 = col_checks_2.checkbox('Exibir Marcadores',
                                help='Quando ativada, esta opção adiciona marcadores aos gráficos de linhas.')

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

fig_5 = px.line(
    dataframe_1,
    x='referencia',
    y='porcentagem_pobreza',
    title='Percentual de Pessoas em Situação de Pobreza (2012-2022)',
    labels={'referencia': 'Ano', 'porcentagem_pobreza': 'Percentual'},
    color_discrete_sequence=['#3498db'],
    markers=check_2,
    )
fig_5.update_layout(
        yaxis_tickformat='.0%',
        yaxis_title='Percentual',
        xaxis_title='',
        showlegend=False,
        )

fig_6 = px.line(
    dataframe_1,
    x='referencia',
    y='porcentagem_extrema_pobreza',
    title='Percentual de Pessoas em Extrema Pobreza (2012-2022)',
    labels={'referencia': 'Ano', 'porcentagem_extrema_pobreza': 'Percentual'},
    color_discrete_sequence=['#3498db'],
    markers=check_2,
    )
fig_6.update_layout(
        yaxis_tickformat='.0%',
        yaxis_title='Percentual',
        xaxis_title='',
        showlegend=False,
        )

dados_periodo = dataframe_1[(dataframe_1['referencia'] >= '2012') & (dataframe_1['referencia'] <= '2022')]

media_pobreza = dados_periodo['pobreza'].mean()

media_extrema_pobreza = dados_periodo['extrema_pobreza'].mean()

media_populacao_estimada = dados_periodo['populacao_estimada'].mean()

dados_fig_8 = pd.DataFrame({
    'Categoria': ['Pobreza', 'Extrema Pobreza', 'População Estimada'],
    'Valor': [media_pobreza, media_extrema_pobreza, media_populacao_estimada]
})

fig_8 = px.pie(
    dados_fig_8, names='Categoria',
    values='Valor',
    title='Média de Atingimento da Pobreza no Brasil (2012-2022)',
    color_discrete_sequence = px.colors.sequential.Bluyl_r,
    )

total = dados_periodo['total'].mean()

dados_fig_9 = pd.DataFrame({
    'Categoria': ['Situação de vulnerabilidade', 'População Estimada'],
    'Valor': [total, media_populacao_estimada]
})

fig_9 = px.pie(
    dados_fig_9, names='Categoria',
    values='Valor',
    title='Média de Pessoas em situação de vulnerabilidade no Brasil (2012-2022)',
    color_discrete_sequence = px.colors.sequential.Bluyl_r,
    )

if check_1 == True:
    columns = ['pobreza', 'extrema_pobreza', 'total']
    select_1 = col_select_1.selectbox('Selecione o Ano', dataframe_1['referencia'])
    select_2 = col_select_2.selectbox('Selecione a Coluna', columns)

    dados_periodo_1 = dataframe_1[(dataframe_1['referencia'] == select_1)]

    option = dados_periodo_1[select_2].mean()
    populacao_estimada = dados_periodo_1['populacao_estimada'].mean()

    dados_fig_10 = pd.DataFrame({
        'Categoria': [f'{select_2}', 'População Estimada'],
        'Valor': [option, populacao_estimada]
    })

    fig_10 = px.pie(
        dados_fig_10,
        names='Categoria',
        values='Valor',
        title='Gráfico Dinâmico por Ano e Categoria',
        color_discrete_sequence = px.colors.sequential.Bluyl_r,
        )

if check_1 == True:
    col_charts_1.plotly_chart(fig_1)
    col_charts_2.plotly_chart(fig_2)
    col_charts_1.plotly_chart(fig_3)
    col_charts_2.plotly_chart(fig_4)
    col_charts_1.plotly_chart(fig_5)
    col_charts_2.plotly_chart(fig_6)
    col_charts_pizza_1.plotly_chart(fig_9, use_container_width=True)
    col_charts_pizza_2.plotly_chart(fig_8, use_container_width=True)
    col_charts_pizza_3.plotly_chart(fig_10, use_container_width=True)