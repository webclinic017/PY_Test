
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de csv
df = pd.read_csv('price.csv')

df['CloseMax'] = df['Close'] + 1000
print(df.head())

# Plot de df
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Close'], df['CloseMax'], marker='*')
ax.set_title('Precios', loc="left", fontdict = {'fontsize':8, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Precios")
df.plot(ax=ax)
plt.show()