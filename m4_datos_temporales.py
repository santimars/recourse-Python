from datetime import datetime, date, time, timedelta
"Datos temporales"
"""
'Problemas con las zonas horarias'
Todos los dias tiene 24 horas
el horario de verano va desde primavera a otoño
todas las horas tienen 2600
GMT Y UTC son los mismo
todos los paises cambia a horario de verano e invierno al mismo tiempo
las zonas horarias se miden incrementos o decrementos de 1 hora desde GMT
la maxima diferencia horaria posible es de 24 horas    
"""
"""
Todo esto es falso    
"""
"Usammos diferentes usos horarios"
'''
cuando desarollamos software, hay que tener presente que manejamos diferentes usos horarios:
-servidor
-base de datos
-back end
-front end (el cliente, navegador, movil, ordenador, etc)
'''
"utc usamos este uso horario"
"""
debemos tener muy encuenta el horario en el que vamos a hacer en nuestros ya que cada
modelo de conjuntos de servidores, bases de datos y otras cosas mas pueden tener muchas fechas de horarios
por eso tenemos que partir con una fecha de inicio como tal
por eso debemos tomar la fecha del servidor sea el que sea ya que este no se puede cambiar la fecha
hay que acostumbrase a la zona horaria del servidor


solucion en python
tenemos varias librerias para poder ayudarnos para controlar diferentes aspectos del tiempo

Modulo de tiempo
time()
datetime()
calendar()

world timezone definitions for python = pytz

IANA Timezone Database:
iana.org/time-zones


se manejan las fechas por tipo str para verlas y ver si son validas antes de hacer eso 
"""
dt = datetime.now() # el horario actual
print(dt)
print(type(dt))
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.microsecond)
print(dt.tzinfo) #zona horaria nula por defecto

print("{}: {}: {}".format(dt.hour,dt.minute,dt.second))
print("{}/{}/{}".format(dt.day,dt.month,dt.year))

""" Crear un datatime manualmente (year, moth, day, hour = 0, minute = 0, second = 0, microsecond = 0, tzinfo = None)"""
#Nota que solo son obligatorios el año, el mes y el dia
dt  = datetime(2019,2,28,10,15,00,00000)
print(dt)
print(type(dt))
