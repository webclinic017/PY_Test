
import pandas as pd
import pandas_ta.overlap as ta_overlap

from stocktrends import indicators

# df = pd.read_csv('HDFCLIFE.csv')
# df.columns = [i.lower() for i in df.columns]

df = pd.read_csv('price.csv')
df.columns = [i.lower() for i in df.columns]

#df['HL2'] = ta_overlap.hl2(high=df['High'], low=df['Low'])
#print("\n *** HL2: \n", df['HL2'])

print("\n *** df: \n", df)

renko = indicators.Renko(df)
renko.brick_size = 100
renko.chart_type = indicators.Renko.PERIOD_CLOSE
data_RK = renko.get_ohlc_data()
print('\n **** Renko', data_RK)
