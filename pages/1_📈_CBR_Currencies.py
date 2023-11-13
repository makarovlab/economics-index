import streamlit as st
from lib.cbrf import CBRFApi
import pandas as pd

st.set_page_config(layout="wide")
st.markdown("## Данные Центрального банка России")

# Пример использования класса
cbrf_api = CBRFApi()

# Получить текущие курсы валют
daily_rates = cbrf_api.get_daily_rates()

# Получить динамику курса доллара за определенный период
# dynamic_rates = cbrf_api.get_dynamic_rates('R01235', '2023-01-01', '2023-01-10')

# Получить список валют
currencies_list = cbrf_api.get_currencies_list()

# Получить информацию о конкретной валюте
col1, col2, col3, col4, col5 = st.columns(5)

dollar_info = cbrf_api.get_currency_info('USD')
col1.metric(
    label=dollar_info['CharCode'],
    value=dollar_info["Value"],
    delta="{0} %".format((dollar_info['Previous'] - dollar_info['Value']) / dollar_info['Previous'])
    )

euro_info = cbrf_api.get_currency_info('EUR')
col2.metric(
    label=euro_info['CharCode'],
    value=euro_info["Value"],
    delta="{0} %".format((euro_info['Previous'] - euro_info['Value']) / euro_info['Previous'])
    )

china_uan_info = cbrf_api.get_currency_info('CNY')
col3.metric(
    label=china_uan_info['CharCode'],
    value=china_uan_info["Value"],
    delta="{0} %".format((china_uan_info['Previous'] - china_uan_info['Value']) / china_uan_info['Previous'])
    )

serbian_dinar_info = cbrf_api.get_currency_info('RSD')
col4.metric(
    label=serbian_dinar_info['CharCode'],
    value=serbian_dinar_info["Value"],
    delta="{0} %".format((serbian_dinar_info['Previous'] - serbian_dinar_info['Value']) / serbian_dinar_info['Previous'])
    )

uk_funt_info = cbrf_api.get_currency_info('GBP')
col5.metric(
    label=uk_funt_info['CharCode'],
    value=uk_funt_info["Value"],
    delta="{0} %".format((uk_funt_info['Previous'] - uk_funt_info['Value']) / uk_funt_info['Previous'])
    )


col1_, col2_ = st.columns(2)
col3_, col4_ = st.columns(2)

# Data Reading
df = pd.DataFrame(currencies_list)
df = df.transpose()

# Feature creation
df["Delta"] = df["Previous"] - df["Value"]
df["Delta, %"] = (df["Previous"] - df["Value"]) / df["Previous"]

df = df[["Nominal", "Name", "Previous", "Value", "Delta", "Delta, %"]]


with col1_:
    def color_column(value):
        color = 'green' if value > 0 else 'red'
        return f'background-color: {color}'
    
    st.markdown("### Сравнение вчерашнего и сегодняшнего курсов")
    select_columns_df = df[["Name", "Nominal", "Previous", "Value", "Delta", "Delta, %"]]
    styled_df = select_columns_df.style.applymap(color_column, subset=['Delta', 'Delta, %'])
    
    st.write(styled_df)


with col2_:
    st.markdown("### Соотношение изменений между валютами, %")
    chart_data = pd.DataFrame(df["Delta, %"])
    st.bar_chart(chart_data)



with col3_:
    df_sorted_asc = df.sort_values(by='Delta, %', ascending=False)
    st.markdown("### Топ 5 роста")

    for index, row in df_sorted_asc[["Name", "Value", "Delta, %"]][:5].iterrows():
        st.metric(
            label=row['Name'],
            value=row["Value"],
            delta="{0} %".format(row['Delta, %'])
            )

with col4_:
    df_sorted_asc = df.sort_values(by='Delta, %', ascending=True)
    st.markdown("### Топ 5 падений")
    for index, row in df_sorted_asc[["Name", "Value", "Delta, %"]][:5].iterrows():
        st.metric(
            label=row['Name'],
            value=row["Value"],
            delta="{0} %".format(row['Delta, %'])
            )