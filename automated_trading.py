import yfinance as yf  # For stock data
import pandas as pd    # For data manipulation
import numpy as np     # For numerical operations
import matplotlib.pyplot as plt  # For visualizations

# Define parameters
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2025-01-01"

# Fetch historical stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Display first few rows
print(data.head())
