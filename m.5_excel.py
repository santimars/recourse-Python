'''
Excel es un software de hoja de cálculo usado en todo el mundo.

Sus inconvenientes son que no puede trabajar con cantidades de datos 
exageradamente grandes, aunque nos permite realizar multitud de operaciones, 
no nos permite aplicar una lógica de programación, su rendimiento decae con el 
volumen de datos y sus ficheros (.xls) tienen un formato muy complejo y 
visual, lo que hace que sean muy pesados.

Por ejemplo, una tabla de Excel con 1 millón de registros ocupa,
 aproximadamente, un tamaño de unos 12MB.

En programación podremos trabajar con ficheros Excel y suplir 
algunas de sus debilidades, o trabajaremos más eficientemente con ficheros CSV.

Vamos a ver cómo trabajar con ficheros tipo Excel (.xls),
 para ello utilizaremos la librería openpyxl, que nos permite 
 acceder y modificar ficheros Excel. Podemos encontrar 
 la documentación en https://openpyxl.readthedocs.io/en/stable/.
   Lo primero será importar dicha librería a nuestro programa mediante
     la instrucción:
'''

import openpyxl
# abrir un archivo excel (workbook)
wb = openpyxl.load_workbook("O2_Excel_data.xlsx")

#imprimir los nombre de las hojas
print("Nombres de hojas:")
print(wb.sheetnames)

print("\nNombres de hojas(otra forma): *")
for sheet in wb:
 print(sheet.title)

# HOJA 1 
# Crear una variable que haga referencia a la primera hoja de excel
 
hoja_uno = wb.sheetnames[0]
print("\nPrimera hoja: ")
print(hoja_uno)

'''
para acceder a una celda de uan hoja concreta 
'''

#Crear una variable que haga referencia a la primera del Excel
hoja_uno = ["address"]

# Acceder a una celda directamente 
print(hoja_uno["A1"].value) # contenido
print(hoja_uno["B1"]) # referencia

# Acceder a uan celda a traves de uan nomenclatura fila-columna

print(hoja_uno.cell(row = 5, column = 2).value)

# Para Acceder a multiples celdas de uan hora concreta:

multiples_cells = hoja_uno["A1":"B3"]
for row in multiples_cells:
 for cell in row:
  print(cell.value)


# Si nesecitamos es acceder a todas las filas de una hoja conreta
for fila in hoja_uno.rows:
 for columna in fila:
  print(columna.coordinate, columna.value)
print("---final de fila---")


#O bien acceder a todas las columnas de una hoja concreta:

for columna in hoja_uno.columns: 
    for fila in columna: 
        print(fila.coordinate, fila.value)
    print("---Final de Columna---")

# Ahora vamos a modificar celdas de una hoja concreta, en nuestro caso, la hoja 2:

import datetime 

# Crear una variable que haga referencia a la segunda hoja del Excel
hoja_dos = wb["ventas"]  

# Modificar una celda (de 3 formas diferentes)
hoja_dos["B6"] = 5
hoja_dos["C6"].value = 5
hoja_dos.cell(row=6, column=4, value=5)

# Añadir la hora actual en la celda E2
hoja_dos["E2"].value = datetime.datetime.now()

# Guardar cambios (¡Importante! El Excel debe estar cerrado)
wb.save("02_Excel_data_xlsx")  


# Modificar la celda B2, que contiene un 40, por un 99
print("Celda B2 antes de modificarla: ", hoja_dos["B2"].value)
hoja_dos["B2"] = 99
print("Celda B2 despues de modificarla: ", hoja_dos["B2"].value)

# Modificar la celda C2, con una formula
print("Celda C2 antes de modificarla con la formula: ", hoja_dos["C2"].value)
hoja_dos["C2"] = "=SUM(B2, 3)"
print("Celda C2 despues de modificarla con la formula: ", hoja_dos["C2"].value)# Modificar la celda B2, que contiene un 40, por un 99
print("Celda B2 antes de modificarla: ", hoja_dos["B2"].value)
hoja_dos["B2"] = 99
print("Celda B2 despues de modificarla: ", hoja_dos["B2"].value)

# Modificar la celda C2, con una formula
print("Celda C2 antes de modificarla con la formula: ", hoja_dos["C2"].value)
hoja_dos["C2"] = "=SUM(B2, 3)"
print("Celda C2 despues de modificarla con la formula: ", hoja_dos["C2"].value)

# Guardar cambios
wb.save("02_Excel_data.xlsx") 

'''Añadimos contenido nuevo a una hoja concreta:

'''
hoja_dos.append(["Junio",99,100])
# Guardar cambios
wb.save("02_Excel_data.xlsx")