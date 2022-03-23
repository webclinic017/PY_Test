
# var1 = "hola ";
# var2 = "soy yo";
# print(var1 + var2)

# https://aprendeconalf.es/docencia/python/manual/matplotlib/
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 2, 0, 0.5])
# plt.show()

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'], marker='*')
ax.plot(dias, temperaturas['Barcelona'], marker='o', linestyle = 'dashed')
ax.set_title('Evolución de la temperatura diaria', loc="left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})

ax.set_xlabel("Días", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Temperatura ºC")

plt.show()