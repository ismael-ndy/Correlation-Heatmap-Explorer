import streamlit as st
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from utils import get_symbols_from_json, get_pairs_midprice_dataframe
from data_processing import extract_csv


# extract_csv()
ticker_list = get_symbols_from_json()


st.title("Correlation Heatmap Explorer")
st.divider()
st.write("This app allows you to visualize the correlation between two FX pairs (January 2025).")
st.divider()
ticker1 = st.selectbox("Select a first ticker", ticker_list, index=0)
ticker2 = st.selectbox("Select another ticker", ticker_list, index=1)

if st.button("Get FX pair correlation heatmap"):
    st.write(f"Fetching data for {ticker1} and {ticker2}...")
    data = get_pairs_midprice_dataframe(ticker1, ticker2)
    if data is not None:
        st.write(f"Data fetched successfully! Number of rows: {len(data)}")
        corr = data[[f"MidPrice_1", f"MidPrice_2"]].corr()

        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        ax.set_title(f"Correlation Heatmap between {ticker1} and {ticker2}")

        st.pyplot(fig)
