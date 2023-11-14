import streamlit as st

# Функция для определения качества показателя
def evaluate_indicator(value, good_threshold, bad_threshold):
    if value >= good_threshold:
        return '🟢', 'Хорошо'
    elif value <= bad_threshold:
        return '🔴', 'Плохо'
    else:
        return '🟡', 'Средне'

# Streamlit UI
def main():
    st.title("Финансовый анализ компании")

    # P/E Ratio
    st.markdown("##### P/E (Price-to-Earnings) Ratio")
    st.caption("Отношение цены акции к прибыли на акцию. Низкий P/E может указывать на недооцененность акций, в то время как высокий P/E может свидетельствовать о переоцененности.")
    pe_ratio = st.number_input("P/E Ratio", value=0.0)
    pb_ratio = st.number_input("P/B Ratio", value=0.0)
    dividend_yield = st.number_input("Дивидендная Доходность (%)", value=0.0)
    roe = st.number_input("ROE (%)", value=0.0)
    roa = st.number_input("ROA (%)", value=0.0)
    debt_ebitda = st.number_input("Долг/EBITDA", value=0.0)
    current_ratio = st.number_input("Текущая Ликвидность", value=0.0)
    quick_ratio = st.number_input("Коэффициент Быстрой Ликвидности", value=0.0)
    operating_cash_flow = st.number_input("Операционный Денежный Поток", value=0.0)
    eps = st.number_input("EPS (Earnings Per Share)", value=0.0)
    revenue_growth = st.number_input("Рост Выручки (%)", value=0.0)
    net_profit_margin = st.number_input("Маржа Чистой Прибыли (%)", value=0.0)

    # Анализ и отображение результатов
    if st.button("Анализировать"):
        pe_indicator, pe_status = evaluate_indicator(pe_ratio, good_threshold=15, bad_threshold=25)
        pb_indicator, pb_status = evaluate_indicator(pb_ratio, good_threshold=0.5, bad_threshold=1.5)
        dividend_indicator, dividend_status = evaluate_indicator(dividend_yield, good_threshold=4, bad_threshold=2)
        roe_indicator, roe_status = evaluate_indicator(roe, good_threshold=15, bad_threshold=5)
        roa_indicator, roa_status = evaluate_indicator(roa, good_threshold=5, bad_threshold=3)
        debt_indicator, debt_status = evaluate_indicator(debt_ebitda, good_threshold=2, bad_threshold=4)
        current_indicator, current_status = evaluate_indicator(current_ratio, good_threshold=1.5, bad_threshold=1)
        quick_indicator, quick_status = evaluate_indicator(quick_ratio, good_threshold=1, bad_threshold=0.5)
        cash_flow_indicator, cash_flow_status = evaluate_indicator(operating_cash_flow, good_threshold=100000, bad_threshold=50000)
        eps_indicator, eps_status = evaluate_indicator(eps, good_threshold=3, bad_threshold=1)
        revenue_growth_indicator, revenue_growth_status = evaluate_indicator(revenue_growth, good_threshold=10, bad_threshold=5)
        net_profit_margin_indicator, net_profit_margin_status = evaluate_indicator(net_profit_margin, good_threshold=20, bad_threshold=10)

        st.markdown(f"P/E Ratio: {pe_indicator} {pe_status}")
        st.markdown(f"P/B Ratio: {pb_indicator} {pb_status}")
        st.markdown(f"Дивидендная Доходность: {dividend_indicator} {dividend_status}")
        st.markdown(f"ROE: {roe_indicator} {roe_status}")
        st.markdown(f"ROA: {roa_indicator} {roa_status}")
        st.markdown(f"Долг/EBITDA: {debt_indicator} {debt_status}")
        st.markdown(f"Текущая Ликвидность: {current_indicator} {current_status}")
        st.markdown(f"Коэффициент Быстрой Ликвидности: {quick_indicator} {quick_status}")
        st.markdown(f"Операционный Денежный Поток: {cash_flow_indicator} {cash_flow_status}")
        st.markdown(f"EPS: {eps_indicator} {eps_status}")
        st.markdown(f"Рост Выручки: {revenue_growth_indicator} {revenue_growth_status}")
        st.markdown(f"Маржа Чистой Прибыли: {net_profit_margin_indicator} {net_profit_margin_status}")

if __name__ == "__main__":
    main()
