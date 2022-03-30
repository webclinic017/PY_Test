
import pandas as pd
from stocktrends import indicators

df = pd.read_csv('price.csv')
df.columns = [i.lower() for i in df.columns]
print("*** df: \n", df)

renko = indicators.Renko(df)
renko.brick_size = 100
renko.chart_type = indicators.Renko.PERIOD_CLOSE
data_RK = renko.get_ohlc_data()
print('\n **** Renko', data_RK)
