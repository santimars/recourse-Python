from cgi import print_arguments
import pandas as pd
import csv as csv
import matplotlib as mlt
import numpy as np
from reflex import cond
from sqlalchemy import column

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

print(d['Humidity'].head(10))

# para obtener el minimo, el maximo y el promedio de una columna

print(d['Humidity'].min())
print(d['Humidity'].max())
print(d['Humidity'].mean())

print(d['Humidity'][:1000].mean())# lo primero que hace es ir a la columna humedad luego filtra la 1000 lineas y lugo hace un promedio
print(d[:1000]['Humidity'].mean())


'''
y por ultimo, para el uso de condicionales (d[”columna”][”condicion”]),
donde se devuelven todos los valores de una “columna” que cumplan una “condicion”:
'''
"""
# Ordenacion y Seleccion de series
temps = d['Temperature (C)'].hist()
print(type(temps)) # como se ve, temps es una serie de panda
temps_ordenadas = temps.sort_values(ascending=False)
print(temps_ordenadas[:10])
# Mostrar la temperatura cuya humedad sea menor o igual que la media de humedades
"""
#Una forma de hacerlo
df_ordenado = d.sort_values(by=["Temperature (C)","Apparent Temperature (C)"],ascending=False)
print(df_ordenado)
print(df_ordenado[:10])


# Para obtener un histograma, la distribucion de los datos de una columna:

print(d['Temperature (C)'].hist())
print(d['Temperature (C)'].plot(kind="kde"))


'''Condiciones simples'''
# df["columna"]["condicion"]
'''
Se devuelve todos los valores de esa columna que cumpla la condicion
con este metodo podemos mostrar:

- Una sola columna
- Todo el dataframe
No podemos, mostrar un numero determinado de columnas, para ello usaremos loc
'''
media_humedad = d['Humidity'].mean()
print("Media de humedad: ",media_humedad)

columna = 'Humidity'
condicion = d['Humidity'] <= media_humedad
print(d[columna][condicion])

# mostrar una columna diferente, de la que se usa para evaluar la condicion 
d['Temperature (C)'][d['Humidity'] <= media_humedad]

#Mostramos toso el dataframe (todas las columnas) que cumplan una condicion
#df [condition]
print(d[d['Humidity']<= media_humedad])# recordemos que no nesecitamos usar print() estando en jupyter como lo estoy haciendo en python tengo que usarlo ya que no reponde con pandas en python

# Mostremos todo el dataframe (todas las colunmas) que cumplan una condicion
#d[condicion]
print(d[d["Summary"] == "Foggy"]) # Si queremos evaluar si es distinto : !=


# Condicion multiple con AND (&)
# &: and (y logico)
# |: or (o logico)
print(d[ (d["Summary"]== "Foggy") & (d["Precip Type"] =="snow" )])

# Condicion multiple  con OR (|)
# &: and (y logico)
# |: or (o logico)
print(d[ ( d["Summary"]== "Foggy") | (d["Precip Type"] == "snow") ] )

#Aplicar un condicional y guardar el resultado en un nuevo dataframe
df2 = d[ (d["Humidity"] == "Foggy") & (d["Precip Type"] == "snow")]
print(df2)

'''
Condicionales complejos : Loc

Con el metodo anterior o mostramos el dataframe completo o solo una columna, pero si queremos aplicar un condicional
y mostrar 2, 3 o 4 columnas no podemos, asi que para estos casos usaremos el metodo loc, cuya estructura es la siguiente:

df.loc[condicion,[columna1,columna2,columna3]]

Se devuelve todos los valores de esas columnas que cumplan la condicion. Con este metodo podemos mostrar todas las
columnas que queramos.
'''

# Estructura de loc
# df.loc[condicion,[columna1,columna2,columna3]]
print(d.loc[d["Humidity"]<= media_humedad,["Humidity","Temperature (C)"] ])

# Alternativa de sintaxis al bloque anterior
condition = d["Humidity"] <= media_humedad
lista_columnas = ["Humidity", "Temperature (C)"]
print(d.loc[condicion, lista_columnas])

# Mostrar todas las columnas (:) que cumplan la condicion
print ("Columans que cumplen la condicion\t")
print(d.loc[ d["Humidity"]<= media_humedad, :])

print(d.loc[10:15,["Humidity","Temperature (C)"]])


print(d.loc[10]) # esto es equivalente a d.loc[10, : ]
print(d.loc[10:12]) #esto es equivalente a d.loc[10, 12, :]
# sirve para hacer condiciones y tambien como una forma de sclising

'''
iloc : Herrmaienta muy similar a loc

El metodo iloc se utiliza en los DataFrames para seleccionar los elementos en base a su ubicacion.
A diferencia de loc, con iloc podemos seleccionar filas PERO TAMBIEN COLUMNAS a traves de su indice
'''
print(d.iloc[0]) # Primera fila
print(d.iloc[:,0])# Primera columna

print(d.iloc[0:5]) # Primera cinco filas 
# Esto seria igual que con el loc
 