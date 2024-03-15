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
print(dicc_frutas2)

dicc_frutas3 = {
    "nombre" :"uvas",
    "cantidad" : 220
}
print(dicc_frutas3)

dicc_frutas4 = {
    "nombre" :"banana",
    "cantidad" : 60
}
print(dicc_frutas4)

# Diccionario de verduras

dicc_verduras = {
    "nombre" :"Lechuga",
    "cantidad" : 40
}
print(dicc_verduras)

dicc_verduras2 = {
    "nombre" :"Tomate",
    "cantidad" : 70
}
print(dicc_verduras2)

dicc_verduras3 = {
    "nombre" :"cebolla",
    "cantidad" : 80
}
print(dicc_verduras3)

dicc_verduras4 = {
    "nombre" :"Zanahoria",
    "cantidad" : 56
}
print(dicc_verduras4)

# lista de Frutas
lista_frutas = [dicc_frutas,
                dicc_frutas2
                ,dicc_frutas3
                ,dicc_frutas4]
print(lista_frutas)
# Lista de Verduras

lista_verduras = [
    dicc_verduras,
    dicc_verduras2,
    dicc_verduras3,
    dicc_verduras4
]
print(lista_verduras)