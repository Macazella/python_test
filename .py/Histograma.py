import seaborn as sns
import matplotlib.pyplot as plt

# Crear el histograma
ax = sns.histplot(df['seconds'], binrange=(40, 100), binwidth=5, color='#4285F4', alpha=1)

# Ajustar las marcas del eje x
ax.set_xticks(range(35, 101, 5))

# Ajustar las marcas del eje y
ax.set_yticks(range(0, 61, 10))

# Añadir el título del gráfico
plt.title('Old Faithful geyser - time between eruptions')

# Mostrar el gráfico
plt.show()
