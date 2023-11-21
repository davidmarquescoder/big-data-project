from pathlib import Path


def file_path_1():
    sub_pasta = 'vendas-carros'
    file_name = 'vendas-carros-1990-2022.csv'
    file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name

    return file_path

def file_path_2(table):
    sub_pasta = 'reclamacoes'

    file_name_1 = 'reclamacoes-fundamentadas-sindec-2012.csv'
    file_name_2 = 'reclamacoes-fundamentadas-sindec-2013.csv'
    file_name_3 = 'reclamacoes-fundamentadas-sindec-2014.csv'
    file_name_4 = 'reclamacoes-fundamentadas-sindec-2015.csv'
    file_name_5 = 'reclamacoes-fundamentadas-sindec-2016.csv'

    match table:
        case 1:
            file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name_1
        case 2:
            file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name_2
        case 3:
            file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name_3
        case 4:
            file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name_4
        case 5:
            file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name_5

    return file_path

def file_path_3():
    sub_pasta = 'Global-Economy'
    file_name = 'Global_Economy_Indicators.csv'
    file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name

    return file_path

def file_path_4(table):
    sub_pasta = 'Indices-de-pobreza-brasil'

    file_name_1 = 'indices_pobreza_consolidado_anual.csv'
    file_name_2 = 'indices_pobreza_consolidado.csv'

    match table:
        case 1:
            file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name_1
        case 2:
            file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name_2
        
    return file_path

def file_path_5():
    sub_pasta = 'Suicidio'
    file_name = 'Suicidio_2014_2018.csv'
    file_path = Path(__file__).parent.parent / 'data' / sub_pasta / file_name

    return file_path