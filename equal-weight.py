import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secret import IEX_CLOUD_API_TOKEN

# Import list of tickers, in prod will use API call here
stocks = pd.read_csv('sp_500_stocks.csv')

# Example - call the IEX API for data
symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()

# Parse API call result
price = data['latestPrice']
market_cap = data['marketCap']

# Add all ticker data to dataframe
my_cols = ['Ticker', 'Stock Price', 'Market Cap', 'Number Shares to Buy']
"""
Example demonstrating how Pandas series is appended to DF

final_df = pd.DataFrame(columns=my_cols)
final_df.append(
    pd.Series(
        [
            symbol,
            price,
            market_cap,
            'N/A'
        ],
    index = my_cols
    ),
    ignore_index=True
)
"""

# Loop through tickers in stocks data
# Call IEX API for data per ticker
final_df = pd.DataFrame(colums=my_cols)
# Limit loop to first 5 tickers due to speed
for stock in stocks['Ticker'][:5]:
    api_url = f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'
    # This will be very slow, creates an HTTP request for each ticker
    # Will optimize this with batch API call in next version
    data = requests.get(api_url).json()
    final_df = final_df.append(
        pd.Series(
            [
                stock,
                data['latestPrice'],
                data['marketCap'],
                'N/A'
            ],
            index = my_cols
        ),
        ignore_index = True
    )
