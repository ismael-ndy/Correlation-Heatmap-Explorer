# 🔗 Correlation Heatmap Explorer

An interactive web application for analyzing correlations between foreign exchange (FX) currency pairs using real-time financial data. Built with Streamlit and powered by Polars for lightning-fast data processing.

## Live Demo

**Try the app now:** [https://correlation-heatmap.streamlit.app/](https://correlation-heatmap.streamlit.app/)

## 🎯 Project Goal

The Correlation Heatmap Explorer is designed to provide traders, analysts, and financial researchers with an intuitive tool to visualize and analyze the correlation relationships between different FX pairs. By processing high-frequency tick data and calculating correlations between currency pairs, users can identify trading opportunities, assess portfolio risk, and understand market dynamics.

## ✨ Features

- **Interactive Web Interface**: User-friendly Streamlit dashboard for selecting and comparing FX pairs
- **High-Performance Data Processing**: Leverages Polars for ultra-fast data manipulation and analysis
- **Real-Time Correlation Analysis**: Calculate correlations between any two FX pairs from the dataset
- **Visual Correlation Heatmaps**: Beautiful correlation matrix visualizations using Seaborn

## 🏗️ Architecture

### Data Pipeline

1. **Raw Data Ingestion**: CSV files containing tick-by-tick FX data (Symbol, Timestamp, Bid, Ask)
2. **Data Processing**: Conversion to efficient Parquet format with timestamp parsing
3. **Analytics**: Mid-price calculations and time-series alignment using asof joins
4. **Visualization**: Interactive correlation heatmaps

### Supported Currency Pairs

- Major Pairs: EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, USDCHF
- Cross Pairs: EURJPY, GBPJPY, AUDJPY, CADJPY, CHFJPY
- Emerging Markets: USDMXN, USDTRY, USDZAR, EURPLN
- Commodity Currencies: AUDNZD, NZDUSD
- European Crosses: EURCHF, EURGBP

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ismael-ndy/Correlation-Heatmap-Explorer.git
   cd Correlation-Heatmap-Explorer
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install streamlit polars pandas numpy matplotlib seaborn
   ```

### Data Preparation

1. **Place your CSV files** in the `data/raw/` directory following this structure:

   ```
   data/raw/
   ├── EURUSD-2025-01/
   │   └── EURUSD-2025-01.csv
   ├── GBPUSD-2025-01/
   │   └── GBPUSD-2025-01.csv
   └── ...
   ```

2. **Process the data** to convert CSV files to optimized Parquet format:
   ```python
   from src.data_processing import extract_csv
   extract_csv()
   ```

### Running the Application

Launch the Streamlit web application:

```bash
streamlit run src/main.py
```

The application will be available at `http://localhost:8501`

## 💻 Usage

1. **Select Currency Pairs**: Choose two FX pairs from the dropdown menus
2. **Generate Correlation**: Click "Get FX pair correlation heatmap" to process the data
3. **Analyze Results**: View the correlation coefficient and interactive heatmap visualization
4. **Interpret Data**:
   - Values close to +1 indicate strong positive correlation
   - Values close to -1 indicate strong negative correlation
   - Values near 0 suggest little to no linear relationship

## 📊 Data Format

Input CSV files should contain the following columns:

- `SYMBOL`: Currency pair identifier (e.g., "EURUSD")
- `TIMESTAMP`: Date and time in format "YYYYMMDD HH:MM:SS.fff"
- `BID`: Bid price (float)
- `ASK`: Ask price (float)

## 🔮 Future Features

- [ ] **Rolling Correlations**: Dynamic correlation windows (e.g., 1-day, 1-week rolling)
- [ ] **Export Functionality**: Download correlation matrices as CSV/Excel
- [ ] **Portfolio Correlation Matrix**: Analyze correlations across multiple pairs simultaneously
- [ ] **Statistical Significance Testing**: P-values and confidence intervals for correlations
- [ ] **Volatility Analysis**: Integrated volatility metrics and correlation with volatility
- [ ] **Historical Comparison**: Compare correlations across different time periods

### Long-term Vision

- [ ] **Machine Learning Integration**: Predictive correlation modeling
- [ ] **Real-time Data Feeds**: Live data integration with FX data providers
- [ ] **Advanced Visualizations**: 3D correlation surfaces and network graphs
- [ ] **API Development**: RESTful API for programmatic access
- [ ] **Multi-asset Support**: Extend beyond FX to commodities, equities, and crypto
- [ ] **Risk Management Tools**: VaR calculations and correlation-based risk metrics

## 📁 Project Structure

```
Correlation-Heatmap-Explorer/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Streamlit web application
│   ├── data_processing.py      # CSV to Parquet conversion
│   ├── utils.py               # Data loading and correlation utilities
│   └── symbol_hashmap.json    # Currency pair mappings
├── data/
│   ├── raw/                   # Original CSV files
│   └── processed/             # Converted Parquet files
├── requirements.txt           # Python dependencies
├── readme.md                 # Project documentation
└── .gitignore               # Git ignore rules
```

## 📈 Performance Metrics (just for me)

- **Data Processing**: ~10x faster than Pandas equivalent
- **Memory Usage**: ~50% reduction compared to traditional DataFrame operations
- **File Size**: Parquet files are ~60% smaller than equivalent CSV files
- **Query Performance**: Sub-second correlation calculations for millions of data points
