# Este sera una estructura perfecta que es muy abitual para nuestras aplicaciones y paginas web
# vamos a poner un sistemas de datos 
#ventajas
'''
podemos cambiar de gestor de bases de datos 
si es que crecen 
vamos a ver que el trabajo que estamos viendo esta
muy alineada con la programacion orientada a objetos
todos de esto vamos a reutilizarlo al 100%
vamos a empezar con la base de datos.
aqui vamos a guardar la siguiente informacion

main.py ->  nuestro fichero principal
venv ->  nuestra carpeta de entorno virtual
models.py -> va a tener nuestras clases
db.py -> va a tener la configuracion de la base de datos
database -> va a tener la base de datos

hay mas carpetas pero pronto lo veremos
este es un projecto pequeño y es lo que deberian tener todos los proyectos

son nombres de convenio donde se llamaran nuestros siguientes projectos futuros

------------------------------ Aqui en el main hacemos nuesta base de datos

cada ves que comenzemos un projecto sigamos este mismo patron
creemos las clases
creamos nuestra base de datos
crear 
editar
visualizar 
eliminar 
se van a usa siempre en cualquier projecto
'''

import db
from models import Persona
import sys
from sqlalchemy import and_, or_, text


#hacer esto nos permite hacer pruebas de forma muy rapida
# hay que probar muchas veces las posibles funciones antes de subirlas al repositorio

def AgregarPersonasIniciales():
 p1 = Persona(nombre="Cristian",edad=23,mail="cristian@mail.com")
 p2 = Persona(nombre="samanta",edad=34,mail="samanta@mail.com")
 p3 = Persona(nombre="sergio",edad=56,mail="seordonez@mail.com")
 p4 = Persona(nombre="andres",edad=33,mail="smithandres@mail.com")
 p5 = Persona(nombre="viviana",edad=21,mail="viviana21@mail.com")
 p6 = Persona(nombre="Alison",edad=12,mail="alison@mail.com")
 listapersonas = [p1,p2,p3,p4,p5,p6]
 #db.session.add(listapersonas) # agregando la persona a la session
 db.session.add_all(listapersonas) # agregando todas las personas de la session
 db.session.commit() # confirmamos que queremos guardarla en la BD
 db.session.close() # Cerramos por que sino esto estalla XD  ---- cada accion te tiene que cerrar -- esto es de buenas practicas

def ConsultasDePrueba():
 print("\n #1. Obtener un objeto a partir de su ID (su primary key). Si no lo encuentra nos devuelve None")
 #result = db.session.query(Persona).get(3) # version obsoleta
 # la mayoria de las operaciones de una base de datos es localizar un objeto
 
 result = db.session.get(Persona, 3)
 print(result)

 print("\n #2. Obtener tosos los objetos de una tabla")
 result = db.session.query(Persona).all()
 for i in result:
  print("Nombre: {} -> Edad: {} -> mail: {}".format(i.nombre,i.edad,i.mail))
 
 print("\n #3.Obtener el primer objeto de una consulta (el mas antiguo)  ")
 result = db.session.query(Persona).first()
 print(result)

 print("\n #4. Contar el numero de elementos devueltos por una consulta")
 result = db.session.query(Persona).count()
 print("El numero de personas registradas es: {} ".format(result))
 
 print("\n #5. Ordenar el resultado de una consulta ")
 result = db.session.query(Persona).order_by("nombre").all()
 for i in result:
  print(i)

 print("\n #6. Ordenar el resultado de una cosulta y mostrar los primeros 3 resultados: ")
 result = db.session.query(Persona).order_by("nombre").limit(3)
 for i in result:
  print(i)
 
 print(" #7. Aplicar filtros a una consulta con filter")
 result = db.session.query(Persona).filter(Persona.edad > 18).all()
 for i in result:
  print(i)
 # podemos concatenar toda esta informacion de la siguiente manera
 print(" #.8 Aplicar un filtro donde me muestre las personas mayores de 18 ademas que los ordene por nombre y ademas solo sean los 3 primeros")
 result = db.session.query(Persona).filter(Persona.edad > 18).order_by("nombre").limit(3)
 for i in result:
  print(i)

  print("# 9. Aplicar el filtro ilike que nos permite buscar patrones")
  result = db.session.query(Persona).filter(Persona.nombre.ilike("Sa%")).all()# le decimos que queremos todos lo valores que empiezen con Sa y % significa todo los valores
 for i in result:
  print(i)

 print(" #10. Aplicar el filtro in_")
 result = db.session.query(Persona).filter(Persona.id_persona.in_([1,2,6])).all()
 #result = db.session.query(Persona).filter(Persona.nombre.in_(["Cristian","Eva"])).all()
 for i in result:
  print(i)
 print(" #11. Aplicar el filtro and_")
 c1 = Persona.id_persona >20
 c2 = Persona.nombre.ilike("%D%")
 result = db.session.query(Persona).filter(and_ (c1, c2)).all()
 for i in result:
  print(i)
 
 print(" #12. Ejecutar instrucciones SQL explicitas")
 
 result = db.session.query(Persona).from_statement(text("SELECT * FROM persona")).all()
 for i in result:
  print(i)
 
  
   
def AgregarPersona():
 print("\n Agregar persona")

 nombres= input("Nombre de la persona: ")
 edads=int(input("Edad de la persona: "))
 mails = input("Mail de la Persona: ")
 p = Persona(nombres,edads,mails)
 db.session.add(p)
 db.session.commit()
 db.session.close()
 print( "Has Agregado a un persona!")


def EditarPersona():
 personas = db.session.query(Persona).all() # filtramos lo que deseamos ver
 for i in personas:
    print("""> ID:{} 
             > Nombre: {}  
             > Edad: {}
             > Mail: {}""".format(i.id_persona,i.nombre,i.edad,i.mail))
 
 persona_id = int(input("\t----- ID de la persona que quieres editar: "))
 person = db.session.query(Persona).filter(Persona.id_persona == persona_id).first()
 # El metodo first nos ayuda a que si encuentra mas de una conincidencia nos envia el primer valor  
 # filtramos lo que deseamos ver
 if person is None:
      print("La persona no existe")
 else:
  print(person)
  edad_nueva = int(input("Introduce la nueva edad: "))
  person.edad = edad_nueva
  db.session.commit()
  db.session.close()
  print("Persona Actualizada")
 

def VerPersonas():
 print("\n -----------Ver listado de personas-------------\n")
 # forma de consultar de forma global nuestra BD
 #persona = db.session.query(Persona) # ponemos el nombre de la clases que  pusimos en models.py
 persona = db.session.query(Persona).all() # podremos ver todo
 while(True):
  print(
        "Ver Todo: 1\n"
        "salir: 2")
  op = int(input("Elija una opcion: "))

  if op == 1:
   for i in persona:
    print("Id:{} Nombre: {}  edad: {} mail: {}".format(i.id_persona,i.nombre,i.edad,i.mail))
   print("-----------Estas viendo toda la lista--------------") 
  elif op ==2:
   print("Haz salido del programa")
   sys.exit(1) #'Fin del programa'
  else:
   print("Dato no valido\n por favor ingresar otras vez")  


def EliminarPersona():
 personas = db.session.query(Persona).all() # filtramos lo que deseamos ver
 for i in personas:
    print("""> ID:{} 
             > Nombre: {}  
             > Edad: {}
             > Mail: {}""".format(i.id_persona,i.nombre,i.edad,i.mail))
 
 persona_id = int(input("\t----- ID de la persona que quieres Borrar: "))
 person = db.session.query(Persona).filter(Persona.id_persona == persona_id).first()
 # El metodo first nos ayuda a que si encuentra mas de una conincidencia nos envia el primer valor  
 # filtramos lo que deseamos ver
 if person is None:
      print("La persona no existe")
 else:
  print(person)
  db.session.delete(person) # borramos los datos de esta persona
  db.session.commit()
  db.session.close()
  print("Persona Borrada")
 
# if __name__ = "__main__": es el incio  para conectar nuestra base de datos
if __name__ == "__main__":
 # Reseteamos la base de datos si existe
 #db.Base.metadata.drop_all(bind=db.engine, checkfirst = True)

 # En la siguiente Linea estamos indicando a SQLAlchemy que cree, si no existe , las tablas
 # de todos los modelos que encuentre en models.py
 db.Base.metadata.create_all(db.engine)
 
 #vamos a hacer un menu con diferente opciones
 while(True):
  # esto es lo principal las consultas, los querys, los selects
  # CRUD = CREAR, MODIFICAR, ELIMINAR, CONSULTAR son las principales que debemos hacer en nuestro proyecto 
  # La diferencia entre cosulta y ver es que cosulta son los filtros que quiero ver que hecho en mi bd osea en este caso personas > 18, personas < 20, etc
  # ver es sencillamente ver a mis datos comun
  print("\n1. Agregar personas iniciales\n"
        "2. Consultas de prueba\n"
        "3. Agregar Persona\n"
        "4. Editar Persona\n"
        "5. Eliminar Persona\n"
        "6. Ver Persona\n"
        "7. Salir")

  opcion = int(input("Introduzca un opcion (1-7): "))
  if opcion == 1:
   AgregarPersonasIniciales()
  elif opcion == 2:
   ConsultasDePrueba()
  elif opcion == 3:
   AgregarPersona() 
  elif opcion == 4:
   EditarPersona()
  elif opcion == 5:
   EliminarPersona()   
  elif opcion == 6:
   VerPersonas() 
  elif opcion == 7:
   print("Haz salido del programa")
   sys.exit(1) #'Fin del programa'
  else:
   print("Opcion no valida") 

      
  
