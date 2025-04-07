import streamlit as st
import pandas as pd
import numpy as np


class Project1:
    def __init__(self):
        pass
    def app(self):
        st.title("Создание ДатаФреймов")

        def load_data(file):
            if file is not None:
                data = pd.read_csv(file)
                return data
            return None

        upload = st.file_uploader("Выберите CSV файл")
        if upload is not None:
            df = load_data(upload)
            st.dataframe(df, height=400, width=600)
            column = st.selectbox("Выберите колонку для фильтра", df.columns)
            if column:
                unique_values = df[column].unique()
                selected_values = st.multiselect(f"Выберите значения для {column}", options=unique_values,
                                                default=unique_values)
                filtered_df = df[df[column].isin(selected_values)]
                st.dataframe(filtered_df, height=400, width=600)
        else:
            st.warning("Пожалуйста, загрузите CSV файл")

        st.markdown("""<style>
        h1 {
        color: green;
        font-size: 18px;
        text-align: center;
        }
        </style>""", unsafe_allow_html=True)
