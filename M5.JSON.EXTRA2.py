'''
Opcion 2: Uso de Types. SimpleNamespace y object_hook para convertir datos JSON en un objeto Python personalizado


podemos usar types.SimpleNamespace como contenedor para objetos JSON. 
Ofrece las siguientes ventajas sobre una solucion manedtuple:

- su tiempo de ejecucion es menor porque no crea una clase para objeto.
- es presico y simplista

pero siguen existiendo desventajas, como por ejemplo:

- todos los objetos son objetos de SimpleNamespace


'''

import json
from types import SimpleNamespace
from json import JSONEncoder

class Estudiante():
    def __int__(self,id_estudiante,nombre,lista_asignaturas):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.lista_asignaturas

class Asignatura:
    def __init__(self,nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

