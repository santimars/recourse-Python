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
dt =dt.replace(year=3000) # Asignacionc correcta con .replace()
# comparando fechas y horas : datetime.time() y date.today()

print("Horas:")
hora1 = time(10,5,0) # Asigna 10h 5m 0s
print("\tHora1:",hora1)
hora2 = time(23,15,0) # Asigna 23h 15m 0s
print("\tHora2:",hora2)

# Compara horas
print("\tHora1 < Hora2: ",hora1<hora2) #True 
Fecha1 = date.today() # Asigna fecha actual 
print("\tFecha1:",Fecha1)

# suma a la fecha actual 2 dias
fecha2 = date.today() + timedelta(days=2)
print("\tFecha2: ",fecha2)

# compara fechas
print("\t Fecha1 > Fecha2:", Fecha1, fecha2) # false

''                            ''' Formateos '''
'Formato automatico ISO (Organizacion Internacional de Normalizacion)'

dt = datetime.now()
print(dt)

print(dt.isoformat()) # esto lo usan muchas bases de dato el formato ISO



'Formateo munual (Ingles por defecto)'
"""
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
"""
print(dt.strftime("%A %d %B %Y %I: %M"))

dt_formateada = dt.strftime("%Y -> %M %d :) %H_%M:%S ")
print(dt_formateada)
print(type(dt_formateada))

"""hay diferentes tipos de formas para crear el horario que nesecitamos 
podemos enviar la fecha de manera str para que no tenga ningun problema con otro programador

podemos traducir tambien als fehcas para que no esten en español

si nesecitamos la cambiar la localicacion de un lugar

usamos la libreria LOCALE"""

import locale
# para mac:
#locale.setlocale(locale.LC_ALL, 'en_US')
#locale.setlocale(locale.LC_ALL, 'en_ES')
#locale.setlocale(locale.LC_ALL, 'en-US') #Por defecto
locale.setlocale(locale.LC_ALL, 'es-ES') #establece el idioma en "es- ES"(español- España)

print(dt.strftime("%A %d %B %Y %I: %M"))
print(dt.strftime("%A %d %B del %Y - %H:%M"))

'este cambio es para este fichero'

'''Sumando y restando tiempo con timedelta'''

dt = datetime.now()
print(dt)

t = timedelta(days=14,hours=4,seconds=1000) #qui en donde dice hours podemos usar, weeks,days,hours,minutes,seconds,microseconds
print(t)

dentro_de_dos_semanas = dt + t
print(dentro_de_dos_semanas)
print(dentro_de_dos_semanas.strftime("%A %d %B del %Y - %H:%M"))

hace_dos_semanas = dt - t
print(hace_dos_semanas)
print(hace_dos_semanas.strftime("%A %d %B del %Y - %H:%M"))

"""calendar"""
#https://dateutil.readthedocs.io/en/stable/

from dateutil.relativedelta import relativedelta
fecha1 = date(year=2023,month=10,day=2)
fecha2 = fecha1 + relativedelta(years=2)#years months days hour minute second mircrosecond
print(fecha1)
print(fecha2)

'''si operamos con dias podemos usar timedelta pero si queremos trabajar con meses y años usamos relativedelta'''
"""
datetime - libreria principal
locale - podemos cambiar de localicacion
calendar -  si queremos algo concreto de un calendario
pytz - zonas horaria
dateutil - para relativedelta    
"""

import calendar

año = 2002
mes = 7
calendario = calendar.TextCalendar(calendar.MONDAY) # se establece el lunes como predertemonado
calendario.prmonth(año,mes)

#para hacer un calendario en nuestra aplicacion 

'Extra: Zonas horarias con  pytz'

import pytz
#pytz.all_timezones
print("\n".join(map(str,pytz.all_timezones)))

print("codigo y nombre de los paises")
for key, val in pytz.country_names.items():
    print(key,'=',val,end='\n')
    
print("Timezones de los paises")
for key, val in pytz.country_timezones.items():
    print(key, "=" ,val, end="\n") # nos muestra las zonas de los paises vemos sus nombres y con eso podemos pedirle a python la zona horaria que nesecitamos

dt = datetime.now(pytz.timezone('Asia/Tokyo'))
print(dt)
print(dt.strftime("%A %d %B del %Y - %H:%M")) # %I 12H - %H 24H

dt = datetime.now(pytz.timezone('Europe/Madrid'))
print(dt)
print(dt.strftime("%A %d %B del %Y - %H:%M")) # %I 12H - %H 24H

'Practicando con varias zonas'
import pytz
import datetime

# Momento actual en formato UTC (en el que suele trabajar)
now_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
# now_utc = datetime.datetime.now(pytz.utc) #otra forma
print("Fecha UTC:    ",now_utc)

#definir una zona
kiev_tz = pytz.timezone("Europe/Kiev")
print(kiev_tz.zone,end=":       ")

# Convertir el momento actual a la zona horaria indicada
kiev_now = now_utc.astimezone(kiev_tz)
print(kiev_now)

# Definir otra zona
madrid_tz = pytz.timezone('Europe/Madrid')
print(madrid_tz.zone,end=": ")

#Convertir el momento actual a la zona horaria indicada
madrid_now = now_utc.astimezone(madrid_tz)
print(madrid_now)  