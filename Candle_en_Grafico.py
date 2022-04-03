
import pandas as pd
import mplfinance as mpf
import pandas_ta.overlap as ta_overlap
import pandas_ta.momentum as ta_momentum
import pandas_ta.trend as ta_trend

#Lectura de csv
df = pd.read_csv('price.csv')
df['HL2'] = (df['High']+df['Low'])/2

df.index = pd.DatetimeIndex(df['Date'])

# Calculo SMAs
size_sma_min=int(3)
sma_rapida=int(3)
df['SMA_Rapida'] = ta_overlap.sma(close=df['HL2'], length=sma_rapida, talib=True)

sma_lenta=int(6)
df['SMA_Lenta'] = ta_overlap.sma(close=df['HL2'], length=sma_lenta, talib=True)

# # Calculo RSI
rsi_periodo=int(16)
df['RSI'] = ta_momentum.rsi(close=df['HL2'], length=rsi_periodo, scalar=None, talib=True)
df['SMA_RSI'] = ta_overlap.sma(close=df['RSI'], length=rsi_periodo, talib=True)
# # print(df.head())   #check primeros values
# # print(df.tail())  #check ultimos values

# Plot de DataFrames
fig = mpf.figure()
ax1 = fig.add_subplot(2,1,1, style='yahoo')
ax2 = fig.add_subplot(2,1,2, sharex=ax1, style='yahoo')

#ax1.plot(df['Date'], df['Close'], marker='*', label='Price Cripto', linestyle='solid', linewidth=3, color='#0091FF')

ap = [ mpf.make_addplot(df[['RSI','SMA_RSI']],type='line', ax=ax2),
       mpf.make_addplot(df[['SMA_Rapida','SMA_Lenta']], type='line', ax=ax1)
     ]


# Segundo grafico
#Hlines grafico
anchoDibujo = int(df['Close'].size)
ax2.hlines(y=30,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)
ax2.hlines(y=50,  xmin=0, xmax=anchoDibujo, colors='grey', linestyle='dotted', linewidth=2)
ax2.hlines(y=70,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)

# Titulos
ax1.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax2.set_title('RSI', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})

#Referencias de lineas
# ax1.legend(loc='best')
# ax2.legend(loc='best')

#size dibujo
fig.set_figheight(10)
fig.set_figwidth(anchoDibujo)

#Ocultar "escala x" en ax1
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(True)

#Grilla
ax1.grid(),ax2.grid()


# Plot grafico
mpf.plot(df, type='candle', ax=ax1, addplot=ap, xrotation=90, datetime_format='%Y-%m-%d')
mpf.show()


