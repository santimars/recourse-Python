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
'''

import db
from models import Persona
import sys

#hacer esto nos permite hacer pruebas de forma muy rapida
# hay que probar muchas veces las posibles funciones antes de subirlas al repositorio

def AgregarPersonasIniciales():
 p1 = Persona(nombre="Cristian",apellido="Rodriguez",edad=23,mail="cristian@mail.com")
 p2 = Persona(nombre="samanta",apellido="Gutierrez",edad=34,mail="samanta@mail.com")
 p3 = Persona(nombre="sergio",apellido="Ordonez",edad=56,mail="seordonez@mail.com")
 p4 = Persona(nombre="andres",apellido="Smith",edad=33,mail="smithandres@mail.com")
 p5 = Persona(nombre="viviana",apellido="Adams",edad=21,mail="viviana21@mail.com")
 p6 = Persona(nombre="Alison",apellido="burgos",edad=12,mail="alison@mail.com")
 db.session.add(p1) # agregando la persona a la session
 db.session.commit() # confirmamos que queremos guardarla en la BD
 db.session.close() # Cerramos por que sino esto estalla XD  ---- cada accion te tiene que cerrar -- esto es de buenas practicas
def ConsultasDePrueba():
 pass

def AgregarPersona():
 pass

def EditarPersona():
 pass

def EliminarPersona():
 pass

if __name__ == "__main__":
 # Reseteamos la base de datos si existe
 #'db.Base.metadata.drop_all(bind=db.engine, checkfirst = True)'

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
        "5. Eliminar Persona"
        "6. Ver Persona\n"
        "7. Salir")

  opcion = int(input("Introduzca un opcion (1-7): "))
  if opcion == 1:
   AgregarPersonasIniciales()
  elif opcion == 2:
   ConsultasDePrueba()
  elif opcion == 4:
   AgregarPersona() 
  elif opcion == 5:
   EditarPersona()
  elif opcion == 6:
   EliminarPersona()   
  elif opcion == 7:
   sys.exit(1) #'Fin del programa'
  else:
   print("Opcion no valida") 

      
  
