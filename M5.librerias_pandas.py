'''
Para usar pandas es solo para usar el 100% de los datos,
si deseamos hacer cambios en un excel o un csv usamos sus respectivas
librerias: openpyxl y csv

Con pandas podremos hacer lo que sea con nuestros datos, el manejo de datos de pandas 
es muy diferente a comolo maneja python, tiene su propia forma de hacer sus datos.
es un todo terremo para analisis de datos y machine learning 
'''
import pandas as pd
# esto es para usarlo cuando estemos usando pandas en jupyter  ----->    %matplotlib inline|
import matplotlib.pyplot as plt
# la siguiente instruccion permite incorporar las graficas en este documento
import  numpy as np

'''
Conozcamos pandas

pandas tiene 3 estructuras de datos principales
DataFrame
Series
Panels (mas avanzada)

DataFrame

es una estructura de datos tabular que se compone de columas y filas ordenadas. Para que todo
se mas sencillo vamos a ver un ejemplo de creacion de un DataFrame(tabla) de un diccionario de
listas. El siguiente Ejemplo muestra un diccionario que consta de dos keys, Name y Age. Y su 
correspondiente lista de valores.
'''

name_age = {

    "Name":["Ali","Bill","David", "Hany","Itsima"],
    "Age" :[32, 55, 20, 43, 30]
}
dataframe =pd.DataFrame(name_age)
print(dataframe)
# Jupyter nos genera una bonita visualizacon de las tablas
# si ponemos la variable en vez de poner print(dataframe)

name_age = {'Name' : ['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'], 
            'Age' : [32, 55, 20, 43, 30]}
data_frame = pd.DataFrame(name_age)
print (data_frame )
# Jupyter nos genera una visualización especial de las tablas si ponemos la variable directamente en vez de en un print (data_frame)

# Se pueden generar alias para los nombres de nuestras filas
data_frame_2 = pd.DataFrame(name_age, columns = ['Name', 'Age'], index = ['a', 'b', 'c', 'd', 'e'])
print(data_frame_2)

'''
Series es un objeto unidemiensional similar a la columna de una tabla si queremos crear un Series para un listado de nombre, opdemos hacer lo siguiente:
'''
series = pd.Series(['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
index = [1, 2, 3, 4, 5])
print(series)
'''
La libreria Pandas tiene varias funciones, vamos a ver algunos ejemplo de las que podemos utilizar con DataFrame y Series.

Las funciones head() y tail() nos permiten ver una muestra de nuestros, datos especialmente cuando tenemos muchisimos.El numero por defecto de elementos a mostrar es 5, pero se puede modificar.

Digamos que tenemos un Series compuesto de 20,000 elementos aleatorios (numeros):
'''
series = pd.Series(np.random.randn(20000))
print(series.head())
print(series.tail())

# Mediante el metodo add() podemos sumar elementos de varios DataFrame:

dict_1 = {'A' : [5, 8, 10, 3, 9], 'B' : [6, 1, 4, 8, 7]}
dict_2 = {'A' : [4, 3, 7, 6, 1], 'B' : [9, 10, 10, 1, 2]}
data_frame_1 = pd.DataFrame(dict_1)
data_frame_2 = pd.DataFrame(dict_2)
data_frame_3 = data_frame_1.add(data_frame_2)
print(data_frame_1)
print(data_frame_2)
print(data_frame_3)
