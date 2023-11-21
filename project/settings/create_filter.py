import streamlit as st


class Component:
    def CreateFilter(self, id, label, dataframe, coluna):
        filter = st.sidebar.multiselect(
            key = id,
            label = label,
            options = dataframe[coluna].unique(),
            default = dataframe[coluna].unique()
            )

        return filter
    
    def CreateFilterInPage(self, id, label, dataframe, coluna):
        filter = st.multiselect(
            key = id,
            label = label,
            options = dataframe[coluna].unique(),
            default = dataframe[coluna].unique()
            )

        return filter
    
    def CreateSelectBox(self, placeholder, dataframe, coluna, position):
        filter = position.selectbox(placeholder, dataframe[coluna].unique())

        return filter
    
    def CreateCheckBox(self, label, help_text, position):
        CheckBox = position.checkbox(label, help = help_text)

        return CheckBox
    