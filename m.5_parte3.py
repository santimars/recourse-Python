"CSV"

"Uso del modulo csv"
"libreria que nos permite trabajar con ficheros CSV.    Documentacion https://docs.python.org/3/library/csv.html"

import csv

# Apertura y lectura de ficheros CSV con reader
'''usaremos el docuemento 02_data.csv'''

#leer el archivo csv con readre

with open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv","r") as my_csv_file:
    reader = csv.reader(my_csv_file)
    for row in reader:
        print(row)

# podremos leer  y escribir en csv
# es normal leer los ficheros csv linea a linea 
print("\t")
# leer archivo csv con reader y optimizando la salida
with open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv","r") as my_csv_file:
    reader = csv.reader(my_csv_file, delimiter=";")
    for row in reader:
        print(",".join(row))

print("\t")
#leer solo cabezeras
with open ("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv","r") as f:
    reader = csv.reader(f)
    cabeceras = next(reader)
print(cabeceras)


# Uso de reader y next

with open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv","r") as my_csv_file:
    reader = csv.reader(my_csv_file, delimiter=",")
    reg0 = next(reader) # leer registro (lista)
    print(reg0)
    reg1 = next(reader) # leer siguiente (lista)
    print(reg1)
    nombre, provincia, consumo = next(reader) # Almacenar en variables el siguiente
                                              # (en el orden que se indica)
    print("Nombre: ",nombre,"Provincia: ",provincia,"consumo: ",consumo) # Mostrar las variables


# leer archico csv con reader, next, bucle y formato de salida
    
with  open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv","r") as my_csv_file:
    reader = csv.reader(my_csv_file, delimiter= ",")
    next(reader) # saltarnos la cabecera del documento csv
    for index, row in enumerate(reader):
        print('lineas: ' + str(index))
        print('\tnombre: ' + row[0], "provincias: " + row[1], "Consumo:" + row[2])

# Ordenacion por campos con operator

"Documentos en https https://docs.python.org/3/library/operator.html"

import operator
print("\n")
# leer archivo scv con reader y mostrarlo ordenando por el tercer campo (consumo)
my_csv_file = open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv")
listaordenada = sorted(my_csv_file,
                       key = operator.itemgetter(2), # es provicia, nos organiza por medio de una cabezera sera provincia
                       reverse=True
                       )
for i in listaordenada:
    print(i)

# O si queremos imprimir la lista de seguido:
# print(listaordenada)
    

# Leer CSV  en formato diccionario

# leer archivo csv como lista de diccionarios con DictReader() y mostrar solo 
print("\n")   
with open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv","r") as my_csv_file:
    reader = csv.DictReader(my_csv_file)
    for reg in reader:
        print(reg['provincia'],"->",reg['consumo']) # para ver informacion de reader toca si o si hacer bucles

# es mas rapido leer documuento por dicionario cuando son datos muy grandes o cuando se conocen los datos



    

print("\n")   
my_csv_file= open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv")
reader = csv.DictReader(my_csv_file)
listadicc = list(reader) # Obtener lista de diccionarios
listafinal = sorted(listadicc,
                    key=operator.itemgetter('consumo'),
                    reverse=True
                    )
for registro in listafinal:
    print(registro)
# Cerrar correctamente un fichero CSV
    
print("\n")   
with open("/Users/santirodriguez/Documents/Python/M5/02_CSV_data.csv","r") as my_csv_file:
     reader = csv.reader(my_csv_file)
     for row in reader:
      print(row)
del reader # Borra objetos
my_csv_file.close()# Cerrar archivo
print("Fichero scv cerrado con exito")

# Crear un Fichero CSV nuevo
'''
Abrir posteriorente el fichero02__CSV_data_2.csv para comprobar que se haya creado con el contenido correcto.
El fichero se creara en el directorio de este proyecto.
'''

#Escribir todas las tuplas de una lista con writerow() y writerows()
# en un ficehro nuebo del fichero con "w" o "wb"
datos = [("aaa",111),
         ("bbb",222),
         ("ccc",333)]
csvsalida = open("02_CSV_data_2.csv","w", newline='')
writer = csv.writer(csvsalida)
writer.writerow(['nombre','precio'])
writer.writerows(datos)

del writer
csvsalida.close()

# Añadir datos a un fichero CSV ya creado
'''
Abrir psoteriormente el fichero 02_CSV_data_2.csv para comprobrar que se haya creado con el 
contenido correcto.
'''
# Añadir todas las tuplas de una lista en un fichero existente
# (apertura del fichero con "a" o "ab", que se viene de apppend y añade info al final)

datosnuevos = [('ddd',444),('eee',555),('fff',666)]
csvsalida = open("02_CSV_data_2.csv", "a", newline= '') # a de append  
writer = csv.writer(csvsalida)
writer.writerows(datosnuevos)

del writer
csvsalida.close()
#statistics invertigar libreria para poder abordar lo que nesecitamos hacer en este 
# terminamos modulo  de excel aqui
# vamos a ver json