
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de csv
df = pd.read_csv('price.csv')

# Calculo SMA
sma_20=int(20)
df['SMA_price'] = df['Close'].rolling(window=sma_20).mean()
# print(df.head())   #check primeros values
# print(sma_price.tail())  #check ultimos values


# Plot de DataFrames
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1 = plt.subplot(211) #filas: 2, Columnas: 1, Ubicacion 1 fila)
ax1.plot(df['Date'], df['Close'], marker='*', label='Price Cripto', linestyle='solid', linewidth=3, color='#0091FF')

ax2 = plt.subplot(212, sharex=ax1) #filas: 2, Columnas: 1, Ubicacion 2 fila)
ax2.plot(df['SMA_price'], marker='.', label='SMA Cripto', linestyle='solid', linewidth=3, color='#FF5A17')

ax1.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax1.set_ylabel("Precios")

#Referencias de lineas
ax1.legend(loc='best')
ax2.legend(loc='best')

#size dibujo
anchoDibujo = int(df['Close'].size)
fig.set_figheight(10)
fig.set_figwidth(anchoDibujo)

#Lineas
plt.hlines(y=4000,  xmin=0, xmax=anchoDibujo, colors='green', linestyle='dotted', linewidth=2)
plt.hlines(y=3000,  xmin=0, xmax=anchoDibujo, colors='red', linestyle='dotted', linewidth=2)

#Rotacion de labels
plt.xticks(rotation=90)

plt.grid()
plt.show()