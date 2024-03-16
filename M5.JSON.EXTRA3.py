'''
Opcion 3: Uso para convertir datos JSON en un objeto Python personalizado

jsonpickle es una biblioteca de Python diseñada para trabajar con objetos Python complejos. Se puede usar jsonpickle
para serializacion y deserializacion datos complejos de Python y JSON. Pueden consultar la documentacion de Jsonpickle para
obtener mas detalles aqui
(https://jsonpickle.github.io/) y la documentacion aqui (https:/json.pickle.github.io/api.html).

las ventajas son:

 - facilidad de uso
 - permite trabajar con datos complejos, como objetos dentro de objetos. En nuestro ejemplo,creara correctamente 
 los objetos de las clases Asignatura dentro de nuestro objeto de la clase Estudiante.

 veamos un Ejemplo:
'''
import jsonpickle

class Estudiante():
 def __init__(self,id_estudiante,nombre,lista_asigaturas):
  self.id_estudiante = id_estudiante
  self.nombre = nombre
  self.lista_asignaturas= lista_asigaturas


class Asignatura:
    def __init__(self,nombre,dificultad):
      self.nombre = nombre
      self.dificultad = dificultad
#Creacion de objetos (principal : Estudiantes y secundario: Asignatura)
a1 = Asignatura("Introduccion a la programacion","Basica")
a2 = Asignatura("Programacion en Python","Intermedia")
a3 = Asignatura("Inteligencia Artificial","Avanzada")
lista_asignaturas = [a1,a2,a3]
e1 = Estudiante(1,"Cristian",lista_asignaturas)

#preparacion del fichero
fichero = 'jsonEmpleado' + '.json'
#codificacion de un objeto (el) a u JSON String
Estudiante_json = jsonpickle.encode(e1,indent=4) # indent = 4 es opcional dino nos da minificado
print("JSON de un Estudiante con el que vamos a trabajar")
print(Estudiante_json)

# Escribimos el JSON String en el fichero
with open(fichero,'w') as f:
  f.write(Estudiante_json)

  '''
  me ha añadido clave valor para ver endonde es la informacion
  me muesta la lista con 3 diccionarios con la clase y la referencia en la que pertenece


  '''
# Abrimos y leemos el fichero
Estudiante_json_leido = open(fichero).read()

Estudiante = jsonpickle.decode(Estudiante_json_leido)
print("\n Objeto de la clase", type(Estudiante).__name__)
print(" - ID de estudiante: ",Estudiante.id_estudiante)
print(" - Lista de asignaturas: ")
for a in Estudiante.lista_asignaturas:
  print("\t Objeto de la clase",type(a).__name__,"Nombre: ",a.nombre,"Dificultad :", a.dificultad)

# si el json ha salido bien tomemos el JSON y lo validamos en un visualizador de JSON para ver que 
# no tengamos errores de index