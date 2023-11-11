import streamlit as st


class FormatingTable:

    def YearToString(self, dataframe, column):
        dataframe[column] = dataframe[column].astype('string')
    
    def RemoveSpacesColumn(sel, dataframe):
        dataframe.columns = dataframe.columns.str.strip()

    def SortingBy(self, dataframe, column_1, column_2):
        dataframe = dataframe.sort_values(by=[column_1, column_2])
        return dataframe