
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de csv
df = pd.read_csv('price.csv')

df['CloseMax'] = df['Close'] + 1000
#print(df.head())

# Plot de df
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Close'], df['CloseMax'], marker='*')
ax.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Precios")
df.plot(ax=ax)

#size dibujo
anchoDibujo = int(df['Close'].size)
fig.set_figheight(10)
fig.set_figwidth(anchoDibujo)

#Lineas
plt.hlines(y=4500,  xmin=0, xmax=anchoDibujo, colors='green', linestyles='solid')
plt.hlines(y=3000,  xmin=0, xmax=anchoDibujo, colors='red', linestyles='solid')

plt.grid()
plt.show()