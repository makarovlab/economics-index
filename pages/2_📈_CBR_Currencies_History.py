import streamlit as st
from lib.cbrf import CBRFApi
import pandas as pd

st.set_page_config(layout="wide")
# Пример использования класса
cbrf_api = CBRFApi()

# Получить текущие курсы валют
daily_rates = cbrf_api.get_daily_rates()

# Получить динамику курса доллара за определенный период
# dynamic_rates = cbrf_api.get_dynamic_rates('R01235', '2023-01-01', '2023-01-10')

# Получить список валют
currencies_list = cbrf_api.get_currencies_list()

# Получить информацию о конкретной валюте
# currency_info = cbrf_api.get_currency_info('USD')

# currency_info

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Data Reading
df = pd.DataFrame(currencies_list)
df = df.transpose()

# Feature creation
df["Delta"] = df["Previous"] - df["Value"]
df["Delta, %"] = (df["Previous"] - df["Value"]) / df["Previous"]

df = df[["Nominal", "Name", "Previous", "Value", "Delta", "Delta, %"]]


with col1:
    def color_column(value):
        color = 'green' if value > 0 else 'red'
        return f'background-color: {color}'
    
    st.markdown("### Данные Центрального банка России")
    select_columns_df = df[["Name", "Nominal", "Previous", "Value", "Delta", "Delta, %"]]
    styled_df = select_columns_df.style.applymap(color_column, subset=['Delta', 'Delta, %'])
    
    st.write(styled_df)


with col2:
    st.markdown("### Соотношение процента изменений")
    chart_data = pd.DataFrame(df["Delta, %"])
    st.bar_chart(chart_data)



with col3:
    df_sorted_asc = df.sort_values(by='Delta, %', ascending=False)
    st.markdown("### Топ 5 роста")

    for index, row in df_sorted_asc[["Name", "Value", "Delta, %"]][:5].iterrows():
        st.metric(
            label=row['Name'],
            value=row["Value"],
            delta="{0} %".format(row['Delta, %'])
            )

with col4:
    df_sorted_asc = df.sort_values(by='Delta, %', ascending=True)
    st.markdown("### Топ 5 падений")
    for index, row in df_sorted_asc[["Name", "Value", "Delta, %"]][:5].iterrows():
        st.metric(
            label=row['Name'],
            value=row["Value"],
            delta="{0} %".format(row['Delta, %'])
            )