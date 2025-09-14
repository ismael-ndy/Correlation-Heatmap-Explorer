import streamlit as st
from yahooquery import Ticker
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sp500 import SP500_TICKERS

st.title("Correlation Heatmap Explorer")
st.divider()
st.write("This app allows you to visualize the correlation between two stocks from the S&P 500 index")
st.divider()
ticker1 = st.selectbox("Select a first ticker", SP500_TICKERS)
ticker2 = st.selectbox("Select another ticker", SP500_TICKERS, index=1)

if st.button("Get stocks correlation heatmap"):
    st.write(f"Fetching data for {ticker1} and {ticker2}...")
    data = yf.download([ticker1, ticker2], period="3y")
    if data is not None:
        data.head()

    #     log_returns = np.log(data / data.shift(1))
    #     correlation = log_returns.corr()

    #     fig, ax = plt.subplots(figsize=(6, 5))
    #     sns.heatmap([[correlation]], annot=True, fmt=".2f", cmap="coolwarm",
    #                 cbar_kws={"label": "Correlation Coefficient"}, ax=ax)
    #     ax.set_xticklabels([ticker1, ticker2])
    #     ax.set_yticklabels([ticker1, ticker2])
    #     plt.title(f"Correlation Heatmap for {ticker1} and {ticker2}")
    #     st.pyplot(fig)
    # else:
    #     st.error("Failed to retrieve data.")