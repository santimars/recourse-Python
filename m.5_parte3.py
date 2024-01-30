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
                                              # (en el oreden que se indica)
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