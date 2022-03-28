
import pandas as pd
import pandas_ta as ta
#
# #Lectura de csv
# df = pd.read_csv('price.csv')
# df['HL_div_2'] = (df['High']+df['Low'])/2
# df_HL = pd.DataFrame()
# df_HL.append(df, ignore_index=True)
# print (df_HL.head())

# first DF
df = pd.read_csv('price.csv')
df['HL_div_2'] = (df['High']+df['Low'])/2

# print the DataFrame
#print(df['HL_div_2'].head())

# create a new DataFrame
df_HL = pd.DataFrame()
df_HL = pd.concat([df, df_HL], axis=1)

df_HL = df_HL.drop(['Open','High','Open','Low','Close','Adj Close','Volume'], axis=1)

# concat and Print the new DataFrame
print(df_HL.head())
