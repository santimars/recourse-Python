# comenzaremos a ver como usar la liberirias statistics
'''
La librería statistics en Python proporciona funciones para realizar cálculos estadísticos básicos. 
Aquí te dejo una breve guía sobre cómo puedes usar algunas de las funciones más comunes de esta librería.

Primero, debes importar la librería:
'''
import statistics
'''
A continuación, puedes utilizar diversas funciones para realizar cálculos estadísticos:
'''

#Media (Promedio):
data = [1, 2, 3, 4, 5]
mean_value = statistics.mean(data)
print("Media:", mean_value)

#Mediana:

data = [1, 2, 3, 4, 5]
median_value = statistics.median(data)
print("Mediana:", median_value)

#Moda:

data = [1, 2, 2, 3, 4]
mode_value = statistics.mode(data)
print("Moda:", mode_value)
'Ten en cuenta que statistics.mode() lanzará una excepción StatisticsError si no hay una moda clara.'

#Desviación estándar y varianza:
data = [1, 2, 3, 4, 5]
stdev_value = statistics.stdev(data)
variance_value = statistics.variance(data)

print("Desviación estándar:", stdev_value)
print("Varianza:", variance_value)

#Percentiles:
data = [1, 2, 3, 4, 5]
percentile_50 = statistics.percentile(data, 50)
percentile_75 = statistics.percentile(data, 75)

print("Percentil 50:", percentile_50)
print("Percentil 75:", percentile_75)

#Frecuencia acumulativa:

data = [1, 2, 2, 3, 4]
cumulative_freq = statistics.cumulative_freq(data)
print("Frecuencia acumulativa:", cumulative_freq)

#Frecuencia acumulativa relativa:


data = [1, 2, 2, 3, 4]
cumulative_rel_freq = statistics.cumulative_rel_freq(data)
print("Frecuencia acumulativa relativa:", cumulative_rel_freq)

#Rango:

data = [1, 2, 3, 4, 5]
range_value = statistics.range(data)
print("Rango:", range_value)

#Mediana baja (percentil 50):

data = [1, 2, 3, 4, 5]
median_low_value = statistics.median_low(data)
print("Mediana baja:", median_low_value)
#Mediana alta (percentil 50):
data = [1, 2, 3, 4, 5]
median_high_value = statistics.median_high(data)
print("Mediana alta:", median_high_value)