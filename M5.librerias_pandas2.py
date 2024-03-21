from ast import And
from cgi import print_arguments
from traceback import print_tb
from httpx import head
from matplotlib.rcsetup import _listify_validator
import pandas as pd
import csv as csv
import matplotlib as mlt
import numpy as np
from reflex import cond
from sqlalchemy import column
import csv
import json
import sqlite3

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

# Otras funciones de formato (para texto)
d["Summary"].str.upper() #nos transforma en Mayusculas
d["Summary"].str.lower()# Nos transforma en minusculas
d["Summary"].str.capitalize()# nos transforma la primera letra de la palabra en Mayuscula
d["Summary"].str.title()# Nos transforma en titulo como esta originalmente osea Primera Letra de una palabra en Mayusulas
d["Summary"].str.swapcase()# Nos trnasforma la primera letra en minusculas y el resto en mayusculas
d["Summary"].str.contains("Cloudy") # Nos muestra en un True o False ya que evalua todas las palabras para si ver si cumple nuestra condicion
d["Summary"].unique() # nos muestra los datos unicos de esa columna
print( len( d["Summary"].unique() ))



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
# sirve para hacer condiciones y tambien como una forma de slicing

'''
iloc : Herrmaienta muy similar a loc

El metodo iloc se utiliza en los DataFrames para seleccionar los elementos en base a su ubicacion.
A diferencia de loc, con iloc podemos seleccionar filas PERO TAMBIEN COLUMNAS a traves de su indice
'''
print(d.iloc[0]) # Primera fila
print(d.iloc[:,0])# Primera columna

print(d.iloc[0:5]) # Primera cinco filas 
# Esto seria igual que con el loc
print(d.iloc[2300:2330,0:3])
print (d.iloc[[0,2,1]]) # primera, tercera y segunda fila
print(d.iloc[:,[0,2,1]]) # Primera, tercera y senga columnas
print(d.iloc[:-1])
# iloc no podemos poner condiciones como == =! >=, si queremos ponerlo debemos usar loc

'''
Agrupaciones (Groupby)
En muchos casos  es muy interesante realizar agrupaciones en base a un campo (sexo, pais, origen,etc)
'''
grouped_df = d.groupby("Summary")
print(type(grouped_df)) # Es un objeto
print(grouped_df)
# Mostremos el primer registro de cada uno
print(grouped_df.first())
print("Numero de grupos: ",len(grouped_df))

# veamos las caracteristicas y sus conincidencias
print(grouped_df.size()) 

# Preguntemos por una categoria
grouped_df.get_group("Light Rain")["Humidity"].count()
grouped_df.get_group("Light Rain")["Humidity"].mean()
print(d.groupby("Summary"))

group = d.groupby(["Summary","Precip Type"]) # puedo hacer agrupaciones con diferentes grupos
print(group)

'''
Conversion
Es ocasiones, se nesecita una serie de pandas en una lista poara poder trabajar de forma nativa
desde Python
'''

temps = d["Temperature (C)"]
print(type(temps)) # Como se ve es una serie de panda
temps_list = d["Temperature (C)"].tolist()
print(type(temps_list))

print("\nListado de temperaturas")
for t in temps_list:
    print(round(t,3))

"""
Exportacion 

vamos a seleccionar un trozo de nuestro CSV y vamos a exportarlo en varios formatos
"""
df_ordenado = d.sort_values(by=["Temperature (C)"],ascending=False)
df_final = df_ordenado.iloc[0:100,0:5] #    primeras 100 filas y primeras 5 columnas
print(df_final)

media_humedad = d["Humidity"].mean()

condicion = (df_ordenado["Humidity"] <= media_humedad) & (df_ordenado["Summary"].str.contains("cloudy",case=False))
df_final  = df_ordenado.loc[condicion,:]
print(df_final)

df_final = df_final.reset_index(drop=True)

df_final = df_final.iloc[0:100,[1,5,9,2]]


# Creamos una nueva columna calculada
d["TempLevel"] = 0  # valor inicial para todas las filas

condicion_positiva = d["Temperature (C)"] > 0
condicion_negativa = d["Temperature (C)"]<= 0
listado_columna = ["TempLevel"]
d.loc[condicion_positiva,listado_columna] = 1
d.loc[condicion_negativa,lista_columnas] = 0

#d.drop([4],axis=0)
#d.drop([4,10],axis=0)
#d.drop([range(4,8,1)],axis = 0)
#d.drop(["Summary", "TempLevel"],axis = 1)
# axis = 0  filas & axis =  1 columnas
'''
Exportacion a CSV
'''
ruta_csv = r"./EXPORT_weather.csv" #r = raw que en spanish es crudo
df_final.to_csv(ruta_csv, index= False, header = True, sep= ",")

"Exportacion a Excell"
ruta_excell = r"./EXPORT_weather.xlsx" 
df_final.to_excel(ruta_excell, index= False, header= True,sheet_name= 'Tiempo')

'''
Exportacion a JSON
'''
ruta_json =r"./EXPORT_weather.json"
df_final.to_json(ruta_json,orient="columns")

"Exportacion a HTML"
ruta_html = r"./EXPORT_weahter.html"
df_final.to_html(ruta_html,index=False)