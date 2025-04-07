import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Project3:
    def __init__(self):
        pass
    def load_data(self, file):
        if file is not None:
            data = pd.read_csv(file)
            return data
        return None


    def clean_and_convert_values(self, df, column):
        df[column] = df[column].astype(str)

        df[column] = df[column].replace({',':'.'},regex=True)
        df[column] = df[column].str.replace(r'\s+','', regex=True)

        df[column] = pd.to_numeric(df[column], errors='coerce')

        return df


    def plot_bar_chart(self, df, category_column, value_column):
        df= self.clean_and_convert_values(df, value_column)

        if df[category_column].dtype == 'object' or df[category_column].dtype.name== 'category':
            if df[value_column].dtype in ['int64', 'float64']:

                category_mean = df.groupby(category_column)[value_column].mean()

                colors = plt.cm.get_cmap('tab20', len(category_mean))

                fig, ax = plt.subplots()
                category_mean.plot ( kind='bar', ax=ax, color=colors(np.arange(len(category_mean))))
                ax.set_title(f'Среднее значение {value_column} по {category_column}')
                ax.set_xlabel(category_column)
                ax.set_ylabel(f'Среднее значение {value_column}')
                st.pyplot(fig)

                st.write(f"Среднее значение {value_column} по {category_column}:")
                st.dataframe(category_mean)
            else:
                st.warning(f"{value_column} не числового типа. Выберите столбец числового типа")
        else:
            st.warning(f"{category_column} не столбец категории. Выберите столбец категории")


    def app(self):
        st.title("Создание ДатаФрейма")
        upload = st.file_uploader("Выберите CSV файл")
        if upload is not None:
            df = self.load_data(upload)
            st.dataframe(df, height=400, width=600)

            category_column = st.selectbox('Выберите столбец категории', df.columns)
            value_column = st.selectbox('Выберите столбец со значениями', df.columns)

            if category_column and value_column:
                st.subheader(f'Бар Чарт и Среднее Значение {value_column} по {category_column}')
                self.plot_bar_chart(df, category_column, value_column)
        else:
            st.warning("Пожалуйста, загрузите CSV файл")

        st.markdown("""<style>
                    h1 {
                    color: green;
                    font-size: 18px;
                    text-align: center;
                    }
                    </style>""", unsafe_allow_html=True)

if __name__ == '__main__':
    project=Project3()
    project.app()