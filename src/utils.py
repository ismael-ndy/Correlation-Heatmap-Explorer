import polars as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json


JSON_SYMBOLS_FILE = "src/symbol_hashmap.json"



def get_symbols_from_json() -> list[str]:
    with open(JSON_SYMBOLS_FILE, 'r') as file:
        data = json.load(file)
    return list(data.keys())


def get_pairs_midprice_dataframe(ticker1: str, ticker2: str) -> pl.DataFrame | None:
    try:
        df1 = pl.read_parquet(f"data/processed/{ticker1}-2025-01.parquet")
        df2 = pl.read_parquet(f"data/processed/{ticker2}-2025-01.parquet")

        df1 = df1.select(
            pl.col("TIMESTAMP"),
            pl.col("BID"),
            pl.col("ASK"),
            ((pl.col("BID") + pl.col("ASK")) / 2).alias("MidPrice_1")
        )

        df2 = df2.select(
            pl.col("TIMESTAMP"),
            pl.col("BID").alias("BID_2"),
            pl.col("ASK").alias("ASK_2"),
            ((pl.col("BID") + pl.col("ASK")) / 2).alias("MidPrice_2")
        )

        df1 = df1.sort("TIMESTAMP")
        df2 = df2.sort("TIMESTAMP")

        merged_df = df1.join_asof(
            df2,
            left_on="TIMESTAMP",
            right_on="TIMESTAMP",
            tolerance="50ms",
            strategy="nearest"
        )

        merged_df = merged_df.drop_nulls()

        return merged_df
        
    except Exception as e:
        print(f"Error loading data for {ticker1} or {ticker2}: {e}")
        return None