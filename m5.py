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
fichero = open("01_fichero.txt","w")
fichero.write(texto)
fichero.close
# las cosas como son en el modulo 6 veremos tambien bases de datos es mas orientado haceia la manipulacion de los datos 
# haremos con python y luegos iremos con excel y librerias internas y externas como eso
