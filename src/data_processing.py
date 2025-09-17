import os
import polars as pl
from pathlib import Path


THIS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = THIS_DIR.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"


COLUMN_NAMES = ["SYMBOL", "TIMESTAMP", "BID", "ASK"]
DTYPES = {
    "SYMBOL": pl.Utf8,
    "TIMESTAMP": pl.Utf8,
    "BID": pl.Float64,
    "ASK": pl.Float64
}


def to_parquet(csv_file_path: str) -> None:
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")

    df = pl.read_csv(csv_file_path, new_columns=COLUMN_NAMES, schema_overrides=DTYPES)
    df = df.with_columns(
        pl.col("TIMESTAMP").str.strptime(
            pl.Datetime,
            format="%Y%m%d %H:%M:%S%.3f"
        )
    )

    folder_name = os.path.basename(os.path.dirname(csv_file_path))  # This is the SYMBOL-date folder
    parquet_file_name = f"{folder_name}.parquet"
    parquet_file_path = os.path.join(DATA_PROCESSED, parquet_file_name)
    
    os.makedirs(DATA_PROCESSED, exist_ok=True)
    df.write_parquet(parquet_file_path)

    print(f"Converted {csv_file_path} to {parquet_file_path}")


def extract_csv():
    """
    Traverses all folders in DATA_RAW, extracts CSV files and converts them to parquet format.
    The parquet files are stored in the corresponding structure under DATA_PROCESSED.
    """
    for symbol_folder in os.listdir(DATA_RAW):
        symbol_folder_path = os.path.join(DATA_RAW, symbol_folder)
        
        if os.path.isdir(symbol_folder_path):
            print(f"Processing folder: {symbol_folder}")
            
            for filename in os.listdir(symbol_folder_path):
                if filename.endswith(".csv"):
                    csv_file_path = os.path.join(symbol_folder_path, filename)
                    to_parquet(csv_file_path)
