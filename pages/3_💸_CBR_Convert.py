import streamlit as st
from lib.cbrf import CBRFApi
import pandas as pd


# Streamlit UI
def main():
    st.title("Currency Converter")

    # Пример использования класса
    cbrf_api = CBRFApi()

    # Получить текущие курсы валют
    currency_data = cbrf_api.get_currencies_list()

    # User inputs
    direction = st.radio("Conversion direction", ('RUB to Foreign Currency', 'Foreign Currency to RUB'))
    amount = st.number_input("Enter amount", min_value=0.0, value=100.0)
    target_currency = st.selectbox("Select target currency", options=list(currency_data.keys()))

    # Conversion
    if st.button("Convert"):
        exchange_rate = currency_data[target_currency]['Value']
        nominal = currency_data[target_currency]['Nominal']
        name = currency_data[target_currency]['Name']

        if direction == 'RUB to Foreign Currency':
            converted_amount = (amount / exchange_rate) * nominal
            st.success(f"{amount} RUB is equal to {converted_amount:.2f} {target_currency} ({name})")
        else:
            converted_amount = (amount * exchange_rate) / nominal
            st.success(f"{amount} {name} ({target_currency}) is equal to {converted_amount:.2f} RUB")


if __name__ == "__main__":
    main()