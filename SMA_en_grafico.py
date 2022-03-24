
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de csv
df = pd.read_csv('price.csv')

df['CloseMax'] = df['Close'] + 1000
#print(df.head())

# Calculo SMA
sma_20=int(20)
df['sma_price'] = df['Close'].rolling(window=sma_20).mean()
# print(sma_price.tail())


# Plot de df
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Close'], df['sma_price'], marker='*')
ax.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Precios")
df.plot(ax=ax)  #cuadro de referencias de lineas

#size dibujo
anchoDibujo = int(df['Close'].size)
fig.set_figheight(10)
fig.set_figwidth(anchoDibujo)

#Lineas
plt.hlines(y=4500,  xmin=0, xmax=anchoDibujo, colors='green', linestyles='solid')
plt.hlines(y=3000,  xmin=0, xmax=anchoDibujo, colors='red', linestyles='solid')

#Rotacion de labels
plt.xticks(rotation=90)

plt.grid()
plt.show()