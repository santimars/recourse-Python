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
import os
import openpyxl

# Obtén la ruta completa al archivo 'fichero.xlsx'
ruta_archivo = os.path.join(os.path.dirname(__file__), 'fichero.xlsx')

# Carga el libro de trabajo
wb = openpyxl.load_workbook(ruta_archivo)


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