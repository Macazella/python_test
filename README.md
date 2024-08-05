# Python_test_selenium
Aquí insertaré mis primeros códigos en Python

Para crear un histograma similar al que has descrito utilizando Seaborn en Python, sigue estos pasos completos, incluyendo cómo preparar la base de datos y el código necesario. 

  

### 1. Preparar el entorno 

  

Primero, asegúrate de tener las librerías necesarias instaladas. Si no lo has hecho, instálalas usando `pip`: 

  

```bash 

pip install seaborn matplotlib pandas 

``` 

  

### 2. Crear o cargar la base de datos 

  

Aquí vamos a utilizar una base de datos ficticia para ilustrar el proceso. Puedes crear un archivo CSV con datos simulados o usar una base de datos existente. 

  

Para este ejemplo, supongamos que tienes un archivo CSV llamado `data.csv` con una columna llamada `seconds` que contiene tiempos entre erupciones. Aquí está cómo podrías crear un archivo CSV ficticio y cargarlo en un DataFrame de pandas: 

  

#### Crear archivo CSV (opcional) 

Si no tienes un archivo CSV, puedes crear uno con el siguiente contenido: 

  

```csv 

seconds 

50 

55 

60 

65 

70 

75 

80 

85 

90 

95 

100 

``` 

  

Guarda esto en un archivo llamado `data.csv`. 

  

### 3. Cargar los datos en un DataFrame 

  

Ahora, carga el archivo CSV en un DataFrame de pandas: 

  

```python 

import pandas as pd 

  

# Cargar el archivo CSV 

df = pd.read_csv('data.csv') 

``` 

  

### 4. Crear el histograma con Seaborn 

  

Aquí está el código para crear el histograma, usando la columna `seconds` del DataFrame `df`: 

  

```python 

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

``` 

  

### Explicación del código 

  

1. **Importar librerías**: `seaborn` para crear el histograma y `matplotlib.pyplot` para personalizar y mostrar el gráfico. 

2. **Crear el histograma**: `sns.histplot()` toma la columna de datos `df['seconds']` y ajusta parámetros como el rango de los bins (`binrange`), el ancho de los bins (`binwidth`), el color (`color`), y la opacidad (`alpha`). 

3. **Configurar los ejes**: `set_xticks()` y `set_yticks()` definen las posiciones de las marcas en los ejes x e y, respectivamente. 

4. **Añadir título**: `plt.title()` agrega un título al gráfico. 

5. **Mostrar gráfico**: `plt.show()` renderiza y muestra el histograma. 

  

### Ejecución 

  

Guarda el código anterior en un archivo Python (por ejemplo, `histograma.py`) y ejecútalo con Python para ver el histograma. 
