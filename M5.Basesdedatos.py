
'''
tener en cuenta que todas la aplicaciones tiene una grande cantidad de bases de datos
por ello es importante en saber manejar mas datos

es mejor diseñar una gran cantidad de datos para que el futuro se preparan para conectar su 
informacion

 a mayor cantidad de datos esta preparadas para analizar muchos datos para que no sean lentas


los programas edducativos se sengundo plano se dejan las bases de datos cuando el 100 por 100 va por 
las bases de datos 

bases de datos distribuidas
'''
# Bases de datos SQLITE

'''

id pedido
fecha
id producto
numero de producto
precio
unidades
si queremo ver los datos en total lo hacemos en programacion 
la redundancia de datos se trata de que no pase 

'''
'''
normalizacion 
ver los elementos que puedo dividir
peude ser | pedido y fecha  |   id  nombre producto precio | 


podemos ahora organizar en que areas hacen parte para pedido y cuales son mas revelantes para producto

ahora como unimos estas 2 tablas
vemos que estan exactamente iguales
hay quehacer una relacion para que las tablas se relaciones

esta ls primary key y la foring key 
una es al principal y la otra es la relacion 

hoy en dia el problema mundial de los datos es la redundancia de datos
ellos tienen muchas informacion repetida

cuando hagamos un prymary key que puedan todos tener 
hagamos un identificador artificial algo que nosotros podamos hacer
algo que podamos lograr hacer sin nesecidad de saber que se va a repetir 
'''



'''Creacion de una tabla utilizando sintaxis SQL

Antes de ejecutar una consulta (query) en codigo SQL, tenemos que crear un cursor

una vez creada la tabla, si intentamos volver a crearla data error indicandonos que esta ya existe.

'''
# Importamos 
import sqlite3

# Nos conectamos ala base de datos ejemplo.db ( la crea si no existe)
conexion =  sqlite3.connect("ejemplo.db")# connect puede acpetar hasta un usuario y contraseña y otros parametros 

# creamos el cursor
c = conexion.cursor()

#Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails.
c.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAT(100))")# esta es una intruccion sql osea Sintaxis sql
# Guardamos los cambios haciendo commit
conexion.commit()# la informacion ha codificado la informacion no se puede visualizar para ellos se usa un programa para ver la visualizacion
# cerramos la conexion, si no la cerramos se mantendra en uso y no podemos gestionar el fichero
conexion.close()
