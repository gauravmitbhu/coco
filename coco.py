import streamlit as st
import numpy as np
import pandas as pd

st.write("Coco helps you invest in Bitcoin - Smartly")
st.write("Coco's Risk model based smart monthly investment")
st.write("Coco uses a risk model to tell you every week when the risk is high or low. This helps you make better decisions on when to buy or sell Bitcoin.")
# CSS to hide Streamlit's default header (and possibly other elements)
hide_streamlit_style = """
            <style>
            /* This hides the Streamlit header */
            header {visibility: hidden;}
            /* Optionally, hide the footer */
            footer {visibility: hidden;}
            </style>
            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # Applying the CSS to the Streamlit app

def calculate_returns(monthly_contribution, years):
    months = years * 12
    monthly_growth_rate = (1 + 30/100) ** (1/12) - 1
    balances = [0]
    for _ in range(1, months):
        balances.append(balances[-1] * (1 + monthly_growth_rate) + monthly_contribution)
    return balances

# st.title('Investment Growth Calculator')
#
# with st.form("my_form"):
#     #initial_investment = st.number_input('Initial Investment ($)', min_value=0.0, value=1000.0)
#     monthly_contribution = st.slider('Monthly Contribution (INR)',1000,50000,5000 )
#     years = st.slider('Since last these many years', 1, 5, 1)
#     #annual_growth_rate = st.slider('Annual Growth Rate (%)', 0.0, 15.0, 7.0) / 100
#     submitted = st.form_submit_button("Calculate")
#
# if submitted:
#     balances = calculate_returns(monthly_contribution, years)
#     st.write(f"After {years} years, your investment would be worth ${balances[-1]:,.2f}!")
#
#     df = pd.DataFrame({
#         "Month": np.arange(len(balances)),
#         "Balance": balances
#     })
#
#     st.line_chart(df.rename(columns={'Month':'index'}).set_index('index'))

from PIL import Image


image = Image.open('images/graph1.png')
st.image(image, caption="Coco's Risk model based smart monthly investment")


st.write("Coco-based investment vs. other investments")
import plotly.express as px
df=px.data.tips()
fig=px.bar(df,x='total_bill',y='day', orientation='h')
st.write(fig)
#opening the image


st.write("Coco's risk model is based on the following parameters:")
st.write("1. Bitcoin's historical price data")
st.write("2. Bitcoin blockchain data")
st.write("3. Bitcoin's volatility")
st.write("4. Bitcoin's trading volume")
st.write("5. Bitcoin's social media sentiment")
