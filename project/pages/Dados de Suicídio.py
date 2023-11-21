import pandas as pd
import streamlit as st
import plotly.express as px

from utils import file_path_5
from settings import PageSettings
from settings import FormatingTable
from settings import Component

# Componentes
component = Component()

# Page config
PageSettings('Suicídios', '☠')

# Formatação
formating = FormatingTable()

# DataFrame
df = pd.read_csv(file_path_5(), sep=',', encoding='latin-1')

# Filtros Globais
col_check_1, col_check_2, col_check_3, col_check_4 = st.columns(4)

check_box_1 = component.CreateCheckBox(
    'Habilitar Filtros',
    'Selecione essa opções se dejar utilizar todos os filtros abaixo.',
    col_check_1
    )

check_box_2 = component.CreateCheckBox(
    'Habilitar Ano',
    'Selecione essa opções se dejar utilizar somente o filtro de ano.',
    col_check_2
    )

check_box_3 = component.CreateCheckBox(
    'Habilitar Estado',
    'Selecione essa opções se dejar utilizar somente o filtro de estado.',
    col_check_3
    )

check_box_4 = component.CreateCheckBox(
    'Habilitar Sexo',
    'Selecione essa opções se dejar utilizar somente o filtro de sexo.',
    col_check_4
    )

col_filter_1, col_filter_2, col_filter_3 = st.columns(3)
select_box_1 = component.CreateSelectBox('Selecione o Ano', df, 'ano', col_filter_1)
select_box_2 = component.CreateSelectBox('Selecione o Estado', df, 'estado', col_filter_2)
select_box_3 = component.CreateSelectBox('Selecione o Sexo', df, 'SEXO', col_filter_3)

if check_box_1 == True:
    df = df.query(
        f'ano == @select_box_1 and estado == @select_box_2 and SEXO == @select_box_3'
        )
if check_box_2 == True:
    df = df.query(f'ano == @select_box_1')
if check_box_3 == True:
    df = df.query(f'estado == @select_box_2')
if check_box_4 == True:
    df = df.query(f'SEXO == @select_box_3')


# Mostrando tabela na tela ou ocultando
col_itens_1, col_itens_2 = st.columns([0.022,0.2])
check_box_ocult = component.CreateCheckBox(
    'Ocultar tabela',
    'Selecione essa opções se dejar ocultar a tabela',
    col_itens_1
    )

col_itens_2.markdown('[Descrição da Tabela](http://localhost:8080/Descrição_Tabela_de_Suicídios)')

if check_box_ocult == False:
    # Formatando a coluna "Ano" da tabela
    formating.YearToString(df, 'ano')

    st.title(
        'Uma Análise Detalhada dos Suicídios no Brasil de 2014 a 2018'
        )
    st.dataframe(df, use_container_width=True)

################### Gráficos ###################
df['RACACOR'].fillna('Não Identificado', inplace=True)
count_by_race = df['RACACOR'].value_counts().reset_index()

fig = px.bar(
    count_by_race,
    y = 'count',
    x = 'RACACOR',
    title = 'Distribuição de Suicídios por Raça/Cor (2014-2018)',
    labels = {'count': '', 'RACACOR': ''},
    color = 'RACACOR',
    color_discrete_sequence = px.colors.sequential.Peach_r,
    )

st.plotly_chart(fig)