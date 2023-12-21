#...................................................................................primer modulo
 
""           """Empiezo otra vez ya que no se encontro practica.py""" 
gracias = "gracias"

# hay palabras reservadas en  python
"""and
as()
assert()
async()
await()
break()
class()
continue()
def()
del()
elif()
else()
except()
False()
finally()
for()
from()
global()
if()
import()
is()
lambda()
None
nonlocal()
not
or
pass
raise
return
True
try
while
with
yield """ 
''           """Palabras reservadas, tipo de datos, variables, constantes y 
                operadores"""

"Comentarios"
# se pueden hacer comentarios en python usando el simbolo # 
# se puede sacar con atl 3
# se pueden hacer de una sola linea #  o multilinea """ """ ''' '''
dsdf = print( "Mundo Hola")

'''                              Tipos de datos                                             '''

# estan los datos Numericos, Diccionario, Booleanos, Sets(Conjuntos), 

#str
california= "las cosas que nunca se tendrán"
print(california)

#int
d=34
e=45
s=67
m= s+e+d
print(m)
                                    
#boleeano
pedro=1
print(pedro==1)
''                           'Entrada de datos'
valor = 45
print(type(valor)) 


#  Tipos de secuencia 
''                           '''' operadores de asignacion '''

#        Permite asignar un valor a una varianle, usando para ello el operador "=" Estos operadores permiten realizar llamada asignacion aumentada, tecnica
#        que implica un codigo mas corto de describir , la vez que mas ediciente en tiempo de ejecicionn esta asignacion aunkmentada se realiza generalmente
#        entre operadores numericos.4

"="#asina el valor del operando de la parte derecha al de la izquieda 
# x = "y"
"+="# suma el valor que hay en el operando de la parte izquierda al de la derecha y lo asigna al de la izquierda 
# x += y
"-=" # resta el valor que hay en el operando dee la parte izquierda al de la derecha y lo asigna al de la izquierda
#x -= y
"**="# lleva el valor que hay en el operando de la parte izquierda al de la derecha y lo asigna al de la izquierda
#x *= y (x = x ** y)
"/="# divide el valor que hay en el operando de la parte izquierda al de la parte derecha y lo asigna al de la izquierda 
# x /= y (x = x ** y)
"//=" # realiza la division entera del valor del operador de la parte izquierda entre el de la derecha y lo asigna al de la izquierda
# x//= y (x = x //y)	
" %= "# realiza la division entera del valor del oprerando de la parte izqauierda entre el de la derecha y lo asigna al de la izquierda:
# x %= y (x = x % y)
"*="# Multiplica el valor que hay en el operando de la parte izquierda al de la derecha y lo asigna al de la izquierda:
# x *= y (x = x * y)

''                                    ''' Operadores aritmetricas '''
" % "# modulo          [7%2=1]      resto de la division entera de x ente y 
"+"# suma              [2+5=7]      x mas y
"-"# resta             [5-3=6]      x menos y
"*"# Multiplicación    [3*2=6]      x multiplicado por y
"**" #exponente        [2**4=16]    x elevado a y
"/"# division          [6/2=3]      x division entre y
"//"#division entera   [7/2=3]      cociente de la division entera de x entre y
"-"# negacion          [-5=-5]      valor x en negativo


''                                    '''Operadores relacionales '''
"" ''' nos permiten comparara dos o mas valores y nos devuelven un resultado booleano'''
"=="# igualdad   Evalua si el valor del operador de la izquierda es igual que el de la derecha , devolvioendo True en caso afirmativo
                 # 5==6 (False) 5==5 (True)
'!='# Distintos  Evalua si el valor del operando de la izquiersa es distinto que el de la derecha
                 # 5!= 6 (True) 5==5 (False)
'>'#  Mayor que  Evalua si el valor del operador de la izquierda es mayor que el de la derecha
                 # 5 > 6 (False) 6 > 5 (True)
'<'#  menor que  Evalua si el valor del operando de la izquierda es menor que el de la derecha
                 # 5 < 6 (True) 6 < 5 (False)
                 
'<='# Mayor o igual que  Evalua si el valor del operando de la izquierda es mayor o igual que el de la derecha
                 # 5 >= 6 (False) 7 >= 6 (True)
'>='# Menor o igual que  Evalua si el operando de la izquierda es menor o igual que el de la derecha
''                                  ''' operadores logicos '''
'' ''' nos permite uni valores comparados o negar (invertir) un valor. Nos
       devuelven un resultado vooleano (verdadero o falso)'''

"and"# devuelve true si los dos operadores son true, en caso contrario devuelve false
     # True and True  (True)
     # True and False (False)
"or"#  Devuelve true si alguno de los operadores es verdadero en caso contrario devuelve false
     # True or False (True)
     # False or False (False)
"not"# Invierte el valor del operando sobre el que actua 
     # not True = (False)
        
''                   ''' Precedencia de los operadores '''
''  ''' Hemos visto operadores relacionales,logicos,aritmetricos. pero cuando se unen
        diferentes tipos de operadores, existen unas reglas de precedecia:'''
        
''        'reglas de precedencia'
''# Primero Los parentesis ()  tiene la maxima prioridad
''# Segundo Las expresiones aritmetricas, respetando sus propias reglas
''# tercer  Las expreciones relacionales o de comparacion
''# cuarto  Las Expreciones logicas   

''              ''' Cambiando tipos de variables'''
'''convertir variables de un tipo a otro se denomina casting, en python podemos
   comprobar el tipo de una variable mediante la funcion type(), o bien mediante
   la funcion isInstance(), como se muestra a conbtinuacion'''
asd = 2.0
ase = 1
print(type(asd))#<class 'float' >
print(type(ase))#<class 'int' >   
'' ''' podemos cambiar el tipo de una varible mediante las funciones 
       int(), complex() y str() '''
print(int(18.6))
print(float(44))
print(complex(2))
'' ''' otras funciones que nos pueden ayudar bastante en la conversion y manejo de
       numeros son:'''
'round()'# nos permite redondear un numero a su entero cercano
'max()'# nos devolvera el numero mayor de una secuencia de nuemrtos pasado como parametro
'min()'# nos devolvera el numero menor de uma secuencia de numeros pasada como parametro
''          ''' Trabajando con cadenoas de caracteres '''


''' Para invluir iuans comillas dentro de una cadena de caracteres devemos recurrir
    a cualquiera de lsa dos opciones de se ven a conrinuacion, bien jugar con la
    alternativa entre comillas dobles y simples, o bien ultilizar el caracter de
    barra invertida o backslash (\) alt 92'''
    
""    'Este texto invluy unas "" '
 
 
'' ''' una de ls operaciones mas comunes que se puede realizar con cadenas es 
        la concatenacion op sums de cadenas se suele realizar con el oprendor +,
        aunque hay varias forms de realizarlas, como se ve a continuacion.
       '''
c = 'esto es una cadena con\n dos lineas '  
print(c+c)

'' ''' Tambien es posible realizar una multiplicacion de cadenas'''
diezespacios = ' '*10
print("aqui hay 10 espacios"+ diezespacios)


# los indice nos permiten posicionarnos en  un caracter especifico de una cade 
# y acceder a el. representan a un umero [indice], que empezando por el 0 indica 
# el caracter de la primera posicion, y asi sucesivamente:
palabra = "python"
print(palabra[0], palabra[1])
# un inide negaticvo, hace referencia al caracter de la codena comenzando por la
# ultima posicion y en sentido inverso. Esto quiere decir que el indice -1 sera
# igual a la ultima posicion, -2 al penultimo, asi sucesivamente:

print(palabra[-1])

''  '''El slicing (rebanando) es una capacidad que tienen las cadenas de devolver un
subconjunto o subcadena utilizando dos índices [inicio:fin]. El primer
índice indica donde empieza la subcadena (se incluye el carácter) y el segundo
índice indica donde acaba la subcadena (se excluye el carácter).'''


print(palabra[0:2])

'' '''Si en el slicing no se indica un índice, se toma por defecto el principio y el final
(incluidos)

'''
print(palabra[2:])

print(palabra[:2])

print(palabra[:])

# Si un índice se encuentra fuera del rango 
# de la cadena, el intérprete de Python dará error:

'''Pero con slicing esto no pasa y simplemente se considera el espacio como vacío:'''
print(palabra[:99])

print(palabra[99:])
'''Una propiedad de las cadenas es la inmutabilidad,
no se pueden modificar. Si intentamos reasignar un carácter, no nos dejará:'''

#palabra[0]= 'N' no nos dejara va a decir: 'str' object does not support item assignment

'''Sin embargo, utilizando slicing y concatenación, podemos generar nuevas cadenas fácilmente:

 '''

palabra = "N" + palabra[1:]
print (palabra)
""" para poder contar palabras es muy util la funciom  len()"""

print(len(palabra))

'''    Como se aprecia anteriormente, la función print() incluye un salto de línea
       cada vez que se ejecuta. Si queremos que Python no añada un salto de línea al
       final de un print(), se definirá el argumento end con el carácter que
       deseemos implementar como terminador de línea: 
'''
print("Una cadena", end=" ")
print("Otra cadena")

print("Una cadena", end=", ")
print("Otra cadena")
####################################################################################################
#range () función devuelve una secuencia 
# de números, comenzando desde 0 de forma predeterminada, se incrementa en 1 
'ejemplo'
#Cree una secuencia de números del 3 al 19, pero incremente en 2 en lugar de 1:
x = range(3, 20, 2)
for n in x:
  print(n)
'''Para permitir la introducción de múltiples valores recurriremos a la instrucción
   for, que veremos más adelante:'''
valores = []
print("Introduce 3 valores")
for x in range(10):
    valores.append( input("Introduzca un valor: ") )
print(valores) 

''' Esta función acepta caracteres especiales como las
    tabulaciones (/t) o los saltos de línea (/n): 
'''
print("Un texto\tunatabulación") 
print("Un texto\nuna nueva línea") 

'''
   Para evitar los caracteres especiales, debemos indicar que una cadena
   es cruda (raw), anteponiendo una r a la cadena de caracteres a mostrar, 
   como se ve a continuación

'''
print(r"C:\nombre\directorio") # r = raw (cruda)

#Podemos utilizar """ (triples comillas) para cadenas multilínea:

print("""Una linea
otra linea
otra linea\tuna tabulación""")

''' Utilizando el parámetro sep, podemos separar cada uno de los caracteres de la
cadena con el carácter indicado y con el parámetro end podemos finalizar la
cadena con el carácter que le indiquemos: '''
print(1, 2, 3, 4) 
print(1, 2, 3, 4, sep='*') 
print(1, 2, 3, 4, sep='#', end='&') 

'''
   Existe una funcionalidad en las cadenas de texto que nos permite formatear
   información cómodamente utilizando identificadores referenciados, para ello
   usamos el método format():
'''
texto = "otro texto"
num = 10 
c = "un texto '{}' y un número '{}'".format(texto,num)
print(c)
''' O podemos utilizar un identificador con una clave y luego pasarlas al método
    format():
'''
print(( "Un texto '{t}' y un número '{n}'").format(t= texto, n= num))

print(("{t},{t},{t}").format(t=texto))
#También podemos realizar un formateo 
#avanzado, alineando a la derecha en 30 caracteres de la siguiente manera:

print(("{:>30}").format("palabra")) 
# O bien alineando a la izquierda en 30 caracteres
print(("{:30}").format("palabra")) 
# O bien alineando al centro en 30 caracteres
print(("{:^30}").format("palabra"))

'''Para realizar un truncamiento de 5 caracteres procederemos de la siguiente
manera:
'''
print(("{:.5}").format("palabra")) 
'''Combinando varios de estos formateos, hacemos un alineamiento a la derecha
en 30 caracteres con truncamiento de 3:'''

print(("{:>30.3}").format("palabra")) 
'''Y, por último, para formatear números enteros, rellenados con ceros, 
realizaremos lo siguiente:'''

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
''' Y eso mismo, si lo quisiéramos hacer con números decimales o flotantes,
lo haremos como a continuación:'''
# Se imprimiran 7 caracteres (inluido el punto), de los cuales 3 serán decimales
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))




''                                                 ''' Tipos de datos avanzados '''
'''Sumarios'''
''' ............................................................'''
"listas"
"tuplas"
"sets" 'o (conjuntos)'
"Diccionarios"
#...............................................................................................

''                                                     '''Listas'''
# Una lista es una estructura en python de datos formada por una secuencia
# ordenadas de objetos, es una coleccion ordenada y mosificable que permite
# miembros duplicados.
# las listas en python son hererogeneas porque pueden estar formadas por
#  elementos de distintos tipos. incluidos otras listas y mutables. porque sus
# elementos pueden modificarse.

numeros = [1,2,3,4]
print(numeros)
# atravez se los indices de una lista podemos cambiar el valor de sus elementos
# haciendo de esta forma la lista mutable
 
datos = [4,"Una cadena",-15,3.14,"Otra cadena"]
print(datos)
print(type(datos)) 

'''
Tanto el acceso a los elementos, que se realiza mediante índices, como el slicing,
se realizan de forma muy similar a las cadenas de caracteres, pudiendo también
acceder a los elementos desde el final con índices negativos, como hemos visto
con las cadenas:

'''
print(datos)
print(datos[0])
print(datos[-1])
print(datos[-2:])
print(datos[1:3])
'''
Las listas también aceptan el operador de suma, cuyo resultado es una nueva
lista que incluye todos los ítems:

'''
numeros = numeros + [5,6,7,8]
print(numeros)
'''
Las listas, como bien indicamos anteriormente, son modificables, y para ello
modificamos el valor a través de sus índices:
'''
pares = [0,2,4,5,8,10]
print(pares)

pares[3]= 6
print(pares)

'''
Asimismo, integran funcionalidades internas, como el método .append()
usado para añadir un ítem al final de la lista:
'''
pares.append(12)
print(pares)

pares.insert(0, 7)
pares.append(7*2)

print(pares)

'''Y
tienen una peculiaridad, que aceptan asignación con slicing para modificar
varios ítems en conjunto:

'''
letras = ['a','b','c','d','e','f']
print(letras[:3])

letras[:3] = ['A','B','C']
print(letras)

'''Si queremos borrar el contenido de una lista solo tenemos que asignar una lista
vacía a la misma:'''

letras[:3] = []
print(letras)

letras = []
print(letras)

'''
Al igual que sucede con las cadenas la función len() devuelve la cantidad de
elementos que contiene la lista o lo que es lo mismo, su longitud:
'''
print(len(letras)) 

print(len(pares)) 

'''
Para buscar un elemento dentro de una lista usaremos el operador in, que nos
devolverá verdadero o falso en función de si encuentra el elemento dentro de la
lista o no:
'''
print(pares)
print(2 in pares)
print(7 in pares)

'''
Podemos incluir listas dentro de listas, llamadas listas anidadas, y las
manipularemos fácilmente utilizando múltiples índices, como si nos
refiriéramos a las filas y columnas de una tabla:

'''
a = [1,2,3]
b = [4,5,6]
c = [7,8,9] 
r = [a,b,c]
print(r)

print(r[0]) # Primera sublista

print(r[-1]) # Ultima sublista

print(r[0][0]) # Primera sublista, primer item

print(r[1][1]) # Segunda sublista, segundo item

print(r[2][2]) # Tercera sublista, tercer item

print(r[-1][-1]) # Última sublista, último item






#............................................................................................................................................


''                                             '''Tuplas'''


'''Una tupla en Python es una estructura de datos formada por una secuencia
ordenada de objetos. Una colección ordenada e inmutable que permite
miembros duplicados.

Podemos decir que las tuplas son listas inmutables, que no pueden modificarse
después de su creación'''


'''Con las tuplas se trabaja exactamente igual que con las listas. La única
diferencia es que las tuplas son inmutables, no se puede modificar su contenido.
Los valores que componen una tupla van ordenados entre ( ) y separados por
comas. A continuación, se muestra cómo declarar una tupla, cómo mostrarla y
comprobar de qué tipo es el elemento creado'''

numeros = (1,2,3,4)
print(numeros)

datos = (44356,"Una cadena",-15,3.14,"Otra cadena")
print(datos)

print(type(datos)) 

'''Las tuplas, en cuanto a índices y slicing, funcionan de una forma muy similar 
a las cadenas de caracteres y las listas:'''


print(datos[0])
print(datos[-1])
print(datos[-2:])
print(datos[1:3])
'''
También podemos realizar la suma de tuplas, que nos dará como resultado una
nueva tupla que incluye todos los ítems:
'''
numeros = numeros + (5,6,7,8)
print(numeros)
'''
Es muy importante tener en cuenta que los elementos de las tuplas no son
modificables, cualquier intento de modificación de los mismos nos dará error:
'''
#Al no ser modificables, no incluyen el método append()
pares = (0,2,4,5,8,10)
print(pares)
#Y tampoco aceptan la asignación con slicing para 
# modificar varios ítems en conjunto:

letras = ('a', 'b', 'c', 'd', 'e', 'f')
print(letras[:3])

'''
La función len() también funciona con las tuplas del mismo modo que en las
listas y cadenas de caracteres:

'''
print(len(letras))
'al igual que en las listas, podemos buscar con el operado in:'
print(pares)

print(2 in pares) # hay 2 dentro del operador (pares) resultado True

print(7 in pares) # hay 7 dentro del operador (pares) resultado False

'''y tambien podemos maniupulas facilmente tuplas anidadas ultilizando multiples
indices, como si nos refirieramos a las filas y columnas de una tabla:'''

a = (1,2,3)
b = (4,5,6)
c = (7,8,9) 
r = (a,b,c)
print(r)

print(r[-1]) # Ultima subtupla

print(r[1][1]) # Segunda subtupla, segundo item

print(r[2][2]) # Tercera subtupla, tercer item

print(r[-1][-1]) # Última subtupla, último item

#.............................................................................................................................................

''                               '''sets'''
''' 
Un conjunto o set, es una coleccion desordenada y no indexada en la no se
permite elementos repetidos. los usos basicos de estos conjutnos incluyen
verificacion de pertenecina y eliminacion de entradas duplicadas.
'''
A = {1,2,3,4}
B = {3,4,5,6}

'''Los valores que se componen un cojunto van indicados entre {} y se separados por
comas. A continuacion, se muetra como declarar u conjunto, como comtrarlo y comprobar
de que tipo es el elementos creado:
'''

numeros = {1,2,3,4} 
print(1,2,3,4)

datos = {4,"Una cadena",-15,3.14,"Otra cadena"}


print(datos)
print(type(datos))
''' No podemos acceder a los elementos de un conjunto set haciendo referencia
a un indice, porque los conjuntos no estan ordenados y debido a esto, los 
elementos no tienen indice. pero podemos recorrer los elementos del conjunto
utilizando un bucle for, que veremos mas adelante, o preguntar si un valor 
especifico esta presente en un conunto utilizando la palabra clave in:'''

lenguajes = { 
             "PYTHON",
             "C++",
             "JAVA"

}
for z in lenguajes:
       print(z)


print("python"in lenguajes)

'''Una vez se cerea un conjunto set, no podemos cambiar sus elementos, pero
podemos agregar nuevos elementos mediante el metodo add() para agregar un elemento a un conjunto
o mediante el metodo update() para agregar de un alementeo a un conjunto. podemos observar como el orden totalmente
aleatorio y dicidido por el lenguaje, como al no aceptar elementos repetidos,



'''
'''
si añadimos de un nuevo un elemento que ya existe, 
no se añadira como un elemento nuevo:
'''
lenguajes = {"Python", "C++", "Java"}
print(lenguajes)


lenguajes.add("C#")
print(lenguajes)
# Como se puede ver, el orden es aleatorio y decidido por el lenguaje

lenguajes.update(["Go", "Javascript", "PHP"])
print(lenguajes)

'La función len() también funciona para los conjuntos:'

print(len(lenguajes))

'''
Para eliminar elementos del conjunto podemos utilizar dos métodos,
discard() o remove(), indicando entre paréntesis el elemento que
queremos eliminar:

'''
lenguajes = {"C#", "Python", "Go", "C++", "Javascript", "Java", "PHP"}
print(lenguajes)

lenguajes.remove("Go")
print(lenguajes)

lenguajes.discard("PHP")
print(lenguajes)


'Si queremos buscar dentro del conjunto lo haremos con el operador in:'


print(lenguajes)

print("C#" in lenguajes)

'''Y si lo que queremos es eliminar todo el contenido de un conjunto, debemos
utilizar el método clear():'''

lenguajes = {"C#", "Python", "Go", "C++", "Javascript", "Java", "PHP"}
print(lenguajes)

lenguajes.clear()
print(lenguajes)

'''Por último, debemos saber que los conjuntos no son anidables, de manera que
no puede haber conjuntos dentro de otros conjuntos:'''\
       
#...............................................................................................
''                                 ''' Diccionarios'''

''' 
Un diccionario en Python es una colección desordenada, modificable e
indexada que no permite miembros duplicados. Un diccionario define una 
relación uno a uno entre claves y valores.'''



vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

print(type(vehiculos))

'''Para acceder a los elementos de un diccionario tenemos dos formas, bien
haciendo referencia a su clave, o bien utilizando el método get(). Ambas
formas nos devolverán el valor correspondiente, como se ve a continuación:'''

valorQueMeInteresa = vehiculos["model"] 
print(valorQueMeInteresa)

valorQueMeInteresa = vehiculos.get("model") 
print(valorQueMeInteresa)

'''Para buscar una clave en un diccionario se utiliza el operador in (solo sirve
para buscar claves):'''

print("model" in vehiculos)

vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

vehiculos["year"] = 2020
print(vehiculos)

'''
Para saber la longitud de un diccionario usaremos la función len(), que
también funciona con los diccionarios: '''

print(len(vehiculos))

'''Para recorrer un diccionario utilizaremos el mismo método que con los
conjuntos:'''

for x in vehiculos:
    print(x)
    
for x in vehiculos:
    print(vehiculos[x])    
    
for x in vehiculos:
    print(x, ": ", vehiculos[x])
    
for x in vehiculos.values():
    print(x)    
    
'''
Existe un método de los diccionarios que nos facilita la lectura en clave y el
valor de los elementos, porque devuelve ambos valores en cada iteración
automáticamente:

'''
for x, y in vehiculos.items():
    print(x, ": ", y)

'''
Para agregar elementos a un diccionario utilizaremos una nueva clave de índice
y le asignaremos un valor:

'''
vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

vehiculos["color"] = "red"
print(vehiculos)

'''
Para eliminar elementos del diccionario utilizaremos uno de estos tres métodos,
según nos sea más conveniente: clear() para borrar todo el diccionario,
pop() para eliminar el elemento con el nombre de clave especificado
y popitem() para eliminar el último elemento insertado. Hay que tener en
cuenta que popitem(), en versiones anteriores a la 3.7 del intérprete, elimina 
un elemento aleatorio del diccionario en lugar de eliminar el último elemento 
insertado:
'''

vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

# Elimina el último elemento insertado (en versiones anteriores a 3.7, se elimina un elemento aleatorio)
eliminado = vehiculos.popitem()
print(vehiculos)
print("Se ha eliminado la siguiente pareja de datos:", eliminado)

vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

eliminado = vehiculos.pop("model")
# Elimina el elemento con la clave especificada
print(vehiculos)
print("Se ha eliminado el valor", eliminado)

vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

vehiculos.clear( ) # Vacía el diccionario
print(vehiculos)

'''Un diccionario no se puede copiar realizando una asignación entre dos 
diccionarios de la forma dict2 = dict1, porque el diccionario dict2 solo 
será una referencia a dict1, y los cambios realizados en dict1 también se
realizarán automáticamente en dict2. Para hacer una copia hay que utilizar
el método copy():
'''
vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

vehiculos_copia = vehiculos.copy()
print(vehiculos_copia)

vehiculos.pop("model") # Elimina el elemento con la clave especificada
print(vehiculos)
print(vehiculos_copia)

'''
Se pueden anidar diccionarios, incluir diccionarios dentro de otros diccionarios.
En la siguiente imagen el diccionario familia contiene otros tres diccionarios'''

familia = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    },
}
print(familia)

'''Y para acceder a los diccionarios “internos” lo haremos de la siguiente manera:'''

valorQueMeInteresa = familia["child1"]
print(valorQueMeInteresa)

valorQueMeInteresa = familia["child3"]["name"]
print(valorQueMeInteresa)

'''Por último, en estos dos ejemplos vemos como incluir listas en nuestros diccionarios'''

diccionario = {
    'nombre' : 'Carlos',
    'edad' : 22,
    'cursos' : ['Python', 'Django', 'Javascript']
}

print("Diccionario completo: ")
print(diccionario)

print("\nElementos del diccionario")
print(diccionario['nombre']) # Carlos
print(diccionario['edad']) # 22
print(diccionario['cursos']) # ['Python', 'Django', 'Javascript']

print("\nItems de la lista cursos: ")
print(diccionario['cursos'][0]) # Python
print(diccionario['cursos'][1]) # Django
print(diccionario['cursos'][2]) # Javascript

print("\nRecorriendo el diccionario con un bucle for")
for key in diccionario:
    print(key, ":", diccionario[key])

clientes = {
    'nombre' : ['Carlos','Cristian','David'] ,
    'edad' : [22,30,32] ,
    'lenguaje_favorito' : ['Python','Django','Javascript']
}

print("Diccionario completo: ")
print(diccionario)

print("\nMostrar todos los datos del primer cliente")
print(clientes['nombre'][0])
print(clientes['edad'][0])
print(clientes['lenguaje_favorito'][0])

print("\nMostrar todos los datos del segundo cliente")
print(clientes['nombre'][1])
print(clientes['edad'][1])
print(clientes['lenguaje_favorito'][1])

print("\nMostrar todos los datos del tercer cliente")
print(clientes['nombre'][2], end=", ")
print(clientes['edad'][2], end=", ")
print(clientes['lenguaje_favorito'][2])




#.......................................................................................................................................................................................

''                                 ''' Condicionales en Python'''

''' 
Una sentencia condicional, como su nombre indica, es una
condición para discernir entre una opción u otra, y en el proceso mental
normalmente se manifiesta con un SI; por ejemplo: Si (va a 
llover), coge el paraguas.'''


'''
Mediante una sentencia condicional seleccionamos un bloque de sentencias
que se ejecutarán cuando dicha condición se cumpla (sea verdadera). Para
entender un poco mejor las instrucciones condicionales, veamos un diagrama
de flujo de un programa con este tipo de instrucciones'''


''                              '''IF'''


'''
Mediante la sentencia if evaluamos una condición y ejecutamos una serie de
instrucciones en caso que la condición evaluada sea verdadera. En caso
contrario, se continúa normalmente con la secuencia de instrucciones del
programa sin ejecutar ninguna de las que indicamos dentro de la sentencia if.
Su diagrama de flujo es el siguiente:'''

'''La instrucción if tiene la siguiente sintaxis'''

'''Una sentencia if permite dividir el flujo de un programa en diferentes
caminos. Las instrucciones que están incluidas dentro del if se ejecutan 
siempre que la expresión que comprueba devuelva True:
'''
if True: # Equivale a if not false
    print("Se cumple la condición")
    print("También se muestra este print")

if True:    # Equivale a if not false
    print("Se cumple la condición")
    print("También se muestra este print")
print("Este print no pertenece al if")

'''
Se pueden encadenar diferentes if:
'''
a = 2
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")
    
'''
O anidar if dentro de otros if:
'''

a = 5
b = 10
if a == 5:
    print("a vale",a)
    b=b+1 
    if b == 10:
        print("y b vale",b)
        
'''Y como condición, podemos evaluar múltiples expresiones, 
siempre que devuelvan True o False:'''

if a==5 and b==10:
    print("a vale 5 y b vale 10")
''                             ''' If else'''


'''Cuando evaluamos una condición, discernimos el caso en que la condición
es verdadera (el if se cumple, da verdadero), pero también podemos evaluar si la
condición es falsa (else / si no). El diagrama de flujo, en este caso, es el 
siguiente:
'''


'''La instrucción if ... else tiene la siguiente sintaxis'''

n = 6
if n >= 0:
    print(n,"es un número mayor o igual que 0")
else:
    print(n,"es un número menor que 0")
    
n = 11
if n % 2 == 0:
    print(n,"es un número par")
else:
    print(n,"es un número impar")


''                         '''if - elif - else'''
'''
a sentencia elif dentro de una sentencia if es el resultado de anidar
varias sentencias if, unas dentro de otras
'''
'''La forma de funcionamiento es la siguiente: tras evaluar la condición de la
sentencia if, y si esta no se cumple, realizamos otra evaluación con la 
sentencia elif y en caso que no se cumpla proseguiremos evaluando las 
siguientes sentencias elif hasta que alguna se cumpla. Si ninguna de las
condiciones anteriores se cumple, se ejecutarán las instrucciones que van
tras la sentencia else. Si alguna de las condiciones se cumple se ejecutará 
el código asociada a la misma.'''

orden = 3
if orden == 1:
    print("Abriendo puerta")
    # Primera condición: Se ejecuta si es true
elif orden == 2:
    print("Cerrando puerta")
elif orden == 3:
    print("Destruyendo puerta")
    # Se evaluan si las anteriores condiciones son false
else:
    print("Orden no encontrada")
    # Solo se ejecuta si ninguna de la anteriores es true

'''La instrucción if ... elif ... else tiene la siguiente sintaxis:'''


'''La instrucción elif se encadena a un if u otro elif para comprobar 
múltiples condiciones, siempre que las anteriores no se ejecuten:'''

comando = "OTRA COSA"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, espero que te lo estés pasando bien aprendiendo Python")
elif comando == "SALIR":
    print("Saliendo del sistema...") 
else:
    print("Este comando no se reconoce")

nota = float(input("Introduce una nota: "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")

'''Es posible simular el funcionamiento de elif con if utilizando expresiones
condicionales, pero esto hace que se ejecuten todas las instrucciones, aunque
no haga falta.

'''
nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 5 and nota < 6:
    print("Suficiente")
else:
    print("Insuficiente")

'''La instrucción condicional switch, existente en otros lenguajes de
programación, no existe en Python, aunque se puede simular mediante el uso
de un diccionario y funciones. El switch es una estructura condicional
múltiple, permite evaluar de manera rápida si un valor coincide con una gran
lista de posibilidades. Por ejemplo, si la variable día vale 0, se escogerá Lunes, si 
la variable día vale 1, se escogerá Martes, etc.:'''


'''
Debido a que en Python han eliminado la estructura switch, vamos a ver cuál 
sería la alternativa para el este ejemplo:'''
# Creamos un diccionario con las opciones
dias = {
    0: "Lunes",
    1: "Martes",
    2: "Miercoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

# Solicitamos al usuario que introduzca un número del 0 al 6 para conocer el nombre del día de la semana
opcionUsuario = int(input("Dia de la semana que quiere mostrar (del 0 al 6): "))

# Con el número introducido por el usuario, accedemos al diccionario y a ese clave-valor en concreto
nombreDia = dias.get(opcionUsuario, "Desconocido")

# Mostramos el resultado
print("El dia", opcionUsuario, "corresponde con:", nombreDia)
'''
switch(dia):
    case 0: "Lunes",
    case 1: "Martes",
    case 2: "Miercoles",
    case 3: "Jueves",
    case 4: "Viernes",
    case 5: "Sabado",
    case 6: "Domingo",
    default: "Desconocido"
'''

''                                '''Bucles en Python'''

'''Un bucle, en programación, es una secuencia que ejecuta repetidas veces 
un trozo de código, hasta que la condición asignada a dicho bucle deja de 
cumplirse. El propósito es repetir un bloque de código mientras una condición 
sea verdadera. Los bucles más utilizados en programación son el bucle while 
y el bucle for. En el siguiente gráfico podemos ver el diagrama de flujo de un 
programa con un bucle y el de un bucle en sí:'''

'''While'''
                                                                                  
'''Un bucle con instrucción while evalúa una condición antes de entrar en el 
bucle y, si se cumple y mientras se cumpla, ejecuta las instrucciones que están 
asociadas a él. La sintaxis es la siguiente:'''


'''Un ejemplo de un bucle while es el siguiente:'''

contador = 0
# Mediante la instrucción while iniciamos el bucle
while contador < 5:  # Condición booleana que hará reiniciar el bucle
    print("Hola") 
    contador = contador + 1
    # Proceso que se repetirá mientras la condición sea true

'''El bucle do ... while, existente en otros lenguajes de programación, 
en Python no existe.'''

'''Un bucle while se basa en iterar un bloque a partir de evaluar una condición 
lógica, siempre que ésta sea True. Queda en manos del programador decidir el 
momento en que la condición cambie a False para hacer que la instrucción 
while finalice.'''

'''“Iterar” es realizar una acción varias veces, cada vez que se repite la acción se 
denomina “iteración”.'''

counter = 1
while counter <= 5:  
    print("Hello world") 
    counter += 1


c = 0
while c <= 5:  
    c+=1 # Equivalente a c = c + 1
    print("c vale",c)
'''Se puede encadenar una sentencia else en un bucle while para ejecutar un 
bloque de código, una vez la condición ya no devuelve True (normalmente al 
final, al salir del bucle)'''

c = 0
while c <= 5:  
    c+=1 
    if (c==4):
        print("Rompemos el bucle cuando c vale",c)
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)

print("por aqui continuamos el programa normal")


'''Debemos tener especial cuidado al utilizar la instrucción break, ya que con ella estamos rompiendo el flujo normal del programa.

También podemos “saltarnos” la iteración actual sin romper el bucle, mediante la instrucción continue:'''

c = 0
while c <= 5:  
    c+=1 
    if c==3 or c==4:
        # print("Continuamos con la siguiente iteracion")
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)
    

''' Gracias a un bucle while podemos crear un menú interactivo:'''



print("Bienvenido al menú interactivo")
while(True):
    print(
        """¿Qué quieres hacer? Escribe una opción
        1) Saludar
        2) Sumar dos números
        3) Salir"""
    )

    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ", n1+n2)
    elif opcion == '3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")


'''
Si la condición del bucle se cumple siempre, el bucle no terminará nunca de ejecutarse y 
tendremos lo que se denomina un bucle infinito:
'''
#contador = 0
#while True:
#    print("Iteración", contador)
#    contador +=1


'''A la derecha del botón “Run” disponemos de un botón “Stop”, con un cuadrado en su interior, para detener el 
proceso en caso que nuestro programa se quede dentro de un bucle infinito.

Veamos ahora un ejemplo práctico de un bucle while:'''

'''
n = 0
while n < 10:
    if (n % 2) == 0:
        print(n,'es un número par') #lo comento para no  sobre cargue la compu con un comando infinito
    else:
        print(n,'es un número impar')
    n = n + 1
    
    
    
 ''                                                      'Bucle For'
'''
"""Los bucles for son otra forma de ejecutar código de manera repetitiva. En lugar de iterar sobre 
una progresión aritmética de números, como es el caso de Pascal, o darle al usuario la posibilidad de definir 
tanto el paso de la iteración como la condición de fin, como en el caso de C, la sentencia for de Python itera 
sobre los elementos de cualquier secuencia, rango, lista o cadena de caracteres, siguiendo el orden que aparece 
en la secuencia, rango, lista o cadena.

La instrucción for tiene la siguiente sintaxis:"""

lista = [10,20,30,40,50]
# Abrimos el bucle con la sentencia for
# elemento (i) y secuencia (lista) sobre la que iteramos
for i in lista: 
    print(i) # Proceso que repetimos
    

'''Como recordatorio, vamos a recorrer los elementos de una lista utilizando while:'''
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros): 
    print(numeros[indice])
    indice+=1
    
'''La función range() sirve para generar una lista de números que podemos recorrer
fácilmente, pero no ocupa memoria porque se interpreta sobre la marcha. De esta forma 
podemos simular un bucle for, como conocemos en cualquier otro lenguaje de programación, 
por ejemplo, C:'''


for i in range(10): 
    print(i)
 
print(range(10))

'''Si queremos conseguir la lista literal, podemos transformar el range() a una lista

'''

list(range(10))    


'''Pero como podemos utilizar listas en la sentencia for, la forma más fácil de recorrer
una lista es de la manera que vemos aquí:

'''
numeros = [1,2,3,4,5,6,7,8,9,10]
for num in numeros: # Para [variable] en [lista] 
    print(num)
    
''''''    
'''De esta manera, podemos modificar ítems de la lista al vuelo. Para asignar un nuevo valor 
a los elementos de una lista mientras la recorremos, podríamos intentar asignar al número el nuevo valor:

'''    

print("Lista inicial: ")
print(numeros)

for numero in numeros:
    numero *= 10
    print(numero, end=", ")
    
'''Sin embargo, esto no funciona. La forma correcta de hacerlo es haciendo referencia al índice de la lista
en lugar de la variable:'''


indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[indice] *= 10
    indice+=1
numeros

'''Podemos utilizar la función enumerate() para conseguir el índice y el valor en cada iteración fácilmente
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
numeros

'''Se puede utilizar la sentencia for con cadenas de caracteres:
'''


cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)
    
'''Pero debemos recordar que las cadenas son inmutables, por lo que si intentamos modificar su contenido obtendremos un error:'''


for i in cadena:
    cadena[i] = "*"
    

'''Para solventar este inconveniente, podemos generar una nueva cadena:'''


cadena2 = ""
for caracter in cadena:
    if(caracter == " ") or (caracter == "H"):
        cadena2 += ""
    else:
        cadena2 += caracter
print(cadena)
print(cadena2)


'''Y por último, recordar que si la condición del bucle se cumple siempre, el bucle no terminará nunca de ejecutarse y tendremos lo que se denomina un bucle infinito.

El bucle for no incluye de forma nativa una manera de implementar un bucle infinito, teniéndose que realizar a través de una librería que veremos más adelante.

'''


contador = 0
for i in counter():
    print("Iteración: ",contador)
    contador += 1

'''Veamos ahora un ejemplo práctico de un bucle for:
'''
idiomas=["ES_España", "IT_Italia", "EN_Reino Unido", "EN_USA", "ES_Argentina"]
contES = 0
contEN = 0
contUNK = 0
for pais in idiomas:
    #print(pais[:2]) # Para debug
    if(pais[:2] == "ES"):
        print("País de habla española: ", pais)
        contES = contES + 1
    elif(pais[:2] == "EN"):
        print("País de habla inglesa: ", end=" ")
        print(pais)
        contEN = contEN + 1
    else:
        print("Pais de habla no registrado: ", end=" ")
        print(pais)
        contUNK = contUNK +1

print("El numero de paises de habla española es: ", contES)   
print("El numero de paises de habla inglesa es: ", contEN)
print("El numero de paises de habla desconocida es: ", contUNK)

''' Setencia For para str 
'''

texto = "Aprendiendo a programar en Python"
contador = 0
for indice, letra in enumerate(texto):# si yo quiero mostrar posiciones debo poner enumerate*()
    if letra == "A" or letra == 'a':
        contador += 1
        print(letra,"en la posicion", indice)
        
print("El numero de  aes es", contador)

# for me permite recorrer listas y str
''' es recomendable siempre recorrer un bucle ante solo usando pritn y ver cada paso que vas '''
# los nombre quye yo ponga en un for no importa solo debo tener encuenta que el primero tendra los los indices y la otra los valores

''                                                  ''' Bucle For range()'''
'''este bucle nos permite hacer rangos '''
''' sirve para generar una lista de numeros qaue podemos recorrer facilmente, pero mo 
ocupa memoria porque se interpreta sonre la marcha:'''

for i in range(5):
 print("Hola mundo")
print(range(10))# range genera una lista del 0 al 10 

for i in [0,1,2,3,4,5,6,7,8,9,10]:
    print(i)

# en la estructura de l for me pide que cuando use range( use i )
''' si queremos conseguir la lista literal podemos transformar el range a una lista: '''
lista10elementos = list(range(10)) # con el comando list hago que el range me cree una lista de manera facil
print(lista10elementos)
print(type(lista10elementos))

for i in range(5, 10):
    print(i)
    
#range nos permirte enteder po niveles
# range(fin)
#range(inicio, final)
#range (inicio,fin,salto)
for i in range(0, 100, 10):
    print(i)

presentacion = "Hola mi nombre es santiago y estoy estudiando python"
for i in range(10,20):
    print(presentacion[i])

inicio = (input("Introcduce Tu numero de inicio "))
final = (input("Introduce Tu numero de final "))
salto = 1
lista_rango_personalizado = list(range(inicio,final,salto))
print(lista_rango_personalizado)
for indice, i in enumerate(lista_rango_personalizado):
    print("Indice", indice, "-> Valor de i: ", i)


# con esto podemos crear rangos numeros que podemos ingresar a una lista diccionarios str bucles
# podemos con ello modificar la informacion de lo que queremos hacer
# se puede hacer de la manera mas sencilla 
# no tiene una funcion definida solo se puede probar la herramienta de que mejor la usaremos 

''                       '''Bucle Infinito For '''

'''Si la condicion del bucle se cumple siempre, el bucle no terminara nunca de ejecutarse y tendremos lo que se denomina un bucle infinito
desponeis del boton de stop para detener el proceso (a ala derecha de run)

el bucle for no incluye de forma nativa de una manera de implementar un bucle infinito. Se tiene que realializar a traves de una libreria (se vera mas adelante).

'''
'''
from itertools import count
contador = 0
for i in count():
    print("Iteracion", contador)
    contador +=1
'''
# lo comento porque no quiero ningun bucle infinito XD
#..........................................................................................................................................................................

''                                    ''' Funciones y modulos'''
'''
concepto de las funciones en python 
implementacion de las funciones
argumentos y parametros 
funciones integradas de python
buenas practicas con las funciones

'''

''' las funciones son lineas cortas de codigo que se busca una modulacion
el uso de funcinoes es algo mas es una ciestion de buenas practicas 
se considera algo muy bueno es muy importante
esposible qu estas practicas es algo que puede ser obligatorio 



todas mis variables tiene que estar en una funcion 
todas mis funciones


se representa en bloques de codigo que realizan tareas especificas y que pueden se llamados desde otra parte del programa.
por ejemplo las diferentes tareas a realizar pueden ser implementadas en funciones y desde una funcion principal hacer llamafas a las mismas cuannfo de requiera
ejecutar a la tarea que llevan asociada

hay que reulizar nuestro codigo
'''
"""funciones implementacion"""
# las palabras reservada de python que indica que comienza una funcion
'def'
#nombre de la funcion
'saludar()'
#parametros que recibe nuestra funcion (vacio si no recibe ninguno)
#saludar()invocacion de la funcion desde el programa principal
'argumentos que se envian a ala duncion (vacio si no envia ninguno)'
# las funciones tienen que ser lo mas descriptivo posible

#las funciones
'''Son fragmentos de codigo que se pueden ejecutar multiples veces. Pueden recibir y devolver
informacion para comunicarse con el proceso principal (con la funcion principal, llamada main).'''

# Definicion y llamada
def saludar():
 print("Hola!!! Este print se llama desde la funcion saludar()") 
 
saludar()# llamo a la funcion que acabo de crear.
  

def lucas():
 hello = "hola"
 print(hello.__annotations__)
 
''                                                                      'Programacion Secuencial'
# lo mejor que se puede hacer tus funciones def() en la parte superior de tu codigo y luego haz tu programa principal 
#no es bueno mescalar las deficiiones con codigo ya que se ve desordenado es mejor por ello poner todas las deficiones arriba y luego el codigo principal 
# es un codigo mucho mas ordenado
#la funciones pueden tener cosas muy complejas pero la idea solo que es haga solo 1 cosa
import time

def dibujar_tabla_del_5():                 #aqui esta mi funcion completa
    for i in range(10):
        print("5 * {} = {}".format(1.1*5))
        time.sleep(5)
        
dibujar_tabla_del_5()
print("Fin")


''               '''  Ambito (scope) de las variables'''
''' Una variable declarada en una funcion no existe en la funcion principal:'''


def test():
    n = 10 
    print("Mostrando el valor  de n dentro de la funcion test:", n)

test()
# simembargo , una variale declarada fuera de la funcion (al mismo nivel), si que es accesible desde la funcion(estasd variables se conocen como globales)
def tests():
    print("Mostrando el valor de m DENTRO de la funcion test:",m)
m = 10# esta variable se ve porque esta escrita en el main 
# una variable creada en el main se puede usar en el main y tambien dentro de la funcion cuando esta la solicite y no nos mostraria ningun error
test()
print("Mostrando el valor de m FUERA de la funcion test: ",m)



'' ''' La intruccion global'''

'podmeos poder modificar una variable extrna en en la funcipn, debemos indicar que que es le global de al siguiente forma:'


# Nota Nota Nota
# Global hace que nuestra variable en la funcion se vuelva publica 
# por ello no es bueno que las uses 
# es mejor que sea tu ultimo recursos 

def testss():
    global o
    o = 5
    print("Variable DENTRO de la funcion", o)
o = 10
print("Variable a FUERA de la funcion", o)
# no es la mejor opcion para usar 
# lo ideal no es usarlo puede ser pelogrisisisismo ya que hace que nuestra variable sea un ambito publico




"  "                                                                '''FUNCION CON LAS VARIABLES GLOBALES'''

""" 
Las variables globales son pelligrosas, hay que tener cuidado con su uso. Si una variable puede ser modificada en 
multiples puntos de nuestro de programa, tenemos que tener un gran control sobre nuesto codigo para no obtener
resultados no esperados. Por eso exiten los ambitos de las variables, si cada variable existe en su ambito limitamos la 
posibilidad de problemas, de que una variable sea modificada o eliminada por error un lugar que no deba.

Pero si cada variable solo existe dentro de su funcion (de su ambito), Como podemos compartir resultados entre
funcionse sin romper la estructura de ambitos de python?

retornado valores y pasando valores por parametro. Lo que veremos a continuacion.

"""




'''
Sabemos que Python es una lenguaje de progrmacion secuencial, lo que significa que ejecuta
las lineas de codifo desde la primera hasta N de una en una. Pero las funciones tienen un 
comportamientoo diferente, sus lineas de codigo solamente se ejecutan cuando la funcion es
llamada. Para verlo, vamos a realizar la trazabilidad del programa, es decir, la secuencia de ejecuciones de nuestro programa:
'''


#usamos main para que mande a otrad funciones y hagan esos trabajos 
# y entre estas funciones mandan a funciones mas pequeñas  para que lo hagan

# leer columna s buscar errores


''                                                   '''La funcion y su ambito
'''
'''Todos lo lenguajes de programacion tiene una funcion main. Es esl punto de inicion de nuestro codigo. Para ser correctos,
Todo nuestro codigo deberia estar dentro de funciones, para una mayor organizacion y reutilizacion. Por lo que tendremos:

- Funcion main: Con el codigo inicial y las llamadas al resto de funciones
- Resto de funciones con funcionalidades particulares

'''
def saludar():
    print("Hola esta print se llama dessde la funcion saludar()")

saludar()

#El ejemplo anterior seria mac correcro de la siguiente manera:

def saludar():
    print("Hola Este print se llama desde la funcion saludar() ")
def despedirse():
 print("Adios")
if __name__ =="__main__":# cuando hacemos referencia sobre  el _ _ main _ _ asi se podria decir que invocamos al main
    print("Inicio del programa con sus inicializaciones")
    saludar()
    print("Continuemos con el resto del codigo")
    despedirse()
    print("Continuamos con el resto del codigo....")
    #Mantemamos esta estructura primmero las funciones y luego hacemos main 
     
     
''
''' Orden de Main y el resto de las funciones'''
def sumar():
    suma = b1 + b2
    return suma

b1 = int(input(""))
b2 = int(input(""))
sumar()
print(sumar())         
     
" "                                                                       """Retorno de valores"""


''' 
para comunicarse con el exterior, las funciones pueden devolver valores al proceso prinicipal gracias a la instruccion return
En el momento de devolver un valor, la ejecucion de la funcion finalizara:
'''

def testes():
    texto = "Un string retornado"
    return texto # return me imprime este string pero solo funciona en jupyter
# mientras en cualquier uso para programar no nos saldran nada.
print("INICIO")
print(testes())
'''
Lo logico, es almacenar en variables lo que nos devuelen las funciones para posteiormente poder operar con
dichos valores
'''     
# por eso hay que capturar y luego mostrarlo
op = testes()
print(op)


textodevuelto = testes()# cuando nosotros invocamos a un funcion volvemos a recorrer la funcion y nos topamos con return y este es el que nos mostrara en el la variable
print(textodevuelto)

'''
Los valores devueltos se tratan como valores literales directos del tipo de dato retornado
(por eso es muy importante conocer los tipos de los datos que estamos
manejando):
'''
'''c = testes() +10''' # crea un error ya que estamos sumando un str con numeros enteros obviamente no se puede
# eso incluye
def nombre():
    return "Cristian"

frase = "Mi nombre es" + nombre() + "Rodriguez"    
print(frase)

def  deo():
    listasdf = [1,2,3,4,5]
    return listasdf    

print(deo())
print(deo()[-1])
print(deo()[1:4])
listadevuelta = deo() # lo mejor siempre es meter a nuestras funciones a una variable y luego hagamos lo que sea 
print(deo()[-1])
f = listadevuelta[-1]
print(f)
  
  
'''
Estos valores se tratan en cojunto como una tupla immutable y se pueden reasignar a
distintas variables:
'''  
'''de manera ordenada solamente como estan organizados las variables dentro de la funcion'''

t,n,l = f()
print(t)
print(n)
print(l)

''                                            ''' Problemas cuando una funcion nos devuelve None'''
def none():
    texto = "Un str retornado"
print(none())# si nuestra funcion tiene un return hay que capturar ese return en una variable luego pero su no lo tiene no esperes a que te muestre lo que tenga la funcion 


''                                                        ''' Envio de valores'''

'''
Para comunicarse con el exterior, las funciones no solo pueden devolver valores (return), tambien 
pueden recibir informacion
'''
'Parametros y argumentos'
''' En la definicion de una funcion, los valores que se reciben se denominan parametors, y en
la llamada se denominan argumentos.'''

def sumar(a,b):# valores que se reciben, llamadas parametos de entrada, o simplemente
 suma = a+b #'a' y 'b 'solo representa lo que queremos que nuestros valores hagan
 return suma   


# Ahora podemos enviar dos valores a la funcion:                                     <---
#                                                                                    #  → 
resultado = sumar(5,6)
print(resultado)

print(sumar(5,8))
# es muy importante el numero / y el orden el numero y el orden de parametros en este caso hay 2 

# con esto hacemos una funcion  que hace solo 1 cosa en este caso sumar
# esta parametrizada ya que puede sumar cualquier pareja de numeros
# asi no tocamos la funcion 
# lo que cambiamos es la copia de la funcion
#la idea es no tocarlas mas


''                                 ''' Retorno multiple'''

'''
Una caracteristica interesante, es la posibilidad de devolver multiples valores separadas por comas.
'''
def t():
    texto = "Una cadena"
    num = 20
    lista = [1,2,3]
    return texto, num, lista
print(t())

#podemos enviar evidentemente, podemos como argumentos variables

def sumar(num1+num2):
 suma = num1 + num2
 return suma
num_a = 2# no hay problema que se llame igual pero tampoco es importante que se llamen asi
num_b = 5
resultado = sumar(num_a+num_b)
print(resultado)#python si pueden concatenar texto si usamos esta funcion 
# hay que hacer comprobasiones si estos parametros son numeros


    
''                             '''Llamada sin argumentos  '''
'''
Al llamar una funcion que tiene definidos unos parametros, si no pasamos los argumentos correctamente provocara un error:
'''

resultado = sumar()
# muestra el error que dice
# sumar() missing 2 required positional arguments: 'num1' and 'num2'
# no encuentra valores para meterlo en la funcion
'''Si yo le intento poner 3 parametros me dara tambien un error'''

''                                        ''' Parametros por defecto'''
'''
Para solucionar el problema de que se realcien llamadas sin argumentos, podemos asignar unos valores por defecto nulos (o
los valores por defecto que queramos) alos parametros, y de esa forma hacer una comprobacion antes de ejecutar el codigo de la funcion:

'''

def sumar (a=535, b = 5000):
 if a == None or b == None:
  print("Error, debes enviar dos numeros a la funcion "
 
 else:
   suma = a+b
   return suma
resutado = sumar(2) # de sta manera sumanos el valor de 3 como a y el b que en su valor original es 2000
# para oider sumar el segundo valor que tenemos que en esta funcion lo hacemos de esta manera
resultado = sumar(a=10,b=3)# intentemos siempre poner los nombre de los parametros
resultado = sumar(b=3)
resultado = sumar(a=3)
resultado = sumar()
print(resultado)
 
# si tenemos um proyecto y no sabemos que poner ponemos None
def x(temperatura = None):
 if temperatura is None:
  print ("No se ha dfinido la temperatura")
 else:
  print(temperatura,"C°")

'''
de esta manera controlamos el error gracias a mi valor por defecto
1 hay que poner valor por defecto 
2 cuando invoquemos siempre intentemos enviar la informacion hacerlo con sus parametros
'''
  

''                                 ''' Ejemplos que combinan condicionales y bucles '''


# lo que hemos hecho aqui es una copia de nuestro valor n
def doblar_valor(numero):
    numero*+2# las funciones tienen su propio espacio de memoria uno esta en el espacio de main y otra esta en el espacio de doblar_valor 
numero = 10
doblar_valor(numero)
print(numero)
# si nosotros enviamoes informacion lo que hace python es una copia de la informacion 
#todo lo que pasa en una funcion se queda hay

def doblar_valores(numeros):
    print("ANTES", numeros)
    for i,n in enumerate(numeros):
        print("Elemento",i,"de la lista,n")
        numeros[i] *=2
        print("DESPUES",numeros)
        
lista_numeros = [10,50,100]#python me cambia el valor de mi lista 
doblar_valores(lista_numeros)# afecta mis datos que estan definido
print(lista_numeros)

# los tipos bsicos se pasan por valor
#los tipos avanzados se pasan por refenrecia   int,float,bool,str
# estos datos no se modificaran 
#valor = copia

#refencia = acceso directo              lista, tuple, set, diccionario
#estos se modificaran en todos ls sitios


# python hace esto porque  por el espacio ya que los simples son mas ligeros
# mientras que los avanzados seria muy pesado por ello no se puede copiar

# ese cambio que se haga en la lista lo anterior que tenia se perdera para siempre
# nesecitamos el return para devorver la informacion y reaccinarla
# en este caso no lo nsedcitamos ya que ya me lo cambia para todo 
# cuando lo consulte en el mail ya estara cambiada

def mayusculas(nombres):
    for n in nombres:
        print(n.upper)
nombres = ["Ana","Marcus","Omar","Oscar","Valentina","Silvana"]
mayusculas(nombres)

#para oasar una lista a una funcion y que me haga una copia podemos en vez de pasar la lista a una funcion podemos es pasar la copia de la lista
#n1 = [1,2,3]
#n2 = n1  y asi tendriamos copiado nuestra lista
#podemos usar el metodo copy()
#n2.copy(n1)
 
""                                                 """Trucos"""
#para modificar los tipos de simpras podemos devolverlos modificaso y reasignarlos:
def doblar_valor(numero):
    numero = numero * 2
    return numero

num = 10
num = doblar_valor(num)
print(num)



# en el caso de los tipos compuesto, podmeos evitar la mosificacion enviando una copia:

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        print("Elemento",i,"dela lista: ",n)
        numeros[i]*=2
    print("Elemento",i,"dela lista: ",n)
lista_numeros = [10,50,100]
doblar_valores(lista_numeros[:])  # Una copia al vuelo de una lista [:]
print(lista_numeros)#[:] este dos puentos no solamente que nos permite ver desde el principio hasta el final sino que tambien nos hace una copia


''         '''   argumentos y parametros indeterminados   '''
'''
Quiza en alguna oxasion no sabemos de antemano cuantos elementosvamos a enviar a una
funcion. En estos casos podemos utilizar los parametros indeterminados por posicion u por nombre.

'''

''                 ''' posicion '''

'''
para recibir un numero indeterminado de parametros por posicion, debemos crear una lista 
dinamica de argumentos (una tupla en realidad)
'''

def indeterminados_posicion(*args):# yo si no se el numero de parametros en el que el usuario va a seguir poniendo uso *args
    print(type(args))              # args viene de arguments
    for item in args:              # es un dato tuple que nos almacena cualquier numero de variables que alfin al cabo no sabemos cuando van a ir
        print(item)

indeterminados_posicion(5,"Hola",[1,2,3,4,5])

            
"por nombre"
"""Para recibir un numero indeterminado d parametros por nombre(clave-valor),debemos crear un
diccionario de argumentos"""

def indeterminados_nombre(**kwargs):# esto significa key word arguments
    # hace refencia a las claves
    # es tipo diccionario
    print(kwargs)
    print(type(kwargs))
indeterminados_nombre(n = 5 ,
                      c = "hola",
                      l =[1,2,3,4,5])# este metodo nos obiga enviarle un nombre por cada variable
# ya que es un dict = diccionario
 
def indeterminados_nombre(**kwargs):
 for item in kwargs:
     print(item," ",kwargs[item])
     
indeterminados_nombre(n = 5,
                      c = "Hola",
                      l = [1,2,3,4,5])
        

def indeterminados_nombre(**kwargs):
 for k,v in kwargs.items():
     print(k," ",v)
#podemos usar el metodo items() hace una especie de enumerate puede seprarme la claves y los valores
indeterminados_nombre(n = 5,
                      c = "Hola",
                      l = [1,2,3,4,5])
#        
''           '''por posicion y nombre a la vez'''

def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminado es",t)
    
    for kwargs in kwargs:
        print(kwargs," ", kwargs[kwargs])
        
super_funcion(10,50,-1,1.26,10,20,300,nombre ='hector',edad =27)


# super ortodoxo es esto

'' '''Funciones integradas del lenguaje'''
#int() Transforma una cadena a un entero(si no es posible da error)
n = int("10")
print(n,"Es del tipo", type(n))
#float() Transforma una cadena a un flotante(si no es posible da error)
f = float("10.3")
print(f,"es del tipo",type(f))


# termina justo aqui mi modulo 2
adios = "Gracias ahora hare otra pagina para el modulo 3"
cuidate = 'eso fue todo  amigos'
print(adios,cuidate)






















#......................................................................................................................................................................


#.....................................................................................................................
#                                               funciones

# concepto de la funciones en python


