
'''Extra

Convertir Datos JSON en Objetos

Aprenderemos como convertir datos JSON en un objeto Python personalizado. Por ejemplo cuando recibimos datos JSON de estudiantes 
de una API o estamso leyendo un archivo JSON y queremos convertirlo directamente en un objeto de la clase estudiante.

Sabemos como codificar a JSON informacion que tengamos en listas y diccionarios usando el metodo json.dumps() y como 
decodificar esta informacion con json.loads(), el cual devuelve un diccionario(dict) que posteriormente podemos manipular.

Pero pensar en las ventajas que tendriamos si al decodificar un fichero o string JSON, lo cargamos directamente en un objeto
que tengamos creada en nuestro proyecto. De esta forma, tras la decodificacion, podemos manipular directamente la informacion
a nivel de objeto.

Hay varias formas de lograrlo. Puede elegir la forma que resulte mas util para cada proyecto. Veamos como desealizar una cadena
o string JSON en un objeto personalizado.




Opcion 1 

Uso de namedtuple y object_hook para convertir datos JSON en un objeto Python personalizado

podemos usale el parametro object_hook del metodo json.loads(). Este parametro permite obtener el diccionario que se genera con
json.loads() y enviarlo a un metodo el cual se encargar de decodificar este diccionario en una estructura especifica (en una 
estructura clase). En este ejemplo, el nombre de este metodo es decodificadorEstudiante(estudianteDict) recibiendo como parametro
el diccionario generado por json.loads().

Dentro del metodo decodificadorEstudiante(estudianteDict) Como convertimos un diccionario en un objeto de una clase? 
Con namedtuple. Se encarga de trasnformar las claves y valores del diccionario en una estructura de clase.

Veamos primero el ejemplo simle y luego podemos pasar al ejemplo practico, En este ejemplo, estamos convirtiendo datos a JSON
de estudiante en un tipo de clase de Estudiante personalizado.
'''
import json
from collections import namedtuple
from json import JSONEncoder

class Estudiante():
 def __init__(self,id_estudiante,nombre,lista_asigaturas):
  self.id_estudiante = id_estudiante
  self.nombre = nombre
  self.lista_asignaturas= lista_asigaturas


class Asignatura:
    def __init__(self,nombre,dificultad):
      self.nombre = nombre
      self.dificultad = dificultad


class EstudianteEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Estudiante):
            return {
                "id_estudiante": o.id_estudiante,
                "nombre": o.nombre,
                "lista_asignaturas": [asignatura.__dict__ for asignatura in o.lista_asignaturas],
            }
        return super().default(o)
    
'''class EstudianteEncoder(JSONEncoder):
  def default(self, o):
    return o.__init__  # toma un objeto y lo muestra en formato diccionario
  '''
# Nota este es e code del profe pero la verdad que me aparece un error ya que no me deja porque es mas avanzado de lo que me deja con el codigo
# por ello para solucionar esto he hecho este codigo donde me permite recorrer completamente sin trabas el codigo

def decoficadorEstudiantes(estudianteDict):
  return namedtuple('Estudiante',estudianteDict.keys())(*estudianteDict.values())

# Vamos a preparar el JSON con el que trabajemos
a1 = Asignatura("Introduccion a la programacion","Basica")
a2 = Asignatura("Programacion en Python", "Intermedia")
a3 = Asignatura("Inteligencia Artificial","Avanzada")

lista_asignaturas =[a1,a2,a3]
e1 = Estudiante(1,"Cristian",lista_asignaturas)
estudiante_json = json.dumps(e1, indent= 4, cls=EstudianteEncoder)

print("JSON de un estudiante con el que vamos a trabajar")
print(estudiante_json)
#dumbs tambien acepta objetos
'''dumbs tiene una limitacion
tengo que pasarle una clase aparte que tiene el nombre original + el nombre JSONEncoder
'''
# dumbs sirve para objetos sirver
#pero en este caso que tenemos objetos en objetos no son sirven ya que es mas pesado


#Ahora vamos a realizar el siguiente proceso:
# Leer JSON -> Generar dict -> Decodificar en objeto de la clase Estudiante

estudiante = json.loads(estudiante_json, object_hook= decoficadorEstudiantes)

print("\nConvertimos el JSON anterior a un objeto de la clase",type(estudiante).__name__)
print(" > ID de estudiante: ",estudiante.id_estudiante)
print(" > Nombre:",estudiante.nombre)
print(" > Lista de asignaturas: ")
for i in estudiante.lista_asignaturas:
  print("\t",i)
print("=========")
print(type(estudiante))
# me estan encapsulando la informacion en la clase estudiante y esto es un problema
