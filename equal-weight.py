import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secret import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'

data = requests.get(api_url)
print(data)