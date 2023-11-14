import streamlit as st
from lib.cbrf import CBRFApi
import pandas as pd

st.set_page_config(layout="wide")
st.markdown("## Данные Центрального банка России")

# Пример использования класса
cbrf_api = CBRFApi()

# Получить список валют
currencies_list = cbrf_api.get_currencies_list()

# Data Reading
df = pd.DataFrame(currencies_list)
df = df.transpose()
df["Delta"] = df["Previous"] - df["Value"]
df["Delta, %"] = (df["Previous"] - df["Value"]) / df["Previous"]


def main_currencies():
    # Получить информацию о конкретной валюте
    columns = st.columns(5)
    currencies = ['USD', 'EUR', 'CNY', 'RSD', 'GBP']

    for i, currency in enumerate(currencies):
        info = cbrf_api.get_currency_info(currency)
        columns[i].metric(
            label=info['CharCode'],
            value=info["Value"],
            delta="{0} %".format((info['Previous'] - info['Value']) / info['Previous'])
            )


def graphs():
    # Feature creation
    col1, col2 = st.columns(2)

    with col1:
        def color_column(value):
            color = 'green' if value > 0 else 'red'
            return f'background-color: {color}'
        
        st.markdown("### Сравнение вчерашнего и сегодняшнего курсов")
        select_columns_df = df[["Name", "Nominal", "Previous", "Value", "Delta", "Delta, %"]]
        styled_df = select_columns_df.style.applymap(color_column, subset=['Delta', 'Delta, %'])
        
        st.write(styled_df)


    with col2:
        st.markdown("### Соотношение изменений между валютами, %")
        chart_data = pd.DataFrame(df["Delta, %"])
        st.bar_chart(chart_data)


def top_up_fall():
    col1, col2 = st.columns(2)

    with col1:
        df_sorted_asc = df.sort_values(by='Delta, %', ascending=False)
        st.markdown("### Топ 5 роста")

        for index, row in df_sorted_asc[["Name", "Value", "Delta, %"]][:5].iterrows():
            if row["Value"] > 0:
                st.metric(
                    label=row['Name'],
                    value=row["Value"],
                    delta="{0} %".format(row['Delta, %'])
                    )

    with col2:
        df_sorted_asc = df.sort_values(by='Delta, %', ascending=True)
        st.markdown("### Топ 5 падений")
        for index, row in df_sorted_asc[["Name", "Value", "Delta, %"]][:5].iterrows():
            if row["Value"] < 0:
                st.metric(
                    label=row['Name'],
                    value=row["Value"],
                    delta="{0} %".format(row['Delta, %'])
                    )


def main():
    main_currencies()
    graphs()
    top_up_fall()


if __name__ == "__main__":
    main()