import pandas as pd
import streamlit as st
import plotly.express as px
import os

# from utils import file_path_5
from settings import PageSettings
from settings import FormatingTable
from settings import Component

# Componentes
component = Component()

# Page config
PageSettings('Suicídios', '☠')

# Formatação
formating = FormatingTable()

st.title('Análise Detalhada dos Suicídios no Brasil de 2014 a 2018')

# DataFrame
diretorio_atual = os.path.dirname(os.path.realpath(__file__))
caminho_arquivo_csv = os.path.join(diretorio_atual, 'data.csv')

df = pd.read_csv(caminho_arquivo_csv, sep=',', encoding='latin-1')

# Colunas métricas
col_met_1, col_met_2, col_met_3, col_met_4 = st.columns(4)

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

    st.dataframe(df, use_container_width=True)

# Métricas
results = df.shape[0]
media_idades = df['idade'].mean()

contagem_assistmed = df['ASSISTMED'].value_counts()
quantidade_sim = contagem_assistmed.get('Sim', 0)
quantidade_nao = contagem_assistmed.get('Não', 0)


col_met_1.metric('Resultados', f'{results} Casos')
col_met_2.metric('Média das idades', f'{media_idades:.0f} Anos')
col_met_3.metric('Recebeu Assistência Médica', f'{quantidade_sim}')
col_met_4.metric('Não Recebeu Assistência Médica', f'{quantidade_nao}')

################### Gráficos ###################
col_chart_1, col_chart_2 = st.columns(2)

# Distribuição de Suicídios por Raça/Cor (2014-2018)
df['RACACOR'].fillna('Não Identificado', inplace=True)
count_by_race = df['RACACOR'].value_counts().reset_index()

fig_1 = px.bar(
    count_by_race,
    y = 'count',
    x = 'RACACOR',
    title = 'Distribuição de Suicídios por Raça/Cor (2014-2018)',
    labels = {'count': '', 'RACACOR': ''},
    color = 'RACACOR',
    color_discrete_sequence = px.colors.sequential.Rainbow_r,
    height=700,
    )

# Evolução Anual de Suicídios por Raça/Cor no Brasil (2014-2018)
df_grouped = df.groupby(['ano', 'RACACOR']).size().reset_index(name='QUANTIDADE')

fig_2 = px.line(
    df_grouped,
    x='ano',
    y='QUANTIDADE',
    color='RACACOR',
    markers=True,
    title='Evolução Anual de Suicídios por Raça/Cor no Brasil (2014-2018)',
    color_discrete_sequence = px.colors.sequential.Rainbow_r,
    height=700,
    )

fig_2.update_layout(
    xaxis_title='',
    yaxis_title='',
    legend_title='Legenda'
    )

# Quantidade Total de Suicídios por Mês no Brasil (2014-2018)

# Agrupando por mês e contando o número total de ocorrências
df_grouped = df.groupby('mes').size().reset_index(name='QUANTIDADE_TOTAL')

# Criando o gráfico de barras
fig_3 = px.line(
    df_grouped,
    x='mes',
    y='QUANTIDADE_TOTAL',
    markers=True,
    title='Quantidade Total de Suicídios por Mês no Brasil (2014-2018)',
    labels={'QUANTIDADE_TOTAL': 'Quantidade Total', 'mes': 'Mês'},
    height=600
    )

# Personalizando o layout do gráfico
fig_3.update_layout(
    xaxis_title='Mês',
    yaxis_title=''
    )


# Exibição
col_chart_1.plotly_chart(fig_1, use_container_width=True)
col_chart_2.plotly_chart(fig_2, use_container_width=True)
st.plotly_chart(fig_3, use_container_width=True)


check_box_municipio = component.CreateCheckBox(
    'Habilitar Municípios',
    'Selecione essa opções se dejar o filtro abaixo.',
    st
    )

municipio = component.CreateMultiSelect(1, 'Filtre um Município', df, 'CODMUNRES', False)
if check_box_municipio == True:
    df = df.query(f'CODMUNRES == @municipio')

# Agrupando por comunidade e contando o número de suicídios
df_grouped = df.groupby('CODMUNRES').size().reset_index(name='QUANTIDADE')

# Criando o gráfico de barras
fig_4 = px.bar(
    df_grouped,
    x='CODMUNRES',
    y='QUANTIDADE',
    title='Número de Suicídios por Município',
    labels={'QUANTIDADE': 'Número de Suicídios', 'CODMUNRES': 'Município'},
    height=600
    )

st.plotly_chart(fig_4, use_container_width=True)

char_col_1, char_col_2 = st.columns(2)

df['OCUP'] = df['OCUP'].replace('0', 'Não identificado')

contagem_ocup = df['OCUP'].value_counts().reset_index()
contagem_ocup.columns = ['Ocupação', 'Número de Suicídios']

top_ocup = contagem_ocup.head(10)

fig_5 = px.bar(
    top_ocup,
    x='Número de Suicídios',
    y='Ocupação',
    orientation='h',
    title='Top 10 Ocupações com Maiores Índices de Suicídio',
    labels={'Número de Suicídios': 'Número de Suicídios', 'Ocupação': 'Ocupação'},
    height=700
    )


contagem_estado = df['estado'].value_counts().reset_index()
contagem_estado.columns = ['Estado', 'Número de Suicídios']

# Criar um gráfico de barras
fig_6 = px.bar(contagem_estado, x='Estado', y='Número de Suicídios',
             title='Índices de Suicídio por Estado',
             labels={'Número de Suicídios': 'Número de Suicídios', 'Estado': 'Estado'}, height=700)


char_col_1.plotly_chart(fig_5, use_container_width=True)
char_col_2.plotly_chart(fig_6, use_container_width=True)