

#Load the required libraries
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

cryptocurrencies = ['ETH-USD']

data = yf.download(cryptocurrencies, start='2022-01-01', end='2022-12-12')
print("*** Columnas:")
print(data.head().columns)

df = pd.DataFrame(data["Close"])
print(df)
df.to_csv(r'price.csv', index=True, header=True)



