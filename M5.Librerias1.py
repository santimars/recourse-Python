'''Librerías especializadas en el manejo de datos I
pypi.org

al buscar en la documentacion de una libreria ir siempre a API references que nos muestra todo lo que puede hacer la libreria'''
"1 Numpy"
import numpy
'''
Un array es una lista

'''
nums = [1,2,3,4]
#array de una dimension
mi_primer_array = numpy.array(nums)
# podemos ver la version de numpy
numpy.__version__

#podemos usar print
print(mi_primer_array)
#comprobar el tipo de dato que contiene
print(type(mi_primer_array))
'''
los arrays de una dimension se crean pasandole una lista como argumentos a la funcion numpy.array. Para ccrear un array de
dos dimensiones le pasaremos una lista de listas:
'''
mi_segundo_array = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(mi_segundo_array)

'''
En ocasiones es un lio escribirlo todo en una linea, por lo que podemos escribirlo en lineas separadas, siempre y cuando
cuidemos el formato. Esto seria una buena manera de definirlo, de acuedo con el PEP 8(indetation):
'''

'''Funciones y constantes de NumPy

Numpy tambien incorpora funciones. Un ejemplo sencillo:
'''
# Suma
print("suma")
print(numpy.sum(mi_primer_array))

# Máximo
print("Maximo")
print(numpy.max(mi_primer_array))

# Seno
print("Seno")
print(numpy.sin(mi_segundo_array))