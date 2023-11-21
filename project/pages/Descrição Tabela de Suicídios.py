import streamlit as st
from settings import PageSettings

# Page config
PageSettings('DashBoard', '📘')

st.markdown('''
### `estado`
- **Descrição:** UF (Unidade da Federação) onde o óbito ocorreu.
- **Exemplo:** SP (São Paulo), RJ (Rio de Janeiro), MG (Minas Gerais), etc.

### `ano`
- **Descrição:** Ano em que o óbito ocorreu.
- **Exemplo:** 2021, 2022, 2023, etc.

### `CIRCOBITO`
- **Descrição:** Circunstância do óbito.
- **Valores:**
  - 1: Acidente
  - 2: Suicídio
  - 3: Homicídio
  - 4: Outro
  - 0, 5, 6, 7, 8, 9: NA (Não especificado)

### `DTOBITO`
- **Descrição:** Data do óbito.
- **Formato:** AAAA-MM-DD (Ano-Mês-Dia)

### `DTNASC`
- **Descrição:** Data de nascimento do falecido.
- **Formato:** AAAA-MM-DD (Ano-Mês-Dia)

### `SEXO`
- **Descrição:** Gênero da pessoa falecida.
- **Valores:**
  - 1: Masculino
  - 2: Feminino
  - 0, 9: NA (Não especificado)

### `RACACOR`
- **Descrição:** Raça ou cor da pessoa falecida.
- **Valores:**
  - 1: Branca
  - 2: Preta
  - 3: Amarela
  - 4: Parda
  - 5: Indígena
  - 0, 6, 7, 8, 9: NA (Não especificado)

### `ESTCIV`
- **Descrição:** Estado civil da pessoa falecida.
- **Valores:**
  - 1: Solteiro
  - 2: Casado
  - 3: Viúvo
  - 4: Separado judicialmente
  - 5: União consensual
  - 0, 6, 7, 8, 9: NA (Não especificado)

### `ESC`
- **Descrição:** Escolaridade da pessoa falecida.
- **Valores:**
  - 1: Nenhuma
  - 2: 1 a 3 anos
  - 3: 4 a 7 anos
  - 4: 8 a 11 anos
  - 5: 12 e mais
  - 8: De 9 a 11 anos
  - 0, 6, 7, 9, A: NA (Não especificado)

### `OCUP`
- **Descrição:** Ocupação da pessoa falecida, seguindo a tabela CBO2002.

### `CODMUNRES`
- **Descrição:** Município de residência do falecido (codificado).

### `LOCOCOR`
- **Descrição:** Local de ocorrência do óbito.
- **Valores:**
  - 1: Hospital
  - 2: Outro estabelecimento de saúde
  - 3: Domicílio
  - 4: Via pública
  - 5: Outros
  - 9: NA (Não especificado)

### `ASSISTMED`
- **Descrição:** Assistência médica recebida pela pessoa falecida.
- **Valores:**
  - 1: Sim
  - 2: Não
  - 9: NA (Não especificado)

### `CAUSABAS`
- **Descrição:** Causa básica do óbito, utilizando o código CID-10.

### `CAUSABAS_O`
- **Descrição:** Causa básica do óbito (outra definição), utilizando o código CID-10.

### `idade`
- **Descrição:** Idade da pessoa falecida.

### `mes`
- **Descrição:** Mês em que o óbito ocorreu.
''')