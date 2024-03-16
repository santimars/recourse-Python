"""
Que es JSON?
es un formato para el intercambio de datos,basicamente JSON describe los datos
es una notacion, es una forma de guardar informacion con una sintaxis dedicada que se usa para identificar y gestionar
los datos. JSON nacio como una alternativa a XML.

Una de las mayores ventajas
"""

'''
hay editores que nos permite ver precisamente lo que hay en el json y nosotros para que ahce r
'''
import json
dicc_frutas = {
    "nombre" :"manzana",
    "cantidad" : 20
}
print(dicc_frutas)
dicc_frutas2 = {
    "nombre" :"pera",
    "cantidad" : 50
}


dicc_frutas3 = {
    "nombre" :"uvas",
    "cantidad" : 220
}


dicc_frutas4 = {
    "nombre" :"banana",
    "cantidad" : 60
}


# Diccionario de verduras

dicc_verduras = {
    "nombre" :"Lechuga",
    "cantidad" : 40
}


dicc_verduras2 = {
    "nombre" :"Tomate",
    "cantidad" : 70
}


dicc_verduras3 = {
    "nombre" :"cebolla",
    "cantidad" : 80
}


dicc_verduras4 = {
    "nombre" :"Zanahoria",
    "cantidad" : 56
}


# lista de Frutas
frutas = [dicc_frutas,dicc_frutas2,dicc_frutas3,dicc_frutas4]
print(frutas)
# Lista de Verduras
verduras = [dicc_verduras,dicc_verduras2,dicc_verduras3,dicc_verduras4]
print(verduras)

Fruteria = [[frutas],[verduras]]
'''
Una vez que tenemos las estructura creada, la codificamos en JSON (dumps)
'''
# Nos develve el String con el JSON
json_fruteria = json.dumps(Fruteria)
print("Tipos de los datos:",type(json_fruteria))
print(json_fruteria)


# Tambien podemos pedirlea dumps que nos lo idente por nosotros o que nos ordene las claves
json_fruteria_identado = json.dumps(frutas,indent=4,sort_keys=True)
print(json_fruteria_identado)


'''Diferencia?'''

print(frutas)
print()
print(json_fruteria)
# despues de hacer la tabulacion y este en formato json
#hay que hacer un fichero JSON
'''
esto nos permitira enviar informacion 
''' 
'''
Y si queremos, lo guardamos en un fichero
'''
with open ('data.json','w',encoding= 'utf-8') as f: # with open es la unidad para esciribir un fichero 
    json.dump(frutas,f, ensure_ascii=False, indent=4) #Ensure ascii es 

# dump dict/list a fichero
with open ('data.json','w',encoding= 'utf-8') as f: # with open es la unidad para esciribir un fichero 
    json.dump(frutas,f, ensure_ascii=False) # ensure_ascii = si tenemos caracteres extraños con esto no habra errores por ello
# si encuentra un caracter extraño lo omite
    

'''
Decodificar JSON (json_loads(String))


Ahora veremos el caso contrario, dado un dato en formato JSON, veremos como decodificarlo
para transformarlo en tipos de datos manejables por Python.
Para ello usaremos la funcion json_loads(String)
'''

# Disponemos de json_Fruteria el cual contiene nuestra informacion en formato JSON

print("Tipos de los datos:",type(json_fruteria))
print("Datos en JSON:\n")
print(json_fruteria)


''' 
DECODIFICAR JSON (json_loads(String))

Ahora veremos de json_fruteria contiene informacion en formato JSON
'''
print("Tipos de los datos:", type(json_fruteria))
print("Datos en JSON:\n")
print(json_fruteria)



f_dict = json.loads(json_fruteria)
print("\nTipo de los datos:", type (f_dict))

print("Datos en estructuras de datos en Python (diccionarios):\n")
print(f_dict)



''' Y SI QUEREMOS, LO ABRIMOS DESDE UN FICHERO'''

with open('data.json','r', encoding='utf-8' ) as file:
    data = json.load(file)
    print(type(data))
    print(data)

'''
antes habiamos hecho de un diccionario con el metodo dumps() lo pasamos a str JSON esto es codificacion
ahora el STR JSON  usamos el metodo loads() y los pasamos a diccionario - dict()   esto es decodificacion
'''
# load y loads para decodificar el fichero

'''
Trabajar con datos JSON

cuando tengamos objetos en formato JSON(que hemos visto que son strings internamente, pero con
un formato pre-estructurado) nos son muy utiles para transferirlos a otros sitios o programas. Por
lo que el proceso de trabajo sera:
- Tener nuestros datos en estrucutras propias de nuestro lenguaje (diccionarios, listas tuplas, ect)
- codificarlo a un string con formato JSON
- enviarlo a otro sitio, programa o lenguaje
- En el destino, recibir ese string con formtao JSON
- Decodificar dicho string y adaptarlo a las estructuras propias que tenga ese sistema,programa o lenguaje(que
pueden se diferentes a las de Python)


Este proceso se realiza asi porque una estructura de datos diccionarios, no es igual en Pytho, en java o en SQL.
Por lo que no tiene sentido enviar unos datos desde Python a esos lenguajes en formato diccionario, ya que no lo van a 
entender. Pero lo que si entiende todo el mundo es la estructura de JSON.

'''
# Ver el diccionario completo
print("Datos completo (tipo",type(f_dict),")")
print(f_dict)

print("\nJSON object Fruta")
print(f_dict,['Fruteria'][0]) #JSON object Fruta
print("\nJSON object verdura") # JSON object verdura
print(f_dict,['Fruteria'][0])# JSON object Fruteria
print(f_dict['Fruteria'][1])

print("\n Numero Manzana")
print(f_dict,["Fruteria"][0]["frutas"][0]["cantidad"]) #Numero de manzanas

'''visualizar contenido JSON 
Hay una multitud de paginas webs y herramientas que nos sirven para visualizar graficamente un objeto JSON. Copia
el siguiente codigo y pegalo en las siguientes webs(pestaña Text parta introducir el codigo y pestaña Viewer para visualizarlo)Ñ

https://jsonviewer.stack.hu/
https://jsonformatter.org/json-viewer

'''



