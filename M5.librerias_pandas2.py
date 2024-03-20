import pandas as pd
import csv as csv
import matplotlib as mlt
import numpy as np

'''
Para carga de datos y exploracion trabajaremos con el fichero 
csv 05_03_weather.csv, que se encuentra dentro de la carpeta correspondiente
en el proyecto Anaconda Jupyter. Para cargarlo procedemos de la siguiente manera:
'''

d = pd.read_csv('05_03_weather.csv')

print(d)
#para obtener su numero de filas:
# Número de filas
print(len(d))

# Para saber los indices de filas  y los encabezados de las columnas:
print(d.index)

print(d.columns)    
#Para obtener todos los valores:
print(d.values)
# Para obtener informacion general del DataFrame:

# Info general
d.info()
# Para acceder a las primera o las ultimas fils del DataFrame usaremos las funciones head() o tail():

# head y tail
d.head() # Primeras 5 filas 


# head y tail
d.head(10) # Primeras 10 filas 

# head y tail
d.tail() # Ultimas 5 filas 


# head y tail
d.tail(10) # Últimas 10 filas 

# Para hacer slicing al DataFrame y obtener los valoes de las filas ubicados entre 2 filas indicadas:

# Obtener 5 filas entre la 20 y 24
d[20:25]

# Para acceder a una columna en concreto:
# Acceder a una columna en particular del dataframe
d['Humidity'].head(10)

# para obtener el minimo, el maximo y el promedio de una columna

print(d['Humidity'].min())
print(d['Humidity'].max())
print(d['Humidity'].mean())

# Para obtener un histograma, la distribucion de los datos de una columna:

d['Temperature (C)'].hist()

'''
y por ultimo, para el uso de condicionales (d[”columna”][”condicion”]),
donde se devuelven todos los valores de una “columna” que cumplan una “condicion”:
'''

# Mostrar la temperatura cuya humedad sea menor o igual que la media de humedades

