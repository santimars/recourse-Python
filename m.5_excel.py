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

# Abrir Archivo Excel (workbook) # importante poner siempre la ruta de acceso como esta el archibo guardado
wb = openpyxl.load_workbook("/Users/santirodriguez/Desktop/02_Excel_data.xlsx")

# imprimir los nombres
print("Nombre de hojas: ")
print(wb.sheetnames)

print("\nNombre de hojas:")
for sheet in wb:
  print("-",sheet.title)

#hoja 1

#crea una hoja que haga referencia a la primera hoja de excel

hoja_uno = wb.sheetnames[0]
print("\n Primera Hoja:")
print("-",hoja_uno)  

hoja_otros = wb.sheetnames[2]

del hoja_otros
for sheet in wb:
  print("-",sheet.title)

wb.save("02_Excel_data.xlsx")  



'''
hay que invertir  mas tiempo leyendo la documentacion de las librerias y buscar las 
solucion y imprementarla en codigo
 un programador tiene 70% leyendo 30 % programando
incovenientes
No puede trabajar con cantidades de datos exageradamente grandes
nos permite realizar multitud de operaciones, pero no aplicar una 
logica de programacion
su rendimiento decae con el volumen de datos 
los ficheros excel .xls tienen un formato muy complejo y visual
lo que hace que sean muy pesados
en Programacion prodemos trabajar con ficheros excel y suplir alfunasd e sus debilidades o trabajaremos mas eficientemente 
con ficheros CSV.

'''
"""
IMPORTANTE

TENER CERRADO SIEMPRE EL EXCEL CUANDO VALLAMOS A EDITAR
ya que se puede corromper 
no se permite que este abierto el excel en cualquier lado
"""
