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