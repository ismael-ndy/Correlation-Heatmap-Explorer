import streamlit as st
from yahooquery import Ticker
import yfinance as yf
import seaborn as sns
import numpy as np

etfs = [
    "SPY",  # SPDR S&P 500
    "QQQ",  # Invesco QQQ (Nasdaq 100)
    "VTI",  # Vanguard Total Stock Market
    "VOO",  # Vanguard S&P 500
    "IVV",  # iShares Core S&P 500
    "XLF",  # Financials
    "XLK",  # Technology
    "XLE",  # Energy
    "XLV",  # Healthcare
    "XLY",  # Consumer Discretionary
    "EFA",  # MSCI EAFE (Developed Markets ex-US/Canada)
    "EEM",  # MSCI Emerging Markets
    "VEA",  # Vanguard FTSE Developed Markets
    "VWO",  # Vanguard FTSE Emerging Markets
    "TLT",  # 20+ Year Treasury Bond
    "IEF",  # 7–10 Year Treasury Bond
    "AGG",  # Aggregate Bond Market
    "GLD",  # SPDR Gold Shares
    "SLV",  # Silver Trust
    "DBC"   # Commodity Index
]

st.title("ETF Correlation Heatmap Explorer")
st.divider()
st.write("""This app allows you to visualize the correlation between the stocks in the selected ETF""")
st.divider()
etf = st.selectbox("Select an ETF", etfs)
ticker = Ticker(etf)
holdings = ticker.fund_holding_info
print(holdings)
# holdings_list = holdings[etf]['holdings']
# stocks = [holding['symbol'] for holding in holdings_list]
# data = yf.download(stocks, period="3y")['Adj Close']

# log_returns = np.log(data / data.shift(1)).dropna()
# correlation_matrix = log_returns.corr()
# sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={"label": "Correlation Coefficient"})
# st.pyplot(bbox_inches='tight')
