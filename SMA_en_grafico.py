
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de csv
df = pd.read_csv('price.csv')

# Calculo SMA
sma_20=int(20)
df['SMA_price'] = df['Close'].rolling(window=sma_20).mean()
# print(df.head())   #check primeros values
# print(sma_price.tail())  #check ultimos values

# Plot de df
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Close'], marker='*', label='Price Cripto', linestyle='solid', linewidth=3, color='#0091FF')
ax.plot(df['SMA_price'], marker='.', label='SMA Cripto', linestyle='solid', linewidth=3, color='#FF5A17')

ax.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Precios")

#Referencias de lineas
ax.legend(loc='best')
# df.plot(ax=ax)

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