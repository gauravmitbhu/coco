import streamlit as st
import numpy as np
import pandas as pd

# CSS to hide Streamlit's default header (and possibly other elements)
hide_streamlit_style = """
            <style>
            /* This hides the Streamlit header */
            header {visibility: hidden;}
            /* Optionally, hide the footer */
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # Applying the CSS to the Streamlit app

def calculate_returns(initial_investment, monthly_contribution, years, annual_growth_rate):
    months = years * 12
    monthly_growth_rate = (1 + annual_growth_rate) ** (1/12) - 1
    balances = [initial_investment]
    for _ in range(1, months):
        balances.append(balances[-1] * (1 + monthly_growth_rate) + monthly_contribution)
    return balances

st.title('Investment Growth Calculator')

with st.form("my_form"):
    initial_investment = st.number_input('Initial Investment ($)', min_value=0.0, value=1000.0)
    monthly_contribution = st.number_input('Monthly Contribution ($)', min_value=0.0, value=100.0)
    years = st.slider('Years of Growth', 1, 40, 10)
    annual_growth_rate = st.slider('Annual Growth Rate (%)', 0.0, 15.0, 7.0) / 100
    submitted = st.form_submit_button("Calculate")

if submitted:
    balances = calculate_returns(initial_investment, monthly_contribution, years, annual_growth_rate)
    st.write(f"After {years} years, your investment would be worth ${balances[-1]:,.2f}!")

    df = pd.DataFrame({
        "Month": np.arange(len(balances)),
        "Balance": balances
    })

    st.line_chart(df.rename(columns={'Month':'index'}).set_index('index'))
