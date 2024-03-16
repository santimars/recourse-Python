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

class EstudianteEncoder(JSONEncoder):
    def default (self, o):
        return o.__dict__
# Vamos a preparar el JSON con el que trabajemos
a1 = Asignatura("Introduccion a la programacion","Basica")
a2 = Asignatura("Programacion en Python", "Intermedia")
a3 = Asignatura("Inteligencia Artificial","Avanzada")

lista_asignaturas =[a1,a2,a3]
e1 = Estudiante(1,"Cristian",lista_asignaturas)
Estudiante_json = json.dumps(e1,indent=4,cls=EstudianteEncoder)

print("JSON de un Estudiante conel que vamos a trabajar")
print(Estudiante_json)

estudiante = json.loads(Estudiante_json,object_hook=lambda d : SimpleNamespace(**d))

#leemos el JSON.loads y lo cargamos en objetos de nuestras correspondientes clases
print("\nConvertimos el JSON anterior aun objeto de la clase", type(estudiante).__name__)
print(" id estudiante:",estudiante.id_estudiante)
print(" Nombre: ",estudiante.nombre)
print("lista de asignaturas:")
for i in estudiante.lista_asignaturas:
    print("\t",i)

'''
Hasta ahora, las opciones que hemos visto son soluciones rapidas que son ideales para cuando queremos des-serializar un
fichero JSON y convertirlo a un objeto Python de una sola clase. Pero si queremos una conversion mas comleja, donde implica
una conversion de objetos, de varias clases, la solucion que hay que abordar es jsonpickle
'''
# En M5.JSON.EXTRA3.PY esta la siguiente parte de este extra 