
import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta.overlap as ta_overlap
import pandas_ta.momentum as ta_momentum
import pandas_ta.trend as ta_trend

#Lectura de csv
df = pd.read_csv('price.csv')
df['HL2'] = (df['High']+df['Low'])/2
#print(df['HL2'].head())

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
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1 = plt.subplot(211) #filas: 2, Columnas: 1, Ubicacion 1 fila)
ax1.plot(df['Date'], df['Close'], marker='*', label='Price Cripto', linestyle='solid', linewidth=3, color='#0091FF')
ax1.plot(df['Date'], df['SMA_Rapida'], marker='*', label='SMA Rapida', linestyle='solid', linewidth=2, color='green')
ax1.plot(df['Date'], df['SMA_Lenta'], marker='*', label='SMA Lenta', linestyle='solid', linewidth=2, color='#FF5A17')

ax2 = plt.subplot(212, sharex=ax1) #filas: 2, Columnas: 1, Ubicacion 2 fila)
ax2.plot(df['RSI'], marker='.', label='RSI', linestyle='solid', linewidth=3, color='green')
ax2.plot(df['SMA_RSI'], marker='.', label='RSI', linestyle='solid', linewidth=3, color='red')

#Hlines grafico
anchoDibujo = int(df['Close'].size)
ax2.hlines(y=30,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)
ax2.hlines(y=50,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)
ax2.hlines(y=70,  xmin=0, xmax=anchoDibujo, colors='orange', linestyle='dotted', linewidth=2)

ax1.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax1.set_ylabel("Precios")

#Referencias de lineas
ax1.legend(loc='best')
ax2.legend(loc='best')

#size dibujo
fig.set_figheight(10)
fig.set_figwidth(anchoDibujo)

#Ocultar "escala x" en ax1
ax1.xaxis.set_visible(False)

#Rotacion de labels
plt.xticks(rotation=90)

#Mostrar rango de items en grafica
plt.xlim(size_sma_min,)

#Grilla
ax1.grid(),ax2.grid()

plt.show()


