
# https://www.statology.org/matplotlib-python-candlestick-chart/

import pandas as pd
import matplotlib.pyplot as plt

# #create DataFrame
# prices = pd.DataFrame({'open': [25, 22, 21, 19, 23, 21, 25, 29],
#                        'close': [24, 20, 17, 23, 22, 25, 29, 31],
#                        'high': [28, 27, 29, 25, 24, 26, 31, 37],
#                        index=pd.date_range("2021-01-01", periods=8, freq="d"))
#                        'low': [22, 16, 14, 17, 19, 18, 22, 26]},

#Lectura de csv
df = pd.read_csv('price.csv')
df['HL2'] = (df['High']+df['Low'])/2

#display DataFrame
print(df)

#create figure
plt.figure()

#define width of candlestick elements
width = .4
width2 = .05

#define up and down prices
up = df[df.Close>=df.Open]
down = df[df.Close<df.Open]

#define colors to use
col1 = 'green'
col2 = 'red'

#plot up prices
plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)

#plot down prices
plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)

#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')

#display candlestick chart
plt.show()