'''
veremos archivos planos
excel
csv
json
bases de datos 
'''
# aqui se hace la programacion tangible salimos a trabajar con cosas externas 
'''
archivos de texto plano
'''

'''
Un archivo de texto simple o texto plano, es un archibo informatico que contiene unicamente texto formado
por solo caracteres que son legibles por humanos, careciendo de cualquier tipo de formato tipografico.

Los archivos de texto simple o texto plano, nos sirven para:
Guardar preferencias del usuario
Guardar logds de actividad o error
Guardar pruebas de anuesrto programa
y en definitiva, cualquier informacion que queramos que nuestro software almacene de manera permanente.

'''
'''
ventajas

hay que abrir y cerrar el archivo cada vez que se utiliza. Si no se cierra adecuadamente
se puede corromper el contenido.

Desvenjadas
son fragiles no tiene ningun mecanismo de seguridad la informacion que esta se ve completa
'''
'Los ficheros hoy en dia tambien se pueden corromper si no se cierra correctamente '
'se dañao'

'''
Que tipo de fichero exiten que sean archivos de texto plano?

cualquiera

podemos crear cualquier fichero de texto y añadirle la extencion que queramos.
Al ser un fichero de texto plano, no depende de ningun programa para que le proporcione un 
formato o unas reglas.
'''


'''
las extenciones mas comunes son txt,dat y log.

podremos crear cualquier fichero que se llame holaquetal.esperoquebien y nos lo va a leer igual

lo que podremos hacer en python es 

 open 
 read 
 write
 close

es muy importante que nosotros siempre siempre siempre cerremos los ficheros para que no se corrompan 
'''
'''
Cuando se trabaja con archivos
cuidado con la codificacion

unicode es un estandar de codificacion de caracter de diseño para facilitar el tratamiento
informatico, transmicion y visualizacion de textos de numerosos idiomas y diciplinas tecnicas
ademas de textos clasicos de lenguas muertas.  
'''

texto = "Una linea con texto\nOtra linea con texto"
fichero = open("01_fichero.txt","w") # el fichero "01_fichero.txt,w" indica la ruta que crearemos, w indica modo de escritura, write
fichero.write(texto) # escribimos el texto el numero que aparece es el numero de caracteres
fichero.close # cerramos el fichero

# las cosas como son en el modulo 6 veremos tambien bases de datos es mas orientado haceia la manipulacion de los datos 
# haremos con python y luegos iremos con excel y librerias internas y externas como eso

#                      '''Lectura de un fichero de texto'''


'https://docs.python.org/3/library/codecs.html#standard-encodings'

fichero = open("01_fichero.txt","r") # modo lectura read, por defecto ya que es r,no es nesecario

texto =fichero.read() # lectura completa

fichero.close # es importante siempre cerrar los ficheros cuando los estamos leyendo siempre toca cerramos no es recomendarble dejamos por mucho tiempo abiertos
print(texto)
print(type(texto))


fichero = open("01_fichero.txt","r")


texto = fichero.readlines() # lee creando una lista de lineas

fichero.close # cerramos fichero
print(texto)
print(type(texto))

print(texto[-1]) # ahora nos permite ver la linea de texto que deseamos sin tener que ver todas las lineas que esten escritas hay.

''                                      ''' pidiendo nombre del fichero al usuario'''

file = "\nsofia" # pedimos lo datos que deseamos que el usuario ingrese
fichero = open("01_fichero.txt","w") # lo abrimos para abrir w es write para escribir pero lo resetea completamente
fichero.write(file) # le decimos que este es el texto para introducir en el fichero
fichero.close()# lo cerramos siempre

fichero = open("01_fichero.txt","r") # le decimos que fichero tiene que abrir o crear 
texto = fichero.read() # lectura completa
fichero.close() # lo cerramos siempre
print("Gracias por unirte\n ",texto) # lo mostramos por pantalla


''                                      '''Añadir contenido al final'''
file = "\nmaicooll" # pedimos datos que queremos que el usuario ingrese
fichero = open("01_fichero.txt","a") # abrimos el achivos, a es append de agregar contenido y asi no elimina el fichero de cero
fichero.write(file)# le decimos que vamos a escribir en el 
fichero.close()# siempre lo cerramos 
fichero = open("01_fichero.txt","r") # volvemos abrir esta vez r, para read que es leer
texto = fichero.read() # decimos que lo leeremos
fichero.close() # cerramos fichero siempre
print("Gracias por unirte\n ",texto) # los mos tramos por pantalla 


''                                  '''lectura de un fichero no existente y creacion automatica'''

fichero = open("01_fichero.txt","a+") # extencion de escritura silmutanea, crea fichero si no esta creado
fichero.close()



''                                       '''Lectura linea a linea'''

fichero = open("01_fichero.txt","r") # abrimos el achivos, a es append de agregar contenido y asi no elimina el fichero de cero
fichero.readline() # readline nos permite leer linea a linea 
fichero.readline()
fichero.readline()
fichero.readline()
fichero.close()

''                              '''Lectura linea a linea secuencial '''

with open("01_fichero.txt","r") as fichero:
    for linea in fichero:
        print(linea,end="")

# python al usar esta forma ya nos ha cerrado el fichero sin tener que utilizar fichero.close()
        

'''
cuando trabajemos con ficheros la probabilidad de error es muy grande por ello es 
muy recomendable que trabajos con try except para que no nos carguemos el documento y podamos 
tener control de los errores que provoquemos si pasa.
'''


''                                '''Ficheros y excepciones'''
try:
    with open("01_fichero.txt","r") as fichero:
     print(fichero.readlines())
     fichero.close()
     if fichero.closed:
        print("/n Exitosamente has salido sin cargarte el fichero y cerrandolo correctamente capo")
     else:
        raise EnvironmentError # Podriamos tambien enviar IOError
except EnvironmentError as e: # Padre de los tipos Erros IOError y OSError
   print("Error en el fichero",type(e).__name__)
except Exception as e:
   print("Error Desconocido",type(e).__name__)

'''Desde OSError es el padre de todas las excepciones de errores que puede pasar mientras estamos en archivos
es por ello recomendable siempre que trabajemos hacer el try y mirar la docs python para asegurarnos de los errores
que pueden surgir'''


''                               '''Manejando el puentero(Marerial Avanzado para investigar)'''


fichero = open("01_fichero.txt","r")
fichero.seek(0) # puntero al principio
fichero.read(10)# lee los 10 caracteres
fichero.read(10)# leemos los siguientes 10 caracteres
fichero.seek(0)
fichero.read()# leemos todo lo que quede del documento hasta el final
fichero.close() # cerramos el fichero muy imporante de hacer