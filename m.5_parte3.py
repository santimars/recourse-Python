"CSV"

"Uso del modulo csv"
"libreria que nos permite trabajar con ficheros CSV.    Documentacion https://docs.python.org/3/library/csv.html"

import csv

# Apertura y lectura de ficheros CSV con reader
'''usaremos el docuemento 02_data.csv'''

#leer el archivo csv con readre

with open("/Users/santirodriguez/Desktop/02_CSV_data.csv","r") as my_csv_file:
    reader = csv.reader(my_csv_file)
    for row in reader:
        print(row)

# podremos leer  y escribir en csv
# es normal leer los ficheros csv linea a linea 
 

