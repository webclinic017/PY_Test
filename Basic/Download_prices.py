

#Load the required libraries
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# list of crptocurrencies as ticker arguments
# cryptocurrencies = ['BNB-USD','BTC-USD', 'ETH-USD', 'XRP-USD']
cryptocurrencies = ['BNB-USD']

data = yf.download(cryptocurrencies, start='2022-01-01', end='2022-12-12')
print(data.head().columns)
print(data["Close"].head())





