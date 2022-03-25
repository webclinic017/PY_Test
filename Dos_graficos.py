
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de csv
df = pd.read_csv('price.csv')

# Calculo SMA
size_sma_max=int(20)
sma_20=int(20)
df['SMA_20_price'] = df['Close'].rolling(window=sma_20).mean()

sma_10=int(10)
df['SMA_10_price'] = df['Close'].rolling(window=sma_10).mean()
# print(df.head())   #check primeros values
# print(sma_price.tail())  #check ultimos values

# Plot de DataFrames
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1 = plt.subplot(211) #filas: 2, Columnas: 1, Ubicacion 1 fila)
ax1.plot(df['Date'], df['Close'], marker='*', label='Price Cripto', linestyle='solid', linewidth=3, color='#0091FF')
ax1.plot(df['Date'], df['SMA_20_price'], marker='*', label='SMA 20', linestyle='solid', linewidth=3, color='#FF5A17')

ax2 = plt.subplot(212, sharex=ax1) #filas: 2, Columnas: 1, Ubicacion 2 fila)
ax2.plot(df['SMA_10_price'], marker='.', label='SMA 10', linestyle='solid', linewidth=3, color='green')

ax1.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax1.set_ylabel("Precios")

#Referencias de lineas
ax1.legend(loc='best')
ax2.legend(loc='best')

#size dibujo
anchoDibujo = int(df['Close'].size)
fig.set_figheight(10)
fig.set_figwidth(anchoDibujo)

#Hlines solo para grafico ax1
ax1.hlines(y=3400,  xmin=0, xmax=anchoDibujo, colors='green', linestyle='dotted', linewidth=2)
ax1.hlines(y=2500,  xmin=0, xmax=anchoDibujo, colors='red', linestyle='dotted', linewidth=2)

#Ocultar "escala x" en ax1
ax1.xaxis.set_visible(False)

#Rotacion de labels
plt.xticks(rotation=90)

#Mostrar rango de items en grafica
plt.xlim(size_sma_max,)

#Grilla
ax1.grid(),ax2.grid()

plt.show()